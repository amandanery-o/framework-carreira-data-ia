
## Descrição

Domínio técnico proporcional ao nível de senioridade, com evolução contínua e influência crescente na qualidade da área. Envolve desde o domínio das ferramentas e práticas até a definição de direções arquiteturais e tecnológicas que impactam a organização.

---

## Dimensões da Excelência Técnica

### 1. Arquitetura & Design de Sistemas

**O que é:**
Capacidade de projetar sistemas escaláveis, resilientes e de fácil manutenção, considerando trade-offs de longo prazo.

**Comportamentos esperados:**
- Compreender como as soluções se integram com outros sistemas e identificar pontos de fricção
- Considerar aspectos de segurança, desempenho, custos e operação desde o design
- Documentar decisões arquiteturais importantes (ADRs - Architecture Decision Records)
- Validar decisões através de POCs (Proof of Concepts) quando apropriado
- Isolar e substituir sistemas legados de forma incremental e segura

**Evolução por nível:**
- **SE I-II**: Entende arquitetura existente, implementa componentes seguindo padrões estabelecidos
- **SE III**: Projeta componentes e features considerando arquitetura do time
- **Lead**: Projeta e evolui arquitetura de sistemas do time, define contratos de dados/APIs
- **Staff**: Desenha arquiteturas para múltiplos times/domínios, define padrões organizacionais
- **Staff II-Principal**: Define estratégia arquitetural da organização, escolhe paradigmas (ex: lakehouse, data mesh)

### 2. Qualidade & Padrões de Código

**O que é:**
Garantia de alta qualidade através de revisões, padrões, testes e automação.

**Comportamentos esperados:**
- Seguir e estabelecer guias de estilo e boas práticas
- Realizar revisões de código educativas, explicando o "porquê" das sugestões
- Escrever código legível, testável e manutenível
- Automatizar verificação de qualidade (linters, CI/CD, análise estática)
- Monitorar métricas de qualidade (cobertura de testes, complexidade, code smells)

**Evolução por nível:**
- **SE I-II**: Segue padrões, documenta código, participa de revisões de código
- **SE III**: Estabelece padrões no time, realiza revisões de código educativas
- **Lead**: Define guidelines de qualidade, gerencia débito técnico do time
- **Staff**: Cria documentação e padrões organization-wide para "alta qualidade"
- **Staff II-Principal**: Define cultura de qualidade e padrões globais da organização

**Métricas de sucesso:**
- Cobertura de testes (target: >80% para código crítico)
- Redução de bugs em produção
- Tempo médio de revisão de código (balanceando velocidade e qualidade)
- Débito técnico gerenciado (target: <15% do backlog)

### 3. Tecnologia & Ferramentas

**O que é:**
Avaliação, adoção e domínio de tecnologias, ferramentas e frameworks apropriados.

**Comportamentos esperados:**
- Dominar ferramentas, linguagens e frameworks centrais do stack
- Experimentar novas tecnologias com alto potencial
- Avaliar tecnologias considerando fit organizacional, curva de aprendizado e ROI
- Promover adoção de ferramentas que reduzam necessidade de escrever mais código
- Manter stack atualizado evitando débito de versões

**Evolução por nível:**
- **SE I-II**: Domina stack básico da área, aprende novas ferramentas quando necessário
- **SE III**: Proficiência avançada, propõe melhorias de ferramentas
- **Lead**: Avalia e recomenda tecnologias para o domínio do time
- **Staff**: Cria tech radars, define guidelines de adoção organization-wide
- **Staff II-Principal**: Define apostas tecnológicas estratégicas da organização

**Métricas de sucesso:**
- Taxa de adoção de tecnologias recomendadas
- Redução de tempo de desenvolvimento ou melhoria de developer experience
- ROI positivo demonstrado em relatórios pós-implantação

### 4. Excelência Operacional

**O que é:**
Garantia de confiabilidade, observabilidade e eficiência operacional dos sistemas.

**Comportamentos esperados:**
- Definir e monitorar SLIs/SLOs para sistemas críticos
- Implementar observabilidade adequada (logs, métricas, traces, alertas)
- Estabelecer cultura de reliability através de boas práticas
- Implementar automação para reduzir trabalho repetitivo
- Conduzir post-mortems focados em aprendizado sistêmico

**Evolução por nível:**
- **SE I-II**: Implementa logs, monitora básico, responde a alertas
- **SE III**: Define métricas de qualidade, participa de on-call, melhora observabilidade
- **Lead**: Define SLIs/SLOs do time, cria runbooks, lidera melhorias operacionais
- **Staff**: Estabelece padrões de reliability organization-wide, chaos engineering
- **Staff II-Principal**: Define estratégia de confiabilidade e operational excellence

**Métricas de sucesso:**
- MTTR (Mean Time To Recovery): <30 min para P0, <1h para P1
- SLO compliance: >99.9% para serviços críticos
- Redução de toil operacional
- Incident frequency e severity em tendência decrescente

### 5. desempenho, Custo & Escalabilidade

**O que é:**
Otimização de sistemas considerando desempenho, custo e capacidade de escalar.

**Comportamentos esperados:**
- Medir e melhorar desempenho, custo e escalabilidade
- Considerar trade-offs entre diferentes aspectos (ex: custo vs latência)
- Implementar caching, indexação e outras otimizações quando apropriado
- Monitorar custos de infraestrutura e propor otimizações
- Projetar sistemas que escalam horizontal e verticalmente

**Evolução por nível:**
- **SE I-II**: Escreve código eficiente, está atento a custos básicos
- **SE III**: Otimiza queries/pipelines, propõe melhorias de desempenho
- **Lead**: Gerencia custos do time, otimiza arquitetura para desempenho
- **Staff**: Define estratégias de otimização cross-team, balanceia custo/desempenho
- **Staff II-Principal**: Define diretrizes globais de desempenho, custo e escalabilidade

### 6. Segurança & Governança

**O que é:**
Garantia de segurança, privacidade e conformidade com regulações.

**Comportamentos esperados:**
- Seguir boas práticas de segurança (autenticação, autorização, criptografia)
- Implementar data governance (qualidade, lineage, catalogação)
- Garantir conformidade com regulações (LGPD, GDPR, etc.)
- Estabelecer data contracts e SLAs
- Proteger dados sensíveis e PII adequadamente

**Evolução por nível:**
- **SE I-II**: Segue práticas de segurança estabelecidas
- **SE III**: Implementa controles de segurança e governança em projetos
- **Lead**: Define padrões de segurança e governança para o time
- **Staff**: Estabelece frameworks de governança organization-wide
- **Staff II-Principal**: Define políticas globais de segurança e compliance

---

## Como essa competência se manifesta

### Em SE I-II (Junior/Pleno)
- Escreve código limpo e testável seguindo padrões
- Aprende rapidamente novas ferramentas e tecnologias
- Identifica e reporta problemas de qualidade
- Contribui para melhorias incrementais

### Em SE III (Senior)
- Domina stack profundamente
- Propõe e lidera melhorias significativas em arquitetura, desempenho ou qualidade
- Estabelece padrões técnicos no time
- Referência técnica em pelo menos um subdomínio

### Em Lead Engineer
- Define direção técnica do time
- Garante qualidade e confiabilidade das entregas
- Gerencia débito técnico conscientemente
- Desenvolve capacidades técnicas do time

### Em Staff Engineer
- Referência técnica em múltiplos times
- Define padrões e práticas organization-wide
- Resolve problemas técnicos complexos que afetam múltiplos times
- Multiplica impacto através de frameworks e ferramentas

### Em Staff II (Senior Staff)
- Referência técnica em múltiplos domínios
- Lidera transformações técnicas de médio prazo
- Influencia direção técnica de toda área
- Desenvolve outros Staff e Lead Engineers

### Em Principal Engineer
- Autoridade técnica máxima
- Define estratégia técnica de longo prazo (1-3 anos)
- Cria alavancas estruturais que aceleram toda organização
- Conecta decisões técnicas a estratégia de negócio

---

## Conexão com Cultura Gupy

**Obsessão pelo Cliente**: Excelência técnica resulta em produtos confiáveis, rápidos e que entregam valor real aos clientes.

**Paixão por Inovar**: Experimentação responsável com novas tecnologias e abordagens, sempre aprendendo e melhorando.

**Agilidade para Resultado**: Equilíbrio entre qualidade e velocidade, evitando tanto perfeccionismo quanto código descuidado.

**Fazer Mais com Menos**: Simplicidade, eficiência, automação e reutilização reduzem desperdício e aumentam impacto.

**Juntos!**: Compartilhamento de conhecimento, revisões de código construtivas, elevação do nível técnico de toda equipe.
