> **Como planejar capacidade, priorizar trabalho e dizer não quando necessário**

---

## 🎯 Princípios de Planejamento

### 1. **Capacidade é finita**
Seu time não tem capacidade infinita. Planejar é escolher o que NÃO fazer.

### 2. **Buffer é obrigatório, não opcional**
Imprevistos sempre acontecem. 100% planned = over-committed.

### 3. **Balance é necessário**
~60-70% features, ~15-20% tech debt, ~15-20% sustentação/bugs.

### 4. **Predictabilidade > Velocidade máxima**
Melhor entregar consistentemente do que sprint heroico seguido de crash.

### 5. **Dizer não é parte do trabalho**
Você protege time de thrash. Nem tudo cabe.

---

## 📊 Entendendo Capacidade do Time

### 🧮 **Calculando Capacidade Real**

**Capacidade Nominal vs Real:**

```
Time de 5 pessoas:
├─ Capacidade nominal: 5 pessoas × 5 dias = 25 person-days
│
├─ Subtrair:
│  ├─ Meetings (daily, retro, planning, etc): 20%
│  ├─ Code review, suporte, interruptions: 15%
│  ├─ Férias, feriados: variável
│  ├─ 1-2 pessoas em sustentação/on-call: 20%
│  └─ Buffer para imprevistos: 15-20%
│
└─ Capacidade REAL: ~10-13 person-days (40-50% da nominal)
```

**Isso é NORMAL!** Se você acha que time tem 100% de capacidade, está iludido.

---

### 📋 **Template de Cálculo de Capacidade**

```markdown
## Capacidade - Sprint [Número] - [Datas]

### Time
- Total de pessoas: [N]
- Person-days totais: [N × dias úteis]

### Subtrações
- **Férias/ausências:**
  - [Nome]: [X dias]
  - Total: [Y person-days]

- **Sustentação/On-call:** [Z person-days]
  - [Quem está de on-call]

- **Meetings/overhead:** ~20% = [N person-days]

- **Tech debt/refactoring:** ~15-20% = [N person-days]

- **Buffer para imprevistos:** ~15-20% = [N person-days]

### Capacidade Real para Features
**[X person-days] (~40-50% da nominal)**

### Capacidade em Story Points (se usa)
**Velocity média: [X pontos]**
**Range esperado: [X-Y pontos]**
```

---

## 🎯 Framework de Priorização

### 📊 **Matriz de Impacto vs Esforço**

```
Alto Impacto
    │
    │  [Ganhos Rápidos]    │  [Grandes Apostas]
    │   → FAZER PRIMEIRO   │   → Planejar bem
    │  - Quick wins         │   - Projetos grandes
    │  - Alto ROI           │   - Preparação necessária
    │                       │
────┼───────────────────────┼─────────────────────────
    │                       │
    │  [Fill-ins]           │  [Money Pit]
    │   → Fazer se sobrar   │   → Evitar/repensar
    │  - Low priority       │   - Muito esforço, pouco retorno
    │  - Nice to have       │   - Questione "por quê?"
    │
Baixo Impacto            Baixo Esforço ───────────────► Alto Esforço
```

### 🎯 **Critérios de Priorização**

Para cada item, avalie:

**Impacto de Negócio:**
- Quantos usuários afeta?
- Impacto em revenue/retenção?
- É blocker para outro time/produto?
- Alinha com OKRs/goals?

**Urgência:**
- Tem deadline real? (não artificial)
- O que acontece se não fizer?
- Janela de oportunidade?

**Esforço:**
- Quantos person-days?
- Complexidade técnica?
- Dependências de outros times?
- Riscos/unknowns?

**Tech Debt/Risk:**
- Reduz dívida técnica?
- Aumenta dívida técnica?
- Riscos operacionais?

**Scoring (0-10):**
```
Prioridade = (Impacto × Urgência) / Esforço

Impacto: 0-10
Urgência: 0-10  
Esforço: 1-10 (nunca zero)

Exemplo:
├─ Feature A: (9 × 8) / 3 = 24 → Alta prioridade
├─ Feature B: (5 × 3) / 8 = 1.9 → Baixa prioridade
└─ Feature C: (8 × 9) / 5 = 14.4 → Média-alta
```

---

## 📅 Planning em Diferentes Níveis

### 📅 **Sprint Planning (1-2 semanas)**

**Objetivo:** O que vamos fazer nos próximos 7-14 dias?

**Processo:**
1. **Review de capacidade**
   - Quem está disponível?
   - Férias, feriados?
   - On-call/sustentação?
   - Capacidade real: X person-days

2. **Priorização com PM**
   - Top prioridades de negócio
   - Bloqueios técnicos críticos
   - Tech debt que não pode esperar
   - Bugs críticos

3. **Commitment realista**
   - Não over-commit
   - Deixar buffer (15-20%)
   - Transparente sobre trade-offs

4. **Clareza de escopo**
   - Cada item tem owner
   - Critérios de aceite claros
   - Dependências identificadas

**Output:** Sprint backlog com commitment realista

---

### 🗓️ **Quarterly Planning (3 meses)**

**Objetivo:** Roadmap do trimestre

**Processo:**
1. **Review do quarter anterior**
   - O que entregamos?
   - O que aprendemos?
   - Velocity real vs planejado?

2. **Alinhamento com estratégia**
   - OKRs do quarter
   - Prioridades de negócio
   - Iniciativas técnicas necessárias

3. **Capacity planning**
   - Férias conhecidas
   - Hiring plans
   - Expectativa de velocity
   - Capacidade total estimada

4. **Roadmap de alto nível**
   - Features principais (60-70%)
   - Tech debt/infra (15-20%)
   - Sustentação/bugs (15-20%)
   - Buffer para imprevistos (20%)

5. **Identificar riscos**
   - Dependências de outros times
   - Unknowns técnicos
   - Capacidade insuficiente?

**Output:** Roadmap do quarter com milestones

---

### 📆 **Anual Planning (12 meses)**

**Objetivo:** Visão de longo prazo

**Processo:**
1. **Estratégia de produto/negócio**
   - Onde empresa quer chegar?
   - OKRs anuais
   - Grandes iniciativas

2. **Capacity planning**
   - Hiring needs
   - Team growth
   - Skills gaps

3. **Tech strategy**
   - Migrations necessárias
   - Tech debt grande
   - Infra investments

4. **Roadmap de alto nível**
   - Quarters/milestones
   - Grandes releases
   - Não muito detalhe (vai mudar)

**Output:** Visão anual e plano de hiring

---

## 📊 Balanceamento de Trabalho

### ⚖️ **Regra 60-20-20**

```
📦 60-70% - Features / Roadmap
   ├─ Trabalho de produto
   ├─ Novas funcionalidades
   └─ Valor direto para usuário

🔧 15-20% - Tech Debt / Infra
   ├─ Refatoração necessária
   ├─ Upgrades de libs
   ├─ Melhorias de arquitetura
   └─ Investimento técnico

🐛 15-20% - Sustentação / Bugs
   ├─ Bugs a resolver
   ├─ Suporte a produção
   ├─ On-call / incidents
   └─ Manutenção geral
```

**Por quê este balance?**

- **60-70% features:** Mostra valor de negócio, progresso visível
- **15-20% tech debt:** Mantém saúde técnica, velocidade futura
- **15-20% sustentação:** Qualidade, reliability, operação saudável

**Red flags:**
- 🚩 90%+ features → Tech debt explodindo, velocity vai cair
- 🚩 40%+ tech debt → Não mostra valor de negócio suficiente
- 🚩 30%+ sustentação → Qualidade ruim ou system instável

---

### 📋 **Tracking de Balance**

```markdown
## Balance de Trabalho - Q1 2025

### Features (Target: 60-70%)
- Feature A: 5 person-days
- Feature B: 8 person-days
- Feature C: 3 person-days
**Total: 16 person-days (64%)** ✅

### Tech Debt (Target: 15-20%)
- Refactor API: 3 person-days
- Upgrade React: 2 person-days
**Total: 5 person-days (20%)** ✅

### Sustentação (Target: 15-20%)
- Bugs críticos: 2 person-days
- On-call: 2 person-days
**Total: 4 person-days (16%)** ✅

**Capacity total: 25 person-days**
```

---

## 🚫 Como Dizer Não

### 🎯 **Quando dizer não?**

- ✅ Não cabe na capacidade (realistically)
- ✅ Não alinha com prioridades/estratégia
- ✅ Há opção melhor (maior impacto)
- ✅ Trade-off não vale a pena
- ✅ Time não tem expertise necessária
- ✅ Timing está errado

### 💬 **Como dizer não efetivamente**

❌ **Ruim:**
> "Não dá para fazer isso."

✅ **Bom:**
> "Entendo a importância. Dado nossa capacidade atual e prioridades existentes, não conseguimos fazer isso neste quarter sem remover [X] ou [Y]. 
> 
> Opções:
> 1. Mover para próximo quarter
> 2. Reduzir escopo para MVP que cabe
> 3. Remover [item atual] para abrir espaço
> 
> Qual faz mais sentido para o negócio?"

**Elementos de "não" efetivo:**
1. Reconhece importância
2. Explica contexto/constraint
3. Oferece alternativas
4. Pergunta o que faz sentido
5. Não é só "não" - é trade-off informado

---

### 📋 **Scripts para Dizer Não**

#### **Não cabe na capacidade:**
> "Adoraria fazer isso, mas nossa capacidade este sprint já está commitada para [X, Y, Z]. Podemos adicionar para próximo sprint ou posso ajudar a re-priorizar o backlog atual. Preferência?"

#### **Não alinha com prioridade:**
> "Vejo o valor nisso. Como isso se compara com [prioridade atual]? Se for mais importante, precisamos mover [item X] para depois. Quer que eu facilite discussão de priorização com [stakeholder]?"

#### **Precisa de mais informação:**
> "Preciso entender melhor antes de committar. Posso ter [X horas] para investigar viabilidade técnica e voltar com estimativa realista e opções?"

#### **Trade-off não vale:**
> "Tecnicamente dá para fazer, mas vai levar [X semanas] e adicionar complexidade significativa. Dado o impacto [relativamente pequeno], recomendo [alternativa mais simples]. Pensamentos?"

#### **Timing ruim:**
> "Isso é importante mas o timing não é ideal. Estamos no meio de [contexto]. Fazer isso agora vai comprometer [X]. Podemos planejar para [quando] quando faz mais sentido?"

---

## 🚨 Lidando com Pressão

### 🔥 **"Precisa ser agora / É urgente"**

**Perguntas para fazer:**

1. **"O que acontece se não fizermos agora?"**
   - Às vezes "urgente" é artificial

2. **"O que podemos mover para depois para abrir espaço?"**
   - Mostra que capacidade é finita

3. **"Podemos fazer MVP/versão reduzida que cabe?"**
   - Oferece alternativa

4. **"Qual o deadline real vs desejado?"**
   - Separa nice-to-have de must-have

5. **"Quem decidiu que é prioridade?"**
   - Escala decisão para nível certo

---

### 💪 **Protegendo o Time de Thrash**

**Thrash = Mudança constante de prioridades**

**Sintomas:**
- Projeto começa, para, recomeça
- Prioridade #1 muda toda semana
- Time nunca termina nada
- Frustração e burnout

**Como proteger:**

1. **Não mude sprint no meio**
   - Sprint commitment é compromisso
   - Mudanças só se emergência real
   - "Urgência" nova vai para próximo sprint

2. **Buffer protege de emergências**
   - 15-20% do sprint é buffer
   - Para lidar com real emergências
   - Não preencha buffer com mais trabalho

3. **Escale thrash para cima**
   - "Estamos mudando prioridades toda semana. Isso está impactando moral e velocity do time. Precisamos de estabilidade."

4. **Estabeleça processo de mudança**
   - Mudanças vão por você, não direto para time
   - Avalia impacto antes de aceitar
   - Negocia com stakeholders

---

## 📊 Métricas de Planejamento

### ✅ **Métricas Saudáveis**

**Sprint Commitment Accuracy:**
- **Target:** 80-90%
- **Cálculo:** (Entregue / Planned) × 100
- **Trend:** Estável ao longo de sprints

**Velocity:**
- **Target:** Estável (não crescente infinitamente)
- **Cálculo:** Story points / sprint (se usa)
- **Trend:** Estável indica predictabilidade

**Balance de Trabalho:**
- **Features:** 60-70%
- **Tech debt:** 15-20%
- **Sustentação:** 15-20%

**Lead Time:**
- **Target:** Consistente
- **Cálculo:** Tempo de início → produção
- **Trend:** Não crescendo

### 🚩 **Red Flags**

- Sprint commitment < 70% ou > 100% consistentemente
- Velocity muito volátil (±50% sprint to sprint)
- Features > 80% consistentemente
- Lead time crescendo
- Rollbacks frequentes (qualidade ruim)

---

## ✅ Checklist de Planejamento Efetivo

**Sprint Planning:**
- [ ] Calculei capacidade real (não nominal)
- [ ] Deixei buffer de 15-20%
- [ ] Balance de features/tech debt/sustentação ok
- [ ] Cada item tem owner claro
- [ ] Dependências identificadas
- [ ] Não over-commitei time

**Quarterly Planning:**
- [ ] Roadmap alinha com OKRs/estratégia
- [ ] Considerei férias e hiring
- [ ] Identifiquei dependências cross-team
- [ ] Deixei buffer para imprevistos
- [ ] Comuniquei claramente a stakeholders

**Ongoing:**
- [ ] Protejo time de thrash
- [ ] Digo não quando necessário
- [ ] Monitoro velocity e commitment accuracy
- [ ] Ajusto planos baseado em realidade

---

## 🎯 Setup - Esta Semana

**Hoje:**
1. [ ] Calcular capacidade real do time (não nominal)
2. [ ] Review balance atual (features/tech debt/sustentação)
3. [ ] Identificar se está over-committed

**Se over-committed:**
4. [ ] Listar o que está no backlog
5. [ ] Re-priorizar com PM
6. [ ] Remover itens que não cabem
7. [ ] Comunicar mudanças

**Planning próximo sprint:**
8. [ ] Usar cálculo real de capacidade
9. [ ] Deixar buffer de 15-20%
10. [ ] Verificar balance de trabalho

---

## 💡 Lembre-se

> **"Planejamento não é sobre preencher 100% da capacidade. É sobre entregar consistentemente e sustentavelmente."**

Bom planejamento é:
- 📊 Baseado em capacidade real, não wishful thinking
- ⚖️ Balanceado entre features, tech debt e sustentação
- 🛡️ Protege time de thrash e over-commitment
- 🚫 Inclui dizer não e negociar trade-offs
- 📈 Gera predictabilidade e confiança

**Próximo passo:** Explore a pasta `templates/` para usar templates práticos prontos!

