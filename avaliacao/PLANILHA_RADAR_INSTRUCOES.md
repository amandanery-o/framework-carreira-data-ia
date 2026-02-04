> Como criar e usar a planilha que gera os radares visuais automaticamente

---

## 📊 Visão Geral

Esta planilha consolida todas as avaliações (auto + pares + gestor) e gera automaticamente:
1. **Radar de Competências** (5 dimensões)
2. **Radar de Valores Gupy** (5 valores)
3. **Análise de Gaps** e priorização de PDI
4. **Comparação 360º** (auto vs. pares vs. gestor)

**Ferramenta:** Google Sheets (recomendado) ou Excel

---

## 🏗️ Estrutura da Planilha

### Abas (Sheets):

1. **📋 Dados** - Input de todas as avaliações
2. **📊 Radar Competências** - Gráfico spider chart das 5 dimensões
3. **🌈 Radar Valores** - Gráfico spider chart dos 5 valores
4. **🎯 Análise de Gaps** - Cálculo automático de gaps e priorização
5. **📈 Comparação 360º** - Comparação visual entre avaliadores
6. **📝 PDI Gerado** - Plano de desenvolvimento baseado nos gaps
7. **⚙️ Configurações** - Expectativas por nível

---

## 🔧 ABA 1: Dados (Input)

### Estrutura da Aba:

| Coluna A | Coluna B | Coluna C | Coluna D | Coluna E | Coluna F |
|----------|----------|----------|----------|----------|----------|
| **Dimensão** | **Auto-Avaliação** | **Par 1** | **Par 2** | **Par 3** | **Gestor** |
| Results | | | | | |
| Direction | | | | | |
| Talent | | | | | |
| Culture | | | | | |
| Craft | | | | | |
| **MÉDIA** | **=AVERAGE(B2:B6)** | | | | |

### Seção 2: Valores Gupy

| Coluna A | Coluna B | Coluna C | Coluna D | Coluna E | Coluna F |
|----------|----------|----------|----------|----------|----------|
| **Valor** | **Auto** | **Par 1** | **Par 2** | **Par 3** | **Gestor** |
| Obsessão Cliente | | | | | |
| Paixão Inovar | | | | | |
| Agilidade Resultado | | | | | |
| Fazer Mais Menos | | | | | |
| Juntos! | | | | | |

### Seção 3: Informações

| Campo | Valor |
|-------|-------|
| **Nome** | [Nome da pessoa] |
| **Nível Atual** | [SE I / SE II / SE III / Lead / Staff] |
| **Trilha** | [Data Eng / Analytics Eng / Cientista Dados] |
| **Período** | [MM/AAAA - MM/AAAA] |
| **Data Avaliação** | [DD/MM/AAAA] |

---

## 📊 ABA 2: Radar Competências

### Dados para o Gráfico:

Criar tabela de dados consolidados:

| Dimensão | Atual (Média) | Nível Atual (Baseline) | Próximo Nível | 2 Níveis Acima |
|----------|---------------|------------------------|---------------|----------------|
| Results | =AVERAGE(Dados!B2,Dados!C2,Dados!D2,Dados!E2,Dados!F2) | =VLOOKUP(Dados!$B$10, Configurações!$A$2:$F$10, 2, FALSE) | [+1 nível] | [+2 níveis] |
| Direction | =AVERAGE(Dados!B3:F3) | [lookup] | [lookup] | [lookup] |
| Talent | =AVERAGE(Dados!B4:F4) | [lookup] | [lookup] | [lookup] |
| Culture | =AVERAGE(Dados!B5:F5) | [lookup] | [lookup] | [lookup] |
| Craft | =AVERAGE(Dados!B6:F6) | [lookup] | [lookup] | [lookup] |

### Como Criar o Gráfico Spider:

**Google Sheets:**
1. Selecionar toda a tabela acima
2. Inserir → Gráfico
3. Tipo de gráfico → Radar (Spider Chart)
4. Personalizar:
   - Série 1 (Atual): Linha azul, espessura 3
   - Série 2 (Nível Atual): Linha vermelha, espessura 2
   - Série 3 (Próximo Nível): Linha amarela, espessura 2
   - Série 4 (2 Níveis): Linha verde tracejada

**Excel:**
1. Selecionar toda a tabela
2. Inserir → Gráficos Recomendados → Radar
3. Formatar séries com cores diferentes

---

## 🌈 ABA 3: Radar Valores

### Dados para o Gráfico:

| Valor | Auto | Pares (Média) | Gestor | Expectativa |
|-------|------|---------------|--------|-------------|
| Obsessão Cliente | =Dados!B8 | =AVERAGE(Dados!C8:E8) | =Dados!F8 | 3.0 |
| Paixão Inovar | =Dados!B9 | =AVERAGE(Dados!C9:E9) | =Dados!F9 | 3.0 |
| Agilidade Resultado | =Dados!B10 | =AVERAGE(Dados!C10:E10) | =Dados!F10 | 3.0 |
| Fazer Mais Menos | =Dados!B11 | =AVERAGE(Dados!C11:E11) | =Dados!F11 | 3.0 |
| Juntos! | =Dados!B12 | =AVERAGE(Dados!C12:E12) | =Dados!F12 | 3.0 |

### Gráfico:
- Mesmo processo do Radar Competências
- 4 séries: Auto (azul), Pares (roxo), Gestor (laranja), Expectativa (vermelho)

---

## 🎯 ABA 4: Análise de Gaps

### Cálculo Automático de Gaps:

| Dimensão | Atual | Expectativa Nível | Gap | Próximo Nível | Gap Promoção | Prioridade |
|----------|-------|-------------------|-----|---------------|--------------|------------|
| Results | [ref] | [ref] | =C2-B2 | [ref] | =E2-B2 | =IF(D2<0,"🔴 CRÍTICO",IF(F2>1,"🟢 PRONTO","🟡 DESENVOLVER")) |
| Direction | | | | | | |
| Talent | | | | | | |
| Culture | | | | | | |
| Craft | | | | | | |

### Interpretação Automática:

| Status | Gap | Significado | Ação |
|--------|-----|-------------|------|
| 🔴 **CRÍTICO** | <0 (abaixo expectativa) | Abaixo do esperado para o nível | PDI urgente |
| 🟡 **DESENVOLVER** | 0 a 1 | No nível, mas longe de promoção | PDI focado |
| 🟢 **PRONTO** | >1 | Supera nível atual | Evidenciar para promoção |

### Priorização Automática:

**Fórmula para ordenar:**
```excel
=SORT(A2:G6, 4, TRUE)  // Ordena por Gap (maior gap = maior prioridade)
```

---

## 📈 ABA 5: Comparação 360º

### Tabela de Discrepâncias:

| Dimensão | Auto | Média Pares | Gestor | Discrepância Auto-Outros | Interpretação |
|----------|------|-------------|--------|--------------------------|---------------|
| Results | [ref] | [média] | [ref] | =ABS(B2-AVERAGE(C2:D2)) | =IF(E2>1,"⚠️ ATENÇÃO","✅ ALINHADO") |

### Gráfico de Barras Comparativo:

- Eixo X: Dimensões
- Barras agrupadas: Auto, Pares, Gestor
- Facilita visualizar onde há desalinhamento

---

## 📝 ABA 6: PDI Gerado

### Template Auto-Populado:

```
# Plano de Desenvolvimento Individual - [Nome]
Período: [Data] a [Data + 6 meses]

## Prioridade 1: [Dimensão com maior gap]
**Gap atual:** [X pontos abaixo da expectativa]
**Meta:** Subir de [atual] para [meta] em 6 meses

### Ações:
1. [Ação sugerida baseada na dimensão]
2. [Ação sugerida baseada na dimensão]
3. [Ação sugerida baseada na dimensão]

### Indicadores de Progresso:
- [ ] [Milestone 1 - Mês 2]
- [ ] [Milestone 2 - Mês 4]
- [ ] [Milestone 3 - Mês 6]

## Prioridade 2: [Segunda dimensão]
...
```

**Sugestões de ações automáticas** baseadas em dimensão/gap:

| Dimensão | Gap | Sugestões Automáticas |
|----------|-----|----------------------|
| **Results** | Baixo | • Liderar 1 projeto de ponta a ponta<br>• Documentar impacto em métricas<br>• Apresentar resultados em demo |
| **Direction** | Baixo | • Propor 2 melhorias de arquitetura<br>• Participar de planning strategy<br>• Criar RFC para iniciativa significativa |
| **Talent** | Baixo | • Mentorar formalmente 1 pessoa<br>• Apresentar 1 tech talk<br>• Fazer 10+ code reviews educativas/semana |
| **Culture** | Baixo | • Aumentar comunicação proativa<br>• Documentar decisões (ADRs)<br>• Participar de initiative cross-funcional |
| **Craft** | Baixo | • Estudar [tech específica da trilha]<br>• Certificação relevante<br>• Contribuir para projeto técnico desafiador |

---

## ⚙️ ABA 7: Configurações

### Expectativas por Nível:

| Nível | Results | Direction | Talent | Culture | Craft | Descrição |
|-------|---------|-----------|--------|---------|-------|-----------|
| **SE I** | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | Junior: Em desenvolvimento |
| **SE II** | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | Pleno: Autônomo |
| **SE III** | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | Senior: Referência |
| **Lead** | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 | Lead: Liderança técnica |
| **Staff** | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | Staff: Excelência |

**Nota:** Estes são valores de referência. Ajuste conforme necessário.

---

## 🚀 Como Usar a Planilha

### 1. Preparação (5 min)
- Fazer cópia do template
- Preencher informações da pessoa (Aba Dados)

### 2. Coletar Avaliações (1-2 semanas)
- Enviar templates para: pessoa, 2-3 pares, gestor
- Receber de volta preenchidos

### 3. Consolidar Dados (10 min)
- Copiar notas dos templates para Aba Dados
- Fórmulas calculam automaticamente

### 4. Gerar Radares (5 min)
- Radares são gerados automaticamente
- Ajustar formatação se necessário

### 5. Analisar (15 min)
- Revisar Aba "Análise de Gaps"
- Revisar "Comparação 360º"
- Preparar exemplos concretos

### 6. Preparar PDI (15 min)
- Revisar sugestões automáticas na Aba PDI
- Customizar para contexto da pessoa
- Preparar discussão para 1:1

### 7. Reunião de Feedback (45-60 min)
- Mostrar radares visuais
- Discutir gaps e forças
- Co-criar PDI final

---

## 💡 Dicas Pro

### 1. Cor-Codifique os Radares
- 🔴 Vermelho: Abaixo da expectativa
- 🟡 Amarelo: No nível
- 🟢 Verde: Pronto para próximo nível

### 2. Exporte como PDF
Para compartilhar com a pessoa:
- Arquivo → Baixar → PDF
- Incluir: Radar + Gaps + PDI

### 3. Versionamento
Salve versões a cada ciclo:
- `Radar_[Nome]_2024-Q1.xlsx`
- `Radar_[Nome]_2024-Q3.xlsx`
- Compare evolução ao longo do tempo

### 4. Gráfico de Linha de Tendência
Crie um gráfico extra mostrando evolução:
- Eixo X: Quarters (Q1, Q2, Q3, Q4)
- Eixo Y: Média das 5 dimensões
- Visualiza progresso ao longo do ano

### 5. Compartilhamento
- Google Sheets: Compartilhar com permissão de visualização
- Excel: Proteger abas de cálculo, deixar apenas Dados editável

---

## 📥 Template Pronto

### Download do Template:

**Opção A - Google Sheets (Recomendado):**
1. Acesse: [Link do template no Google Drive]
2. Arquivo → Fazer uma cópia
3. Renomear: `Radar_[Nome]_[Período]`

**Opção B - Excel:**
1. Download: `planilha_radar_template.xlsx`
2. Salvar como: `Radar_[Nome]_[Período].xlsx`

**Opção C - Criar do Zero:**
Siga as instruções deste documento para criar sua própria planilha.

---

## 🔧 Troubleshooting

### Problema: Gráfico não aparece
**Solução:** Verifique se dados estão no formato correto (números, não texto)

### Problema: Fórmulas não calculam
**Solução:** Verifique referências de células, ajuste conforme sua estrutura

### Problema: Discrepância 360º muito alta (>2 pontos)
**Solução:** Normal! Discuta com a pessoa:
- "Por que você se avalia diferente?"
- "Pode ser falta de visibilidade do seu trabalho?"

### Problema: Todas as dimensões abaixo da expectativa
**Solução:** Pode indicar:
- Promoção prematura
- Necessidade de PDI intensivo
- Revisar se expectativas estão calibradas

---

## 📈 Evolução ao Longo do Tempo

### Acompanhamento Mensal:
Crie aba extra "Evolução Mensal":

| Mês | Results | Direction | Talent | Culture | Craft | Média |
|-----|---------|-----------|--------|---------|-------|-------|
| Jan | 3.2 | 3.0 | 2.8 | 3.1 | 3.5 | 3.12 |
| Fev | 3.3 | 3.1 | 3.0 | 3.2 | 3.6 | 3.24 |
| Mar | 3.5 | 3.3 | 3.2 | 3.4 | 3.7 | 3.42 |

**Gráfico de linha mostrando progresso** - Motivador!

---

## 🎯 Sucesso com a Planilha

Você saberá que está usando bem quando:

✅ **Feedback visual** torna conversas mais objetivas  
✅ **PDI focado** em 2-3 áreas prioritárias  
✅ **Comparação 360º** gera insights sobre visibilidade  
✅ **Evolução no tempo** motiva e mostra progresso  
✅ **Promoções baseadas** em dados do radar (4.0+ no próximo nível)

---

**Próximos arquivos:**
- `exemplo_radar_preenchido.xlsx` - Exemplo com dados reais
- `rubrica_craft_[trilha].md` - Avaliação detalhada de habilidades técnicas por trilha

**Dúvidas?** Consulte `GUIA_AVALIACAO_360.md`

