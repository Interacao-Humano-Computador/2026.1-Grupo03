# Funcionalidades

Este documento detalha as funcionalidades propostas para a modernização do portal PROCON-DF, focando em transparência, agilidade e acessibilidade digital tanto para consumidores quanto para fornecedores.

---

### 1. Portal de Acompanhamento de Reclamações com Notificações Ativas

#### Visão Geral
Implementar um painel personalizado de acompanhamento que permita ao consumidor visualizar, em tempo real, o status e o histórico de cada etapa do seu processo de reclamação — com envio automático de notificações por e-mail e/ou SMS sempre que houver atualização, prazo crítico se aproximando ou ação necessária por parte do usuário.

#### Como funciona hoje (Estado Atual)
*   O usuário acessa o site e navega manualmente até "Acompanhar reclamação", **sem qualquer notificação ativa**.
*   A consulta retorna apenas um código de status genérico (ex.: *"Em análise"*), sem histórico ou prazo.
*   Não há comunicação proativa: o consumidor não sabe se precisa enviar documentos ou aguardar.
*   A ausência de feedback leva a ligações repetidas ao PROCON-DF e à **sensação de abandono do processo**.

#### Nova Experiência (Estado Proposto)
*   **Painel autenticado** com linha do tempo visual de todas as etapas do processo, com datas e responsáveis.
*   **Status descritivo** em cada fase: o que aconteceu, o que está pendente e qual o próximo passo.
*   **Notificações automáticas** por e-mail/SMS quando há atualização, documento solicitado ou prazo se aproximando.
*   **Canal de resposta integrado**: o consumidor pode enviar documentos ou responder ao PROCON diretamente pelo painel.

#### Fluxo de Funcionamento
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
**Problema identificado:** O site atual do PROCON-DF oferece a opção "Acompanhar reclamação", mas ela exibe apenas um status estático e genérico, gerando ansiedade e descrédito no órgão.
**Justificativa com base no Grupo de Foco:** Usuários relataram que o site atual é **"confuso"** e que sentem **frustração com a falta de retorno**. A funcionalidade resolve isso eliminando a necessidade de buscas manuais incessantes.

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Heitor Macedo Ricardo**, responsável pela funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas*.

---

### 2. Sala de Conciliação Virtual com Mediação Assistida

#### Visão Geral
Implementar uma plataforma de videochamada integrada diretamente ao processo administrativo do portal. A funcionalidade permite a realização de audiências de conciliação remotas entre o consumidor, o representante da empresa (fornecedor) e o mediador do PROCON-DF, eliminando a necessidade de deslocamento físico e agilizando a resolução de conflitos.

#### Como funciona hoje (Estado Atual)
*   As audiências são majoritariamente **presenciais**, exigindo que todas as partes se desloquem até uma unidade física do PROCON-DF.
*   Há um alto índice de **absenteísmo** (faltas) devido a conflitos de logística, trânsito e horário comercial.
*   O agendamento é rígido e a infraestrutura física limita a quantidade de audiências diárias.
*   Consumidores e pequenos empresários perdem horas de trabalho para resolver disputas de baixo valor financeiro.

#### Nova Experiência (Estado Proposto)
*   **Ambiente de Vídeo Nativo**: Sala virtual segura acessada via link único enviado por e-mail/WhatsApp.
*   **Mediação Assistida**: O mediador possui ferramentas de controle (moderação de fala, chat para documentos e tela compartilhada para leitura do termo de acordo).
*   **Assinatura Digital Integrada**: Caso haja acordo, o termo é gerado e assinado digitalmente pelas partes na mesma interface, com validade jurídica imediata.
*   **Acessibilidade**: Interface otimizada para smartphones (mobile-first), permitindo que o usuário participe da audiência de qualquer lugar.

#### Fluxo de Funcionamento
```
Agendamento da audiência pelo mediador
→ Notificação para Consumidor e Fornecedor (Link da Sala)
→ Teste de periféricos (Câmera/Microfone) no portal
→ Início da sessão de vídeo no horário marcado
→ Discussão mediada e chat para troca de evidências
→ Elaboração do termo de acordo em tempo real
→ Assinatura digital (Gov.br ou similar)
→ Encerramento e envio do PDF por e-mail
```

#### Heurísticas de Nielsen Atendidas
| Heurística | Como é atendida |
| :--- | :--- |
| **Prevenção de erros** | O sistema exige teste de áudio/vídeo antes da entrada na sala para evitar falhas técnicas durante a audiência. |
| **Ajuda e documentação** | Guia rápido de "Como se comportar em uma audiência virtual" e suporte técnico via chat na sala. |
| **Controle e liberdade do usuário** | O usuário pode silenciar seu microfone ou fechar a câmera, além de pedir "momento privado" com o mediador. |
| **Reconhecimento em vez de recordação** | A tela de vídeo exibe o nome e o papel de cada participante (Consumidor, Fornecedor, Mediador) permanentemente. |

#### Declaração da Funcionalidade
**Nome:** Sala de Conciliação Virtual com Mediação Assistida
**Problema identificado:** A obrigatoriedade de audiências presenciais atua como uma barreira para a resolução de conflitos, onerando as partes e saturando as unidades físicas do PROCON-DF. 
**Justificativa com base na Entrevista e Grupo de Foco:** O perfil do **microempreendedor (Gustavo)** indicou que o tempo é um recurso escasso e sites governamentais devem ser funcionais. Já o perfil do **consumidor (Lucas e Laura)** demanda soluções digitais rápidas. A sala virtual atende a ambos ao transformar o processo burocrático em uma tarefa digital de 20 minutos.

**Comparação: estado atual × nova solução**

| Critério | Estado Atual (Presencial) | Nova Funcionalidade (Virtual) |
| :--- | :--- | :--- |
| Deslocamento | Exigido (Custo de tempo/transporte) | Zero (Acesso remoto via portal) |
| Assinatura | Física em papel | Digital com validade jurídica |
| Logística | Limitada por salas físicas | Escalável (Múltiplas salas simultâneas) |
| Taxa de Faltas | Alta (Logística difícil) | Reduzida (Facilidade de acesso) |

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Pedro Augusto Moretti Moreira**, responsável pela funcionalidade *Sala de Conciliação Virtual com Mediação Assistida*.

---

## Agradecimentos à IA

Agradecimento ao Gemini pela ajuda na estruturação, redação e consolidação das funcionalidades deste projeto.

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Criação da funcionalidade: Portal de Acompanhamento | Heitor Macedo Ricardo | A definir |
| `1.1` | 01/05/2026 | Integração da funcionalidade: Sala de Conciliação Virtual | Pedro Augusto Moretti Moreira | A definir |