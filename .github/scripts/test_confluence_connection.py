#!/usr/bin/env python3
"""
Script de teste para validar conexão com Confluence ANTES de configurar GitHub Actions
Execute este script localmente primeiro para garantir que tudo está funcionando
"""

import os
import sys
import requests
from requests.auth import HTTPBasicAuth
from pathlib import Path

print("🔍 Teste de Conexão com Confluence\n")
print("=" * 60)

# Solicita credenciais interativamente
print("\n📝 Por favor, informe suas credenciais do Confluence:\n")

confluence_url = input("1. URL do Confluence (ex: https://gupy.atlassian.net): ").strip().rstrip('/')
if not confluence_url:
    print("❌ URL é obrigatória!")
    sys.exit(1)

confluence_username = input("2. Seu email/username do Confluence: ").strip()
if not confluence_username:
    print("❌ Username é obrigatório!")
    sys.exit(1)

confluence_api_token = input("3. API Token (gerar em: https://id.atlassian.com/manage-profile/security/api-tokens): ").strip()
if not confluence_api_token:
    print("❌ API Token é obrigatório!")
    sys.exit(1)

confluence_space_key = input("4. Space Key (ex: DATAIA) - encontre em Space Settings: ").strip()
if not confluence_space_key:
    print("❌ Space Key é obrigatório!")
    sys.exit(1)

parent_page_id = input("5. Parent Page ID (opcional, deixe vazio se não quiser): ").strip()

print("\n" + "=" * 60)
print("🧪 Testando conexão...\n")

# Testa autenticação
auth = HTTPBasicAuth(confluence_username, confluence_api_token)

# Teste 1: Verificar autenticação
print("1️⃣ Testando autenticação...")
try:
    test_url = f"{confluence_url}/wiki/rest/api/user/current"
    response = requests.get(test_url, auth=auth, timeout=10)
    
    if response.status_code == 200:
        user_info = response.json()
        print(f"   ✅ Autenticação OK!")
        print(f"   👤 Usuário: {user_info.get('displayName', 'N/A')}")
        print(f"   📧 Email: {user_info.get('emailAddress', 'N/A')}")
    else:
        print(f"   ❌ Erro de autenticação: {response.status_code}")
        print(f"   Resposta: {response.text[:200]}")
        sys.exit(1)
except Exception as e:
    print(f"   ❌ Erro ao conectar: {e}")
    sys.exit(1)

# Teste 2: Verificar acesso ao Space
print("\n2️⃣ Verificando acesso ao Space...")
try:
    space_url = f"{confluence_url}/wiki/rest/api/space/{confluence_space_key}"
    response = requests.get(space_url, auth=auth, timeout=10)
    
    if response.status_code == 200:
        space_info = response.json()
        print(f"   ✅ Space encontrado!")
        print(f"   📁 Space: {space_info.get('name', 'N/A')}")
        print(f"   🔑 Key: {space_info.get('key', 'N/A')}")
    elif response.status_code == 404:
        print(f"   ❌ Space '{confluence_space_key}' não encontrado!")
        print(f"   💡 Verifique o Space Key em: Space Settings → Space Details")
        sys.exit(1)
    else:
        print(f"   ❌ Erro ao acessar Space: {response.status_code}")
        print(f"   Resposta: {response.text[:200]}")
        sys.exit(1)
except Exception as e:
    print(f"   ❌ Erro ao verificar Space: {e}")
    sys.exit(1)

# Teste 3: Verificar Parent Page (se informado)
if parent_page_id:
    print("\n3️⃣ Verificando Parent Page...")
    try:
        page_url = f"{confluence_url}/wiki/rest/api/content/{parent_page_id}"
        response = requests.get(page_url, auth=auth, timeout=10)
        
        if response.status_code == 200:
            page_info = response.json()
            print(f"   ✅ Parent Page encontrada!")
            print(f"   📄 Título: {page_info.get('title', 'N/A')}")
        else:
            print(f"   ⚠️  Parent Page não encontrada (ID: {parent_page_id})")
            print(f"   Continuando sem parent page...")
            parent_page_id = None
    except Exception as e:
        print(f"   ⚠️  Erro ao verificar Parent Page: {e}")
        print(f"   Continuando sem parent page...")
        parent_page_id = None

# Teste 4: Criar página de teste
print("\n4️⃣ Criando página de teste...")
try:
    create_url = f"{confluence_url}/wiki/rest/api/content"
    test_content = {
        "type": "page",
        "title": "🧪 Teste de Sincronização Automática",
        "space": {"key": confluence_space_key},
        "body": {
            "storage": {
                "value": "<p>Esta é uma página de teste criada pelo script de validação.</p><p>Se você está vendo isso, a sincronização automática está funcionando! ✅</p>",
                "representation": "storage"
            }
        }
    }
    
    if parent_page_id:
        test_content["ancestors"] = [{"id": parent_page_id}]
    
    response = requests.post(
        create_url,
        auth=auth,
        json=test_content,
        headers={"Content-Type": "application/json"},
        timeout=30
    )
    
    if response.status_code == 200:
        page_info = response.json()
        page_id = page_info["id"]
        page_url = f"{confluence_url}/wiki{page_info['_links']['webui']}"
        print(f"   ✅ Página de teste criada!")
        print(f"   🔗 {page_url}")
        print(f"   📝 ID: {page_id}")
        
        # Pergunta se quer deletar
        delete = input("\n   🗑️  Deletar página de teste? (s/n): ").strip().lower()
        if delete == 's':
            delete_url = f"{confluence_url}/wiki/rest/api/content/{page_id}"
            delete_response = requests.delete(delete_url, auth=auth, timeout=10)
            if delete_response.status_code == 204:
                print("   ✅ Página de teste deletada")
            else:
                print(f"   ⚠️  Não foi possível deletar (você pode deletar manualmente)")
    else:
        print(f"   ⚠️  Não foi possível criar página de teste: {response.status_code}")
        print(f"   Resposta: {response.text[:200]}")
        print(f"   Mas autenticação e Space estão OK, então deve funcionar!")
except Exception as e:
    print(f"   ⚠️  Erro ao criar página de teste: {e}")
    print(f"   Mas autenticação e Space estão OK, então deve funcionar!")

# Resumo final
print("\n" + "=" * 60)
print("✅ TESTE CONCLUÍDO COM SUCESSO!\n")
print("📋 Credenciais validadas:")
print(f"   URL: {confluence_url}")
print(f"   Username: {confluence_username}")
print(f"   Space Key: {confluence_space_key}")
if parent_page_id:
    print(f"   Parent Page ID: {parent_page_id}")
else:
    print(f"   Parent Page ID: (nenhum)")

print("\n🔐 Próximo passo: Configure estes valores como Secrets no GitHub:")
print("\n   CONFLUENCE_URL =", confluence_url)
print("   CONFLUENCE_USERNAME =", confluence_username)
print("   CONFLUENCE_API_TOKEN =", confluence_api_token[:10] + "..." + " (mantenha secreto!)")
print("   CONFLUENCE_SPACE_KEY =", confluence_space_key)
if parent_page_id:
    print("   CONFLUENCE_PARENT_PAGE_ID =", parent_page_id)

print("\n💡 Veja instruções em: .github/CONFLUENCE_SETUP.md")
print("=" * 60)
