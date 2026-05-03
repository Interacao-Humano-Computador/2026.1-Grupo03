# Análise de Tarefas: Acompanhamento de Reclamação

## Introdução

A Análise de Tarefas é uma etapa fundamental na engenharia de requisitos de sistemas interativos. Segundo Barbosa e Silva (2021), seu objetivo é compreender **como os usuários realizam seu trabalho, quais atividades executam e por quê**, identificando as estruturas que organizam as tarefas, os recursos cognitivos necessários e as possíveis fontes de erro. Ela pode ser aplicada tanto para avaliar sistemas existentes quanto para orientar o design de novos sistemas, e deve ser fundamentada em dados reais coletados junto aos usuários — como os obtidos no Grupo de Foco realizado com a Persona Laura em 30/04/2026.

Neste documento são aplicadas duas técnicas de modelagem complementares:

- **Análise Hierárquica de Tarefas (HTA):** decompõe o objetivo principal do usuário em subobjetivos e operações elementares, organizados hierarquicamente, identificando problemas e recomendações em cada nível (Barbosa e Silva, 2021, p. 165–166).
- **Árvores de Tarefas Concorrentes (CTT):** classifica cada tarefa por tipo (Usuário, Sistema, Interativa ou Abstrata) e modela as relações de ordem, ativação e concorrência entre elas (Barbosa e Silva, 2021, p. 173–174).

A tarefa analisada é: **"Acessar o andamento da reclamação via notificação ativa e tomar uma decisão sobre a proposta da empresa"**, modelada com base na Persona Primária **Laura** e na funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas*.

---

## 1. Análise Hierárquica de Tarefas (HTA)

A **Análise Hierárquica de Tarefas** (*Hierarchical Task Analysis* — HTA) é uma técnica que examina tarefas complexas que requerem planejamento e resolução de problemas. Ela parte de um **objetivo de alto nível** e o decompõe recursivamente em **subobjetivos** e, por fim, em **operações** elementares — ações que não se subdividem mais. A cada nível, um **plano** descreve como os subobjetivos se relacionam (sequência, seleção ou concorrência). A técnica também documenta os **problemas** potenciais de cada operação e as **recomendações** de IHC para mitigá-los (BARBOSA; SILVA, 2021, p. 165–166).

<p align="center">
  <img src="../images/HTA-Heitor.png" alt="Diagrama HTA — Acompanhar reclamação e responder proposta" width="750">
  <br><em>Figura 1 — Diagrama HTA: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo com auxílio do Mermaid.js (2026).</em>
</p>

**Tabela de Representação HTA — Acompanhar reclamação e responder proposta:**

| Objetivos / Operações | Problemas e Recomendações | Plano |
| :--- | :--- | :--- |
| **0.** Acompanhar reclamação e responder à proposta da empresa | — | Plano 0: 1 >> 2 >> 3 (sequência obrigatória) |
| **1.** Acessar o portal via notificação ativa | — | Plano 1: 1.1 >> 1.2 (sequência) |
| **1.1** Receber e ler a notificação proativa (WhatsApp/SMS/e-mail) | **Problema:** notificação pode ser ignorada ou cair em spam. **Recomendação:** usar canal preferido pelo usuário (WhatsApp) e mensagem objetiva com o nome do usuário e número de protocolo. | — |
| **1.2** Tocar no link seguro da notificação para abrir o painel | **Problema:** link expirado ou com tempo de sessão muito curto. **Recomendação:** links com validade mínima de 7 dias e autenticação simplificada por token (sem necessidade de senha). | — |
| **2.** Interpretar o status e a proposta da empresa | — | Plano 2: 2.1 >> 2.2 (sequência) |
| **2.1** Visualizar a linha do tempo do processo | **Problema:** uso de jargões jurídicos (ex: "manifestação do fornecedor") pode confundir o usuário leigo. **Recomendação:** linguagem simples e direta em todas as etapas, com exemplos concretos de prazos (ex: "A empresa tem 5 dias para responder"). | — |
| **2.2** Ler o resumo da proposta em linguagem simples | **Problema:** proposta longa ou com termos técnicos pode levar ao abandono. **Recomendação:** o sistema deve gerar um resumo automático em até 3 linhas, destacando o valor e a condição da proposta. | — |
| **3.** Registrar decisão sobre a proposta | — | Plano 3: [3.1] ou [3.2] (seleção exclusiva) |
| **3.1** Aceitar a proposta da empresa | **Problema:** usuário pode aceitar sem entender as implicações (ex: não haverá reabertura do processo). **Recomendação:** exibir um aviso claro antes da confirmação: "Ao aceitar, o processo será encerrado." | — |
| **3.2** Recusar a proposta e continuar o processo | **Problema:** usuário pode não saber o que acontecerá após a recusa. **Recomendação:** após a recusa, o sistema deve informar o próximo passo ("O PROCON analisará o impasse e poderá convocar uma audiência"). | — |

*Tabela 1 — Representação textual do HTA: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo (2026).*

**Tabela de Representação HTA — Participar de audiência de conciliação virtual**

<p align="center">
  <img src="../images/HTA-Moretti.png" alt="Diagrama HTA — Acompanhar reclamação e responder proposta" width="750">
  <br><em>Figura 2 — Diagrama HTA: . Fonte: Participar de audiência de conciliação virtual. Elaborado por Pedro Augusto Moretti Moreira com auxílio do Mermaid.js (2026).</em>
</p>

| Objetivos / Operações | Problemas e Recomendações | Plano |
| :--- | :--- | :--- |
| **0.** Participar de audiência de conciliação virtual | — | Plano 0: 1 >> 2 >> 3 >> 4 (sequência obrigatória) |
| **1.** Preparar‑se para a audiência | — | Plano 1: 1.1 >> 1.2 (sequência) |
| **1.1** Receber e ler a notificação com o link da sala de conciliação | **Problema:** notificação pode ser ignorada ou cair em spam. **Recomendação:** enviar notificação por múltiplos canais (WhatsApp e e‑mail) com assunto claro, data/horário da audiência e identificação do processo. | — |
| **1.2** Separar documentos e evidências que pretende apresentar | **Problema:** o usuário pode não saber quais documentos são relevantes para a audiência. **Recomendação:** incluir na notificação uma lista de sugestão (comprovantes, fotos, prints, etc.) e permitir o upload antecipado no portal. | — |
| **2.** Acessar a sala virtual | — | Plano 2: 2.1 >> 2.2 (sequência) |
| **2.1** Clicar no link seguro da notificação e acessar o portal no horário agendado | **Problema:** link expirado ou usuário tenta acessar fora do horário. **Recomendação:** manter o link ativo por pelo menos 24 h após o horário, redirecionar para sala de espera e exibir contagem regressiva para o início da sessão. | — |
| **2.2** Realizar o teste de periféricos (câmera e microfone) e confirmar o funcionamento | **Problema:** o usuário pode não conceder as permissões do navegador ou os dispositivos podem não funcionar. **Recomendação:** oferecer um guia visual para ativar permissões, ferramenta de diagnóstico automático e permitir a participação apenas por áudio caso o vídeo falhe. | — |
| **3.** Participar da sessão de conciliação | — | Plano 3: 3.1 = 3.2 = 3.3 (tarefas independentes; a ordem não é fixa) |
| **3.1** Visualizar na tela o nome e o papel de cada participante (consumidor, fornecedor, mediador) | **Problema:** interface poluída pode dificultar a identificação de quem está falando. **Recomendação:** exibir permanentemente os nomes e papéis sobrepostos ao vídeo e destacar o participante ativo no momento. | — |
| **3.2** Participar da discussão, ativando/desativando o microfone e a câmera conforme necessário | **Problema:** o usuário pode esquecer o microfone ligado e causar interferências, ou não saber como silenciar. **Recomendação:** indicador visual claro de _microfone ligado/desligado_, atalho para silenciar com um clique e dica de etiqueta no início da sessão. | — |
| **3.3** Utilizar o chat de evidências para trocar documentos com as outras partes | **Problema:** dificuldade em localizar a funcionalidade de chat durante a discussão. **Recomendação:** posicionar o ícone do chat em local fixo e visível na tela, com notificação discreta sempre que um novo documento for recebido. | — |
| **4.** Finalizar a participação na audiência | — | Plano 4: se houver acordo [4.1] senão [4.2] (escolha exclusiva) |
| **4.1** Revisar e assinar digitalmente o termo de acordo gerado pelo mediador | **Problema:** o usuário pode não saber como realizar a assinatura digital (Gov.br) ou ter receio sobre a validade jurídica. **Recomendação:** exibir um tutorial rápido sobre assinatura digital, destacar a validade jurídica do documento e solicitar confirmação explícita antes de finalizar. | — |
| **4.2** Receber a comunicação de encerramento sem acordo e a informação sobre os próximos passos | **Problema:** o usuário pode ficar sem saber o que acontecerá após uma audiência sem acordo. **Recomendação:** o sistema deve exibir de forma clara o novo _status_ do processo e informar, em linguagem simples, o prazo e a etapa seguinte (ex.: "Seu processo seguirá para análise do PROCON, que poderá convocar uma nova audiência ou emitir uma decisão em até 30 dias"). | — |

*Tabela 2 — Representação textual do HTA: Participar de audiência de conciliação virtual. Fonte: Elaborado por Pedro Augusto Moretti Moreira (2026).*

---

## 2. Árvores de Tarefas Concorrentes (CTT)

As **Árvores de Tarefas Concorrentes** (*ConcurTaskTrees* — CTT) são uma técnica de modelagem que classifica cada tarefa em um de quatro tipos e modela as relações de ordem e concorrência entre elas. Os quatro tipos de tarefa são (BARBOSA; SILVA, 2021, p. 173–174):

| Ícone | Tipo | Descrição |
| :---: | :--- | :--- |
| 👤 | **Tarefa do Usuário** | Realizada mentalmente, sem interação direta com o sistema. |
| 💻 | **Tarefa do Sistema** | Executada automaticamente pelo sistema, sem ação do usuário. |
| 🖱️ | **Tarefa Interativa** | Envolve interação direta entre usuário e sistema (ação + feedback). |
| ☁️ | **Tarefa Abstrata** | Decompõe-se em subtarefas; não é executada diretamente. |

Os principais **operadores de relação** utilizados são:

- `>>` Ativação (T1 deve ser completada antes de T2 iniciar)
- `[]` Escolha (T1 ou T2, mutuamente exclusivas)
- `=` Concorrência (T1 e T2 podem ocorrer em qualquer ordem)
- `[]>>` Ativação com passagem de informação (T1 ativa T2 e envia dados)

<p align="center">
  <img src="../images/CTT-Heitor.drawio.png" alt="Árvore CTT — Acompanhar reclamação e responder proposta" width="750">
  <br><em>Figura 3 — Árvore CTT: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo com auxílio do Draw.io (2026).</em>
</p>

**Representação textual hierárquica do CTT:**

```
☁️ T0 — Acompanhar reclamação e responder à proposta
   [Plano: T1 >> T2 >> T3]
   │
   ├── ☁️ T1 — Acessar portal via notificação ativa
   │    [Plano: T1.1 []>> T1.2]
   │    ├── 💻 T1.1 — Sistema envia notificação proativa (WhatsApp/SMS/e-mail)
   │    └── 🖱️ T1.2 — Usuário toca no link da notificação e o sistema abre o painel
   │
   ├── ☁️ T2 — Interpretar status e proposta da empresa
   │    [Plano: T2.1 >> T2.2]
   │    ├── 💻 T2.1 — Sistema exibe linha do tempo do processo com status descritivo
   │    └── 👤 T2.2 — Usuário lê e interpreta o resumo da proposta da empresa
   │
   └── ☁️ T3 — Registrar decisão
        [Plano: T3.1 [] T3.2  (escolha exclusiva)]
        ├── 🖱️ T3.1 — Usuário seleciona "Aceitar" e confirma
        │    └── 💻 T3.1a — Sistema registra aceite, notifica empresa e envia confirmação ao usuário
        └── 🖱️ T3.2 — Usuário seleciona "Recusar" e confirma
             └── 💻 T3.2a — Sistema registra recusa e informa o próximo passo do processo
```

*Figura 4 — Representação textual hierárquica da árvore CTT: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo (2026).*

<p align="center">
  <img src="../images/CTT-Moretti.svg" alt="Árvore CTT — Participar de audiência de conciliação virtual" width="100%">
  <br><em>Figura 5 — Árvore CTT: Participar de audiência de conciliação virtual. Fonte: Elaborado por Pedro Augusto Moretti Moreira com auxílio do Mermaid.js (2026).</em>
</p>

**Representação textual hierárquica do CTT:**

```
☁️ T0 — Participar de audiência de conciliação virtual
   [Plano: T1 >> T2 >> T3 >> T4]
   │
   ├── ☁️ T1 — Preparar‑se para a audiência
   │    [Plano: T1.1 >> T1.2]
   │    ├── 💻 T1.1 — Sistema envia notificação com link da sala e orientações
   │    └── 👤 T1.2 — Usuário lê a notificação e separa documentos e evidências
   │
   ├── ☁️ T2 — Acessar a sala virtual
   │    [Plano: T2.1 >> T2.2]
   │    ├── 🖱️ T2.1 — Usuário clica no link da notificação e o sistema abre o portal
   │    └── ☁️ T2.2 — Realizar teste de periféricos
   │         [Plano: (T2.2.1 = T2.2.2 = T2.2.3) >> T2.2.4]
   │         ├── 💻 T2.2.1 — Sistema solicita permissão para usar câmera e microfone
   │         ├── 🖱️ T2.2.2 — Usuário concede permissões de hardware
   │         ├── 💻 T2.2.3 — Sistema reproduz áudio/vídeo de teste para conferência
   │         └── 🖱️ T2.2.4 — Usuário confirma que áudio e vídeo estão funcionando
   │
   ├── ☁️ T3 — Participar da sessão de conciliação
   │    [Plano: T3.1 = T3.2 = T3.3]
   │    ├── 💻 T3.1 — Sistema exibe vídeo, nome e papel de cada participante na tela
   │    ├── 🖱️ T3.2 — Usuário participa da discussão, ativa/desativa microfone e câmera
   │    └── ☁️ T3.3 — Consultar documentos durante a sessão
   │         [Plano: T3.3.1 >> T3.3.2]
   │         ├── 🖱️ T3.3.1 — Usuário acessa o chat de evidências para trocar documentos
   │         └── 💻 T3.3.2 — Sistema exibe documentos compartilhados na tela
   │
   └── ☁️ T4 — Finalizar participação na audiência
        [Plano: Se acordo (T4.1) senão (T4.2)]
        ├── ☁️ T4.1 — Assinar termo de acordo
        │    [Plano: T4.1.1 >> T4.1.2 >> T4.1.3]
        │    ├── 💻 T4.1.1 — Mediador elabora termo de acordo e sistema exibe para as partes
        │    ├── 🖱️ T4.1.2 — Usuário revisa o termo e realiza assinatura digital (Gov.br)
        │    └── 💻 T4.1.3 — Sistema registra assinatura, encerra a sessão e envia PDF por e‑mail
        │
        └── ☁️ T4.2 — Encerrar sessão sem acordo
             [Plano: T4.2.1 >> T4.2.2]
             ├── 💻 T4.2.1 — Mediador comunica o encerramento e sistema finaliza a sessão
             └── 💻 T4.2.2 — Sistema registra o status "Sem acordo" e notifica as partes sobre o prosseguimento
```

*Figura 6 — Representação textual hierárquica da árvore CTT: Participar de audiência de conciliação virtual. Fonte: Elaborado por Pedro Augusto Moretti Moreira (2026).*

!!! info "Responsável por este artefato"
    Este documento foi elaborado por **Pedro Augusto Moretti Moreira**, responsável pela funcionalidade *Sala de Conciliação Virtual com Mediação Assistida* na Etapa 2 do projeto. 

!!! info "Responsáveis pelas funcionalidades"
    Portal de Acompanhamento de Reclamações com Notificações Ativas: **Heitor Macedo Ricardo** (HTA e CTT apresentados nas Figuras 1, 3 e 4). Sala de Conciliação Virtual com Mediação Assistida: **Pedro Augusto Moretti Moreira** (HTA e CTT apresentados nas Figuras 2, 5 e 6). Integra o conjunto de artefatos das funcionalidades: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Cenários](cenarios.md).

## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação e redação da Análise de Tarefas deste documento.

---

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Elaboração da Análise de Tarefas com HTA e CTT para a funcionalidade de Acompanhamento de Reclamação. | Heitor Macedo Ricardo | A definir |
