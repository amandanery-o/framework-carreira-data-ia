# 📊 Dashboard Interativo - Framework de Carreira

Dashboard Streamlit para visualização interativa do Framework de Carreira Data & IA.

## 🌐 Acesso Online

**Dashboard ao vivo:** https://framework-carreira-data-ia.streamlit.app (após deploy)

## 🚀 Rodar Localmente

```bash
# Instalar dependências
pip install -r requirements-streamlit.txt

# Rodar dashboard
streamlit run app.py
```

O dashboard estará disponível em: http://localhost:8501

## 📊 Funcionalidades

### 🎯 Radar de Expectativas
- Visualização radar das 4 dimensões (Results, Direction, Talent, Culture)
- Comparação entre níveis
- Notas detalhadas por dimensão

### 🛠️ Skills por Trilha
- Exploração de skills técnicas por trilha
- Filtro por nível
- Agrupamento por categoria

### 📊 Comparação de Níveis
- Comparação lado a lado de dois níveis
- Visualização de gaps de crescimento
- Gráficos interativos

### 💎 Valores Gupy
- Como valores da Gupy se manifestam por nível
- Exemplos práticos

## 📁 Estrutura de Dados

Os dados são carregados dos CSVs em `/data/`:
- `niveis.csv` - Informações dos níveis
- `expectativas.csv` - Expectativas por dimensão
- `skills.csv` - Skills técnicas por trilha
- `valores_gupy.csv` - Manifestação dos valores

## 🔄 Atualizar Dados

Para atualizar os dados do dashboard:
1. Atualize os arquivos CSV na pasta `/data/`
2. Faça commit e push
3. O Streamlit Cloud fará deploy automático

---

**Desenvolvido com ❤️ pela liderança de Data & AI Engineering da Gupy**

