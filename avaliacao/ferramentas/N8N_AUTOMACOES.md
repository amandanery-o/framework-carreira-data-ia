# 🤖 Automatizações com n8n - Sistema 360º

> Como usar n8n para automatizar ainda mais o sistema de avaliação

---

## 🎯 TL;DR - Vale a Pena?

**Resposta curta:** SIM, mas **não no início**! 

### Estratégia Recomendada:

```
Fase 1 (Semana 1): Google Forms + Sheets ✅
                   └─> Sistema básico funcionando

Fase 2 (Mês 2-3): Adicionar n8n 🤖
                   └─> Automatizações que economizam tempo
```

**Por quê?** Validar o sistema primeiro, depois otimizar.

---

## 💡 Onde n8n Agrega MUITO Valor

### 🔥 Top 5 Automatizações Úteis:

1. **Envio Automático de Emails** ⭐⭐⭐
2. **Lembretes Automáticos** ⭐⭐⭐
3. **Notificações no Slack** ⭐⭐
4. **Agendamento de 1:1s** ⭐⭐
5. **Geração de PDFs** ⭐

---

## 🚀 Automatização 1: Envio Automático de Emails

### O Que Faz:
Quando você inicia uma avaliação 360º, n8n envia automaticamente:
- Email para a pessoa (auto-avaliação)
- Emails para 3 pares (avaliação de par)
- Email para você (lembrete de avaliar como gestor)

### Workflow n8n:

```
Trigger: Webhook ou Google Sheets (nova linha)
   ↓
Buscar Dados: Nome, Email, Pares
   ↓
Send Email 1: Para pessoa (link Form Auto)
   ↓
Send Email 2: Para Par 1 (link Form Par)
   ↓
Send Email 3: Para Par 2 (link Form Par)
   ↓
Send Email 4: Para Par 3 (link Form Par)
   ↓
Send Email 5: Para Gestor (link Form Gestor)
```

### Nós n8n:

1. **Webhook** (ou Google Sheets Trigger)
2. **HTTP Request** (ou Item Lists)
3. **Gmail** (ou SMTP) - 5x (1 por email)

### Template de Email:

**Subject:** [360º] Sua Avaliação de {Nome da Pessoa}

**Body:**
```
Olá {Nome do Avaliador},

Você foi convidado(a) para participar da avaliação 360º de {Nome da Pessoa}.

Por favor, preencha o formulário abaixo até {Data Limite}:

🔗 Link: {Link do Form}

Tempo estimado: {15-45} minutos

A avaliação é {confidencial/anônima} e será usada para desenvolvimento.

Obrigado!
{Seu Nome}
```

### Benefício:
- ⚡ Economiza ~10 minutos por avaliação
- ✅ Padroniza comunicação
- 📧 Menos chance de esquecer alguém

---

## ⏰ Automatização 2: Lembretes Automáticos

### O Que Faz:
Envia lembretes para quem não completou a avaliação.

### Workflow n8n:

```
Trigger: Cron (diário às 9h)
   ↓
Buscar: Google Sheets - Lista de avaliações ativas
   ↓
Checar: Quem NÃO respondeu ainda
   ↓
Filtrar: Enviar lembrete apenas se >3 dias
   ↓
Send Email: Lembrete gentil
```

### Lógica:

- **Dia 0:** Email inicial
- **Dia 3:** Primeiro lembrete (se não respondeu)
- **Dia 7:** Segundo lembrete
- **Dia 10:** Lembrete final + notificar gestor

### Template de Lembrete:

**Subject:** 🔔 Lembrete: Avaliação 360º de {Nome}

**Body:**
```
Olá {Nome},

Só um lembrete gentil sobre a avaliação 360º de {Nome da Pessoa}.

Ainda não recebemos sua resposta. Se possível, preencha até {Data}:

🔗 Link: {Link do Form}

Se já preencheu, ignore este email!

Obrigado!
```

### Benefício:
- ⚡ Aumenta taxa de resposta de 60% → 90%
- ⏱️ Economiza ~20 min/semana de follow-ups manuais

---

## 💬 Automatização 3: Notificações no Slack

### O Que Faz:
Notifica no Slack quando:
- Todas avaliações foram completadas ✅
- Radares estão prontos 📊
- Deadline está próximo ⏰

### Workflow n8n:

```
Trigger: Google Sheets - Quando nova resposta
   ↓
Contar: Quantas respostas completadas
   ↓
IF: Todas 5 respostas completas?
   ↓ SIM
Send Slack: "🎉 Radares de {Nome} prontos!"
```

### Mensagem Slack:

```
🎉 Avaliação 360º Completa!

Pessoa: {Nome da Pessoa}
Respostas: 5/5 ✅
Status: Radares prontos para visualização

📊 Ver planilha: {Link}
📅 Agendar 1:1: {Sugestão de horário}
```

### Benefício:
- 📱 Notificação imediata
- 🚀 Agiliza processo
- 👀 Visibilidade para time

---

## 📅 Automatização 4: Agendamento Automático de 1:1

### O Que Faz:
Quando radares ficam prontos, n8n:
1. Busca slots livres no Google Calendar (seu e da pessoa)
2. Cria evento de 1:1
3. Envia email/Slack com confirmação

### Workflow n8n:

```
Trigger: Slack ou Sheets (avaliação completa)
   ↓
Google Calendar: Buscar disponibilidade
   ↓
Filtrar: Próximos 7 dias, 1h de duração
   ↓
Create Event: "1:1 - Feedback 360º: {Nome}"
   ↓
Send Email: Confirmação com agenda
```

### Evento Criado:

**Título:** 🎯 1:1 Feedback 360º - {Nome}

**Descrição:**
```
Reunião de feedback baseada na avaliação 360º.

📊 Planilha com radares: {Link}
📝 Agenda:
  • Apresentar radares (20 min)
  • Discutir gaps e forças (15 min)
  • Co-criar PDI (20 min)
  • Próximos passos (5 min)

Preparação:
  • Revisar radares antes da reunião
  • Pensar em exemplos concretos
```

### Benefício:
- ⚡ Economiza ~5 min de agendamento
- 📅 Garante que feedback acontece rápido
- 📋 Agenda já estruturada

---

## 📄 Automatização 5: Geração de PDF

### O Que Faz:
Gera PDF dos radares automaticamente e envia por email.

### Workflow n8n:

```
Trigger: Sheets - Avaliação completa
   ↓
HTTP Request: Google Sheets API (exportar como PDF)
   ↓
Google Drive: Salvar PDF
   ↓
Gmail: Enviar PDF anexo
```

### Email com PDF:

**Subject:** 📊 Seus Radares 360º - {Período}

**Body:**
```
Olá {Nome},

Segue anexo o resultado da sua avaliação 360º.

📎 PDF inclui:
  • Radar de Competências
  • Radar de Valores Gupy
  • Análise de Gaps
  • PDI Sugerido

Vamos discutir na nossa próxima 1:1 em {Data}.

Abraço!
```

### Benefício:
- 📄 Pessoa tem registro para consultar
- 💾 Histórico automático
- 📧 Facilita compartilhamento

---

## 🛠️ Automatização BÔNUS: Dashboard Consolidado

### O Que Faz:
Consolida dados de múltiplas pessoas em uma planilha "master".

### Workflow n8n:

```
Trigger: Cron (semanal)
   ↓
Loop: Para cada pessoa avaliada
   ↓
Buscar: Médias das 5 dimensões
   ↓
Append: Planilha "Dashboard Time"
   ↓
Calcular: Médias do time, gaps comuns
```

### Dashboard Gerado:

| Nome | Results | Direction | Talent | Culture | Craft | Média | Status |
|------|---------|-----------|--------|---------|-------|-------|--------|
| João | 3.8 | 3.5 | 3.2 | 3.0 | 4.0 | 3.50 | 🟡 |
| Maria | 4.2 | 3.6 | 3.4 | 3.0 | 4.0 | 3.64 | 🟢 |
| Pedro | 3.0 | 2.8 | 3.0 | 2.9 | 3.2 | 2.98 | 🔴 |

**Insights Automáticos:**
- Gap comum do time: Culture (média 3.0)
- Forças do time: Craft (média 3.7)
- Pronto para promoção: Maria (3.64)

### Benefício:
- 📊 Visão de time em tempo real
- 🎯 Identificar gaps organizacionais
- 📈 Tracking de evolução do time

---

## 🚦 Quando Usar n8n? (Roadmap Recomendado)

### ❌ NÃO USE n8n na Fase 1 (Mês 1):

**Por quê?**
- Sistema ainda não validado
- Adiciona complexidade desnecessária
- Você ainda está aprendendo o fluxo

**Faça:** Rodar 2-3 avaliações manualmente primeiro

---

### ✅ USE n8n na Fase 2 (Mês 2-3):

**Quando:**
- Você já fez 3+ avaliações
- Processo está funcionando
- Você sente as "dores" (follow-ups, lembretes, etc.)

**Comece com:**
1. Automação 1: Envio de emails (a mais útil!)
2. Automação 2: Lembretes (economiza muito tempo)
3. Depois adicione outras conforme necessidade

---

### 🚀 USE n8n Avançado na Fase 3 (Mês 6+):

**Quando:**
- Sistema rodando para todo o time (10+ pessoas)
- Quer escalar para outros times
- Quer dashboard consolidado

**Adicione:**
- Automatização 3: Slack
- Automatização 4: Agendamento
- Automatização 5: PDF
- Automatização BÔNUS: Dashboard

---

## 📐 Workflows n8n Prontos

### Workflow 1: Envio Inicial de Emails

**Nós:**
```json
1. Webhook (POST)
   Body: {
     "pessoa_nome": "João Silva",
     "pessoa_email": "joao@empresa.com",
     "par1_email": "maria@empresa.com",
     "par2_email": "pedro@empresa.com",
     "par3_email": "ana@empresa.com",
     "gestor_email": "voce@empresa.com",
     "form_auto_link": "https://forms.google.com/...",
     "form_par_link": "https://forms.google.com/...",
     "form_gestor_link": "https://forms.google.com/..."
   }

2. Set (Preparar dados)
   
3. Gmail - Enviar para pessoa
   To: {{ $json.pessoa_email }}
   Subject: Sua Auto-Avaliação 360º
   Body: [Template acima]

4. Gmail - Enviar para Par 1
   To: {{ $json.par1_email }}
   Subject: Avaliação 360º de {{ $json.pessoa_nome }}
   
[... repetir para Par 2, Par 3, Gestor]
```

---

### Workflow 2: Lembretes Automáticos

**Nós:**
```json
1. Schedule Trigger (Diário às 9h)

2. Google Sheets - Read
   Spreadsheet: "Tracking 360º"
   Sheet: "Avaliações Ativas"

3. Filter (Não respondeu + >3 dias)
   {{ $json.status }} == "pendente" &&
   {{ $json.dias_desde_envio }} >= 3

4. Loop através de cada item

5. Gmail - Enviar lembrete
   To: {{ $json.email }}
   Subject: Lembrete: Avaliação 360º
```

---

### Workflow 3: Notificação Slack (Completo)

**Nós:**
```json
1. Google Sheets Trigger (Nova resposta)

2. Google Sheets - Count
   Contar respostas da pessoa X

3. IF (5 respostas completas?)
   {{ $json.count }} == 5

4. Slack - Send Message
   Channel: #team-feedback
   Message: 🎉 Radares de {{ $json.nome }} prontos!
```

---

## 💰 Custo-Benefício

### Tempo Investido vs. Tempo Economizado:

| Automatização | Setup n8n | Economia por Ciclo | ROI após |
|---------------|-----------|-------------------|----------|
| **Envio de emails** | 1h | 10 min | 6 avaliações |
| **Lembretes** | 1.5h | 20 min/semana | 4 semanas |
| **Slack** | 30 min | 5 min | 6 avaliações |
| **Agendamento** | 1h | 5 min | 12 avaliações |
| **PDF** | 1h | 3 min | 20 avaliações |

**Total setup:** ~5 horas  
**Economia anual** (10 pessoas, 2 ciclos): **~40 horas** 🎉

---

## 🎯 Minha Recomendação Específica para Você

### Fase 1 (Agora - Semana 1): ✅ SEM n8n

```
✅ Implementar Google Forms + Sheets
✅ Fazer 2-3 avaliações manualmente
✅ Validar processo
✅ Ajustar conforme feedback
```

**Por quê?** Você ainda não sabe exatamente como vai usar. Validar primeiro!

---

### Fase 2 (Mês 2): 🤖 Adicionar n8n

**Começar com apenas 1 automatização:**

**Opção A (Recomendada):** Envio de Emails
- Maior impacto
- Uso mais frequente
- Economiza 10 min/avaliação

**Opção B:** Lembretes
- Se tiver problema com baixa taxa de resposta
- Economiza follow-ups manuais

**Como:**
1. Criar workflow simples
2. Testar com 1 pessoa
3. Ajustar
4. Usar em todas próximas avaliações

---

### Fase 3 (Mês 4-6): 🚀 Expandir

Adicionar outras automatizações conforme necessidade:
- Slack (se time usa muito)
- Agendamento (se fizer muitas avaliações)
- Dashboard (se avaliar 10+ pessoas)

---

## 🛠️ Como Começar com n8n (Quando Chegar a Fase 2)

### Passo 1: Criar Workflow de Envio de Emails

1. Abrir n8n
2. Novo workflow: "360º - Envio de Emails"
3. Adicionar nós:
   - Webhook (trigger)
   - Gmail (5x para 5 emails)
4. Testar manualmente
5. Salvar e ativar

### Passo 2: Criar Interface para Trigger

**Opção A:** Usar Postman/Insomnia para chamar webhook

**Opção B:** Criar form simples que chama webhook:
```html
<form action="https://seu-n8n.com/webhook/360" method="POST">
  <input name="pessoa_nome" placeholder="Nome">
  <input name="pessoa_email" placeholder="Email">
  <!-- etc -->
  <button>Iniciar Avaliação 360º</button>
</form>
```

**Opção C:** Botão no Google Sheets (Apps Script)
```javascript
function iniciarAvaliacao360() {
  var data = {
    pessoa_nome: "João Silva",
    // ... outros campos
  };
  
  UrlFetchApp.fetch("https://seu-n8n.com/webhook/360", {
    method: "POST",
    contentType: "application/json",
    payload: JSON.stringify(data)
  });
}
```

---

## ⚠️ Cuidados ao Usar n8n

### 1. Não Sobre-Automatizar
- ❌ Automatizar tudo de uma vez
- ✅ Começar com 1 workflow, adicionar outros depois

### 2. Manter Simplicidade
- ❌ Workflows complexos com 20+ nós
- ✅ Workflows simples e diretos

### 3. Testar Bem
- ❌ Ativar workflow sem testar
- ✅ Testar múltiplas vezes antes de usar

### 4. Documentar
- ❌ Workflows sem descrição
- ✅ Adicionar notas explicando cada nó

### 5. Monitorar
- ❌ "Set and forget"
- ✅ Verificar execuções regularmente

---

## 🎓 Recursos para n8n

### Documentação:
- [n8n Docs](https://docs.n8n.io/)
- [n8n Gmail Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/)
- [n8n Google Sheets](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/)
- [n8n Slack](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/)

### Templates:
- n8n Community Workflows
- (Posso criar templates específicos se precisar!)

---

## ✅ Checklist de Decisão

**Use n8n SE:**
- [ ] Você já validou o processo (3+ avaliações)
- [ ] Você sente "dores" (follow-ups, lembretes, etc.)
- [ ] Você já conhece n8n (curva de aprendizado menor)
- [ ] Vai avaliar 5+ pessoas regularmente
- [ ] Quer escalar o processo

**NÃO use n8n SE:**
- [ ] Primeira vez usando o sistema
- [ ] Vai avaliar só 1-2 pessoas
- [ ] Processo ainda está mudando muito
- [ ] Não conhece n8n (aprenda o básico primeiro)

---

## 🎯 Resumo Final

### n8n Vale a Pena? **SIM!** 🎉

**Mas não agora. Depois de validar o sistema.**

### Estratégia:

```
Semana 1-4:   Google Forms + Sheets (manual)
               └─> Validar processo ✅

Mês 2-3:      Adicionar n8n (1 workflow)
               └─> Automatizar envio de emails 🤖

Mês 4+:       Expandir n8n (mais workflows)
               └─> Lembretes, Slack, etc. 🚀
```

### Benefícios quando adicionar n8n:
- ⚡ Economiza ~40h/ano
- 📧 Comunicação padronizada
- 📈 Maior taxa de resposta
- 🎯 Processo mais profissional

**Vale 100% a pena, mas no momento certo!** ✨

---

## 🚀 Próximo Passo

**Hoje:** Implementar Google Forms + Sheets (sem n8n)

**Daqui 1 mês:** Revisar este documento e decidir qual automatização adicionar primeiro

**Daqui 3 meses:** Ter sistema totalmente automatizado com n8n

---

**Me chame quando chegar na Fase 2 e eu te ajudo a criar os workflows n8n específicos! 😊**

