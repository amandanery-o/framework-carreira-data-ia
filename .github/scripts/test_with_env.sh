#!/bin/bash
# Script para testar conexão usando variáveis de ambiente

echo "🧪 Teste de Conexão com Confluence"
echo "===================================="
echo ""
echo "Configure as variáveis abaixo e execute este script:"
echo ""
echo "export CONFLUENCE_URL='https://gupy.atlassian.net'"
echo "export CONFLUENCE_USERNAME='seu-email@gupy.com'"
echo "export CONFLUENCE_API_TOKEN='seu-token-aqui'"
echo "export CONFLUENCE_SPACE_KEY='DATAIA'"
echo "export CONFLUENCE_PARENT_PAGE_ID=''"
echo ""
echo "Ou edite este script e configure diretamente abaixo:"
echo ""

# ============================================
# CONFIGURE AQUI SUAS CREDENCIAIS
# ============================================

CONFLUENCE_URL="${CONFLUENCE_URL:-https://gupy.atlassian.net}"
CONFLUENCE_USERNAME="${CONFLUENCE_USERNAME:-}"
CONFLUENCE_API_TOKEN="${CONFLUENCE_API_TOKEN:-ATATT3xFfGF0UxDpS3ZQThQlDIuSXPyYUo8RlKNM1ROoTAZcL_-3VmItfgP7hMnm8p5i7qkfO1lK_wbuCiP1h3vrFP7x2gizwe-hIHxV_n9WGMHR_JfnXidHsZXyZdH3JxFsoK7wauAgDO88kD7SBnHNQJNwN7F2wCCGJww4LhUH61WD49xU5dA=043E0A6C}"
CONFLUENCE_SPACE_KEY="${CONFLUENCE_SPACE_KEY:-}"
CONFLUENCE_PARENT_PAGE_ID="${CONFLUENCE_PARENT_PAGE_ID:-}"

# ============================================

if [ -z "$CONFLUENCE_USERNAME" ]; then
    echo "❌ Configure CONFLUENCE_USERNAME"
    exit 1
fi

if [ -z "$CONFLUENCE_SPACE_KEY" ]; then
    echo "❌ Configure CONFLUENCE_SPACE_KEY"
    exit 1
fi

echo "🔍 Testando conexão..."
echo ""

python3 <<EOF
import os
import sys
import requests
from requests.auth import HTTPBasicAuth

CONFLUENCE_URL = "$CONFLUENCE_URL"
CONFLUENCE_USERNAME = "$CONFLUENCE_USERNAME"
CONFLUENCE_API_TOKEN = "$CONFLUENCE_API_TOKEN"
CONFLUENCE_SPACE_KEY = "$CONFLUENCE_SPACE_KEY"
CONFLUENCE_PARENT_PAGE_ID = "$CONFLUENCE_PARENT_PAGE_ID" if "$CONFLUENCE_PARENT_PAGE_ID" else None

auth = HTTPBasicAuth(CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN)

# Teste 1: Autenticação
print("1️⃣ Testando autenticação...")
try:
    response = requests.get(f"{CONFLUENCE_URL}/wiki/rest/api/user/current", auth=auth, timeout=10)
    if response.status_code == 200:
        user_info = response.json()
        print(f"   ✅ Autenticação OK!")
        print(f"   👤 Usuário: {user_info.get('displayName', 'N/A')}")
    else:
        print(f"   ❌ Erro: {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"   ❌ Erro: {e}")
    sys.exit(1)

# Teste 2: Space
print("\n2️⃣ Verificando Space...")
try:
    response = requests.get(f"{CONFLUENCE_URL}/wiki/rest/api/space/{CONFLUENCE_SPACE_KEY}", auth=auth, timeout=10)
    if response.status_code == 200:
        space_info = response.json()
        print(f"   ✅ Space encontrado: {space_info.get('name', 'N/A')}")
    else:
        print(f"   ❌ Space não encontrado: {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"   ❌ Erro: {e}")
    sys.exit(1)

print("\n✅ Tudo OK! Credenciais validadas!")
print(f"\n📋 Configure no GitHub Secrets:")
print(f"   CONFLUENCE_URL = {CONFLUENCE_URL}")
print(f"   CONFLUENCE_USERNAME = {CONFLUENCE_USERNAME}")
print(f"   CONFLUENCE_API_TOKEN = {CONFLUENCE_API_TOKEN[:20]}...")
print(f"   CONFLUENCE_SPACE_KEY = {CONFLUENCE_SPACE_KEY}")
EOF
