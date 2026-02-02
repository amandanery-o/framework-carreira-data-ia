# ✅ Configurar Secrets no GitHub - Passo a Passo

O teste manual funcionou! Agora vamos configurar para funcionar automaticamente.

---

## 🎯 PASSO 1: Acessar Secrets do GitHub

1. Abra no navegador:
   **https://github.com/amandanery-o/framework-carreira-data-ia/settings/secrets/actions**

2. Você verá a página de **"Secrets and variables"** → **"Actions"**

---

## 🔐 PASSO 2: Adicionar cada Secret

Clique em **"New repository secret"** para cada um abaixo:

### **Secret 1: CONFLUENCE_URL**

```
Name: CONFLUENCE_URL
Value: [cole a URL que você usou no teste, ex: https://gupy.atlassian.net]
```

**⚠️ IMPORTANTE:** Sem barra `/` no final!

---

### **Secret 2: CONFLUENCE_USERNAME**

```
Name: CONFLUENCE_USERNAME
Value: [seu email que você usou no teste]
```

---

### **Secret 3: CONFLUENCE_API_TOKEN**

```
Name: CONFLUENCE_API_TOKEN
Value: ATATT3xFfGF0UxDpS3ZQThQlDIuSXPyYUo8RlKNM1ROoTAZcL_-3VmItfgP7hMnm8p5i7qkfO1lK_wbuCiP1h3vrFP7x2gizwe-hIHxV_n9WGMHR_JfnXidHsZXyZdH3JxFsoK7wauAgDO88kD7SBnHNQJNwN7F2wCCGJww4LhUH61WD49xU5dA=043E0A6C
```

---

### **Secret 4: CONFLUENCE_SPACE_KEY**

```
Name: CONFLUENCE_SPACE_KEY
Value: [o Space Key que você usou no teste, ex: DATAIA]
```

---

### **Secret 5: CONFLUENCE_PARENT_PAGE_ID** (Opcional)

```
Name: CONFLUENCE_PARENT_PAGE_ID
Value: [deixe vazio se não usou, ou cole o ID se usou]
```

**Se você não usou Parent Page no teste:** Deixe este secret vazio ou não crie ele.

---

## ✅ PASSO 3: Verificar Secrets Criados

Você deve ter criado **4 ou 5 secrets**:

- ✅ CONFLUENCE_URL
- ✅ CONFLUENCE_USERNAME
- ✅ CONFLUENCE_API_TOKEN
- ✅ CONFLUENCE_SPACE_KEY
- ✅ CONFLUENCE_PARENT_PAGE_ID (opcional)

---

## 🧪 PASSO 4: Testar Sincronização Automática

### **Opção A: Push de teste**

1. Faça uma pequena alteração em qualquer arquivo de `levels/`:
   ```bash
   # Edite levels/SE_I_junior.md (adicione um espaço ou comentário)
   ```

2. Commit e push:
   ```bash
   git add levels/
   git commit -m "test: sincronização automática Confluence"
   git push origin main
   ```

3. Vá para **Actions** no GitHub:
   **https://github.com/amandanery-o/framework-carreira-data-ia/actions**

4. Você verá um workflow **"Sync to Confluence"** rodando!

5. Clique nele para ver os logs

6. Se tudo der certo: ✅ Verde e páginas criadas no Confluence!

---

### **Opção B: Executar manualmente (mais rápido para testar)**

1. Vá para: **https://github.com/amandanery-o/framework-carreira-data-ia/actions**

2. Clique em **"Sync to Confluence"** (workflow no lado esquerdo)

3. Clique no botão **"Run workflow"** (no topo direito)

4. Selecione branch `main`

5. Clique em **"Run workflow"**

6. Aguarde alguns segundos e clique no workflow que aparecer

7. Veja os logs - deve mostrar páginas sendo criadas/atualizadas!

---

## 🎉 Pronto!

Depois que funcionar, **sempre que você fizer push** em arquivos de `levels/`, o Confluence será atualizado automaticamente!

---

## 🚨 Se algo der errado:

- Verifique os logs do workflow em **Actions**
- Verifique se nomes dos secrets estão EXATOS (case-sensitive)
- Verifique se valores estão corretos (sem espaços extras)

---

**Configure os secrets agora e me avise quando terminar! Depois testamos juntos!** 🚀
