# Cenários

## Introdução

Cenários são narrativas textuais ricas em detalhes contextuais que descrevem situações concretas de uso de um sistema, envolvendo personas específicas, seus objetivos, o ambiente em que atuam e a sequência de interações que realizam. Segundo Barbosa e Silva (2021, p. 158), um cenário é uma ferramenta fundamental para explorar ideias de design antes que o sistema seja construído, pois permite avaliar se a solução proposta satisfaz as necessidades reais dos usuários ao situá-los em situações verossímeis do cotidiano. Um bom cenário deve conter sete elementos obrigatórios: **ambiente ou contexto**, **atores**, **objetivos**, **planejamento**, **ações**, **eventos** e **avaliação**.

Os cenários deste projeto foram elaborados com base na Persona Primária **Laura** e na funcionalidade central da Etapa 2: o **Portal de Acompanhamento de Reclamações com Notificações Ativas**. Ao todo, foram produzidos **2 cenários**: o Cenário 1 modela o uso da funcionalidade de notificação proativa por Laura, e o Cenário 2 permanece como esqueleto a ser preenchido.

---

## Cenário 1: Laura e a Notificação de Andamento do Processo

### Narrativa

Era uma terça-feira à tarde quando Laura, sentada no banco de um corredor da Universidade de Brasília esperando o intervalo acabar, desbloqueou o celular distraidamente para ver as notificações. Entre as atualizações das redes sociais, havia uma mensagem no WhatsApp com o remetente identificado como "PROCON-DF": *"Olá, Laura! A empresa Telecom Express respondeu à sua reclamação (Protocolo #2026-48321). Toque aqui para ver a proposta dela e nos dizer o que você decide."*

Laura coçou a cabeça — ela havia aberto a reclamação havia quase três semanas e, desde então, não tinha mais entrado no site do PROCON porque era trabalhoso demais ficar tentando lembrar a senha e caçar onde ficava a opção de acompanhamento. Aliviada por não ter que fazer isso desta vez, ela tocou no link da mensagem. O navegador abriu um painel limpo e direto, que mostrava a linha do tempo do processo dela: *Reclamação registrada* → *Empresa notificada* → *Empresa respondeu* (marcado em verde, com a data de hoje) → *Aguardando sua decisão* → *Encerramento*. Abaixo da linha do tempo, um resumo em linguagem simples descrevia o que a empresa propôs — devolver os R$ 89,90 cobrados indevidamente e cancelar a cobrança futura — sem uma única palavra jurídica que ela não soubesse o que significava.

Laura leu o resumo duas vezes. Entendeu na primeira, releu só para ter certeza. O sistema apresentava dois botões evidentes: *"Aceitar a proposta"* e *"Recusar e continuar o processo"*. Ela tocou em *"Aceitar"*, confirmou sua decisão na tela seguinte e recebeu imediatamente uma mensagem de confirmação, também pelo WhatsApp: *"Decisão registrada! O PROCON-DF vai comunicar a empresa. Em até 5 dias úteis, a operadora deverá realizar o estorno."* Todo o processo, do momento em que tocou na notificação até a confirmação, levou menos de três minutos.

Ela guardou o celular satisfeita. Não tinha precisado logar em nada com senha, não tinha precisado ler um PDF de legislação, não tinha precisado ligar para nenhum número de atendimento. O processo tinha funcionado — e o mais surpreendente para Laura foi ter descoberto apenas por causa de uma mensagem que o sistema enviou para ela, sem que ela tivesse que correr atrás.

---

### Análise dos Elementos do Cenário

Segundo Barbosa e Silva (2021, p. 158), os 7 elementos obrigatórios de um cenário estão presentes na narrativa acima da seguinte forma:

- **Ambiente ou contexto:** Corredor da Universidade de Brasília, durante o intervalo de uma tarde de terça-feira. Laura usa seu smartphone pessoal com conexão de dados móveis. O contexto é informal, com pouco tempo disponível e baixa concentração — típico de uso mobile em trânsito.

- **Atores:** Laura Mendes — jovem universitária de 22 anos, Persona Primária do projeto. Alta fluência tecnológica, leiga em Direito do Consumidor, foco exclusivo no smartphone, aversão a processos longos e burocráticos.

- **Objetivos:** Verificar o andamento da reclamação aberta contra a operadora de telefonia (Telecom Express) pelo valor cobrado indevidamente, e registrar sua decisão sobre a proposta da empresa — resolvendo o caso de forma definitiva sem sair do celular.

- **Planejamento:** Laura não havia planejado acessar o sistema naquele momento; a ação foi desencadeada pela notificação proativa recebida via WhatsApp. Sua atividade mental consistiu em avaliar a proposta da empresa, comparar com o que ela esperava receber, e decidir se o acordo era satisfatório — tudo dentro do painel, sem precisar de fontes externas.

- **Ações:** (1) Receber e ler a notificação no WhatsApp; (2) tocar no link da mensagem; (3) visualizar a linha do tempo do processo; (4) ler o resumo da proposta da empresa em linguagem simples; (5) selecionar a opção "Aceitar a proposta"; (6) confirmar a decisão na tela seguinte; (7) ler a mensagem de confirmação enviada pelo sistema.

- **Eventos:** (1) O sistema detecta que a empresa respondeu à reclamação e dispara automaticamente a notificação via WhatsApp; (2) o sistema serve o painel de acompanhamento no link acessado, renderizando a linha do tempo e o resumo da proposta em linguagem simples; (3) ao registrar a decisão de Laura, o sistema confirma o aceite e envia notificação de confirmação pelo WhatsApp; (4) o sistema registra o compromisso de estorno e comunica a empresa.

- **Avaliação:** Laura sente-se aliviada e surpreendida positivamente com a eficiência do processo. A experiência superou sua expectativa porque ela *não precisou agir proativamente*: foi o sistema que a avisou, guiou e confirmou cada etapa. A ausência de jargão jurídico, a interface de linha do tempo e a fluidez mobile eliminaram as barreiras que normalmente a afastariam de um sistema governamental.

> **Responsável por este artefato:** O **Cenário 1** foi elaborado por **Heitor Macedo Ricardo**, responsável pela funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade, que inclui também a [Funcionalidade](funcionalidades.md), o [Perfil de Usuário](perfil-usuario.md), as [Personas](personas.md) e a [Análise de Tarefas](analise-tarefas.md).
---

## Cenário 2 — [Título Descritivo do Cenário]

### Contexto e Ambiente

| Elemento | Descrição |
| :--- | :--- |
| **Ambiente** | [Ex: ...] |
| **Data/Horário** | [Ex: ...] |
| **Dispositivo** | [Ex: ...] |
| **Pré-condições** | [Ex: ...] |

### Atores

- **Ator Principal:** [Nome da Persona] — [papel]
- **Ator Secundário:** [Se houver]

### Objetivos

- **Objetivo Final:** [...]
- **Objetivos Intermediários:**
    - [...]
    - [...]

### Planejamento

> [...]

### Sequência de Ações

1. [...]
2. [...]
3. [...]

### Eventos

- [...]
- [...]

### Avaliação

> [...]

---

## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação e redação dos cenários de interação deste documento.

---

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Elaboração do Cenário 1 de interação — Acompanhamento de Reclamação (Persona Laura). | Heitor Macedo Ricardo | A definir |
