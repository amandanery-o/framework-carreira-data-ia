Este guia configura a sincronização automática: **sempre que você fizer push no git, o Confluence será atualizado automaticamente!**

---

## 🎯 Como Funciona

1. Você faz push no git (ex: `git push origin main`)
2. GitHub Actions detecta mudanças em `docs/levels/`
3. Script Python roda automaticamente
4. Páginas são criadas/atualizadas no Confluence
5. ✅ Pronto! Confluence sempre sincronizado com git

---

## ⚙️ Configuração (Uma vez apenas)

### **Passo 1: Gerar API Token do Confluence**

1. Acesse: https://id.atlassian.com/manage-profile/security/api-tokens
2. Clique em **"Create API token"**
3. Dê um nome (ex: "GitHub Actions Sync")
4. **Copie o token** (você só verá uma vez!)

### **Passo 2: Configurar Secrets no GitHub**

1. Vá para seu repositório: https://github.com/amandanery-o/framework-carreira-data-ia
2. **Settings** → **Secrets and variables** → **Actions**
3. Clique em **"New repository secret"**
4. Adicione os seguintes secrets:

#### **Secret 1: CONFLUENCE_URL**
```
Name: CONFLUENCE_URL
Value: https://gupy.atlassian.net
```
*(Substitua pelo seu domínio do Confluence)*

#### **Secret 2: CONFLUENCE_USERNAME**
```
Name: CONFLUENCE_USERNAME
Value: seu-email@gupy.com
```
*(Seu email de acesso ao Confluence)*

#### **Secret 3: CONFLUENCE_API_TOKEN**
```
Name: CONFLUENCE_API_TOKEN
Value: [cole o token gerado no Passo 1]
```

#### **Secret 4: CONFLUENCE_SPACE_KEY**
```
Name: CONFLUENCE_SPACE_KEY
Value: DATAIA
```
*(Encontre em: Space Settings → Space Details → Space Key)*

#### **Secret 5: CONFLUENCE_PARENT_PAGE_ID (Opcional)**
```
Name: CONFLUENCE_PARENT_PAGE_ID
Value: 123456789
```
*(ID da página pai se quiser organizar em hierarquia. Deixe vazio se não quiser)*

**Como encontrar Parent Page ID:**
- Abra a página no Confluence
- Olhe a URL: `.../pages/viewpage.action?pageId=123456789`
- O número após `pageId=` é o ID

---

## ✅ Testar

### **Teste 1: Push manual**

1. Faça uma pequena alteração em qualquer arquivo de `docs/levels/`
2. Commit e push:
   ```bash
   git add docs/levels/
   git commit -m "test: sincronização Confluence"
   git push origin main
   ```
3. Vá para **Actions** no GitHub
4. Veja o workflow rodando
5. Verifique se página foi atualizada no Confluence

### **Teste 2: Rodar manualmente**

1. Vá para **Actions** no GitHub
2. Clique em **"Sync to Confluence"**
3. Clique em **"Run workflow"**
4. Selecione branch `main`
5. Clique em **"Run workflow"**

---

## 🔍 Monitoramento

### **Ver logs do workflow:**

1. GitHub → **Actions**
2. Clique no workflow que rodou
3. Clique no job **"Sync Levels to Confluence"**
4. Veja logs detalhados

### **Verificar no Confluence:**

- Páginas criadas/atualizadas aparecem automaticamente
- Links são exibidos nos logs do GitHub Actions

---

## 🚨 Troubleshooting

### **Erro: "Variáveis de ambiente não configuradas"**
- ✅ Verifique se todos os secrets estão configurados
- ✅ Nomes dos secrets devem ser EXATOS (case-sensitive)

### **Erro: "401 Unauthorized"**
- ✅ Verifique CONFLUENCE_USERNAME (deve ser email completo)
- ✅ Verifique CONFLUENCE_API_TOKEN (gere novo se necessário)
- ✅ Verifique se usuário tem permissão no Space

### **Erro: "404 Space not found"**
- ✅ Verifique CONFLUENCE_SPACE_KEY (case-sensitive)
- ✅ Verifique se Space Key está correto em Space Settings

### **Páginas não estão sendo criadas**
- ✅ Verifique logs do GitHub Actions
- ✅ Verifique permissões do usuário no Confluence
- ✅ Verifique se CONFLUENCE_URL está correto (sem barra final)

### **Formatação não ficou boa**
- ✅ Confluence pode não renderizar alguns elementos markdown
- ✅ Ajuste manualmente após primeira sincronização
- ✅ Próximas atualizações manterão suas edições manuais

---

## 📋 O que é sincronizado

**Arquivos sincronizados automaticamente:**
- ✅ Todos os `.md` em `docs/levels/`

**Quando sincroniza:**
- ✅ Push para branch `main`
- ✅ Mudanças em arquivos de `docs/levels/`
- ✅ Execução manual via GitHub Actions

**O que NÃO sincroniza automaticamente:**
- ❌ Arquivos em outras pastas (docs/competencies, docs/tracks, etc)
- ❌ Mudanças em outras branches

---

## 🔧 Customizar

### **Sincronizar outras pastas:**

Edite `.github/workflows/confluence-sync.yml`:

```yaml
paths:
  - 'docs/levels/**'
  - 'docs/competencies/**'      # Adicione aqui
  - 'docs/tracks/**'           # Adicione aqui
```

### **Sincronizar em outras branches:**

Edite `.github/workflows/confluence-sync.yml`:

```yaml
branches:
  - main
  - develop              # Adicione aqui
```

---

## 💡 Dicas

- **Primeira execução:** Pode demorar mais (cria todas as páginas)
- **Atualizações:** São rápidas (apenas atualiza páginas existentes)
- **Histórico:** Confluence mantém histórico de versões automaticamente
- **Edições manuais:** Se você editar manualmente no Confluence, serão preservadas até próxima sincronização

---

## ✅ Checklist de Setup

- [ ] API Token do Confluence gerado
- [ ] CONFLUENCE_URL configurado no GitHub Secrets
- [ ] CONFLUENCE_USERNAME configurado
- [ ] CONFLUENCE_API_TOKEN configurado
- [ ] CONFLUENCE_SPACE_KEY configurado
- [ ] CONFLUENCE_PARENT_PAGE_ID configurado (opcional)
- [ ] Teste feito com push
- [ ] Workflow rodou com sucesso
- [ ] Páginas apareceram no Confluence

---

**Pronto! Agora seu Confluence sempre estará sincronizado com o git! 🎉**
