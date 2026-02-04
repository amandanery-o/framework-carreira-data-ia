# 🚀 Setup Confluence - Passo a Passo Completo

Vamos configurar a sincronização automática juntos! Siga cada passo.

---

## ✅ PASSO 1: Gerar API Token do Confluence

### **1.1 Acesse a página de API Tokens**

Abra no navegador:
**https://id.atlassian.com/manage-profile/security/api-tokens**

### **1.2 Criar novo token**

1. Clique em **"Create API token"**
2. Dê um nome: `GitHub Actions - Framework Carreira`
3. Clique em **"Create"**
4. **COPIE O TOKEN** (você só verá uma vez!)
   - Exemplo: `ATATT3xFfGF0...` (é uma string longa)

### **1.3 Guarde o token**

Cole em algum lugar temporário (vamos usar depois).

---

## ✅ PASSO 2: Encontrar Space Key do Confluence

### **2.1 Acesse seu Confluence**

1. Vá para: `https://gupy.atlassian.net` (ou seu domínio)
2. Entre no Space onde quer criar as páginas

### **2.2 Encontrar Space Key**

1. No Confluence, vá em: **Space Settings** (ícone de engrenagem)
2. Clique em **"Space details"**
3. Procure por **"Space Key"**
   - Exemplo: `DATAIA`, `ENG`, `DEV`
4. **ANOTE O SPACE KEY**

---

## ✅ PASSO 3: Encontrar Parent Page ID (Opcional)

**Se você quer organizar as páginas dentro de uma página pai:**

1. Abra a página pai no Confluence
2. Olhe a URL do navegador
3. Procure por `pageId=123456789`
4. O número após `pageId=` é o ID
5. **ANOTE O ID** (ou deixe vazio se não quiser)

**Se não quiser página pai:** Pule este passo, deixe vazio.

---

## ✅ PASSO 4: Testar Conexão Localmente

Vamos testar ANTES de configurar no GitHub!

### **4.1 Instalar dependências**

Execute no terminal:

```bash
cd "/Users/amandanery/Workspace/trilha de carreira data & ia"
pip3 install requests markdown html2text
```

### **4.2 Rodar script de teste**

```bash
python3 .github/scripts/test_confluence_connection.py
```

O script vai perguntar:
1. URL do Confluence
2. Seu email/username
3. API Token (que você gerou no Passo 1)
4. Space Key (que você encontrou no Passo 2)
5. Parent Page ID (opcional)

**Se tudo der certo:** Você verá ✅ em todos os testes!

---

## ✅ PASSO 5: Configurar Secrets no GitHub

Agora vamos configurar no GitHub para funcionar automaticamente!

### **5.1 Acessar Secrets do Repositório**

1. Vá para: **https://github.com/amandanery-o/framework-carreira-data-ia**
2. Clique em **Settings** (no topo do repositório)
3. No menu lateral, clique em **Secrets and variables** → **Actions**

### **5.2 Adicionar cada Secret**

Clique em **"New repository secret"** para cada um:

#### **Secret 1: CONFLUENCE_URL**
```
Name: CONFLUENCE_URL
Value: https://gupy.atlassian.net
```
*(Substitua pelo seu domínio)*

#### **Secret 2: CONFLUENCE_USERNAME**
```
Name: CONFLUENCE_USERNAME
Value: seu-email@gupy.com
```
*(Seu email de acesso ao Confluence)*

#### **Secret 3: CONFLUENCE_API_TOKEN**
```
Name: CONFLUENCE_API_TOKEN
Value: [cole o token que você gerou no Passo 1]
```

#### **Secret 4: CONFLUENCE_SPACE_KEY**
```
Name: CONFLUENCE_SPACE_KEY
Value: DATAIA
```
*(O Space Key que você encontrou no Passo 2)*

#### **Secret 5: CONFLUENCE_PARENT_PAGE_ID** (Opcional)
```
Name: CONFLUENCE_PARENT_PAGE_ID
Value: 123456789
```
*(O ID que você encontrou no Passo 3, ou deixe vazio)*

**⚠️ IMPORTANTE:** Nomes dos secrets devem ser EXATOS (case-sensitive)!

---

## ✅ PASSO 6: Testar Sincronização Automática

### **6.1 Fazer alteração de teste**

Edite qualquer arquivo em `docs/levels/`:

```bash
cd "/Users/amandanery/Workspace/trilha de carreira data & ia"
# Edite docs/levels/SE_I_junior.md (adicione um espaço ou comentário)
```

### **6.2 Commit e Push**

```bash
git add docs/levels/
git commit -m "test: sincronização automática Confluence"
git push origin main
```

### **6.3 Verificar no GitHub Actions**

1. Vá para: **https://github.com/amandanery-o/framework-carreira-data-ia/actions**
2. Você verá um workflow **"Sync to Confluence"** rodando
3. Clique nele para ver logs
4. Se tudo der certo: ✅ verde!

### **6.4 Verificar no Confluence**

1. Abra seu Confluence
2. Vá para o Space configurado
3. Você deve ver as páginas criadas/atualizadas!

---

## ✅ PASSO 7: Testar Manualmente (Opcional)

Se quiser testar sem fazer push:

1. Vá para: **https://github.com/amandanery-o/framework-carreira-data-ia/actions**
2. Clique em **"Sync to Confluence"** (workflow)
3. Clique em **"Run workflow"** (botão no topo direito)
4. Selecione branch `main`
5. Clique em **"Run workflow"**
6. Aguarde e veja os logs!

---

## 🎉 Pronto!

Agora **sempre que você fizer push** em arquivos de `docs/levels/`, o Confluence será atualizado automaticamente!

---

## 🚨 Se algo der errado

### **Erro no teste local:**
- Verifique se API Token está correto
- Verifique se Space Key está correto
- Verifique se usuário tem permissão no Space

### **Erro no GitHub Actions:**
- Verifique se todos os secrets estão configurados
- Verifique logs do workflow em Actions
- Verifique se nomes dos secrets estão corretos (case-sensitive)

### **Páginas não aparecem:**
- Verifique logs do GitHub Actions
- Verifique se Space Key está correto
- Verifique permissões do usuário

---

## 📞 Precisa de ajuda?

Veja mais detalhes em: `.github/CONFLUENCE_SETUP.md`

---

**Vamos começar pelo Passo 1? Me avise quando estiver pronto!** 🚀
