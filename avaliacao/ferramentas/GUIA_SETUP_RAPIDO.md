> Coloque o sistema no ar em 10 passos (30 minutos)

---

## 📋 Checklist Rápido

- [ ] **Passo 1:** Criar 3 Google Forms (10 min)
- [ ] **Passo 2:** Criar Google Sheets (5 min)
- [ ] **Passo 3:** Conectar Forms → Sheets (3 min)
- [ ] **Passo 4:** Copiar fórmulas e estrutura (5 min)
- [ ] **Passo 5:** Configurar gráficos radar (5 min)
- [ ] **Passo 6:** Adicionar Apps Script (2 min)
- [ ] **Passo 7:** Testar sistema (5 min)
- [ ] **Passo 8:** Salvar como template (2 min)
- [ ] **Passo 9:** Fazer primeira avaliação de teste (variável)
- [ ] **Passo 10:** Ajustar e escalar

**Tempo total:** ~30-40 minutos

---

## 🎯 PASSO 1: Criar Google Forms

### Form 1: Auto-Avaliação

1. Ir para [forms.google.com](https://forms.google.com)
2. Clicar em "+" (Novo formulário em branco)
3. Título: **"Avaliação 360º - Auto-Avaliação"**
4. Descrição: **"Avalie a si mesmo nas 5 dimensões (0-5). Tempo: 30-45 min"**

#### Seção 1: Informações Básicas

**Pergunta 1:** Nome (Resposta curta, obrigatório)
**Pergunta 2:** Nível Atual (Múltipla escolha, obrigatório)
- SE I (Junior)
- SE II (Pleno)
- SE III (Senior)
- Lead Engineer
- Staff Engineer
- Staff II (Senior Staff)
- Principal Engineer

**Pergunta 3:** Trilha (Múltipla escolha, obrigatório)
- Data Engineering
- Analytics Engineering
- Cientista de Dados

**Pergunta 4:** Período de Avaliação (Resposta curta)
- Exemplo: "Jan-Jun 2025"

---

#### Seção 2: Dimensões (Escala Linear 0-5)

**Instruções na seção:**
```
Avalie cada dimensão de 0 a 5:
0 = Não demonstrado
1 = Raramente
2 = Às vezes
3 = Frequentemente (expectativa do nível)
4 = Consistentemente (supera expectativas)
5 = Exemplar (próximo nível)
```

**Pergunta 5:** 🏆 **Results** - Impacto, Ownership, Decisões (Escala linear 0-5, obrigatório)

**Pergunta 6:** 🌟 **Direction** - Agilidade, Inovação, Estratégia (Escala linear 0-5, obrigatório)

**Pergunta 7:** 🌳 **Talent** - Crescimento Pessoal, Desenvolvimento de Outros (Escala linear 0-5, obrigatório)

**Pergunta 8:** 🌈 **Culture** - Colaboração, Comunicação, Liderança Cultural (Escala linear 0-5, obrigatório)

**Pergunta 9:** 🛠️ **Craft** - Habilidades Técnicas (Escala linear 0-5, obrigatório)

---

#### Seção 3: Valores Gupy (Escala Linear 0-5)

**Pergunta 10:** 🎯 **Obsessão pelo Cliente** (Escala linear 0-5, obrigatório)

**Pergunta 11:** 💡 **Paixão por Inovar** (Escala linear 0-5, obrigatório)

**Pergunta 12:** ⚡ **Agilidade para Resultado** (Escala linear 0-5, obrigatório)

**Pergunta 13:** 💰 **Fazer Mais com Menos** (Escala linear 0-5, obrigatório)

**Pergunta 14:** 🤝 **Juntos!** (Escala linear 0-5, obrigatório)

---

#### Seção 4: Reflexões (Opcional mas Valioso)

**Pergunta 15:** Principais Forças - Quais são suas 2-3 maiores forças? (Parágrafo, opcional)

**Pergunta 16:** Áreas de Desenvolvimento - Quais 2-3 áreas você quer desenvolver? (Parágrafo, opcional)

**Pergunta 17:** O Que Te Surpreendeu? (Parágrafo, opcional)

---

5. **Configurações do Form:**
   - ⚙️ Configurações → Coletar endereço de email: SIM
   - Limitar a 1 resposta: SIM (opcional)
   - Editar após enviar: NÃO

6. **Salvar o link**
   - Clicar em "Enviar" → Copiar link
   - Salvar: `Link Form Auto-Avaliação: [URL]`

---

### Form 2: Avaliação de Par (SIMPLIFICADA)

1. **Duplicar** o Form 1 (mais rápido)
2. Mudar título: **"Avaliação 360º - Avaliação de Par"**
3. Mudar descrição: **"Avalie seu colega nas 5 dimensões (0-5). Tempo: 15-20 min"**

#### Mudanças:

**Seção 1: Informações**
- **Pergunta 1:** Seu Nome (Resposta curta, obrigatório)
- **Pergunta 2:** Nome da Pessoa que Você Está Avaliando (Resposta curta, obrigatório)
- **REMOVER:** Perguntas 2, 3, 4 (nível, trilha, período)

**Seção 2: Dimensões** (MANTER igual - perguntas 5-9)

**Seção 3: Valores Gupy** (MANTER igual - perguntas 10-14)

**Seção 4: Reflexões** (SIMPLIFICAR)
- **REMOVER** perguntas 16, 17
- **MANTER apenas:**
  - Pergunta 15: O que essa pessoa faz excepcionalmente bem? (Parágrafo, opcional)
  - Pergunta 16 (nova): Uma oportunidade de crescimento? (Parágrafo, opcional)

3. **Salvar o link**
   - `Link Form Par: [URL]`

---

### Form 3: Avaliação do Gestor (COMPLETA)

1. **Duplicar** o Form 1 (Auto-Avaliação)
2. Mudar título: **"Avaliação 360º - Avaliação do Gestor"**
3. Mudar descrição: **"Avalie seu liderado nas 5 dimensões (0-5). Tempo: 30-45 min"**

#### Mudanças:

**Seção 1: Informações**
- **Pergunta 1:** Nome da Pessoa Avaliada (Resposta curta, obrigatório)
- **Pergunta 2:** Nível Atual (manter)
- **Pergunta 3:** Trilha (manter)
- **Pergunta 4:** Período (manter)
- **Pergunta 5 (nova):** Seu Nome (Gestor) (Resposta curta, obrigatório)

**Seção 2 e 3:** MANTER igual (dimensões + valores)

**Seção 4: Análise do Gestor** (EXPANDIR)
- Pergunta 15: Principais Forças (Top 3) (Parágrafo, obrigatório)
- Pergunta 16: Áreas de Desenvolvimento (Top 2-3) (Parágrafo, obrigatório)
- Pergunta 17: Prontidão para Próximo Nível (Múltipla escolha, obrigatório)
  * Não - Opera no nível atual ou abaixo
  * Quase - Demonstra algumas capacidades inconsistentemente
  * Pronto - Demonstra consistentemente (6+ meses)
  * Muito Pronto - Opera acima do próximo nível
- Pergunta 18: Justificativa da Prontidão (Parágrafo, obrigatório)

3. **Salvar o link**
   - `Link Form Gestor: [URL]`

---

## 📊 PASSO 2: Criar Google Sheets

1. Ir para [sheets.google.com](https://sheets.google.com)
2. Criar planilha nova: **"Sistema 360º - [Nome da Pessoa]"**

### Criar 7 Abas:

1. **📋 Respostas Auto** (será populada pelo Form 1)
2. **📋 Respostas Pares** (será populada pelo Form 2)
3. **📋 Respostas Gestor** (será populada pelo Form 3)
4. **📊 Consolidação** (você vai criar fórmulas)
5. **📈 Radar Competências** (gráfico)
6. **🌈 Radar Valores** (gráfico)
7. **🎯 Análise Gaps** (cálculos)

---

## 🔗 PASSO 3: Conectar Forms → Sheets

### Form 1 (Auto-Avaliação):

1. Abrir o Form 1
2. Clicar em "Respostas" (aba superior)
3. Clicar no ícone Google Sheets (verde) no canto superior direito
4. Selecionar: **"Selecionar planilha existente"**
5. Escolher a planilha criada no Passo 2
6. Escolher aba: **"📋 Respostas Auto"**
7. Criar

### Form 2 (Par):

1. Repetir processo
2. Conectar à aba: **"📋 Respostas Pares"**

### Form 3 (Gestor):

1. Repetir processo
2. Conectar à aba: **"📋 Respostas Gestor"**

---

## 📐 PASSO 4: Estruturar Aba "Consolidação"

**Vou fornecer a estrutura exata abaixo** ⬇️

### Aba: 📊 Consolidação

#### Seção 1: Informações da Pessoa (A1:B5)

| A | B |
|---|---|
| **Nome** | =Respostas Auto!B2 |
| **Nível** | =Respostas Auto!C2 |
| **Trilha** | =Respostas Auto!D2 |
| **Período** | =Respostas Auto!E2 |
| **Data Avaliação** | =TODAY() |

---

#### Seção 2: Dimensões Consolidadas (A8:G14)

| Dimensão | Auto | Par 1 | Par 2 | Par 3 | Gestor | Média Geral |
|----------|------|-------|-------|-------|--------|-------------|
| Results | =Respostas Auto!F2 | =Respostas Pares!D2 | =Respostas Pares!D3 | =Respostas Pares!D4 | =Respostas Gestor!F2 | =AVERAGE(B9:F9) |
| Direction | =Respostas Auto!G2 | =Respostas Pares!E2 | =Respostas Pares!E3 | =Respostas Pares!E4 | =Respostas Gestor!G2 | =AVERAGE(B10:F10) |
| Talent | =Respostas Auto!H2 | =Respostas Pares!F2 | =Respostas Pares!F3 | =Respostas Pares!F4 | =Respostas Gestor!H2 | =AVERAGE(B11:F11) |
| Culture | =Respostas Auto!I2 | =Respostas Pares!G2 | =Respostas Pares!G3 | =Respostas Pares!G4 | =Respostas Gestor!I2 | =AVERAGE(B12:F12) |
| Craft | =Respostas Auto!J2 | =Respostas Pares!H2 | =Respostas Pares!H3 | =Respostas Pares!H4 | =Respostas Gestor!J2 | =AVERAGE(B13:F13) |
| **MÉDIA** | =AVERAGE(B9:B13) | =AVERAGE(C9:C13) | =AVERAGE(D9:D13) | =AVERAGE(E9:E13) | =AVERAGE(F9:F13) | =AVERAGE(G9:G13) |

**Nota:** Ajuste as referências das colunas conforme a ordem das perguntas nos seus forms!

---

#### Seção 3: Valores Gupy (A17:G23)

| Valor | Auto | Par 1 | Par 2 | Par 3 | Gestor | Média Geral |
|-------|------|-------|-------|-------|--------|-------------|
| Obsessão Cliente | =Respostas Auto!K2 | =Respostas Pares!I2 | =Respostas Pares!I3 | =Respostas Pares!I4 | =Respostas Gestor!K2 | =AVERAGE(B18:F18) |
| Paixão Inovar | =Respostas Auto!L2 | =Respostas Pares!J2 | =Respostas Pares!J3 | =Respostas Pares!J4 | =Respostas Gestor!L2 | =AVERAGE(B19:F19) |
| Agilidade Resultado | =Respostas Auto!M2 | =Respostas Pares!K2 | =Respostas Pares!K3 | =Respostas Pares!K4 | =Respostas Gestor!M2 | =AVERAGE(B20:F20) |
| Fazer Mais Menos | =Respostas Auto!N2 | =Respostas Pares!L2 | =Respostas Pares!L3 | =Respostas Pares!L4 | =Respostas Gestor!N2 | =AVERAGE(B21:F21) |
| Juntos! | =Respostas Auto!O2 | =Respostas Pares!M2 | =Respostas Pares!M3 | =Respostas Pares!M4 | =Respostas Gestor!O2 | =AVERAGE(B22:F22) |
| **MÉDIA** | =AVERAGE(B18:B22) | =AVERAGE(C18:C22) | =AVERAGE(D18:D22) | =AVERAGE(E18:E22) | =AVERAGE(F18:F22) | =AVERAGE(G18:G22) |

---

#### Seção 4: Expectativas por Nível (A26:F32)

| Nível | Results | Direction | Talent | Culture | Craft |
|-------|---------|-----------|--------|---------|-------|
| SE I | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 |
| SE II | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| SE III | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 |
| Lead | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 |
| Staff | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 |

---

## 📈 PASSO 5: Criar Gráficos Radar

### Aba: 📈 Radar Competências

#### Preparar Dados para o Gráfico (A1:E6):

| Dimensão | Atual | Nível Atual | Próximo Nível | 2 Níveis |
|----------|-------|-------------|---------------|----------|
| Results | =Consolidação!G9 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,2,0) | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,2,0)+1 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,2,0)+2 |
| Direction | =Consolidação!G10 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,3,0) | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,3,0)+1 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,3,0)+2 |
| Talent | =Consolidação!G11 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,4,0) | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,4,0)+1 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,4,0)+2 |
| Culture | =Consolidação!G12 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,5,0) | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,5,0)+1 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,5,0)+2 |
| Craft | =Consolidação!G13 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,6,0) | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,6,0)+1 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,6,0)+2 |

**Nota:** Ajuste o VLOOKUP para buscar o nível correto. Pode precisar usar IF para mapear o texto do nível.

#### Criar Gráfico:

1. Selecionar toda a tabela (A1:E6)
2. Inserir → Gráfico
3. Tipo de gráfico: **Radar** (ou Scatter se radar não disponível)
4. Personalizar:
   - Série "Atual": Azul, linha grossa
   - Série "Nível Atual": Vermelho, linha média
   - Série "Próximo Nível": Amarelo, linha média
   - Série "2 Níveis": Verde, linha tracejada

---

### Aba: 🌈 Radar Valores

#### Preparar Dados (A1:E6):

| Valor | Auto | Pares Média | Gestor | Expectativa |
|-------|------|-------------|--------|-------------|
| Obsessão Cliente | =Consolidação!B18 | =AVERAGE(Consolidação!C18:E18) | =Consolidação!F18 | 3.0 |
| Paixão Inovar | =Consolidação!B19 | =AVERAGE(Consolidação!C19:E19) | =Consolidação!F19 | 3.0 |
| Agilidade Resultado | =Consolidação!B20 | =AVERAGE(Consolidação!C20:E20) | =Consolidação!F20 | 3.0 |
| Fazer Mais Menos | =Consolidação!B21 | =AVERAGE(Consolidação!C21:E21) | =Consolidação!F21 | 3.0 |
| Juntos! | =Consolidação!B22 | =AVERAGE(Consolidação!C22:E22) | =Consolidação!F22 | 3.0 |

#### Criar Gráfico:

1. Selecionar A1:E6
2. Inserir → Gráfico → Radar
3. Personalizar cores:
   - Auto: Azul
   - Pares: Roxo
   - Gestor: Laranja
   - Expectativa: Vermelho

---

## 🎯 PASSO 6: Aba Análise de Gaps

### Aba: 🎯 Análise Gaps

#### Gaps vs. Nível Atual (A1:E7):

| Dimensão | Atual | Expectativa | Gap | Status |
|----------|-------|-------------|-----|--------|
| Results | =Consolidação!G9 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,2,0) | =B2-C2 | =IF(D2<0,"🔴 ABAIXO",IF(D2>0.5,"🟢 SUPERA","🟡 ATENDE")) |
| Direction | =Consolidação!G10 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,3,0) | =B3-C3 | =IF(D3<0,"🔴 ABAIXO",IF(D3>0.5,"🟢 SUPERA","🟡 ATENDE")) |
| Talent | =Consolidação!G11 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,4,0) | =B4-C4 | =IF(D4<0,"🔴 ABAIXO",IF(D4>0.5,"🟢 SUPERA","🟡 ATENDE")) |
| Culture | =Consolidação!G12 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,5,0) | =B5-C5 | =IF(D5<0,"🔴 ABAIXO",IF(D5>0.5,"🟢 SUPERA","🟡 ATENDE")) |
| Craft | =Consolidação!G13 | =VLOOKUP(Consolidação!B2,Consolidação!A27:F32,6,0) | =B6-C6 | =IF(D6<0,"🔴 ABAIXO",IF(D6>0.5,"🟢 SUPERA","🟡 ATENDE")) |

#### Gaps vs. Próximo Nível (A10:F16):

| Dimensão | Atual | Próximo Nível | Gap | Prioridade | Ordem |
|----------|-------|---------------|-----|------------|-------|
| Results | =B2 | =C2+1 | =B11-C11 | =IF(D11<-0.5,"🔴 P1",IF(D11<0,"🟡 P2","🟢 PRONTO")) | =RANK(D11,$D$11:$D$15,1) |
| Direction | =B3 | =C3+1 | =B12-C12 | =IF(D12<-0.5,"🔴 P1",IF(D12<0,"🟡 P2","🟢 PRONTO")) | =RANK(D12,$D$11:$D$15,1) |
| Talent | =B4 | =C4+1 | =B13-C13 | =IF(D13<-0.5,"🔴 P1",IF(D13<0,"🟡 P2","🟢 PRONTO")) | =RANK(D13,$D$11:$D$15,1) |
| Culture | =B5 | =C5+1 | =B14-C14 | =IF(D14<-0.5,"🔴 P1",IF(D14<0,"🟡 P2","🟢 PRONTO")) | =RANK(D14,$D$11:$D$15,1) |
| Craft | =B6 | =C6+1 | =B15-C15 | =IF(D15<-0.5,"🔴 P1",IF(D15<0,"🟡 P2","🟢 PRONTO")) | =RANK(D15,$D$11:$D$15,1) |

**Formatação Condicional:**
- Coluna Status: Verde para 🟢, Amarelo para 🟡, Vermelho para 🔴

---

## 🤖 PASSO 7: Apps Script (Opcional - Automação Extra)

**Por enquanto, pule este passo!** O sistema já funciona com as fórmulas.

Apps Script seria usado para:
- Enviar emails automáticos
- Gerar PDFs automaticamente
- Notificações quando forms completados

**Podemos adicionar depois se precisar!**

---

## ✅ PASSO 8: Testar o Sistema

### Teste Completo:

1. **Preencher Form 1** (Auto) com dados de teste
2. **Preencher Form 2** (Par) 3 vezes (simular 3 pares)
3. **Preencher Form 3** (Gestor) 1 vez
4. **Verificar aba Consolidação**: Dados apareceram?
5. **Verificar Radares**: Gráficos gerados?
6. **Verificar Gaps**: Cálculos corretos?

**Se tudo funcionar: ✅ Sistema pronto!**

---

## 💾 PASSO 9: Salvar como Template

1. Fazer cópia da planilha: **"[TEMPLATE] Sistema 360º"**
2. Limpar abas de respostas (deixar só a estrutura)
3. Toda vez que for avaliar alguém novo:
   - Copiar o template
   - Renomear: "Sistema 360º - [Nome da Pessoa]"
   - Enviar links dos forms

---

## 🚀 PASSO 10: Usar!

### Para Cada Nova Avaliação:

1. **Copiar** o template
2. **Renomear** com nome da pessoa
3. **Enviar links**:
   - Form 1 → Para a pessoa
   - Form 2 → Para 2-3 pares
   - Form 3 → Para você (gestor)
4. **Aguardar** 1-2 semanas
5. **Abrir planilha** → Radares prontos!
6. **Exportar PDF** dos radares
7. **Fazer reunião** 1:1 de feedback

**Tempo:** 5 minutos por avaliação! ⚡

---

## 🎯 Resultado Final

Você terá:
- ✅ 3 Google Forms (coleta automatizada)
- ✅ 1 Google Sheets (processamento automático)
- ✅ Radares visuais (gerados automaticamente)
- ✅ Análise de gaps (calculada automaticamente)
- ✅ Sistema escalável (1 pessoa ou 50)

**Custo:** $0 (tudo gratuito no Google Workspace)

---

## 🆘 Troubleshooting

### Problema: Forms não conectaram ao Sheets
**Solução:** Verificar permissões, refazer conexão

### Problema: Fórmulas dando erro
**Solução:** Verificar referências das colunas (pode variar conforme ordem das perguntas)

### Problema: Gráfico não aparece
**Solução:** Dados precisam ser numéricos (0-5), não texto

### Problema: Múltiplos pares (mais de 3)
**Solução:** Adicionar colunas Par 4, Par 5... e ajustar fórmula AVERAGE

---

## 📞 Precisa de Ajuda?

Se tiver dúvidas durante o setup, me chame! Posso ajustar as fórmulas ou criar versão mais simples.

**Próximo passo:** Começar a criar os forms! 🚀

