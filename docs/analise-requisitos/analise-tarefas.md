# Análise de Tarefas: Acompanhamento de Reclamação

## Introdução

A Análise de Tarefas é uma etapa fundamental na engenharia de requisitos de sistemas interativos. Segundo Barbosa e Silva (2021), seu objetivo é compreender **como os usuários realizam seu trabalho, quais atividades executam e por quê**, identificando as estruturas que organizam as tarefas, os recursos cognitivos necessários e as possíveis fontes de erro. Ela pode ser aplicada tanto para avaliar sistemas existentes quanto para orientar o design de novos sistemas, e deve ser fundamentada em dados reais coletados junto aos usuários — como os obtidos no Grupo de Foco realizado com a Persona Laura em 30/04/2026.

Neste documento são aplicadas duas técnicas de modelagem complementares:

- **Análise Hierárquica de Tarefas (HTA):** decompõe o objetivo principal do usuário em subobjetivos e operações elementares, organizados hierarquicamente, identificando problemas e recomendações em cada nível (Barbosa e Silva, 2021, p. 165–166).
- **Árvores de Tarefas Concorrentes (CTT):** classifica cada tarefa por tipo (Usuário, Sistema, Interativa ou Abstrata) e modela as relações de ordem, ativação e concorrência entre elas (Barbosa e Silva, 2021, p. 173–174).
- **GOMS (Goals, Operators, Methods, and Selection Rules):** descreve o conhecimento procedimental necessário para realizar tarefas em sistemas computacionais, permitindo prever o desempenho e avaliar a eficiência do design (Barbosa e Silva, 2021, p. 161).

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
  <br><em>Figura 2 — Diagrama HTA: Participar de audiência de conciliação virtual. Fonte: Elaborado por Pedro Augusto Moretti Moreira com auxílio do Mermaid.js (2026).</em>
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

<p align="center">
  <img src="../images/HTA-Heloisa.png" alt="Diagrama HTA — Validação com OCR" width="750">
  <br><em>Figura 3 — Diagrama HTA: Validação de documento com OCR. Fonte: Elaborado por Heloisa Laura Santos da Silva com auxílio do Mermaid.js (2026).</em>
</p>

**Tabela de Representação HTA — Validação de documentos com OCR:**

| Operação (Objetivo / Operação) | Inputs (circunstâncias) | Ações (actions) | Feedback / Testes (condições de sucesso) | Problemas potenciais | Recomendações de IHC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0.0** Validar documento anexado com OCR (objetivo geral) | Usuário autenticado; processo aberto; arquivo selecionado (PDF/IMG) | Sequência: 1 >> 1.1 >> 1.2 >> 1.3 >> 1.4 >> 1.7 | Documento anexado e marcado como Aceito / Pendência / Rejeitado; protocolo gerado | Falhas de upload; perda de sessão | Fornecer orientação clara, formatos aceitos e feedback imediato de upload |
| **1.** Iniciar anexação | Processo aberto; botão "Anexar documento" disponível | Usuário seleciona "Anexar" → escolhe arquivo → confirma envio | Barra de progresso; thumbnail/preview; mensagem "Upload concluído" | Arquivo muito grande; conexão interrompida | Mostrar formatos/limites antes do envio; upload resumível; confirmação visual clara |
| **1.1** Pré-processamento (sistema) | Arquivo enviado (PDF/JPEG/PNG); metadados do arquivo | Normalizar imagem/PDF (deskew, crop, desaturate), separar páginas | Preview do arquivo pré-processado; flag inicial de qualidade | Imagem com baixa resolução; páginas faltando | Apresentar preview e instruções de captura (ex.: iluminação, foco) |
| **1.2** Extração OCR | Imagem/páginas pré-processadas | Executar OCR por página → extrair texto, tabelas e campos-chave (CPF/CNPJ, datas, valores) | Resultado OCR com confiança por bloco; campos-chave preenchidos automaticamente | Baixa confiança; textos manuscritos; idiomas mistos | Exibir scores de confiança; destacar trechos incertos para correção manual |
| **1.3** Verificação de legibilidade e qualidade | Scores OCR; resolução da imagem; presença de artefatos | Calcular índice de legibilidade; detectar páginas borradas/recortadas | Status legível / ilegível; recomendações para recaptura | Borrões, reflexos, corte de borda | Definir thresholds e mostrar instruções específicas (ex.: recortar, re-fotografar) |
| **1.4** Avaliação de aderência ao tipo de evidência | Texto extraído; metadados do processo (tipo de prova requerida) | Aplicar regras (palavras-chave, padrões de nota fiscal, campos obrigatórios) | Resultado: Aceito / Pendência (faltam campos) / Rejeitado (não corresponde) com justificativa | Falsos negativos por variações de formato | Mostrar motivo claro (ex.: "faltou CNPJ"), exibir trecho correspondente e permitir mapeamento manual |
| **1.5** Comunicação de pendência e correção | Resultado da avaliação (Pendência) + instruções padrão | Sistema informa usuário com mensagem objetiva e passos (re-enviar, editar, marcar páginas) | Usuário recebe instruções e botões para ação (Reenviar / Editar extração) | Mensagens vagas que geram confusão | Mensagens orientadas por ação, com exemplos visuais do que corrigir |
| **1.6** Correção pelo usuário | Visualização do OCR com destaques; formulário pré-preenchido | Usuário edita campos críticos (ex.: CPF, data), reenvia novo arquivo ou aceita correções | Reexecução OCR / revalidação; confirmação de recebimento | Usuário pode não entender destaques | Fornecer ajuda contextual (tooltip) e opção de chat/FAQ rápido |
| **1.7** Finalização e anexação definitiva | Documento aceito; campos extraídos validados | Sistema anexa documento ao processo, grava metadados, gera protocolo e notifica usuário | Mensagem "Documento aceito" + número de protocolo + timestamp | Falha na gravação ou duplicidade | Operação transacional; filas de retry; confirmação clara e opção de baixar comprovante |

*Tabela 3 — Representação textual do HTA: Validação de documentos com OCR. Fonte: Elaborado por Heloisa Laura Santos da Silva (2026).* 

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

### Árvore CTT — Acompanhar reclamação e responder proposta

<p align="center">
  <img src="../images/CTT-Heitor.drawio.png" alt="Árvore CTT — Acompanhar reclamação e responder proposta" width="750">
  <br><em>Figura 4 — Árvore CTT: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo com auxílio do Draw.io (2026).</em>
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

*Figura 5 — Representação textual hierárquica da árvore CTT: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo (2026).*

<p align="center">
  <img src="../images/CTT-Moretti.svg" alt="Árvore CTT — Participar de audiência de conciliação virtual" width="100%">
  <br><em>Figura 6 — Árvore CTT: Participar de audiência de conciliação virtual. Fonte: Elaborado por Pedro Augusto Moretti Moreira com auxílio do Mermaid.js (2026).</em>
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

*Figura 7 — Representação textual hierárquica da árvore CTT: Participar de audiência de conciliação virtual. Fonte: Elaborado por Pedro Augusto Moretti Moreira (2026).*

!!! info "Responsáveis pelas funcionalidades"
    Portal de Acompanhamento de Reclamações com Notificações Ativas: **Heitor Macedo Ricardo** (HTA e CTT apresentados nas Figuras 1, 3 e 4). Sala de Conciliação Virtual com Mediação Assistida: **Pedro Augusto Moretti Moreira** (HTA e CTT apresentados nas Figuras 2, 5 e 6). Integra o conjunto de artefatos das funcionalidades: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Cenários](cenarios.md).

### Árvore CTT — Validação de Documentos com OCR

<p align="center">
  <img src="../images/CTT_Heloisa.drawio.png" alt="Árvore CTT — Validação de documento com OCR" width="750">
  <br><em>Figura 8 — Árvore CTT: Validação de documento com OCR. Fonte: Elaborado por Heloisa Laura Santos da Silva com auxílio do Draw.io (2026).</em>
</p>

**Representação textual hierárquica do CTT:**

```
☁️ T0 — Validar Documento com OCR
[Plano: T1 >> T2 >> T3]
│
├── ☁️ T1 — Fazer Upload de Documento
│    [Plano: T1.1 >> T1.2]
│    ├── 💻 T1.1 — Exibir campo para upload de arquivo
│    └── 🖱️ T1.2 — Selecionar arquivo e enviar
│
├── ☁️ T2 — Enviar Notificação de Recebimento do Arquivo
│    [Plano: T2.1 | T2.2]
│    ├── 💻 T2.1 — Notifica aceitação do arquivo
│    └── 💻 T2.2 — Notifica rejeição do arquivo
│
└── ☁️ T3 — Notificar Sobre Validação do Documento
[Plano: T3.1 >> T3.2 >> (T3.3 | T3.4)]
├── 💻 T3.1 — Extração de dados e metadados do documento
├── 💻 T3.2 — Análise do conteúdo com LLM
├── 💻 T3.3 — Notifica validação do documento
└── 💻 T3.4 — Notifica não validação
```
*Figura 9 — Representação textual hierárquica da árvore CTT: Validar documento com OCR. Fonte: Elaborado por Heloisa Laura Santos da Silva (2026).*

!!! info "Responsável por este artefato"
    Este documento foi elaborado por **Heloisa Laura Santos da Silva**, responsável pela funcionalidade *Validação de documentos com OCR* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Cenários](cenarios.md).

---

## 3. GOMS (Goals, Operators, Methods, and Selection Rules)

O método **GOMS** (*Goals, Operators, Methods, and Selection Rules*) é utilizado para descrever o conhecimento procedimental que um usuário possui para realizar tarefas dentro de um sistema computacional. Diferente do HTA, o GOMS foca na eficiência e no desempenho do usuário experiente, decompondo a tarefa em quatro elementos principais (BARBOSA; SILVA, 2021, p. 161):

- **Goals (Metas):** o que o usuário quer realizar (ex: Registrar reclamação).
- **Operators (Operadores):** ações primitivas (físicas ou mentais) que o sistema permite realizar (ex: clicar, digitar, pensar).
- **Methods (Métodos):** sequências de submetas e operadores para atingir uma meta.
- **Selection Rules (Regras de Seleção):** tomadas de decisão quando há mais de um método para a mesma meta.

A técnica aplicada a seguir é a variação **CMN-GOMS** (Card, Moran e Newell), que utiliza uma estrutura de pseudocódigo. A tarefa analisada é: **"Registrar uma contestação de cobrança indevida (Assuntos Financeiros) via Desktop"**, baseada na Persona Primária **Roberto Oliveira**.

### Representação CMN-GOMS: Registrar Reclamação Financeira

<p align="center">
  <img src="../images/GOMS-Mateus.png" alt="Diagrama GOMS — Registrar Reclamação Financeira" width="750">
  <br><em>Figura 10 — Diagrama GOMS: Registrar Reclamação Financeira. Fonte: Elaborado por Mateus Rodrigues Barreto com auxílio do Mermaid.js (2026).</em>
</p>

```
GOAL 0: REGISTRAR RECLAMAÇÃO FINANCEIRA
  GOAL 1: ACESSAR ÁREA DE RECLAMAÇÃO
    METHOD 1.A: NAVEGAÇÃO POR MENU
      OP 1.A.1: MOVER MOUSE PARA "RECLAMAÇÕES"
      OP 1.A.2: CLICAR EM "NOVA RECLAMAÇÃO"
    METHOD 1.B: ACESSO DIRETO VIA PAINEL DE MONITORAMENTO
      OP 1.B.1: MOVER MOUSE PARA BOTÃO "REGISTRAR AGORA" NO PAINEL
      OP 1.B.2: CLICAR NO BOTÃO
    SEL. RULE: USAR METHOD 1.B SE O BOTÃO ESTIVER VISÍVEL NO LOGIN, CASO CONTRÁRIO USAR 1.A

  GOAL 2: DEFINIR CATEGORIA E FORNECEDOR
    OP 2.1: DIGITAR NOME DO BANCO NO CAMPO DE BUSCA
    OP 2.2: SELECIONAR FORNECEDOR NA LISTA DE RESULTADOS
    OP 2.3: CLICAR NO DROPDOWN "CATEGORIA"
    OP 2.4: SELECIONAR "ASSUNTOS FINANCEIROS"

  GOAL 3: DESCREVER O PROBLEMA E ANEXAR PROVAS
    OP 3.1: PENSAR NO RELATO DO OCORRIDO (OP. MENTAL)
    OP 3.2: DIGITAR DESCRIÇÃO DA COBRANÇA INDEVIDA
    OP 3.3: CLICAR EM "ADICIONAR ANEXO"
    OP 3.4: SELECIONAR ARQUIVO "FATURA_CARTAO.PDF" NA PASTA LOCAL
    OP 3.5: CLICAR EM "CONFIRMAR UPLOAD"

  GOAL 4: FINALIZAR E SALVAR PROTOCOLO
    OP 4.1: CLICAR EM "FINALIZAR RECLAMAÇÃO"
    OP 4.2: AGUARDAR GERAÇÃO DO PROTOCOLO (OP. SISTEMA)
    OP 4.3: CLICAR EM "BAIXAR COMPROVANTE PDF"
    OP 4.4: VERIFICAR SE O ARQUIVO FOI SALVO (OP. MENTAL)
```

*Figura 11 — Representação em pseudocódigo (CMN-GOMS): Registrar Reclamação Financeira. Fonte: Elaborado por Mateus Rodrigues Barreto (2026).*

**Análise de Eficiência (Insights do GOMS):**

- **Caminho Crítico:** O Goal 3 é o que consome mais tempo devido aos operadores de digitação e seleção de arquivos. Recomenda-se a implementação de **OCR (Reconhecimento Óptico de Caracteres)** para que a fatura preencha automaticamente os campos de valor e data, reduzindo drasticamente o número de operadores de digitação e minimizando erros.

- **Regra de Seleção:** A presença do método 1.B (**Painel de Monitoramento**) é vital para o Roberto, pois economiza 2 operadores de navegação manual, alinhando-se ao seu perfil pragmático de resolução rápida.

!!! info "Responsável por este artefato"
    A seção de GOMS (Goals, Operators, Methods, and Selection Rules) foi elaborada por **Mateus Rodrigues Barreto**, baseada na funcionalidade *Painel de monitoramento de prazos com alertas jurídicos*. Integra o conjunto de artefatos da funcionalidade: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Cenários](cenarios.md).

## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação e redação da Análise de Tarefas deste documento.

---

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Elaboração da Análise de Tarefas com HTA e CTT para a funcionalidade de Acompanhamento de Reclamação. | Heitor Macedo Ricardo | Heloisa Silva |
| `1.1` | 30/04/2026 | Elaboração da Análise de Tarefas com HTA e CTT para a funcionalidade de Conciliação Virtual. | Pedro Augusto Moretti Moreira | Heitor Macedo |
| `1.2` | 03/05/2026 | Inserção da HTA e CTT de validação de documentos com OCR e ajustes de conteúdo. | Heloisa Silva | Pedro Augusto Moretti |
| `1.3` | 03/05/2026 | Adição da Análise GOMS para a tarefa de registro de reclamação financeira. | Mateus Rodrigues Barreto | Heloisa Silva |