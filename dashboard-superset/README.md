# 📊 Dashboard Superset - Framework de Carreira Interativo

> Transforme os markdowns do framework em um dashboard interativo no Superset

---

## 🎯 Objetivo

Criar um dashboard no Superset onde engenheiros podem:
- Selecionar seu nível e trilha
- Ver expectativas em formato visual (radar)
- Explorar skills técnicas necessárias
- Comparar níveis diferentes
- Entender como valores Gupy se manifestam

---

## 📁 Estrutura do Projeto

```
dashboard-superset/
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências Python
│
├── scripts/                  # Scripts de processamento
│   ├── parse_framework.py    # Parseia markdowns → CSV
│   └── load_to_db.py        # Carrega CSV → PostgreSQL
│
├── sql/                      # Schema e queries
│   ├── schema.sql           # Criar tabelas
│   ├── seed_data.sql        # Dados iniciais
│   └── views.sql            # Views úteis
│
├── data/                     # CSVs gerados
│   ├── niveis.csv
│   ├── expectativas.csv
│   ├── skills.csv
│   └── valores_gupy.csv
│
├── queries/                  # Queries para Superset
│   ├── radar_expectativas.sql
│   ├── skills_por_trilha.sql
│   └── comparacao_niveis.sql
│
└── docs/                     # Documentação
    ├── SETUP.md             # Como configurar
    ├── DASHBOARD_DESIGN.md  # Design do dashboard
    └── MOCKUP.md            # Mockup visual
```

---

## 🚀 Quick Start

### 1. Instalar Dependências

```bash
cd dashboard-superset
pip install -r requirements.txt
```

### 2. Processar Markdowns

```bash
python scripts/parse_framework.py
```

Isso vai gerar CSVs na pasta `data/`

### 3. Criar Banco de Dados

```bash
# Conectar no PostgreSQL
psql -U seu_usuario -d seu_banco

# Rodar schema
\i sql/schema.sql

# Carregar dados
python scripts/load_to_db.py
```

### 4. Configurar Superset

1. Adicionar database connection no Superset
2. Adicionar datasets (ver `docs/SETUP.md`)
3. Criar dashboard (ver `docs/DASHBOARD_DESIGN.md`)

---

## 📊 Datasets Gerados

### 1. `niveis`
Informações básicas de cada nível de carreira

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INT | ID único |
| nome | VARCHAR | Ex: "SE II (Pleno)" |
| escopo | TEXT | Descrição do escopo |
| alcance_colaborativo | TEXT | Descrição do alcance |
| alavancas | TEXT | Principais alavancas |

### 2. `expectativas`
Expectativas por dimensão e nível

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INT | ID único |
| nivel_id | INT | FK para niveis |
| dimensao | VARCHAR | "Results", "Direction", etc |
| subdimensao | VARCHAR | "Impact", "Ownership", etc |
| descricao | TEXT | Descrição detalhada |
| nota_esperada | DECIMAL | 0.0 a 5.0 |

### 3. `skills`
Skills técnicas por trilha e nível

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INT | ID único |
| nivel_id | INT | FK para niveis |
| trilha | VARCHAR | "Data Engineering", etc |
| categoria | VARCHAR | "SQL", "Python", etc |
| skill | VARCHAR | Skill específica |
| nivel_esperado | VARCHAR | "Básico", "Intermediário", etc |
| detalhes | TEXT | Detalhes da skill |

### 4. `valores_gupy`
Como valores Gupy se manifestam por nível

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INT | ID único |
| nivel_id | INT | FK para niveis |
| valor | VARCHAR | "Obsessão pelo Cliente", etc |
| manifestacao | TEXT | Como se manifesta no nível |

---

## 🎨 Abas do Dashboard

### **Aba 1: Visão Geral**
- Filtros: Nível + Trilha
- Radar de expectativas
- Cards: Escopo, Alcance, Alavancas

### **Aba 2: Dimensões**
- Navegação por dimensão
- Texto completo das expectativas
- Exemplos práticos

### **Aba 3: Skills Técnicas**
- Tabela de skills por categoria
- Nível esperado para cada skill
- Comparação com outros níveis

### **Aba 4: Comparação**
- Lado a lado: Atual vs. Próximo Nível
- Gaps de skills
- Gaps comportamentais

### **Aba 5: Valores Gupy**
- Como cada valor se manifesta
- Exemplos por nível

---

## 🛠️ Stack Técnica

- **Python 3.8+** - Processamento dos markdowns
- **PostgreSQL** - Banco de dados
- **Superset** - Visualização
- **Markdown Parser** - Processar .md files

---

## 📝 Próximos Passos

- [ ] Executar `parse_framework.py`
- [ ] Validar CSVs gerados
- [ ] Criar banco de dados
- [ ] Carregar dados
- [ ] Configurar Superset
- [ ] Criar dashboard
- [ ] Testar filtros e interatividade

---

## 🤝 Contribuindo

Este é um projeto paralelo ao framework principal. 

Para atualizar os dados:
1. Atualizar markdowns no repo principal
2. Re-executar `parse_framework.py`
3. Re-carregar dados no banco

---

## 📞 Suporte

Dúvidas sobre este projeto? Consulte:
- `docs/SETUP.md` - Setup passo-a-passo
- `docs/DASHBOARD_DESIGN.md` - Design e funcionalidades
- Ou abra uma issue

---

**Versão:** 1.0  
**Última atualização:** Novembro 2024  
**Mantido por:** Liderança Data & IA Engineering

