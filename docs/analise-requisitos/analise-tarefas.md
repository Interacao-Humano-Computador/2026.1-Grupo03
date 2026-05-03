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

---
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

*Tabela 2 — Representação textual do HTA: Validação de documentos com OCR. Fonte: Elaborado por Heloisa Laura Santos da Silva (2026).* 

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
  <br><em>Figura 2 — Árvore CTT: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo com auxílio do Draw.io (2026).</em>
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

*Figura 3 — Representação textual hierárquica da árvore CTT: Acompanhar reclamação e responder proposta. Fonte: Elaborado por Heitor Macedo Ricardo (2026).*

!!! info "Responsável por este artefato"
    Este documento foi elaborado por **Heitor Macedo Ricardo**, responsável pela funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Cenários](cenarios.md).

---

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
| `1.1` | 03/05/2026 | Inserção da HTA de validação de documentos com OCR e ajustes de conteúdo. | Heloisa Silva | Heitor Macedo |
