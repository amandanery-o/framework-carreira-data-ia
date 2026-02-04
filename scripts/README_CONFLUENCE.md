# 📤 Upload para Confluence - Guia Rápido

Este guia te ajuda a fazer upload dos arquivos de **docs/levels/** para o Confluence de forma automatizada.

---

## 🚀 Opção 1: Script Python (Recomendado)

### **Passo 1: Instalar dependências**

```bash
cd scripts/
pip install -r requirements_confluence.txt
```

### **Passo 2: Gerar API Token do Confluence**

1. Acesse: https://id.atlassian.com/manage-profile/security/api-tokens
2. Clique em **"Create API token"**
3. Dê um nome (ex: "Upload Script")
4. Copie o token gerado

### **Passo 3: Configurar o script**

Edite `confluence_upload.py` e ajuste:

```python
CONFLUENCE_URL = "https://gupy.atlassian.net"  # Seu domínio
CONFLUENCE_USERNAME = "seu-email@gupy.com"
CONFLUENCE_API_TOKEN = "seu-token-aqui"
CONFLUENCE_SPACE_KEY = "DATAIA"  # Ou o space key do seu Confluence
CONFLUENCE_PARENT_PAGE_ID = None  # Ou ID da página pai se quiser organizar
```

### **Passo 4: Executar**

```bash
python scripts/confluence_upload.py
```

**Pronto!** Todos os arquivos de `docs/levels/` serão criados/atualizados no Confluence.

---

## 🎯 Opção 2: Usar Ferramenta Pronta (Mais Simples)

### **Confluence Publisher (VS Code Extension)**

1. Instale extensão: **"Confluence Publisher"** no VS Code
2. Configure credenciais
3. Selecione arquivos e publique

### **Markdown to Confluence (Online)**

1. Acesse: https://markdown-to-confluence.atlassian.net/
2. Cole seu markdown
3. Copie HTML gerado
4. Cole no Confluence (modo de edição)

---

## 📋 Opção 3: Manual (Se preferir controle total)

### **Passo a passo:**

1. **Abra arquivo** em `docs/levels/` (ex: `SE_I_junior.md`)
2. **Copie conteúdo** completo
3. **No Confluence:**
   - Criar nova página
   - Colar conteúdo
   - Confluence converte markdown automaticamente!
4. **Ajustar formatação** se necessário
5. **Repetir** para cada arquivo

**Dica:** Confluence tem suporte nativo a Markdown! Só colar e funciona.

---

## 🔧 Troubleshooting

### **Erro de autenticação**
- Verifique API token
- Verifique username (deve ser email completo)
- Verifique permissões no Confluence

### **Erro de Space Key**
- Encontre o Space Key em: Space Settings > Space Details
- Geralmente é maiúsculo (ex: DATAIA, ENG)

### **Formatação não ficou boa**
- Confluence pode não renderizar alguns elementos markdown
- Ajuste manualmente após upload
- Ou use HTML direto no script

---

## 💡 Dicas

- **Teste com 1 arquivo primeiro** antes de fazer todos
- **Backup:** Confluence mantém histórico de versões
- **Organização:** Use `CONFLUENCE_PARENT_PAGE_ID` para criar hierarquia
- **Atualizações:** Script atualiza páginas existentes automaticamente

---

## 📚 Próximos Passos

Depois de fazer upload dos levels, você pode:

1. Fazer upload de `docs/competencies/`
2. Fazer upload de `docs/tracks/`
3. Criar índice/página principal
4. Organizar em hierarquia

---

**Precisa de ajuda?** Ajuste o script conforme sua necessidade!
