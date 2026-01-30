# GUIA COMPLEMENTAR: SE III (SENIOR) NA PRÁTICA
## Material de apoio ao Framework Oficial

---

**Leia primeiro:** [Framework SE III - Documento Oficial](../../levels/SE_III_senior.md)

**Este documento:** Exemplos práticos para facilitar o entendimento do framework oficial

---

## O QUE MUDA DE SE II PARA SE III?

### SE II (Pleno)
- Implementa features completas com qualidade
- Resolve problemas técnicos complexos
- Colabora bem com o time

### SE III (Senior) - O QUE É NOVO:
- **Lidera tecnicamente** projetos (não só implementa)
- **Define estratégia** (roadmap, padrões, decisões arquiteturais)
- **Influencia além do time** (mentoria, padrões, visibilidade)
- **Pensa em impacto de negócio** (não só em código que funciona)

---

## EXEMPLOS PRÁTICOS POR PILAR

### 1. RESULTS (Resultados)

#### Impact (Impacto)

**Framework diz:**
> "Compreendo profundamente o contexto de negócio e uso isso para maximizar impacto nas decisões técnicas"

**Na prática:**
- ❌ "Implementei o filtro de data. Funciona bem."
- ✅ "Implementei filtro de data. Resultado: +15% de uso dos dashboards (métrica de engajamento que impacta retenção)."

**Framework diz:**
> "Tomo decisões técnicas com clareza de argumentação e documentação"

**Na prática:**
- ❌ Escolhe tecnologia e implementa
- ✅ Escreve tech spec explicando trade-offs: "Escolhi Nivo ao invés de Recharts porque precisamos de customização avançada (requisito para 5 casos de uso futuros). Trade-off: curva de aprendizado maior, mas aceitável dado que charts são core do produto."

---

#### Ownership

**Framework diz:**
> "Busco ativamente e elimino fontes de toil no time"

**Na prática:**
- Time perde 2h/semana debuggando problemas de cache
- SE III propõe e implementa solução de observabilidade que reduz tempo de debug em 70%

---

### 2. DIRECTION (Direção)

#### Strategy (Estratégia)

**Framework diz:**
> "Defino roadmap técnico para projetos impactantes de múltiplas fases"

**Na prática:**
- ❌ Pega tickets e implementa
- ✅ "Performance dos dashboards está ruim. Propus roadmap de 3 meses: (1) Lazy loading de componentes, (2) Otimização de queries, (3) Implementação de cache. Priorizei baseado em impacto vs esforço."

**Framework diz:**
> "Contribuo de forma consistente para padrões, boas práticas e referências"

**Na prática:**
- Cria documento: "Guia de Componentes Reutilizáveis" 
- Apresenta em tech talk
- Usa em code reviews como referência

---

### 3. TALENT (Talento)

#### Team Development

**Framework diz:**
> "Mentoro ativamente SE I/SE II, ajudando na evolução de hard e soft skills"

**Na prática - Code Review que ensina:**
```
❌ "LGTM 🚀"

✅ "Boa implementação! Algumas sugestões:

1. Performance: O useMemo não está prevenindo re-render porque
   a dependency array tem objeto novo toda vez. Sugiro extrair
   para constante fora do componente.
   
2. Testabilidade: Componente está fazendo demais (fetch + display).
   Vamos extrair lógica para custom hook? Facilita testar.
   
3. Ref: [link para guia de patterns]

Posso fazer pair programming se quiser!"
```

**Contexto especial - Guilherme:**
Como você é o único frontend no time, vamos discutir no 1:1 alternativas de mentoria: cross-time, tech talks, documentação educacional, etc.

---

### 4. CULTURE (Cultura)

#### Communication

**Framework diz:**
> "Comunico com clareza, adapto mensagem à audiência"

**Na prática:**
- **Para time técnico:** "Migrei para Nivo porque precisamos de customização avançada de tooltips e legends. Performance é similar ao Recharts mas API é mais verbosa."
- **Para produto:** "Consegui implementar as 3 visualizações customizadas que vocês pediram. Agora podemos criar novos tipos de gráficos 3x mais rápido."

---

## CRAFT PARA FRONTEND EM CONTEXTO DE DATA

O framework oficial fala de "dbt, pipelines, LLM". Para frontend em analytics:

### Fluência Técnica
- React, TypeScript, state management
- Visualização de dados (Nivo, D3, charts)
- Cube.js / queries / agregações (básico)
- Testing (unit, integration, E2E)

### Arquitetura
- Design systems e component libraries
- Performance (lazy loading, memoization, code splitting)
- State management em apps complexos
- Integração com backend/APIs de dados

### Estratégia Técnica
- Propor melhorias de DX (Storybook, visual regression)
- Otimizar performance de dashboards
- Definir padrões de componentes reutilizáveis
- Implementar observabilidade frontend

---

## CHECKLIST RÁPIDO: "ESTOU AGINDO COMO SE III?"

### Sobre Projetos:
- [ ] Lidero projetos tecnicamente (não só implemento)
- [ ] Documento decisões importantes (tech specs, ADRs)
- [ ] Penso em múltiplas fases (não só "fazer funcionar agora")

### Sobre Impacto:
- [ ] Sei explicar impacto de negócio do meu trabalho
- [ ] Proponho melhorias (não só reajo a demandas)
- [ ] Meço resultados (métricas, não só "deployei")

### Sobre Influência:
- [ ] Outros me procuram para dúvidas técnicas
- [ ] Contribuo com padrões/documentação
- [ ] Participo de decisões além do meu time

### Sobre Pessoas:
- [ ] Ajudo outros a crescerem (mentoria, reviews, pair programming)
- [ ] Dou feedback construtivo e específico
- [ ] Compartilho conhecimento (tech talks, docs, exemplos)

---

## 3 PERGUNTAS PARA REFLEXÃO

Antes de preencher a autoavaliação, reflita:

1. **"Qual projeto recente teve meu 'DNA' de liderança técnica?"**
   - Não só implementei, mas defini arquitetura, tomei decisões, documentei?

2. **"Quando foi a última vez que influenciei além do meu trabalho direto?"**
   - Padrão que criei? Mentoria que dei? Decisão que ajudei outro time?

3. **"Como meço sucesso do meu trabalho?"**
   - Só "funcionou"? Ou tenho métricas de impacto (performance, uso, satisfação)?

---

## PRÓXIMOS PASSOS

1. ✅ Leu o Framework Oficial completo
2. ✅ Leu este guia complementar
3. Agora preencha a autoavaliação
4. Anote dúvidas para o 1:1

---

**Lembre-se:** SE III não é sobre ser perfeito em tudo. É sobre:
- Liderar tecnicamente (estratégia, decisões, documentação)
- Influenciar positivamente (mentoria, padrões, colaboração)
- Pensar em impacto (negócio, não só código)

**Nos vemos na segunda!**
