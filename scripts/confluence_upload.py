#!/usr/bin/env python3
"""
Script para fazer upload de arquivos Markdown para Confluence
Foca inicialmente nos arquivos de docs/levels/
"""

import os
import sys
import requests
from pathlib import Path
from requests.auth import HTTPBasicAuth
import json
from markdown import markdown
from html2text import html2text
import re

# ============================================
# CONFIGURAÇÃO - AJUSTE AQUI
# ============================================

CONFLUENCE_URL = "https://seu-dominio.atlassian.net"  # Ex: https://gupy.atlassian.net
CONFLUENCE_USERNAME = "seu-email@exemplo.com"
CONFLUENCE_API_TOKEN = "seu-api-token"  # Gerar em: Account Settings > Security > API tokens
CONFLUENCE_SPACE_KEY = "SEU-SPACE-KEY"  # Ex: DATAIA, ENG, etc
CONFLUENCE_PARENT_PAGE_ID = None  # ID da página pai (opcional, deixe None para criar na raiz)

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def markdown_to_confluence_html(markdown_content):
    """
    Converte Markdown para HTML compatível com Confluence
    """
    # Converte markdown para HTML
    html = markdown(markdown_content, extensions=['extra', 'codehilite', 'tables'])
    
    # Ajustes específicos do Confluence
    # Confluence usa <ac:structured-macro> para alguns elementos
    
    # Converter code blocks para Confluence code macro
    html = re.sub(
        r'<pre><code class="language-(\w+)">(.*?)</code></pre>',
        r'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">\1</ac:parameter><ac:parameter ac:name="theme">RDark</ac:parameter><ac:plain-text-body><![CDATA[\2]]></ac:plain-text-body></ac:structured-macro>',
        html,
        flags=re.DOTALL
    )
    
    # Converter code blocks simples
    html = re.sub(
        r'<pre><code>(.*?)</code></pre>',
        r'<ac:structured-macro ac:name="code"><ac:parameter ac:name="theme">RDark</ac:parameter><ac:plain-text-body><![CDATA[\1]]></ac:plain-text-body></ac:structured-macro>',
        html,
        flags=re.DOTALL
    )
    
    # Converter headers para Confluence
    html = re.sub(r'<h1>(.*?)</h1>', r'<h1>\1</h1>', html)
    html = re.sub(r'<h2>(.*?)</h2>', r'<h2>\1</h2>', html)
    
    return html


def get_page_title_from_file(file_path):
    """
    Extrai título da página do primeiro H1 do arquivo
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Procura primeiro H1
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        # Se não tem H1, usa nome do arquivo
        return Path(file_path).stem.replace('_', ' ').title()


def create_or_update_page(title, content_html, space_key, parent_id=None):
    """
    Cria ou atualiza página no Confluence
    """
    auth = HTTPBasicAuth(CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN)
    
    # Verifica se página já existe
    search_url = f"{CONFLUENCE_URL}/wiki/rest/api/content"
    search_params = {
        "spaceKey": space_key,
        "title": title,
        "expand": "version"
    }
    
    response = requests.get(search_url, auth=auth, params=search_params)
    
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            # Página existe, atualiza
            page_id = results[0]["id"]
            version = results[0]["version"]["number"] + 1
            
            update_url = f"{CONFLUENCE_URL}/wiki/rest/api/content/{page_id}"
            update_data = {
                "id": page_id,
                "type": "page",
                "title": title,
                "space": {"key": space_key},
                "body": {
                    "storage": {
                        "value": content_html,
                        "representation": "storage"
                    }
                },
                "version": {"number": version}
            }
            
            if parent_id:
                update_data["ancestors"] = [{"id": parent_id}]
            
            response = requests.put(update_url, auth=auth, json=update_data, headers={"Content-Type": "application/json"})
            
            if response.status_code == 200:
                print(f"✅ Atualizada: {title}")
                return response.json()
            else:
                print(f"❌ Erro ao atualizar {title}: {response.status_code} - {response.text}")
                return None
        else:
            # Página não existe, cria
            create_url = f"{CONFLUENCE_URL}/wiki/rest/api/content"
            create_data = {
                "type": "page",
                "title": title,
                "space": {"key": space_key},
                "body": {
                    "storage": {
                        "value": content_html,
                        "representation": "storage"
                    }
                }
            }
            
            if parent_id:
                create_data["ancestors"] = [{"id": parent_id}]
            
            response = requests.post(create_url, auth=auth, json=create_data, headers={"Content-Type": "application/json"})
            
            if response.status_code == 200:
                print(f"✅ Criada: {title}")
                return response.json()
            else:
                print(f"❌ Erro ao criar {title}: {response.status_code} - {response.text}")
                return None
    else:
        print(f"❌ Erro ao buscar página: {response.status_code} - {response.text}")
        return None


def upload_levels_to_confluence():
    """
    Faz upload de todos os arquivos de docs/levels/ para Confluence
    """
    levels_dir = Path(__file__).parent.parent / "levels"
    
    if not levels_dir.exists():
        print(f"❌ Diretório não encontrado: {levels_dir}")
        return
    
    # Lista arquivos markdown
    md_files = list(levels_dir.glob("*.md"))
    
    if not md_files:
        print(f"❌ Nenhum arquivo .md encontrado em {levels_dir}")
        return
    
    print(f"📤 Encontrados {len(md_files)} arquivos para upload\n")
    
    for md_file in sorted(md_files):
        print(f"📄 Processando: {md_file.name}")
        
        # Lê conteúdo
        with open(md_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Converte para HTML do Confluence
        html_content = markdown_to_confluence_html(markdown_content)
        
        # Extrai título
        title = get_page_title_from_file(md_file)
        
        # Cria/atualiza página
        result = create_or_update_page(
            title=title,
            content_html=html_content,
            space_key=CONFLUENCE_SPACE_KEY,
            parent_id=CONFLUENCE_PARENT_PAGE_ID
        )
        
        if result:
            page_url = f"{CONFLUENCE_URL}/wiki{result['_links']['webui']}"
            print(f"   🔗 {page_url}\n")
        else:
            print(f"   ❌ Falhou\n")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("🚀 Iniciando upload para Confluence...\n")
    print("⚠️  CERTIFIQUE-SE DE CONFIGURAR AS VARIÁVEIS NO INÍCIO DO SCRIPT!\n")
    
    # Verifica configuração
    if CONFLUENCE_URL == "https://seu-dominio.atlassian.net":
        print("❌ ERRO: Configure CONFLUENCE_URL no script!")
        sys.exit(1)
    
    if CONFLUENCE_USERNAME == "seu-email@exemplo.com":
        print("❌ ERRO: Configure CONFLUENCE_USERNAME no script!")
        sys.exit(1)
    
    if CONFLUENCE_API_TOKEN == "seu-api-token":
        print("❌ ERRO: Configure CONFLUENCE_API_TOKEN no script!")
        print("   💡 Gere em: Account Settings > Security > API tokens")
        sys.exit(1)
    
    if CONFLUENCE_SPACE_KEY == "SEU-SPACE-KEY":
        print("❌ ERRO: Configure CONFLUENCE_SPACE_KEY no script!")
        sys.exit(1)
    
    # Faz upload
    upload_levels_to_confluence()
    
    print("\n✅ Concluído!")
