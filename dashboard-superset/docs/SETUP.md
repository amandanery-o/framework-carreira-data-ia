# 🚀 Setup do Dashboard Superset

> Guia passo-a-passo para colocar o dashboard no ar

---

## 📋 Pré-requisitos

- Python 3.8+
- PostgreSQL 12+
- Apache Superset configurado
- Acesso ao repositório do framework

---

## 🔧 Passo 1: Preparar Ambiente Python

```bash
# Navegar para pasta do projeto
cd dashboard-superset

# Criar virtual environment (recomendado)
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

---

## 🗄️ Passo 2: Preparar Banco de Dados

### 2.1 Criar Database

```bash
# Conectar no PostgreSQL
psql -U postgres

# Criar database
CREATE DATABASE framework_carreira;

# Conectar no database
\c framework_carreira
```

### 2.2 Criar Schema

```bash
# Executar schema.sql
\i sql/schema.sql

# Verificar tabelas criadas
\dt
```

Você deve ver:
- `niveis`
- `expectativas`
- `skills`
- `valores_gupy`

E as views:
- `radar_expectativas`
- `skills_consolidadas`
- `comparacao_niveis`
- `valores_por_nivel`

---

## 📊 Passo 3: Processar Dados

### 3.1 Parsear Markdowns

```bash
# Executar script de parse
python scripts/parse_framework.py
```

Isso vai gerar 4 CSVs na pasta `data/`:
- `niveis.csv`
- `expectativas.csv`
- `skills.csv`
- `valores_gupy.csv`

### 3.2 Verificar CSVs

```bash
# Ver primeiras linhas
head data/niveis.csv
head data/expectativas.csv
```

### 3.3 Configurar Conexão ao Banco

Criar arquivo `.env` na raiz do projeto `dashboard-superset/`:

```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=framework_carreira
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

### 3.4 Carregar no Banco

```bash
python scripts/load_to_db.py
```

Quando perguntar se quer limpar tabelas, responda:
- `s` - Se for primeira vez ou quiser recarregar tudo
- `n` - Se quiser preservar dados existentes

---

## 🎨 Passo 4: Configurar Superset

### 4.1 Adicionar Database Connection

1. Abrir Superset
2. Settings → Database Connections → + Database
3. Selecionar: **PostgreSQL**
4. Configurar:
   ```
   Host: localhost
   Port: 5432
   Database: framework_carreira
   Username: postgres
   Password: sua_senha
   Display Name: Framework Carreira
   ```
5. Test Connection → Connect

### 4.2 Adicionar Datasets

Criar um dataset para cada view/tabela:

**Dataset 1: Radar de Expectativas**
- Table: `radar_expectativas`
- Database: Framework Carreira
- Nomear: "Radar - Expectativas"

**Dataset 2: Skills Consolidadas**
- Table: `skills_consolidadas`
- Database: Framework Carreira
- Nomear: "Skills por Trilha"

**Dataset 3: Comparação de Níveis**
- Table: `comparacao_niveis`
- Database: Framework Carreira
- Nomear: "Comparação Níveis"

**Dataset 4: Valores Gupy**
- Table: `valores_por_nivel`
- Database: Framework Carreira
- Nomear: "Valores Gupy"

### 4.3 Criar SQL Lab Queries (Opcional)

Para queries parametrizadas, usar SQL Lab:

1. SQL → SQL Lab
2. Nova Query
3. Copiar conteúdo de `queries/radar_expectativas.sql`
4. Salvar como "Query - Radar Expectativas"

Repetir para as outras queries em `queries/`

---

## 📊 Passo 5: Criar Dashboard

### 5.1 Criar Dashboard Novo

1. Dashboards → + Dashboard
2. Nome: "Framework de Carreira - Explorer"
3. Salvar

### 5.2 Adicionar Filtros (Dashboard Filters)

**Filtro 1: Nível**
- Column: `nivel_nome`
- Default: "SE II (Pleno)"
- Label: "Selecione o Nível"

**Filtro 2: Trilha**
- Column: `trilha`
- Default: "Data Engineering"
- Label: "Selecione a Trilha"

### 5.3 Adicionar Charts

**Chart 1: Radar de Expectativas**
- Dataset: Radar - Expectativas
- Chart Type: Radar
- Dimensions: dimensao
- Metric: AVG(nota_media)
- Filtros: Aplicar filtro de Nível

**Chart 2: Tabela de Skills**
- Dataset: Skills por Trilha
- Chart Type: Table
- Columns: categoria, skill, nivel_esperado, detalhes
- Filtros: Aplicar filtros de Nível e Trilha

**Chart 3: Comparação de Níveis**
- Dataset: Comparação Níveis
- Chart Type: Table
- Columns: dimensao, nota_atual, nota_proximo, gap
- Filtros: Aplicar filtro de Nível
- Conditional Formatting: gap < 0 = vermelho

**Chart 4: Cards de Resumo**
- Dataset: radar_expectativas
- Chart Type: Big Number
- Metric: AVG(nota_media)
- Group by: nivel_nome

### 5.4 Organizar Layout

Sugestão de layout:

```
┌─────────────────────────────────────────┐
│ [Filtro Nível] [Filtro Trilha]         │
├───────────────────┬─────────────────────┤
│                   │                     │
│  Radar Chart      │  Cards de Resumo    │
│                   │                     │
├───────────────────┴─────────────────────┤
│                                         │
│  Tabela de Skills                      │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│  Comparação de Níveis                  │
│                                         │
└─────────────────────────────────────────┘
```

---

## ✅ Passo 6: Testar

### 6.1 Testar Filtros

1. Selecionar diferentes níveis
2. Verificar se radar atualiza
3. Selecionar diferentes trilhas
4. Verificar se tabela de skills muda

### 6.2 Testar Drill-down

1. Clicar em uma dimensão no radar
2. Ver se expande detalhes
3. Testar navegação entre charts

---

## 🔄 Atualizar Dados

Quando o framework mudar:

```bash
# 1. Re-parsear markdowns
python scripts/parse_framework.py

# 2. Re-carregar no banco
python scripts/load_to_db.py
# Responder 's' para limpar tabelas

# 3. Refresh cache no Superset
# Data → Datasets → [seu dataset] → Edit → Advanced → Cache Timeout: 0
```

---

## 🐛 Troubleshooting

### Erro: "Connection refused"
**Causa:** PostgreSQL não está rodando  
**Solução:** `sudo service postgresql start`

### Erro: "Permission denied"
**Causa:** User do Superset não tem acesso ao database  
**Solução:**
```sql
GRANT SELECT ON ALL TABLES IN SCHEMA public TO superset_user;
```

### Erro: "No data"
**Causa:** Dados não foram carregados  
**Solução:** Re-executar `python scripts/load_to_db.py`

### Charts não atualizam
**Causa:** Cache do Superset  
**Solução:** Dashboard → ⋮ → Force Refresh

---

## 📚 Próximos Passos

- [ ] Criar mais charts (valores Gupy, timeline)
- [ ] Adicionar drill-downs
- [ ] Integrar com avaliações 360º
- [ ] Criar dashboard de analytics (uso do framework)
- [ ] Adicionar exportação para PDF

---

## 🤝 Contribuindo

Para melhorar este setup:
1. Documente problemas encontrados
2. Sugira melhorias no processo
3. Compartilhe screenshots do dashboard final

---

**Pronto! 🎉 Dashboard no ar!**

Dúvidas? Consulte `README.md` ou `DASHBOARD_DESIGN.md`

