> Copie e cole estas fórmulas direto na sua planilha!

---

## 🎯 Aba: Consolidação

### Seção 1: Informações (Cole em A1)

```
Nome	=IFERROR('Respostas Auto'!B2,"[Aguardando]")
Nível	=IFERROR('Respostas Auto'!C2,"[Aguardando]")
Trilha	=IFERROR('Respostas Auto'!D2,"[Aguardando]")
Período	=IFERROR('Respostas Auto'!E2,"[Aguardando]")
Data Avaliação	=TODAY()
```

---

### Seção 2: Dimensões (Cole em A7)

```
Dimensão	Auto	Par 1	Par 2	Par 3	Gestor	Média Geral
Results	='Respostas Auto'!F2	='Respostas Pares'!D2	='Respostas Pares'!D3	='Respostas Pares'!D4	='Respostas Gestor'!F2	=IFERROR(AVERAGE(B8:F8),"")
Direction	='Respostas Auto'!G2	='Respostas Pares'!E2	='Respostas Pares'!E3	='Respostas Pares'!E4	='Respostas Gestor'!G2	=IFERROR(AVERAGE(B9:F9),"")
Talent	='Respostas Auto'!H2	='Respostas Pares'!F2	='Respostas Pares'!F3	='Respostas Pares'!F4	='Respostas Gestor'!H2	=IFERROR(AVERAGE(B10:F10),"")
Culture	='Respostas Auto'!I2	='Respostas Pares'!G2	='Respostas Pares'!G3	='Respostas Pares'!G4	='Respostas Gestor'!I2	=IFERROR(AVERAGE(B11:F11),"")
Craft	='Respostas Auto'!J2	='Respostas Pares'!H2	='Respostas Pares'!H3	='Respostas Pares'!H4	='Respostas Gestor'!J2	=IFERROR(AVERAGE(B12:F12),"")
MÉDIA	=IFERROR(AVERAGE(B8:B12),"")	=IFERROR(AVERAGE(C8:C12),"")	=IFERROR(AVERAGE(D8:D12),"")	=IFERROR(AVERAGE(E8:E12),"")	=IFERROR(AVERAGE(F8:F12),"")	=IFERROR(AVERAGE(G8:G12),"")
```

**⚠️ IMPORTANTE:** Ajuste as colunas F, G, H, I, J conforme a ordem das perguntas nos seus forms!

---

### Seção 3: Valores Gupy (Cole em A15)

```
Valor	Auto	Par 1	Par 2	Par 3	Gestor	Média Geral
Obsessão Cliente	='Respostas Auto'!K2	='Respostas Pares'!I2	='Respostas Pares'!I3	='Respostas Pares'!I4	='Respostas Gestor'!K2	=IFERROR(AVERAGE(B16:F16),"")
Paixão Inovar	='Respostas Auto'!L2	='Respostas Pares'!J2	='Respostas Pares'!J3	='Respostas Pares'!J4	='Respostas Gestor'!L2	=IFERROR(AVERAGE(B17:F17),"")
Agilidade Resultado	='Respostas Auto'!M2	='Respostas Pares'!K2	='Respostas Pares'!K3	='Respostas Pares'!K4	='Respostas Gestor'!M2	=IFERROR(AVERAGE(B18:F18),"")
Fazer Mais Menos	='Respostas Auto'!N2	='Respostas Pares'!L2	='Respostas Pares'!L3	='Respostas Pares'!L4	='Respostas Gestor'!N2	=IFERROR(AVERAGE(B19:F19),"")
Juntos!	='Respostas Auto'!O2	='Respostas Pares'!M2	='Respostas Pares'!M3	='Respostas Pares'!M4	='Respostas Gestor'!O2	=IFERROR(AVERAGE(B20:F20),"")
MÉDIA	=IFERROR(AVERAGE(B16:B20),"")	=IFERROR(AVERAGE(C16:C20),"")	=IFERROR(AVERAGE(D16:D20),"")	=IFERROR(AVERAGE(E16:E20),"")	=IFERROR(AVERAGE(F16:F20),"")	=IFERROR(AVERAGE(G16:G20),"")
```

**⚠️ IMPORTANTE:** Ajuste as colunas K, L, M, N, O conforme seus forms!

---

### Seção 4: Expectativas por Nível (Cole em A24)

```
Nível	Results	Direction	Talent	Culture	Craft
SE I	2.0	2.0	2.0	2.0	2.0
SE II	3.0	3.0	3.0	3.0	3.0
SE III	4.0	4.0	4.0	4.0	4.0
Lead	4.5	4.5	4.5	4.5	4.5
Staff	5.0	5.0	5.0	5.0	5.0
```

---

## 📈 Aba: Radar Competências

### Dados para Gráfico (Cole em A1)

**Versão Simples (3 linhas):**

```
Dimensão	Atual	Nível Atual	Próximo Nível
Results	=Consolidação!G8	3.0	4.0
Direction	=Consolidação!G9	3.0	4.0
Talent	=Consolidação!G10	3.0	4.0
Culture	=Consolidação!G11	3.0	4.0
Craft	=Consolidação!G12	3.0	4.0
```

**Nota:** Substitua 3.0 e 4.0 pelo nível da pessoa. Para SE II = baseline 3.0, próximo nível 4.0.

---

**Versão Avançada (com VLOOKUP automático):**

Primeiro, crie aba auxiliar chamada "Config" com:

```
SE I	2.0
SE II	3.0
SE III	4.0
Lead	4.5
Staff	5.0
```

Depois use:

```
Dimensão	Atual	Nível Atual	Próximo Nível	2 Níveis
Results	=Consolidação!G8	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+1	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+2
Direction	=Consolidação!G9	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+1	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+2
Talent	=Consolidação!G10	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+1	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+2
Culture	=Consolidação!G11	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+1	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+2
Craft	=Consolidação!G12	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+1	=VLOOKUP(Consolidação!B2,Config!A:B,2,0)+2
```

---

## 🌈 Aba: Radar Valores

### Dados para Gráfico (Cole em A1)

```
Valor	Auto	Pares (Média)	Gestor	Expectativa
Obsessão Cliente	=Consolidação!B16	=AVERAGE(Consolidação!C16:E16)	=Consolidação!F16	3.0
Paixão Inovar	=Consolidação!B17	=AVERAGE(Consolidação!C17:E17)	=Consolidação!F17	3.0
Agilidade Resultado	=Consolidação!B18	=AVERAGE(Consolidação!C18:E18)	=Consolidação!F18	3.0
Fazer Mais Menos	=Consolidação!B19	=AVERAGE(Consolidação!C19:E19)	=Consolidação!F19	3.0
Juntos!	=Consolidação!B20	=AVERAGE(Consolidação!C20:E20)	=Consolidação!F20	3.0
```

---

## 🎯 Aba: Análise de Gaps

### Gaps vs. Nível Atual (Cole em A1)

```
Dimensão	Atual	Expectativa	Gap	Status
Results	=Consolidação!G8	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,2,0)	=B2-C2	=IF(D2<0,"🔴 ABAIXO",IF(D2>0.5,"🟢 SUPERA","🟡 ATENDE"))
Direction	=Consolidação!G9	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,3,0)	=B3-C3	=IF(D3<0,"🔴 ABAIXO",IF(D3>0.5,"🟢 SUPERA","🟡 ATENDE"))
Talent	=Consolidação!G10	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,4,0)	=B4-C4	=IF(D4<0,"🔴 ABAIXO",IF(D4>0.5,"🟢 SUPERA","🟡 ATENDE"))
Culture	=Consolidação!G11	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,5,0)	=B5-C5	=IF(D5<0,"🔴 ABAIXO",IF(D5>0.5,"🟢 SUPERA","🟡 ATENDE"))
Craft	=Consolidação!G12	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,6,0)	=B6-C6	=IF(D6<0,"🔴 ABAIXO",IF(D6>0.5,"🟢 SUPERA","🟡 ATENDE"))
```

---

### Gaps vs. Próximo Nível (Cole em A9)

```
Dimensão	Atual	Próximo Nível	Gap	Prioridade	Ranking
Results	=B2	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,2,0)+1	=B10-C10	=IF(D10<-0.5,"🔴 PRIORIDADE 1",IF(D10<0,"🟡 PRIORIDADE 2","🟢 PRONTO"))	=RANK(D10,$D$10:$D$14,1)
Direction	=B3	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,3,0)+1	=B11-C11	=IF(D11<-0.5,"🔴 PRIORIDADE 1",IF(D11<0,"🟡 PRIORIDADE 2","🟢 PRONTO"))	=RANK(D11,$D$10:$D$14,1)
Talent	=B4	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,4,0)+1	=B12-C12	=IF(D12<-0.5,"🔴 PRIORIDADE 1",IF(D12<0,"🟡 PRIORIDADE 2","🟢 PRONTO"))	=RANK(D12,$D$10:$D$14,1)
Culture	=B5	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,5,0)+1	=B13-C13	=IF(D13<-0.5,"🔴 PRIORIDADE 1",IF(D13<0,"🟡 PRIORIDADE 2","🟢 PRONTO"))	=RANK(D13,$D$10:$D$14,1)
Craft	=B6	=VLOOKUP(Consolidação!B2,Consolidação!A25:F30,6,0)+1	=B14-C14	=IF(D14<-0.5,"🔴 PRIORIDADE 1",IF(D14<0,"🟡 PRIORIDADE 2","🟢 PRONTO"))	=RANK(D14,$D$10:$D$14,1)
```

---

### Discrepâncias 360º (Cole em A17)

```
Dimensão	Auto	Pares (Média)	Gestor	Discrepância Auto-Outros	Alinhamento
Results	=Consolidação!B8	=AVERAGE(Consolidação!C8:E8)	=Consolidação!F8	=ABS(B18-AVERAGE(C18:D18))	=IF(E18>1,"⚠️ ATENÇÃO","✅ ALINHADO")
Direction	=Consolidação!B9	=AVERAGE(Consolidação!C9:E9)	=Consolidação!F9	=ABS(B19-AVERAGE(C19:D19))	=IF(E19>1,"⚠️ ATENÇÃO","✅ ALINHADO")
Talent	=Consolidação!B10	=AVERAGE(Consolidação!C10:E10)	=Consolidação!F10	=ABS(B20-AVERAGE(C20:D20))	=IF(E20>1,"⚠️ ATENÇÃO","✅ ALINHADO")
Culture	=Consolidação!B11	=AVERAGE(Consolidação!C11:E11)	=Consolidação!F11	=ABS(B21-AVERAGE(C21:D21))	=IF(E21>1,"⚠️ ATENÇÃO","✅ ALINHADO")
Craft	=Consolidação!B12	=AVERAGE(Consolidação!C12:E12)	=Consolidação!F12	=ABS(B22-AVERAGE(C22:D22))	=IF(E22>1,"⚠️ ATENÇÃO","✅ ALINHADO")
```

---

## 🎨 Formatação Condicional

### Para Coluna "Status" (Aba Gaps):

1. Selecionar coluna E (Status)
2. Formatar → Formatação condicional
3. Regra 1: **Se o texto contém "🔴"** → Fundo vermelho claro
4. Regra 2: **Se o texto contém "🟡"** → Fundo amarelo claro
5. Regra 3: **Se o texto contém "🟢"** → Fundo verde claro

---

### Para Coluna "Gap":

1. Selecionar coluna D (Gap)
2. Formatação condicional → Escala de cores
3. Mínimo (vermelho): -2
4. Ponto médio (amarelo): 0
5. Máximo (verde): +2

---

## 📊 Como Criar Gráfico Radar

### Google Sheets:

1. Selecionar dados preparados (ex: A1:E6)
2. Inserir → Gráfico
3. **Tipo de gráfico:** 
   - Se houver "Radar": Selecionar
   - Se não: Usar "Gráfico de Dispersão" ou "Linha"
4. Personalizar:
   - Editor de gráfico → Personalizar
   - Série 1 (Atual): Cor azul, linha grossa (3px)
   - Série 2 (Baseline): Cor vermelha, linha média (2px)
   - Série 3 (Meta): Cor amarela, linha média (2px)
   - Série 4 (Aspiracional): Cor verde, linha tracejada

---

## 🔧 Troubleshooting de Fórmulas

### Erro: #REF!
**Causa:** Referência de célula errada  
**Solução:** Verificar nome das abas e colunas

### Erro: #VALUE!
**Causa:** Tipo de dado errado (texto ao invés de número)  
**Solução:** Verificar se forms estão configurados para "Escala linear 0-5"

### Erro: #N/A (em VLOOKUP)
**Causa:** Valor não encontrado na tabela de lookup  
**Solução:** Verificar se nível da pessoa está escrito exatamente igual

### Fórmula não calcula
**Causa:** Ainda não há dados nos forms  
**Solução:** Normal! Aguardar respostas ou usar IFERROR

---

## 💡 Dicas Pro

### 1. Usar IFERROR

Envolva todas as fórmulas em IFERROR para evitar erros antes de coletar dados:

```
=IFERROR(AVERAGE(B8:F8), "Aguardando dados")
```

### 2. Validação de Dados

Na aba Consolidação, célula B2 (Nível):
- Validação de dados → Lista de itens
- SE I, SE II, SE III, Lead, Staff

### 3. Proteção de Abas

Proteger abas com fórmulas:
- Clicar com direito na aba → Proteger planilha
- Permitir edição apenas para você

### 4. Nomes de Intervalos

Para facilitar fórmulas, criar nomes:
- Selecionar A25:F30 → Dados → Intervalos nomeados → "ExpectativasNivel"
- Usar em fórmula: =VLOOKUP(B2, ExpectativasNivel, 2, 0)

---

## ✅ Checklist de Fórmulas

Depois de colar todas as fórmulas:

- [ ] Aba Consolidação: Seção Informações
- [ ] Aba Consolidação: Seção Dimensões
- [ ] Aba Consolidação: Seção Valores
- [ ] Aba Consolidação: Seção Expectativas
- [ ] Aba Radar Competências: Dados preparados
- [ ] Aba Radar Valores: Dados preparados
- [ ] Aba Gaps: Gaps vs. Nível Atual
- [ ] Aba Gaps: Gaps vs. Próximo Nível
- [ ] Aba Gaps: Discrepâncias 360º
- [ ] Gráfico Radar 1 criado
- [ ] Gráfico Radar 2 criado
- [ ] Formatação condicional aplicada
- [ ] Teste com dados fictícios ✅

---

**Próximo:** Criar os Google Forms! 📝

