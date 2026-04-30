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

> **Responsável por este artefato:** Este documento foi elaborado por **Heitor Macedo Ricardo**, responsável pela funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade, que inclui também o [Perfil de Usuário](perfil-usuario.md), as [Personas](personas.md), os [Cenários](cenarios.md) e a [Análise de Tarefas](analise-tarefas.md).
---
## Agradecimentos à IA

Agradecimento ao Claude pela ajuda na estruturação e redação da funcionalidade.

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Nova Funcionalidade | Heitor Macedo Ricardo | A definir |