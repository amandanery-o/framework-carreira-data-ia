#!/bin/bash
# Script para criar secrets no GitHub automaticamente usando gh CLI

echo "🔐 Configurando Secrets no GitHub"
echo "=================================="
echo ""

REPO="amandanery-o/framework-carreira-data-ia"

# Valores que você usou no teste manual
read -p "1. URL do Confluence (ex: https://gupy.atlassian.net): " CONFLUENCE_URL
read -p "2. Seu email/username: " CONFLUENCE_USERNAME
read -p "3. Space Key (ex: DATAIA): " CONFLUENCE_SPACE_KEY
read -p "4. Parent Page ID (opcional, deixe vazio): " PARENT_PAGE_ID

# API Token já temos
CONFLUENCE_API_TOKEN="ATATT3xFfGF0UxDpS3ZQThQlDIuSXPyYUo8RlKNM1ROoTAZcL_-3VmItfgP7hMnm8p5i7qkfO1lK_wbuCiP1h3vrFP7x2gizwe-hIHxV_n9WGMHR_JfnXidHsZXyZdH3JxFsoK7wauAgDO88kD7SBnHNQJNwN7F2wCCGJww4LhUH61WD49xU5dA=043E0A6C"

echo ""
echo "📤 Criando secrets no GitHub..."
echo ""

# Criar cada secret
echo "1. Criando CONFLUENCE_URL..."
echo "$CONFLUENCE_URL" | gh secret set CONFLUENCE_URL --repo "$REPO"

echo "2. Criando CONFLUENCE_USERNAME..."
echo "$CONFLUENCE_USERNAME" | gh secret set CONFLUENCE_USERNAME --repo "$REPO"

echo "3. Criando CONFLUENCE_API_TOKEN..."
echo "$CONFLUENCE_API_TOKEN" | gh secret set CONFLUENCE_API_TOKEN --repo "$REPO"

echo "4. Criando CONFLUENCE_SPACE_KEY..."
echo "$CONFLUENCE_SPACE_KEY" | gh secret set CONFLUENCE_SPACE_KEY --repo "$REPO"

if [ -n "$PARENT_PAGE_ID" ]; then
    echo "5. Criando CONFLUENCE_PARENT_PAGE_ID..."
    echo "$PARENT_PAGE_ID" | gh secret set CONFLUENCE_PARENT_PAGE_ID --repo "$REPO"
else
    echo "5. Pulando CONFLUENCE_PARENT_PAGE_ID (vazio)"
fi

echo ""
echo "✅ Secrets criados com sucesso!"
echo ""
echo "🧪 Agora vamos testar:"
echo "   1. Vá para: https://github.com/$REPO/actions"
echo "   2. Clique em 'Sync to Confluence'"
echo "   3. Clique em 'Run workflow'"
echo "   4. Selecione branch 'main'"
echo "   5. Clique em 'Run workflow'"
echo ""
