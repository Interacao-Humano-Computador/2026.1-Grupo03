# Funcionalidades

### Portal de Acompanhamento de Reclamações com Notificações Ativas

#### Visão Geral

Implementar um painel personalizado de acompanhamento que permita ao consumidor visualizar, em tempo real, o status e o histórico de cada etapa do seu processo de reclamação — com envio automático de notificações por e-mail e/ou SMS sempre que houver atualização, prazo crítico se aproximando ou ação necessária por parte do usuário.

#### Como funciona hoje (Estado Atual)

- O usuário acessa o site e navega manualmente até "Acompanhar reclamação", **sem qualquer notificação ativa**.
- A consulta retorna apenas um código de status genérico (ex.: *"Em análise"*), sem histórico ou prazo.
- Não há comunicação proativa: o consumidor não sabe se precisa enviar documentos ou aguardar.
- A ausência de feedback leva a ligações repetidas ao PROCON-DF e à **sensação de abandono do processo**.

#### Nova Experiência (Estado Proposto)

- **Painel autenticado** com linha do tempo visual de todas as etapas do processo, com datas e responsáveis.
- **Status descritivo** em cada fase: o que aconteceu, o que está pendente e qual o próximo passo.
- **Notificações automáticas** por e-mail/SMS quando há atualização, documento solicitado ou prazo se aproximando.
- **Canal de resposta integrado**: o consumidor pode enviar documentos ou responder ao PROCON diretamente pelo painel.

#### Fluxo de Funcionamento

O fluxo abaixo descreve o caminho completo do usuário, desde o acesso até a resolução da reclamação:

```
Usuário acessa o portal
→ Autenticação (CPF + senha)
→ Painel "Minhas Reclamações"
→ Seleciona processo
→ Visualiza linha do tempo
→ Atualização gerada pelo PROCON
→ Notificação e-mail/SMS
→ Usuário retorna ao painel
→ Responde ou envia documento
→ Resolução / Arquivamento
```

#### Heurísticas de Nielsen Atendidas

| Heurística | Como é atendida |
| :--- | :--- |
| **Visibilidade do status do sistema** | O usuário sabe sempre em que etapa está e o que acontecerá a seguir. |
| **Controle e liberdade do usuário** | O consumidor pode responder, anexar documentos ou solicitar esclarecimento a qualquer momento. |
| **Prevenção de erros** | Alertas de prazo evitam que o usuário perca janelas críticas por desconhecimento. |
| **Correspondência com o mundo real** | A linha do tempo usa linguagem simples e datas concretas, sem jargão jurídico ou técnico. |

#### Declaração da Funcionalidade

**Nome:** Portal de Acompanhamento de Reclamações com Notificações Ativas

**Problema identificado:** O site atual do PROCON-DF oferece a opção "Acompanhar reclamação", mas ela exibe apenas um status estático e genérico (ex.: *"Em análise"*), sem histórico de etapas, prazos ou comunicação proativa. O consumidor fica sem saber se precisa agir, se a empresa respondeu ou quando esperar uma resolução — gerando ansiedade, ligações desnecessárias ao órgão e sensação de abandono do processo.

**Justificativa com base no Grupo de Foco:** Os usuários participantes relataram que o site atual é **"confuso"**, **"desorientador"** e que sentem **frustração com a demora e a falta de retorno**. A funcionalidade proposta resolve diretamente essa ansiedade por meio de notificações automáticas, eliminando a necessidade de o usuário acessar o site repetidamente para verificar atualizações.

**Comparação: estado atual × nova solução**

| Critério | Estado Atual | Nova Funcionalidade |
| :--- | :--- | :--- |
| Visibilidade do status | Código genérico único | Linha do tempo com etapas descritivas |
| Comunicação proativa | Nenhuma | E-mail + SMS automáticos em cada evento |
| Ação do usuário | Apenas consulta | Envio de documentos e respostas integrado |
| Contexto de prazo | Ausente | Prazos visíveis com alertas antecipados |
| Transparência | Baixa | Alta — responsável e data em cada etapa |

!!! info "Responsável por este artefato"
    Este documento foi elaborado por **Heitor Macedo Ricardo**, responsável pela funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade: [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Cenários](cenarios.md) · [Análise de Tarefas](analise-tarefas.md).
---
### Assistente de Triagem Guiada para Reclamações

#### Visão Geral

Implementar um assistente interativo na página inicial que substitua a sobrecarga de informações por um fluxo de perguntas e respostas simples. O objetivo é conduzir o consumidor — com foco em perfis de maior vulnerabilidade tecnológica — desde a identificação do problema até a abertura da reclamação, eliminando as barreiras cognitivas geradas pela atual desorganização visual do portal.

#### Como funciona hoje (Estado Atual)

- O usuário depara-se com uma interface saturada de informações, onde links de serviços, notícias e banners externos competem por atenção de forma desordenada.
- A estética datada e o excesso de textos pequenos geram uma percepção de "spam" ou "páginas de pirataria", o que reduz a confiança do usuário no canal oficial[cite: 1].
- Não há um direcionamento claro ou um botão de ação (CTA) evidente; o usuário "não sabe por onde começar" para registrar uma queixa[cite: 1].
- Existe uma confusão sobre o papel do Procon, muitas vezes confundido com o Poder Judiciário, sem que o site esclareça essa distinção logo na entrada[cite: 1].

#### Nova Experiência (Estado Proposto)

- **Interface Minimalista (Clean Design):** Redução drástica de elementos visuais na home, priorizando o acesso ao serviço principal[cite: 1].
- **Fluxo de Triagem (Wizard):** Um sistema passo a passo que instrui o usuário desde o início, perguntando sobre a natureza do problema e tentativas prévias de contato[cite: 1].
- **Linguagem Cidadã:** Orientações claras e simples que explicam o que o Procon pode resolver, atuando como um facilitador pedagógico[cite: 1].
- **Foco em Mobile:** Interface otimizada para smartphones, garantindo que o fluxo guiado seja intuitivo em telas menores[cite: 1].

#### Fluxo de Funcionamento

O fluxo abaixo descreve o caminho do usuário através do assistente de triagem:

Usuário acessa o portal
→ Visualiza Botão Central ("Iniciar Reclamação")
→ Seleciona categoria do problema (ex: Produto com Defeito)
→ Assistente pergunta: "Você já tentou contato com a empresa?"
→ Explicação sobre o papel do Procon vs. Justiça
→ Cadastro ou Login (Gov.br)
→ Upload guiado de documentos (Foto da nota/comprovante)
→ Revisão dos dados
→ Protocolo gerado e enviado para o novo Portal de Acompanhamento

#### Heurísticas de Nielsen Atendidas

| Heurística | Como é atendida |
| :--- | :--- |
| **Estética e design minimalista** | O design remove a poluição visual e foca apenas nas informações essenciais para a tarefa de reclamar. |
| **Reconhecimento em vez de recordação** | O fluxo passo a passo guia o usuário com opções claras, evitando que ele precise pesquisar externamente "como usar o site". |
| **Ajuda e documentação** | O assistente oferece explicações contextuais sobre o Código de Defesa do Consumidor durante o preenchimento. |
| **Correspondência com o mundo real** | Utiliza termos simples para descrever problemas cotidianos (ex: "atendimento de tortura" ou "atraso") em vez de jargão jurídico puro. |

#### Declaração da Funcionalidade

**Nome:** Assistente de Triagem Guiada para Reclamações

**Problema identificado:** O site atual do PROCON-DF é descrito como "poluído", "confuso" e "desorientador", atuando como uma barreira que empurra os consumidores para soluções privadas ou para a desistência do processo por excesso de burocracia percebida.

**Justificativa com base no Grupo de Foco:** Os participantes relataram frustração com fluxos ineficientes e sugeriram que o "site perfeito" deveria ter um botão central destacado de "Registrar Reclamação" e um sistema que os guiasse passo a passo. Esta funcionalidade atende diretamente a necessidade de clareza e facilidade de uso via smartphone.

**Comparação: estado atual × nova solução**

| Critério | Estado Atual | Nova Funcionalidade |
| :--- | :--- | :--- |
| Interface | Poluída e com estética de "spam" | Limpa (Clean Design) e profissional |
| Direcionamento | Inexistente; usuário fica "perdido" | Botão central (CTA) de alto contraste|
| Processo | Cadastro manual em formulários densos | Fluxo interativo e assistido (Wizard) |
| Orientação | Ausência de instruções claras | Explicação integrada sobre o papel do órgão |

!!! info "Responsável por este artefato"
    Este documento foi elaborado por **Pedro Augusto**, responsável pela funcionalidade *Assistente de Triagem Guiada para Reclamações* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade: [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Cenários](cenarios.md) · [Análise de Tarefas](analise-tarefas.md).

---
## Agradecimentos à IA

Agradecimento ao Claude pela ajuda na estruturação e redação da funcionalidade.

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.1` | 02/05/2026 | Nova Funcionalidade | Pedro Macedo | A definir |
| `1.0` | 30/04/2026 | Nova Funcionalidade | Heitor Macedo Ricardo | A definir |