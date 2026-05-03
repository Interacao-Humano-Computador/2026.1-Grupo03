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

### 3. Dossiê digital com OCR e validação de documentos

#### Visão Geral
Implementar na plataforma a opção de anexar documentos ao processo de petição como notas fiscais, contratos e prints de conversa, por meio de uma interface simples e guiada. Com o uso de OCR, o sistema identifica automaticamente o conteúdo do arquivo anexado, confere se ele é legível e avalia sua aderência ao tipo de evidência solicitada. Isso elimina a necessidade de entrega física de documentos, reduz o tempo de conferência manual e acelera a análise inicial do processo.

#### Como funciona hoje (Estado Atual)
*   O usuário precisa reunir os documentos manualmente e, em muitos casos, comparecer presencialmente para apresentar ou complementar informações.
*   Há espera entre a solicitação e a validação do material, já que a conferência depende de análise humana e de filas internas de atendimento.
*   O processo fica mais lento quando o documento está ilegível, incompleto ou fora do padrão esperado, exigindo retrabalho e novo contato com o cidadão.
*   Consumidores e pequenos empresários perdem tempo com deslocamentos, reenvios e retornos desnecessários para tarefas que poderiam ser resolvidas digitalmente.

#### Nova Experiência (Estado Proposto)
*   **Envio imediato de documentos**: o usuário anexa os arquivos diretamente no portal, sem precisar aguardar atendimento presencial ou novo protocolo físico.
*   **Validação automática com OCR**: o sistema faz uma triagem inicial do conteúdo, reduzindo o tempo de conferência manual e acelerando a resposta sobre aceitação ou pendência do documento.
*   **Menos retrabalho**: se houver problema no arquivo, o usuário recebe orientação rápida sobre o que corrigir, evitando ciclos longos de retorno ao atendimento.
*   **Processo mais célere**: a documentação entra no fluxo administrativo mais rapidamente, diminuindo o tempo de espera entre a petição e a análise efetiva do caso.
*   **Acesso contínuo**: o envio pode ser feito a qualquer hora, sem depender do horário de funcionamento da unidade, o que reduz filas e atrasos operacionais.

#### Fluxo de Funcionamento
```
Usuário acessa o processo
→ Seleciona a opção de anexar documento
→ Envia nota fiscal, contrato ou print de conversa
→ Sistema executa OCR e validação inicial
→ Portal indica aceite, pendência ou necessidade de correção
→ Documento segue para análise administrativa
→ Processo avança com menos espera e menos retrabalho
```

#### Heurísticas de Nielsen Atendidas
| Heurística | Como é atendida |
| :--- | :--- |
| **Prevenção de erros** | A validação automática identifica documentos ilegíveis, incompletos ou fora do padrão antes de eles seguirem para análise. |
| **Ajuda e documentação** | O portal orienta o usuário sobre quais tipos de documentos são aceitos e como enviá-los corretamente. |
| **Visibilidade do status do sistema** | O usuário acompanha se o arquivo foi aceito, se há pendências ou se precisa reenviar algum documento. |


#### Declaração da Funcionalidade
**Nome:** Dossiê digital com OCR e validação de documentos
**Problema identificado:** A necessidade de envio e conferência manual de documentos cria espera desnecessária, retrabalho e lentidão na abertura e na continuidade do processo, além de aumentar a dependência de atendimento presencial.
**Justificativa com base na Entrevista e Grupo de Foco:** O perfil do **microempreendedor (Gustavo)** indicou que o tempo é um recurso escasso e sites governamentais devem ser funcionais. Já o perfil do **consumidor (Lucas e Laura)** demanda soluções digitais rápidas. O dossiê digital com OCR atende a ambos ao reduzir deslocamentos, eliminar etapas repetitivas de validação e tornar a tramitação mais rápida e previsível.

**Comparação: estado atual × nova solução**

| Critério | Estado Atual (Presencial) | Nova Funcionalidade (Virtual) |
| :--- | :--- | :--- |
| Deslocamento | Exigido para entrega e conferência física | Eliminado ou reduzido ao máximo, com envio digital |
| Espera | Depende de filas e análise manual | Reduzida com triagem automática e retorno imediato |
| Retrabalho | Alto, quando faltam ou sobram documentos | Menor, com validação prévia do conteúdo |
| Celeridade | Processo mais lento e sujeito a interrupções | Processo mais rápido e contínuo dentro do portal |

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Heloisa Laura Santos da Silva**, responsável pela funcionalidade *Dossiê digital com OCR e validação de documentos*.

---

### 4. Painel de monitoramento de prazos com alertas jurídicos

#### Visão Geral
Implementar um dashboard inteligente que mapeia e monitora automaticamente todos os prazos legais de um processo de reclamação. O sistema alerta o consumidor sobre prazos de resposta da empresa, datas de audiência e, crucialmente, o prazo prescricional, sugerindo ações judiciais caso o conflito não seja resolvido administrativamente.

#### Como funciona hoje (Estado Atual)
*   O consumidor é o único responsável por controlar os prazos de seu processo.
*   Não existe alerta sobre o **prazo prescricional** (perda do direito de entrar na justiça).
*   Se a empresa não responde, o processo pode ficar "parado" no sistema sem que o usuário saiba que já pode escalar para outras instâncias.
*   Consumidores perdem direitos por desconhecimento técnico das leis de prazos (CDC e CP).

#### Nova Experiência (Estado Proposto)
*   **Mapeamento Automático:** Ao abrir a reclamação, o sistema define a "agenda" do processo com base no Código de Defesa do Consumidor.
*   **Linha do Tempo de Prazos:** Visualização clara de quantos dias a empresa tem para responder e quando o direito de ação caduca.
*   **Alertas Inteligentes:** Notificações em contagem regressiva (30, 15 e 7 dias) antes de prazos fatais.
*   **Encaminhamento Judicial:** Sugestão automática de abertura de ação em Juizados Especiais caso a via administrativa falhe.

#### Fluxo de Funcionamento
```
Abertura da Reclamação
→ Motor de regras mapeia prazos legais aplicáveis
→ Criação da linha do tempo visual (Resposta, Audiência, Prescrição)
→ Monitoramento em tempo real do status
→ Notificação de atraso da empresa (Botão de Escalonamento)
→ Alerta de proximidade de prazo prescricional
→ Sugestão de ação judicial + Orientações sobre Juizado Especial
→ Exportação de Dossiê em PDF para uso judicial
```

#### Heurísticas de Nielsen Atendidas
| Heurística | Como é atendida |
| :--- | :--- |
| **Visibilidade do status do sistema** | O usuário visualiza o "relógio" do seu processo, sabendo exatamente quanto tempo resta para cada etapa. |
| **Ajuda e documentação** | O sistema oferece orientações jurídicas básicas sobre o que fazer se o prazo vencer (ex: procurar Juizado Especial). |
| **Reconhecimento em vez de recordação** | O sistema envia alertas proativos, eliminando a necessidade do usuário memorizar datas ou calcular prazos legais. |

#### Declaração da Funcionalidade
**Nome:** Painel de monitoramento de prazos com alertas jurídicos
**Problema identificado:** Muitos consumidores abandonam processos ou perdem o direito de agir judicialmente por não compreenderem os prazos legais e prescricionais envolvidos em suas reclamações.
**Justificativa com base na Persona Roberto:** Roberto é um usuário pragmático que valoriza o tempo e a prova documental. Para ele, saber o prazo exato que o banco tem para responder e ter um PDF pronto para uma ação judicial é o diferencial entre o sistema ser útil ou apenas "mais uma burocracia".

**Comparação: estado atual × nova solução**

| Critério | Estado Atual (Manual) | Nova Funcionalidade (Automatizada) |
| :--- | :--- | :--- |
| Controle de Prazos | Inteiramente por conta do usuário | Automatizado pelo sistema |
| Alerta de Prescrição | Inexistente | Proativo (30, 15 e 7 dias) |
| Resolução de Impasses | Usuário precisa decidir sozinho o que fazer | Sistema sugere ação judicial e orienta o fluxo |
| Saída de Dados | Consulta simples na tela | Exportação de PDF processual completo |

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Mateus Rodrigues Barreto**, responsável pela funcionalidade *Painel de monitoramento de prazos com alertas jurídicos*.
---

## Agradecimentos à IA

Agradecimento ao Gemini pela ajuda na estruturação, redação e consolidação das funcionalidades deste projeto.

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Criação da funcionalidade: Portal de Acompanhamento | Heitor Macedo Ricardo | Pedro Moretti |
| `1.1` | 01/05/2026 | Integração da funcionalidade: Sala de Conciliação Virtual | Pedro Augusto Moretti Moreira | Heloisa Silva |
| `1.1` | 01/05/2026 | Integração da funcionalidade:  Dossiê digital com OCR e validação de documentos | Heloisa Silva | Heitor Macedo |
| `1.2` | 03/05/2026 | Integração da funcionalidade: Painel de monitoramento de prazos com alertas jurídicos | Mateus Rodrigues Barreto | A definir |
