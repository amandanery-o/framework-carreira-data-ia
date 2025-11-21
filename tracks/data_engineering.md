# Trilha Técnica – Data Engineering

> Esta trilha foca exclusivamente em **habilidades técnicas (Craft)** para Data Engineers. Para competências comportamentais (Results, Direction, Talent, Culture), consulte os arquivos em [`/levels/`](../levels/).

---

## Visão Geral

**Data Engineers** são responsáveis por construir e manter pipelines, modelos de dados e arquiteturas que tornem dados confiáveis, acessíveis e úteis para produtos, análises e modelos de IA.

### Tech Stack & Tools
- **Data Warehouse**: BigQuery, Snowflake
- **Ingestion & Integration**: Fivetran, Airbyte, APIs
- **Orchestration**: Apache Airflow, Dagster
- **Transformation**: dbt (data build tool)
- **Languages**: SQL (avançado), Python
- **Infrastructure**: Docker, Kubernetes, Terraform
- **CI/CD**: GitHub Actions, GitLab CI
- **Observability**: Datadog, Monte Carlo, dbt Cloud

---

## SE I – Junior Data Engineer

🔗 **Competências comportamentais**: [`SE_I_junior.md`](../levels/SE_I_junior.md)

### Entregas Principais
- Implementa componentes individuais de produtos de dados sob orientação
- Escreve queries SQL simples a médias e scripts Python básicos
- Contribui em partes de pipelines de dados existentes

### SQL & Queries
- Proficiente em SELECT, JOIN, GROUP BY, HAVING, subqueries
- Entende diferença entre INNER/LEFT/RIGHT/FULL OUTER JOIN
- Usa CTEs (Common Table Expressions) para organizar queries
- Aplica funções de agregação (SUM, COUNT, AVG, MIN, MAX)
- Entende conceitos básicos de window functions

### Python
- Escreve scripts para manipulação de dados (pandas básico)
- Usa bibliotecas como requests para APIs
- Entende list comprehensions, dictionaries, functions
- Segue PEP 8 (guia de estilo Python)

### dbt (data build tool)
- Entende estrutura de projeto dbt (models, tests, docs)
- Escreve models simples (.sql files)
- Adiciona testes de esquema (not_null, unique)
- Documenta models com descriptions

### Pipelines & Orchestration
- Entende conceito de DAGs (Directed Acyclic Graphs)
- Executa e monitora DAGs existentes no Airflow
- Identifica falhas básicas e reporta

### Qualidade de Dados
- Escreve testes de esquema básicos no dbt
- Valida outputs comparando com especificações
- Documenta processos e assumptions

### Boas Práticas
- Segue guias de estilo e convenções do time
- Comenta código adequadamente
- Mantém trilha de auditoria (trabalho replicável)
- Usa versionamento (git) efetivamente

---

## SE II – Pleno Data Engineer

🔗 **Competências comportamentais**: [`SE_II_pleno.md`](../levels/SE_II_pleno.md)

### Entregas Principais (SE I+)
- Implementa componentes completos de forma independente
- Desenvolve pipelines end-to-end com testes
- Automatiza processos repetitivos

### SQL & Queries (SE I+)
- **Fluente** em SQL: escreve queries complexas com múltiplos CTEs
- Domina window functions (ROW_NUMBER, RANK, LAG, LEAD)
- Usa QUALIFY, PIVOT/UNPIVOT quando apropriado
- Otimiza queries para performance (analisa query plans)
- Entende particionamento e clustering

### Python (SE I+)
- Proficiente em pandas para ETL
- Escreve código modular e testável (functions, classes)
- Usa type hints e docstrings
- Trabalha com APIs (requests, autenticação)
- Entende async/await para operações I/O

### dbt (SE I+)
- Cria models complexos com macros e Jinja
- Implementa testes de dados customizados
- Usa pacotes dbt (dbt_utils, dbt_expectations)
- Configura materializations (table, view, incremental)
- Documenta com docs blocks e schema.yml

### Pipelines & Orchestration (SE I+)
- Cria DAGs no Airflow com operators apropriados
- Implementa retries, timeouts e alertas
- Usa XComs para passar dados entre tasks
- Entende dependency management

### Modelagem de Dados
- Aplica normalização vs denormalização
- Cria fact e dimension tables (Kimball básico)
- Entende slowly changing dimensions (SCD Type 1, 2)
- Modela dados para analytics (star schema)

### Qualidade de Dados (SE I+)
- Implementa testes de integridade (referential integrity)
- Cria alertas proativos para anomalias
- Monitora freshness de dados
- Documenta data quality checks

### Performance & Otimização
- Otimiza queries analisando execution plans
- Usa particionamento e clustering efetivamente
- Entende custos de queries no BigQuery
- Implementa caching quando apropriado

---

## SE III – Senior Data Engineer

🔗 **Competências comportamentais**: [`SE_III_senior.md`](../levels/SE_III_senior.md)

### Entregas Principais (SE II+)
- Desenha e implementa sistemas de dados completos
- Define arquitetura de pipelines e modelos
- Lidera tecnicamente projetos de dados complexos

### SQL & Queries (SE II+)
- **Expert** em SQL: otimização avançada, window functions complexas
- Resolve problemas de performance de queries
- Usa SQL procedural (stored procedures, user-defined functions)
- Entende profundamente query execution e planos

### Python (SE II+)
- Escreve código production-ready com testes abrangentes
- Usa design patterns apropriados
- Implementa logging e monitoring
- Trabalha com frameworks (FastAPI, Flask para APIs)
- Otimiza código para performance (profiling)

### dbt (SE II+)
- Arquiteta estrutura de projetos dbt complexos
- Cria macros reutilizáveis e packages internos
- Implementa estratégias avançadas de incremental models
- Otimiza builds dbt para performance
- Define padrões de modelagem para o time

### Modelagem de Dados Avançada
- **Kimball**: fact tables, dimension tables, conformed dimensions
- **Data Vault**: hubs, links, satellites
- **Abordagens orientadas a domínio**: bounded contexts
- Escolhe abordagem apropriada para caso de uso
- Desenha data contracts entre serviços

### Pipelines & Orchestration (SE II+)
- Arquiteta pipelines complexos com múltiplas dependências
- Implementa patterns de resiliência (idempotência, retries exponenciais)
- Otimiza paralelização de tasks
- Implementa monitoring e alerting robusto
- Usa sensors e hooks avançados no Airflow

### Qualidade & Observabilidade
- Implementa framework de testes de dados comprehensivo
  - Testes de esquema (schema)
  - Testes de qualidade (nulls, ranges, distributions)
  - Testes de consistência (cross-checks)
- Configura **data lineage** (OpenLineage, Monte Carlo)
- Implementa **data observability** (freshness, volume, schema)
- Define SLOs para pipelines críticos
- Cria dashboards de monitoring de pipelines

### Infrastructure as Code
- Usa Terraform para provisionar recursos (BigQuery datasets, tables, views)
- Implementa CI/CD para pipelines de dados
- Configura ambientes (dev, staging, prod)
- Automatiza deployments via GitHub Actions

### Performance & Otimização (SE II+)
- Otimiza **custo** de queries e storage
- Implementa estratégias de particionamento e clustering avançadas
- Usa materialized views quando apropriado
- Profila pipelines para identificar bottlenecks
- Implementa caching strategies (Redis, Memcached)

### Segurança & Governança
- Implementa column-level security
- Configura roles e permissions (least privilege)
- Garante compliance (LGPD, GDPR)
- Implementa data masking para dados sensíveis
- Documenta data catalog e metadata

---

## Lead Engineer

🔗 **Competências comportamentais**: [`Lead_engineer.md`](../levels/Lead_engineer.md)

### Entregas Principais (SE III+)
- Define arquitetura de dados de longo prazo para a área
- Resolve problemas técnicos mais complexos da organização
- Cria frameworks e patterns reutilizáveis

### Arquitetura de Dados
- Desenha **arquitetura de dados** escalável para múltiplos domínios
- Define **data mesh** vs **data lake** vs **data warehouse** strategies
- Implementa **data lakehouse** patterns (Delta Lake, Iceberg)
- Arquiteta para **multi-tenancy** e **isolation**
- Define estratégias de **data retention** e **archiving**

### Plataforma de Dados
- Desenha abstrações e interfaces que permitem self-service
- Cria frameworks internos (ex: dbt packages, Airflow operators customizados)
- Implementa **data platform APIs**
- Define **data contracts** e governance
- Estabelece **data quality framework** organizacional

### Performance em Escala
- Otimiza para **escala** (TB → PB de dados)
- Implementa **streaming** (Kafka, Pub/Sub) quando apropriado
- Desenha para **real-time** vs **batch** appropriadamente
- Otimiza custos em escala (query optimization, storage tiering)

### Expertise Profunda
- Expert em pelo menos um domínio (ex: streaming, ML pipelines, data lakehouse)
- Referência técnica para Data Engineers do time
- Contribui para comunidade (blog posts, talks, open source)

---

## Staff Engineer

🔗 **Competências comportamentais**: [`Staff_engineer.md`](../levels/Staff_engineer.md)

### Entregas Principais (Lead+)
- Define estratégia técnica de dados multi-ano
- Influencia arquitetura de dados de múltiplos times
- Cria capacidades técnicas que impactam toda organização

### Estratégia de Dados
- Define **visão de plataforma de dados** de 2-3 anos
- Avalia e promove adoção de novas tecnologias (ex: dbt Cloud, Fivetran vs custom)
- Define estratégia de **build vs buy** para componentes de plataforma
- Alinha estratégia técnica com objetivos de negócio

### Arquitetura Organizacional
- Desenha **data architecture** que serve múltiplos times
- Define **standards e best practices** organizacionais
- Cria **governance model** escalável
- Implementa **federated data platform** (data mesh principles)

### Liderança Técnica
- Eleva capacidade técnica de múltiplos times
- Mentora Lead e Senior Engineers
- Conduz **RFCs** (Request for Comments) técnicos significativos
- Representa Data Engineering em decisões arquiteturais company-wide

---

## Staff II & Principal Engineer

🔗 **Competências comportamentais**: 
- [`Staff_II_senior_staff.md`](../levels/Staff_II_senior_staff.md)
- [`Principal_engineer.md`](../levels/Principal_engineer.md)

### Entregas Principais
- Define direção técnica de dados para a empresa inteira
- Resolve os desafios técnicos mais complexos e estratégicos
- Influencia indústria através de liderança de pensamento

### Estratégia Company-Wide
- Define arquitetura de dados de 3-5 anos alinhada com estratégia de negócio
- Avalia e influencia decisões de M&A do ponto de vista de dados
- Define **data strategy** que cria vantagem competitiva

### Technical Vision
- Articula visão técnica que inspira organização
- Identifica tendências tecnológicas e posiciona empresa
- Cria frameworks que transformam capacidades da empresa

### Industry Leadership
- Publica pesquisa, contribui para open source significativo
- Palestras em conferências principais
- Representa empresa como líder de pensamento em dados

---

## 📚 Recursos de Aprendizado

### Fundamentos
- [SQL for Data Scientists](https://mode.com/sql-tutorial/)
- [Python for Data Engineering](https://realpython.com/)
- [dbt Learn](https://courses.getdbt.com/)

### Avançado
- [Data Engineering Zoomcamp (DataTalks.Club)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [The Data Engineering Cookbook](https://github.com/andkret/Cookbook)
- [Fundamentals of Data Engineering (O'Reilly Book)](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)

### Certificações Relevantes
- **Google Cloud**: Professional Data Engineer
- **dbt**: Analytics Engineer Certification
- **Airflow**: Astronomer Certification

---

## 🔄 Como Usar Esta Trilha

1. **Identifique seu nível atual** nos arquivos de `/levels/`
2. **Compare** suas habilidades técnicas com as expectativas desta trilha
3. **Identifique gaps** técnicos específicos
4. **Crie plano de desenvolvimento** focado nas skills técnicas que faltam
5. **Pratique** através de projetos reais no time
6. **Busque mentoria** de engineers mais seniores em áreas específicas

**Lembre-se**: Craft técnico é importante, mas não é suficiente para promoção. Você também precisa demonstrar crescimento nas 4 dimensões: Results, Direction, Talent e Culture.
