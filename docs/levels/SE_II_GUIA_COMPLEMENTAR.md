# GUIA COMPLEMENTAR: SE II (PLENO) NA PRÁTICA
## Material de apoio ao Framework Oficial

---

**Leia primeiro:** [Framework SE II - Documento Oficial](https://github.com/amandanery-o/framework-carreira-data-ia/blob/main/levels/SE_II_pleno.md)

**Este documento:** Exemplos práticos para facilitar o entendimento do framework oficial

---

## O QUE MUDA DE SE I PARA SE II?

### SE I (Junior)
- Executa tarefas menores com orientação
- Foco em aprender e ganhar autonomia
- Trabalha em partes de projetos

### SE II (Pleno) - O QUE É NOVO:
- **Executa projetos completos** com autonomia
- **Toma decisões técnicas** sem supervisão constante
- **Resolve problemas complexos** de forma independente
- **Mentora juniores** e compartilha conhecimento

---

## EXEMPLOS PRÁTICOS POR PILAR

### 1. Resultados

#### Impacto

**Framework diz:**
> "Entrego projetos completos de complexidade média no prazo e com qualidade"

**Na prática:**
- ❌ Entrega apenas tarefas isoladas
- ✅ Pega feature completa (frontend + backend + testes + documentação) e entrega end-to-end

**Exemplo concreto:**
- Feature: "Adicionar filtro de período nos relatórios"
- SE I: Implementa apenas o componente visual do filtro
- SE II: Implementa filtro (frontend), ajusta queries (backend), adiciona testes, atualiza documentação, valida com produto

---

#### Responsabilidade

**Framework diz:**
> "Participo de rotações de on-call e respondo a incidentes de forma efetiva"

**Na prática:**
- ❌ Fica perdido durante incidentes, quase sempre escala
- ✅ Investiga, resolve problemas comuns, documenta, escala quando necessário

**Exemplo de resposta a incidente:**
```
1. Recebe alerta: "Query lenta no dashboard X"
2. Investiga logs, identifica query específica
3. Analisa explain plan, identifica falta de índice
4. Cria índice temporário, valida melhoria
5. Abre ticket para fix permanente
6. Documenta no runbook
```

---

#### Tomada de Decisão

**Framework diz:**
> "Tomo decisões técnicas para problemas bem definidos com autonomia"

**Na prática:**
- ❌ Precisa perguntar tudo: "Qual biblioteca uso?", "Como estruturo isso?"
- ✅ Pesquisa alternativas, avalia trade-offs, decide, implementa, comunica decisão

**Exemplo:**
```
Problema: Precisa cachear dados de referência

❌ SE I: "Como faço cache? Redis ou memória?"

✅ SE II: 
"Analisando o caso:
- Dados mudam 1x/dia
- Tamanho: ~10MB
- Acesso: leitura frequente

Decisão: Cache em memória (simples, suficiente)
Trade-off: Precisa restartar app para atualizar
Alternativa futura: Redis se precisar invalidação dinâmica"
```

---

### 2. Direção

#### Agilidade

**Framework diz:**
> "Me adapto rapidamente a mudanças de prioridade e requisitos"

**Na prática:**
- ❌ Fica frustrado com mudanças, resiste, reclama
- ✅ Entende contexto, ajusta trabalho, replaneja, segue em frente

**Exemplo:**
```
Situação: Estava desenvolvendo Feature A, 
          agora prioridade mudou para Bug Crítico B

❌ "Mas eu estava quase terminando A..."

✅ "Entendi. Vou:
   1. Commitar trabalho atual de A em branch
   2. Focar em B imediatamente
   3. Retomar A assim que B estiver resolvido
   Consigo resolver B hoje ainda."
```

---

#### Inovação

**Framework diz:**
> "Identifico oportunidades de melhorias além da minha tarefa imediata"

**Na prática:**
- ❌ Faz apenas o que foi pedido, não questiona
- ✅ Implementa o pedido + propõe melhorias relacionadas

**Exemplo:**
```
Tarefa: "Corrigir bug no filtro X"

SE II faz:
1. ✅ Corrige o bug
2. ✅ Adiciona teste para prevenir regressão
3. ✅ Nota que filtros Y e Z têm código similar
4. ✅ Propõe: "Vi que temos 3 filtros com lógica parecida.
              Posso refatorar para componente reutilizável?
              Benefício: menos duplicação, mais fácil manter."
```

---

### 3. Talento

#### Crescimento Pessoal

**Framework diz:**
> "Recebo feedback bem, implemento melhorias e busco crescimento continuamente"

**Na prática - revisão de código:**
```
❌ Atitude defensiva:
"Mas funciona desse jeito também..."
"Não entendi por que precisa mudar..."

✅ Atitude de crescimento:
"Interessante, não tinha pensado nisso. Faz sentido por [razão]."
"Vou mudar. Aproveitando, tem algum padrão documentado sobre isso?"
"Obrigado pelo feedback! Vou aplicar em outros lugares também."
```

---

#### Desenvolvimento do Time (Mentoria)

**Framework diz:**
> "Posso mentorar novos membros, estagiários ou engenheiros mais juniores"

**Na prática - mentoria em revisão de código:**
```
❌ Crítica sem contexto:
"Esse código está ruim. Refaz."

✅ Mentoria educativa:
"Boa implementação! Algumas sugestões:

1. Performance: Essa query faz N+1. 
   Sugestão: Usar join ou eager loading.
   Exemplo: [link/código]

2. Legibilidade: Nomes de variáveis pouco descritivos.
   Sugestão: `data` → `salesByMonth`
   
3. Quer fazer pair programming para discutir?"
```

**Na prática - programação em par:**
- Explica o "porquê", não só o "como"
- Deixa o junior tentar primeiro, orienta quando trava
- Compartilha atalhos e dicas de ferramentas

---

### 4. Cultura

#### Colaboração

**Framework diz:**
> "Colaboro efetivamente com PM, Design, Data, outros times"

**Na prática - kickoff de projeto:**
```
❌ Atitude passiva:
- Ouve a spec
- Começa a codar
- Descobre problemas depois

✅ Atitude proativa:
- Ouve a spec
- Faz perguntas técnicas relevantes:
  * "Qual volume de dados esperamos?"
  * "Tem dependência de outro time?"
  * "Qual prazo crítico de negócio?"
- Identifica riscos cedo
- Propõe alternativas se necessário
```

---

#### Comunicação

**Framework diz:**
> "Comunico proativamente progresso, riscos e decisões técnicas"

**Na prática - update em projeto:**
```
❌ Update vago:
"Projeto indo bem"

✅ Update estruturado:
"Status do Projeto X:
- ✅ Concluído: Backend (API + testes)
- 🟡 Em progresso: Frontend (70% pronto)
- ⏱️ Próximo: Integração + validação (2 dias)
- ⚠️ Risco: Dependência do time Y (aguardando aprovação)
- 📅 Entrega: Mantém para sexta-feira"
```

---

## CHECKLIST RÁPIDO: "ESTOU AGINDO COMO SE II?"

### Sobre Projetos:
- [ ] Entrego features completas, não só tarefas isoladas
- [ ] Tomo decisões técnicas sem perguntar tudo
- [ ] Identifico e escalo riscos proativamente

### Sobre Qualidade:
- [ ] Meus PRs incluem testes automatizados
- [ ] Documento decisões técnicas não-óbvias
- [ ] Penso em manutenibilidade de longo prazo

### Sobre Autonomia:
- [ ] Pesquiso e avalio alternativas antes de perguntar
- [ ] Resolvo problemas comuns sozinho
- [ ] Sei quando escalar vs. quando resolver

### Sobre Colaboração:
- [ ] Dou feedback construtivo em revisões de código
- [ ] Ajudo juniores ativamente (não só quando pedem)
- [ ] Comunico progresso e riscos claramente

---

## 3 PERGUNTAS PARA REFLEXÃO

Antes de preencher a autoavaliação, reflita:

1. **"Qual foi o último projeto completo que entreguei end-to-end?"**
   - Foi apenas uma tarefa isolada? Ou feature completa com testes + doc?

2. **"Como lido com ambiguidade e mudanças de prioridade?"**
   - Fico paralisado esperando direção? Ou busco informações e sigo?

3. **"Estou desenvolvendo outros engenheiros?"**
   - Minhas revisões de código ensinam? Ou só aprovam/rejeitam?

---

## DIFERENÇAS-CHAVE: SE I → SE II → SE III

### Escopo de Trabalho
- **SE I:** Tarefas menores, bem definidas
- **SE II:** Projetos completos, complexidade média
- **SE III:** Projetos multi-fase, alta complexidade

### Autonomia
- **SE I:** Precisa de orientação frequente
- **SE II:** Decide tecnicamente com mínima orientação
- **SE III:** Define direção técnica e padrões

### Mentoria
- **SE I:** Recebe mentoria, colabora com pares
- **SE II:** Mentora juniores ativamente
- **SE III:** Mentora plenos, influencia time inteiro

### Impacto
- **SE I:** Impacto em tarefas individuais
- **SE II:** Impacto em projetos do time
- **SE III:** Impacto em estratégia e arquitetura

---

## PRÓXIMOS PASSOS

1. ✅ Leu o Framework Oficial completo
2. ✅ Leu este guia complementar
3. Agora preencha a autoavaliação
4. Anote dúvidas para o 1:1

---

## SINAIS DE QUE ESTÁ PRONTO PARA SE III

Você vem fazendo isso de forma consistente (6+ meses):
- ✅ Liderando projetos tecnicamente (não só implementando)
- ✅ Influenciando decisões arquiteturais
- ✅ Mentorando juniores e plenos com impacto visível
- ✅ Pensando em impacto de negócio, não só código
- ✅ Sendo referência técnica em 1-2 áreas

---

**Lembre-se:** SE II não é sobre saber tudo. É sobre:
- Executar projetos completos com qualidade
- Decidir tecnicamente com autonomia
- Colaborar efetivamente cross-time
- Desenvolver outros engenheiros
