# 📦 Guia de Commit - Framework de Carreira

> Como preparar o repositório para mostrar ao chefe

---

## ✅ O Que VAI no Commit (Framework Core)

### 📁 Arquivos Principais:
```
✅ README.md                      (Visão geral do framework)
✅ SUMARIO.md                     (Resumo executivo)
✅ NIVEIS_REFERENCIA.md           (Matriz Scope/Reach/Impact)
✅ INDICE_COMPLETO.md             (Navegação completa)
✅ 0_COMECE_AQUI.md               (Guia de início rápido)
```

### 📁 Níveis (9 arquivos):
```
✅ levels/SE_I_junior.md
✅ levels/SE_II_pleno.md
✅ levels/SE_III_senior.md
✅ levels/Lead_engineer.md
✅ levels/Staff_engineer.md
✅ levels/Staff_II_senior_staff.md
✅ levels/Principal_engineer.md
✅ levels/Tech_lead.md
✅ levels/Engineering_manager.md
```

### 📁 Competências (4 arquivos):
```
✅ competencies/tech_excellence.md
✅ competencies/execution.md
✅ competencies/communication.md
✅ competencies/leadership.md
```

### 📁 Trilhas Técnicas (3 arquivos):
```
✅ tracks/data_engineering.md
✅ tracks/analytics_engineering.md
✅ tracks/cientista_de_dados.md
```

### 📁 Cultura (1 arquivo):
```
✅ culture/mapping_to_gupy_culture.md
```

### 📁 Promoção (2 arquivos):
```
✅ promotion/template_promotion.md
✅ promotion/calibration_guide.md
```

### 📁 Materiais de Apresentação:
```
✅ REVISAO_PRE_APRESENTACAO.md    (Análise completa)
✅ SLIDES_APRESENTACAO.md         (22 slides executivos)
✅ CHECKLIST_FINAL.md             (Checklist de preparação)
✅ RESUMO_EXECUTIVO.md            (One-pager pro chefe)
```

**Total:** ~27 arquivos ✅

---

## ❌ O Que NÃO VAI no Commit (Por Enquanto)

### 🚫 Sistema de Avaliação 360º:
```
❌ avaliacao/                     (Toda a pasta)
   ├── GUIA_AVALIACAO_360.md
   ├── templates de avaliação
   ├── ferramentas/ (Google Forms + n8n)
   └── exemplos
```

**Por quê?** Mostrar depois de validar o framework core.

### 🚫 EM Operating System:
```
❌ em-operating-system/           (Toda a pasta)
   ├── README.md
   ├── rotinas-e-rituais.md
   └── outros
```

**Por quê?** Pode adicionar depois se o chefe quiser.

### 🚫 Arquivos Internos:
```
❌ COMO_COMITAR.md               (Este arquivo - é só pra você)
❌ .DS_Store, *.tmp, etc.
```

---

## 🚀 Como Fazer o Commit

### Passo 1: Verificar .gitignore

O `.gitignore` já está criado excluindo:
- `avaliacao/`
- `em-operating-system/`
- Arquivos temporários

✅ Pronto!

---

### Passo 2: Inicializar Git (se ainda não fez)

```bash
cd "/Users/amandanery/Workspace/trilha de carreira data & ia"
git init
```

---

### Passo 3: Adicionar Arquivos

```bash
# Adicionar tudo (menos o que está no .gitignore)
git add .

# Verificar o que vai ser commitado
git status
```

**Deve mostrar:**
- ✅ README.md, SUMARIO.md, etc.
- ✅ levels/
- ✅ competencies/
- ✅ tracks/
- ✅ culture/
- ✅ promotion/
- ❌ avaliacao/ (ignorado)
- ❌ em-operating-system/ (ignorado)

---

### Passo 4: Fazer Commit

```bash
git commit -m "feat: Framework de Carreira Data & IA - Versão Inicial

- 9 níveis (SE I → Principal + TL + EM)
- 4 competências transversais
- 3 trilhas técnicas (DE, AE, Cientista Dados)
- Mapeamento cultura Gupy
- Processo de promoção estruturado
- Materiais de apresentação

Inspirado no Dropbox Engineering Career Framework
Customizado para Data & IA @ Gupy"
```

---

### Passo 5: Criar Repositório no GitHub/GitLab

#### Opção A: GitHub

1. Ir para github.com/new
2. Nome: `framework-carreira-data-ia`
3. Descrição: `Framework de Carreira para Data & IA Engineering`
4. Privado: ✅ (por enquanto)
5. Criar repositório

#### Opção B: GitLab (interno Gupy)

1. Ir para gitlab da empresa
2. Novo projeto
3. Nome: `framework-carreira-data-ia`
4. Visibilidade: Internal ou Private

---

### Passo 6: Push para Repositório

```bash
# Adicionar remote (substitua URL)
git remote add origin https://github.com/seu-usuario/framework-carreira-data-ia.git

# Push
git push -u origin main
```

Se der erro de branch, tente:
```bash
git branch -M main
git push -u origin main
```

---

## 📧 Como Compartilhar com Chefe

### Opção A: Link do Repositório + README

**Email/Slack:**
```
Olá [Nome do Chefe],

Finalizei o Framework de Carreira para Data & IA! 🎉

📂 Repositório: [LINK]

📖 Por onde começar:
• 0_COMECE_AQUI.md - Quick start
• RESUMO_EXECUTIVO.md - One-pager
• SLIDES_APRESENTACAO.md - 22 slides executivos

⏰ Gostaria de agendar 30-45 min para apresentar?

Abraço!
```

---

### Opção B: Apresentação + Repositório

1. **Agendar reunião** (30-45 min)
2. **Apresentar** usando SLIDES_APRESENTACAO.md
3. **Compartilhar** link do repo durante/depois

---

### Opção C: Documento + Repo

Exportar key highlights como PDF:
- RESUMO_EXECUTIVO.md → PDF
- SLIDES_APRESENTACAO.md → PDF
- Enviar por email + link do repo

---

## 🎯 Estrutura Final do Repo (O Que o Chefe Vai Ver)

```
framework-carreira-data-ia/
│
├── 📄 README.md ⭐ (Primeira coisa que ele vai ver)
├── 📄 0_COMECE_AQUI.md
├── 📄 SUMARIO.md
├── 📄 NIVEIS_REFERENCIA.md
│
├── 📂 levels/ (9 níveis)
│   ├── SE_I_junior.md
│   ├── SE_II_pleno.md
│   ├── SE_III_senior.md
│   └── ...
│
├── 📂 competencies/ (4 competências)
│   ├── tech_excellence.md
│   ├── execution.md
│   ├── communication.md
│   └── leadership.md
│
├── 📂 tracks/ (3 trilhas)
│   ├── data_engineering.md
│   ├── analytics_engineering.md
│   └── cientista_de_dados.md
│
├── 📂 culture/
│   └── mapping_to_gupy_culture.md
│
├── 📂 promotion/
│   ├── template_promotion.md
│   └── calibration_guide.md
│
├── 📄 REVISAO_PRE_APRESENTACAO.md
├── 📄 SLIDES_APRESENTACAO.md
├── 📄 CHECKLIST_FINAL.md
└── 📄 RESUMO_EXECUTIVO.md
```

**Clean, profissional, focado! ✨**

---

## 💡 Dicas Pro

### 1. README.md está Otimizado
Ele tem:
- ✅ Badges bonitinhos
- ✅ Navegação clara
- ✅ Créditos ao Dropbox
- ✅ Próximos passos

**Primeira impressão conta!**

---

### 2. Adicionar Depois (Fase 2)
Quando o chefe aprovar:
```bash
# Remover avaliacao/ do .gitignore
# Comitar sistema 360º
git add avaliacao/
git commit -m "feat: Sistema de Avaliação 360º com Radares Visuais"
git push
```

---

### 3. Manter Atualizado
Após feedback do chefe:
```bash
# Fazer ajustes
git add .
git commit -m "fix: Ajustes baseados em feedback [nome do chefe]"
git push
```

---

## ✅ Checklist Pré-Commit

Antes de fazer push, verificar:

- [ ] `.gitignore` criado
- [ ] `avaliacao/` não está no commit
- [ ] `em-operating-system/` não está no commit (ou incluir se quiser)
- [ ] README.md está atualizado
- [ ] Links internos funcionam
- [ ] Sem arquivos temporários (.DS_Store, etc.)
- [ ] Mensagem de commit clara e profissional
- [ ] Repositório é privado (por enquanto)

---

## 🎯 Próximos Passos Após Commit

### 1. Compartilhar com Chefe ✅
### 2. Aguardar Feedback 📝
### 3. Fazer Ajustes 🔧
### 4. Quando Aprovado:
   - Apresentar para outros leads
   - Adicionar sistema 360º (avaliação/)
   - Tornar público (se aplicável)
   - Comunicar ao time

---

## 🚀 Comando Rápido (Copiar/Colar)

Se já tem repo remoto criado:

```bash
cd "/Users/amandanery/Workspace/trilha de carreira data & ia"
git init
git add .
git commit -m "feat: Framework de Carreira Data & IA - Versão Inicial"
git branch -M main
git remote add origin [URL_DO_SEU_REPO]
git push -u origin main
```

**Pronto! 🎉**

---

## ❓ FAQ

### P: E se o chefe quiser ver o sistema 360º também?
**R:** Fácil! Remova `avaliacao/` do `.gitignore` e faça novo commit.

### P: Posso commitar o EM Operating System?
**R:** Sim! Remova `em-operating-system/` do `.gitignore` se quiser incluir.

### P: Como faço para adicionar mais arquivos depois?
**R:** `git add [arquivo]` → `git commit -m "descrição"` → `git push`

### P: E se eu quiser um repo público?
**R:** GitHub: Settings → Danger Zone → Change visibility → Public

---

**Boa sorte com a apresentação! 🚀✨**

**Me chama depois para contar como foi a reação do chefe! 😊**

