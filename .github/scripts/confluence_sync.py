#!/usr/bin/env python3
"""
Script para sincronizar arquivos Markdown com Confluence
Usado pelo GitHub Actions para atualização automática
"""

import os
import sys
import requests
from pathlib import Path
from requests.auth import HTTPBasicAuth
import re
from markdown import markdown

# Variáveis de ambiente (configuradas no GitHub Secrets)
CONFLUENCE_URL = os.getenv("CONFLUENCE_URL", "").rstrip('/')
CONFLUENCE_USERNAME = os.getenv("CONFLUENCE_USERNAME", "")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN", "")
CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")
CONFLUENCE_PARENT_PAGE_ID = os.getenv("CONFLUENCE_PARENT_PAGE_ID", "")

# Verifica configuração
if not all([CONFLUENCE_URL, CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN, CONFLUENCE_SPACE_KEY]):
    print("❌ ERRO: Variáveis de ambiente não configuradas!")
    print("   Configure os secrets no GitHub:")
    print("   - CONFLUENCE_URL")
    print("   - CONFLUENCE_USERNAME")
    print("   - CONFLUENCE_API_TOKEN")
    print("   - CONFLUENCE_SPACE_KEY")
    sys.exit(1)


def markdown_to_confluence_html(markdown_content):
    """
    Converte Markdown para HTML compatível com Confluence Storage Format
    """
    # Converte markdown para HTML
    html = markdown(markdown_content, extensions=['extra', 'codehilite', 'tables', 'fenced_code'])
    
    # Confluence Storage Format usa <ac:structured-macro> para code blocks
    # Converte code blocks para formato Confluence
    html = re.sub(
        r'<pre><code class="language-(\w+)">(.*?)</code></pre>',
        lambda m: f'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">{m.group(1)}</ac:parameter><ac:parameter ac:name="theme">RDark</ac:parameter><ac:plain-text-body><![CDATA[{m.group(2)}]]></ac:plain-text-body></ac:structured-macro>',
        html,
        flags=re.DOTALL
    )
    
    # Code blocks sem linguagem
    html = re.sub(
        r'<pre><code>(.*?)</code></pre>',
        lambda m: f'<ac:structured-macro ac:name="code"><ac:parameter ac:name="theme">RDark</ac:parameter><ac:plain-text-body><![CDATA[{m.group(1)}]]></ac:plain-text-body></ac:structured-macro>',
        html,
        flags=re.DOTALL
    )
    
    # Converte emojis para texto (Confluence pode não renderizar)
    emoji_map = {
        '📋': '📋',
        '🎯': '🎯',
        '🏆': '🏆',
        '🌟': '🌟',
        '🌳': '🌳',
        '🌈': '🌈',
    }
    
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


def find_existing_page(title, space_key, auth):
    """
    Busca página existente no Confluence
    """
    search_url = f"{CONFLUENCE_URL}/wiki/rest/api/content"
    search_params = {
        "spaceKey": space_key,
        "title": title,
        "expand": "version,ancestors"
    }
    
    try:
        response = requests.get(search_url, auth=auth, params=search_params, timeout=10)
        if response.status_code == 200:
            results = response.json().get("results", [])
            if results:
                return results[0]
        return None
    except Exception as e:
        print(f"⚠️  Erro ao buscar página '{title}': {e}")
        return None


def create_page(title, content_html, space_key, parent_id, auth):
    """
    Cria nova página no Confluence
    """
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
    
    try:
        response = requests.post(
            create_url,
            auth=auth,
            json=create_data,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Erro ao criar '{title}': {response.status_code}")
            print(f"   Resposta: {response.text[:200]}")
            return None
    except Exception as e:
        print(f"❌ Erro ao criar '{title}': {e}")
        return None


def update_page(page_id, title, content_html, version, auth):
    """
    Atualiza página existente no Confluence
    """
    update_url = f"{CONFLUENCE_URL}/wiki/rest/api/content/{page_id}"
    update_data = {
        "id": page_id,
        "type": "page",
        "title": title,
        "body": {
            "storage": {
                "value": content_html,
                "representation": "storage"
            }
        },
        "version": {"number": version + 1}
    }
    
    try:
        response = requests.put(
            update_url,
            auth=auth,
            json=update_data,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Erro ao atualizar '{title}': {response.status_code}")
            print(f"   Resposta: {response.text[:200]}")
            return None
    except Exception as e:
        print(f"❌ Erro ao atualizar '{title}': {e}")
        return None


def sync_file_to_confluence(file_path, space_key, parent_id, auth):
    """
    Sincroniza um arquivo markdown com Confluence
    """
    # Lê conteúdo
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except Exception as e:
        print(f"❌ Erro ao ler {file_path}: {e}")
        return False
    
    # Converte para HTML
    html_content = markdown_to_confluence_html(markdown_content)
    
    # Extrai título
    title = get_page_title_from_file(file_path)
    
    # Busca página existente
    existing_page = find_existing_page(title, space_key, auth)
    
    if existing_page:
        # Atualiza página existente
        page_id = existing_page["id"]
        version = existing_page["version"]["number"]
        
        result = update_page(page_id, title, html_content, version, auth)
        
        if result:
            page_url = f"{CONFLUENCE_URL}/wiki{result['_links']['webui']}"
            print(f"✅ Atualizada: {title}")
            print(f"   🔗 {page_url}")
            return True
        else:
            return False
    else:
        # Cria nova página
        result = create_page(title, html_content, space_key, parent_id, auth)
        
        if result:
            page_url = f"{CONFLUENCE_URL}/wiki{result['_links']['webui']}"
            print(f"✅ Criada: {title}")
            print(f"   🔗 {page_url}")
            return True
        else:
            return False


def main():
    """
    Função principal
    """
    print("🚀 Iniciando sincronização com Confluence...\n")
    
    # Setup
    auth = HTTPBasicAuth(CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN)
    parent_id = CONFLUENCE_PARENT_PAGE_ID if CONFLUENCE_PARENT_PAGE_ID else None
    
    # Busca arquivos para sincronizar
    # Primeiro tenta docs/levels/, depois levels/
    levels_dirs = [
        Path("docs/levels"),
        Path("levels")
    ]
    
    md_files = []
    for levels_dir in levels_dirs:
        if levels_dir.exists():
            md_files.extend(list(levels_dir.glob("*.md")))
    
    if not md_files:
        print("⚠️  Nenhum arquivo .md encontrado em levels/ ou docs/levels/")
        return
    
    print(f"📤 Encontrados {len(md_files)} arquivos para sincronizar\n")
    
    # Sincroniza cada arquivo
    success_count = 0
    for md_file in sorted(md_files):
        print(f"📄 Processando: {md_file.name}")
        
        if sync_file_to_confluence(md_file, CONFLUENCE_SPACE_KEY, parent_id, auth):
            success_count += 1
        print()
    
    # Resumo
    print(f"\n{'='*50}")
    print(f"✅ Sincronização concluída!")
    print(f"   Sucesso: {success_count}/{len(md_files)}")
    print(f"{'='*50}")
    
    if success_count < len(md_files):
        sys.exit(1)


if __name__ == "__main__":
    main()
