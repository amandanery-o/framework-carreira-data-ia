Framework de progressão de carreira para Data & AI Engineering na Gupy.

## 📖 Visualizar a Documentação

Este projeto está configurado para ser publicado automaticamente como um site usando MkDocs + GitHub Pages.

**🌐 Acesse a documentação online:** `https://amandanery-o.github.io/framework-carreira-data-ia/`

## 🚀 Como Publicar

### Configuração Inicial (Uma vez apenas)

1. **Faça push deste repositório para o GitHub**
   ```bash
   git add .
   git commit -m "Configurar MkDocs para publicação"
   git push origin main
   ```

2. **Habilite GitHub Pages**
   - Vá para o repositório no GitHub
   - Navegue para: **Settings → Pages**
   - Em "Source", selecione: **Deploy from a branch**
   - Em "Branch", selecione: **gh-pages** e **/root**
   - Clique em **Save**

3. **Aguarde o deploy**
   - O GitHub Actions irá fazer o build e deploy automaticamente
   - Acompanhe em: **Actions** (no menu do repositório)
   - Em 2-3 minutos seu site estará no ar!

### Atualizações Futuras

Toda vez que você fizer push para a branch `main`, o site será atualizado automaticamente! 🎉

```bash
# Edite seus arquivos markdown
git add .
git commit -m "Atualizar documentação"
git push origin main
# O site será atualizado automaticamente em poucos minutos
```

## 🧪 Testar Localmente (Opcional)

Se quiser visualizar o site antes de publicar:

```bash
# Instalar dependências
pip install -r requirements.txt

# Servir localmente
mkdocs serve

# Acesse: http://127.0.0.1:8000
```

## 📁 Estrutura do Projeto

```
career-ladder/
├── docs/                     # Arquivos fonte da documentação
│   ├── index.md             # Página inicial
│   ├── competencies/        # Competências
│   ├── levels/              # Níveis de carreira
│   ├── tracks/              # Trilhas técnicas
│   ├── promotion/           # Processo de promoção
│   └── culture/             # Cultura
├── mkdocs.yml               # Configuração do MkDocs
├── requirements.txt         # Dependências Python
└── .github/workflows/       # GitHub Actions (deploy automático)
```

## 🎨 Personalização

Edite o arquivo `mkdocs.yml` para:
- Alterar cores e tema
- Reorganizar a navegação
- Adicionar/remover seções
- Configurar URL do repositório

## ❓ Precisa de Ajuda?

- **Documentação MkDocs**: https://www.mkdocs.org
- **Material Theme**: https://squidfunk.github.io/mkdocs-material/
- **GitHub Pages**: https://pages.github.com

---

**Desenvolvido com ❤️ para o time de Data & AI Engineering da Gupy**
