
> Esta trilha foca exclusivamente em **habilidades técnicas (Habilidade Técnica)** para Analytics Engineers. Para competências comportamentais (Results, Direction, Talent, Culture), consulte os arquivos em [`/levels/`](../levels/).

---

## Visão Geral

**Analytics Engineers** são responsáveis por transformar dados brutos em modelos analíticos confiáveis, construir métricas de negócio e habilitar análises através de modelagem dimensional, dbt e integração com ferramentas de BI.

### Tech Stack & Tools
- **Transformation**: dbt (data build tool) - Core expertise
- **Data Warehouse**: BigQuery, Snowflake
- **BI Tools**: Looker, Tableau, Power BI, Metabase
- **Version Control**: Git, GitHub
- **Languages**: SQL (expert), Python (básico a intermediário)
- **Metrics Layer**: dbt Metrics, Lightdash
- **Documentation**: dbt docs, Confluence

---

## SE I – Junior Analytics Engineer

🔗 **Competências comportamentais**: [`SE_I_junior.md`](../levels/SE_I_junior.md)

### Entregas Principais
- Cria modelos dbt básicos com orientação
- Documenta modelos e métricas
- Contribui em projetos analíticos existentes

### SQL
- Proficiente em SELECT, JOIN, WHERE, GROUP BY
- Usa CTEs (Common Table Expressions)
- Entende agregações básicas (SUM, COUNT, AVG)
- Aplica filtros e ordenação
- Compreende diferença entre tipos de JOIN

### dbt Fundamentals
- Entende estrutura de projeto dbt (models, tests, docs, seeds)
- Escreve **models básicos** (.sql files em staging e marts)
- Adiciona **testes de esquema** (not_null, unique, accepted_values)
- Documenta models com **descriptions** no schema.yml
- Executa `dbt run`, `dbt test`, `dbt docs generate`
- Entende **materializations** básicas (table, view)

### Modelagem Dimensional Básica
- Entende conceitos de **fact** vs **dimension** tables
- Identifica métricas (measures) vs atributos (dimensions)
- Reconhece relacionamentos 1:N

### BI & Visualização
- Consome modelos dbt em ferramentas de BI
- Cria dashboards simples com orientação
- Entende conceitos básicos de visualização (gráficos de barra, linha, pizza)

### Boas Práticas
- Segue convenções de nomenclatura do time (stg_, int_, fct_, dim_)
- Comenta SQL quando necessário
- Usa versionamento (git) efetivamente
- Documenta assumptions e business logic

---

## SE II – Pleno Analytics Engineer

🔗 **Competências comportamentais**: [`SE_II_pleno.md`](../levels/SE_II_pleno.md)

### Entregas Principais (SE I+)
- Desenvolve modelos dbt end-to-end independentemente
- Define métricas de negócio
- Colabora com stakeholders para entender requisitos analíticos

### SQL (SE I+)
- **Fluente** em SQL: queries complexas com múltiplos CTEs
- Domina **window functions** (ROW_NUMBER, RANK, LAG, LEAD)
- Usa **QUALIFY**, **PIVOT/UNPIVOT**
- Otimiza queries para performance
- Trabalha com **recursive CTEs** quando apropriado

### dbt Intermediário (SE I+)
- Cria models com **Jinja** e **macros**
- Implementa **incremental models** eficientemente
- Usa **ref()** e **source()** corretamente
- Configura **materializations** apropriadas para cada caso
- Implementa **exposures** para ligar models a dashboards
- Usa pacotes dbt (**dbt_utils**, **dbt_expectations**)
- Cria **generic tests** customizados
- Configura **tags** e **selectors** para runs eficientes

### Modelagem Dimensional (SE I+)
- Aplica **Star Schema** (fact + dimensions)
- Cria **slowly changing dimensions** (SCD Type 1, 2)
- Implementa **conformed dimensions**
- Modela **fact tables** (transaction, snapshot, accumulating)
- Entende **grain** de tabelas e garante consistência
- Cria **bridge tables** para relacionamentos M:N

### Métricas & Business Logic
- Define **métricas de negócio** claras (ex: MRR, churn rate, CAC)
- Implementa **calculated metrics** (ratios, percentages)
- Documenta **business logic** e assumptions
- Valida métricas com stakeholders

### dbt Testing & Quality
- Implementa testes comprehensivos:
  - **Schema tests**: not_null, unique, relationships
  - **Data tests**: custom SQL tests
  - **dbt_expectations**: testes estatísticos
- Cria testes para **business rules** específicas
- Monitora **test failures** e investiga causas

### Performance & Otimização
- Otimiza models para **tempo de build**
- Usa **incremental models** quando apropriado
- Configura **partition_by** e **cluster_by**
- Analisa query execution plans
- Reduz custos de queries

---

## SE III – Senior Analytics Engineer

🔗 **Competências comportamentais**: [`SE_III_senior.md`](../levels/SE_III_senior.md)

### Entregas Principais (SE II+)
- Arquiteta projetos dbt complexos
- Define padrões de modelagem para o time
- Lidera tecnicamente projetos analíticos estratégicos

### SQL (SE II+)
- **Expert** em SQL: otimização avançada, window functions complexas
- Resolve problemas complexos de modelagem
- Usa SQL procedural quando necessário
- Entende profundamente query optimization

### dbt Avançado (SE II+)
- **Arquiteta estrutura** de projetos dbt escaláveis
  - **Staging** (stg_): raw → typed, renamed, light cleaning
  - **Intermediate** (int_): business logic, joins, complex transformations
  - **Marts** (fct_, dim_): modelos finais prontos para consumo
- Cria **macros reutilizáveis** e **packages internos**
- Implementa **hooks** (pre-hook, post-hook, on-run-start, on-run-end)
- Usa **vars** e **env_vars** para configuração
- Implementa **dbt metrics** (metrics.yml)
- Configura **CI/CD** para dbt (Slim CI)
- Otimiza **dbt builds** para performance (selectors, defer)

### Modelagem Dimensional Avançada
- **Kimball Methodology** completa:
  - Dimensional modeling
  - Slowly Changing Dimensions (Types 0-7)
  - Factless fact tables
  - Degenerate dimensions
  - Role-playing dimensions
- **Data Vault** (quando apropriado):
  - Hubs, Links, Satellites
- **One Big Table (OBT)** vs **Normalized** - escolhe apropriadamente
- Define **data contracts** com consumidores

### Métricas & Semantic Layer
- Implementa **metrics layer** (dbt Metrics ou Lightdash)
- Define **metric trees** (como métricas se relacionam)
- Cria **KPI frameworks** organizacionais
- Implementa **metric definitions** consistentes
- Documenta **metric calculation logic** claramente

### Data Quality & Observability
- Implementa framework de **data quality** robusto:
  - Schema validation
  - Business rule validation
  - Anomaly detection
  - Freshness checks
- Configura **dbt exposures** para rastrear dependências
- Implementa **data lineage** (dbt docs + ferramentas)
- Cria **dashboards de monitoring** de data quality

### Governance & Documentation
- Define **naming conventions** e **style guides**
- Implementa **data catalog** (dbt docs + tags + meta)
- Documenta **data dictionary** comprehensive
- Cria **ERDs** (Entity Relationship Diagrams)
- Implementa **data classification** (PII, sensitive, public)

### BI & Self-Service Analytics
- Desenha **semantic models** em BI tools (Looker LookML, Tableau)
- Habilita **self-service analytics** através de bons modelos
- Cria **reusable dashboards** e **templates**
- Treina usuários de negócio em ferramentas de BI

---

## Lead Engineer

🔗 **Competências comportamentais**: [`Lead_engineer.md`](../levels/Lead_engineer.md)

### Entregas Principais (SE III+)
- Define arquitetura analítica de longo prazo
- Cria frameworks e padrões organizacionais
- Resolve problemas técnicos mais complexos

### Arquitetura Analítica
- Desenha **analytics architecture** escalável
  - Raw → Staging → Intermediate → Marts → Metrics
  - Define boundaries e responsabilidades de cada camada
- Implementa **metrics store** organizacional
- Define estratégia de **self-service analytics**
- Cria **data products** reutilizáveis

### Platform & Standards
- Cria **dbt packages internos** reutilizáveis
- Define **analytics engineering best practices**
- Implementa **dbt style guide** e linters
- Estabelece **code review standards**
- Cria **templates** e **generators** (ex: Jinja macros avançados)

### Performance & Scale
- Otimiza para **scale** (100s de models, TBs de dados)
- Implementa **caching strategies**
- Otimiza **dbt build times** (parallelização, selectors)
- Reduz custos de queries em escala

### Expertise Profunda
- Expert em modelagem dimensional (Kimball, Data Vault)
- Referência em dbt avançado (macros, packages, performance)
- Contribui para comunidade (blog posts, dbt packages código aberto)

---

## Staff Engineer

🔗 **Competências comportamentais**: [`Staff_engineer.md`](../levels/Staff_engineer.md)

### Entregas Principais (Lead+)
- Define estratégia de analytics engineering multi-ano
- Influencia práticas de múltiplos times
- Cria capacidades que impactam toda organização

### Estratégia de Analytics
- Define **visão de analytics platform** de 2-3 anos
- Avalia e promove adoção de ferramentas (dbt Cloud, Lightdash, etc.)
- Define **semantic layer strategy**
- Alinha estratégia analítica com objetivos de negócio

### Organizational Impact
- Estabelece **analytics engineering function** na organização
- Define **career paths** para analytics engineers
- Cria **training programs** e **onboarding**
- Eleva capacidade técnica de múltiplos times

### Governance em Escala
- Implementa **metrics governance** organizacional
- Define **data contracts** entre teams
- Cria **data quality SLOs** company-wide
- Estabelece **standards** que escalam

---

## Staff II & Principal Engineer

🔗 **Competências comportamentais**: 
- [`Staff_II_senior_staff.md`](../levels/Staff_II_senior_staff.md)
- [`Principal_engineer.md`](../levels/Principal_engineer.md)

### Entregas Principais
- Define direção de analytics para empresa inteira
- Cria vantagem competitiva através de analytics
- Influencia indústria através de liderança de pensamento

### Company-Wide Analytics Strategy
- Define como analytics cria vantagem competitiva
- Influencia decisões de build vs buy para analytics stack
- Alinha analytics strategy com estratégia de negócio

### Liderança da Indústria
- Contribui para dbt código aberto ou cria ferramentas influentes
- Palestras em conferências (Coalesce, dbt Meetups)
- Publica artigos técnicos influentes
- Define o que é state-of-the-art em analytics engineering

---

## 📚 Recursos de Aprendizado

### Fundamentos
- **[dbt Learn](https://courses.getdbt.com/)** - Cursos oficiais dbt (grátis)
- **[SQL for Data Analysis (Mode)](https://mode.com/sql-tutorial/)** - SQL intermediário/avançado
- **[The Data Warehouse Toolkit (Kimball)](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/)** - Bíblia de modelagem dimensional

### Avançado
- **[Analytics Engineering Guide](https://www.getdbt.com/analytics-engineering/)** - dbt Labs
- **[dbt Discourse](https://discourse.getdbt.com/)** - Comunidade dbt
- **[Locally Optimistic](https://locallyoptimistic.com/)** - Blog sobre analytics engineering

### Certificações
- **dbt Analytics Engineering Certification** - Certificação oficial
- **Looker Business Analyst** - Para Looker expertise
- **Google Cloud Professional Data Engineer** - Contexto de plataforma

---

## 🔄 Como Usar Esta Trilha

1. **Identifique seu nível atual** nos arquivos de `/levels/`
2. **Compare** suas habilidades de dbt, SQL e modelagem com as expectativas
3. **Identifique gaps** técnicos específicos (ex: "preciso aprender incremental models")
4. **Crie plano de desenvolvimento**:
   - Faça cursos do dbt Learn
   - Leia documentação oficial
   - Pratique em projetos reais
   - Peça code review de seniors
5. **Busque mentoria** em áreas específicas (modelagem dimensional, performance, etc.)

**Lembre-se**: Domínio de dbt e SQL é crítico, mas não suficiente para promoção. Você também precisa crescer em Results, Direction, Talent e Culture.
