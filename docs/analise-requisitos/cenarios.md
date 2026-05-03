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

!!! info "Responsável por este artefato"
    O **Cenário 1** foi elaborado por **Heitor Macedo Ricardo**, responsável pela funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Análise de Tarefas](analise-tarefas.md).
---

## Cenário 2: Dona Ivone e a Superação da Barreira Digital

### Narrativa

Era uma noite de quinta-feira e Dona Ivone estava na cozinha de sua casa em Ceilândia, terminando de guardar a louça enquanto olhava para o balcão vazio onde deveria estar a fritadeira elétrica que comprou há dois meses em um site estrangeiro. Após semanas enfrentando o que ela descrevia como um "atendimento de tortura" — sendo transferida entre múltiplos atendentes que nunca resolviam o sumiço do produto — ela sentia que o prejuízo financeiro era inevitável. Seguindo o conselho de uma vizinha que teve um problema similar, Ivone decidiu que era hora de procurar o Procon, mas o medo de "mexer com essas coisas de internet" ainda a assombrava.

Sentada à mesa da cozinha, ela pegou seu celular com as mãos ainda levemente úmidas do trabalho doméstico. Ivone tinha uma aversão profunda a sites oficiais; para ela, as páginas do governo eram sempre "poluídas", cheias de banners que pareciam "links de vírus" ou "spam". Ao digitar "Procon" no Google, ela respirou fundo e clicou no primeiro resultado, esperando encontrar aquela confusão desorientadora de notícias e textos pequenos que sempre a faziam desistir[cite: 1]. No entanto, ao carregar o novo portal, ela não viu o caos habitual. No centro da tela, um botão grande, de cor vibrante e com excelente contraste, exibia apenas duas palavras: **"REGISTRAR RECLAMAÇÃO"**.

"Parece o botão daquele site que o povo fala, o Reclame Aqui", pensou Ivone, sentindo uma pontada de confiança por reconhecer um padrão visual amigável[cite: 1]. Ela tocou no botão. Imediatamente, todos os banners de notícias e links externos desapareceram, dando lugar a um fluxo guiado que perguntou, em letras grandes: *"Qual empresa te causou problemas?"*. Ela digitou o nome da loja e, em seguida, o sistema solicitou uma foto do comprovante. Ivone usou a própria câmera do celular, tirou uma foto da nota fiscal que estava sobre a mesa e, com mais dois toques, recebeu o aviso: *"Tudo pronto, Ivone! O Procon já recebeu seu pedido e vai falar com a empresa por você"*[cite: 1]. Ela guardou o celular com um sorriso; pela primeira vez, não precisou de um tutorial ou da ajuda dos filhos para exercer seus direitos[cite: 1].

---

### Análise dos Elementos do Cenário

Segundo **Barbosa e Silva (2021, p. 158)**, os 7 elementos obrigatórios de um cenário estão presentes na narrativa acima da seguinte forma:

- **Ambiente ou contexto:** Cozinha da residência em Ceilândia, DF, durante o período noturno. Dona Ivone utiliza um smartphone pessoal de entrada, com tela pequena e conexão Wi-Fi doméstica. O ambiente é doméstico e calmo, mas a usuária possui pressa em resolver o problema devido ao cansaço do dia de trabalho.

- **Atores:** Ivone Maria da Silva — auxiliar de limpeza de 56 anos, Persona Primária do projeto. Possui baixa fluência digital, medo crônico de interfaces poluídas (percepção de "spam") e é leiga em terminologias jurídicas[cite: 1].

- **Objetivos:** Registrar formalmente uma reclamação contra um site de e-commerce internacional por produto não entregue e obter o suporte mediador do Procon sem precisar de deslocamento físico ou auxílio técnico de terceiros[cite: 1].

- **Planejamento:** O planejamento de Ivone foi motivado pela necessidade de reaver seu dinheiro após a falha nos canais diretos da empresa[cite: 1]. Sua atividade mental consistiu em superar a desconfiança inicial em relação ao site oficial e buscar um ponto de interação óbvio que confirmasse que ela estava no caminho certo para "reclamar".

- **Ações:** (1) Acessar o portal pelo navegador do celular; (2) identificar e tocar no botão centralizado "Registrar Reclamação"; (3) digitar o nome da empresa fornecedora; (4) acionar a câmera do celular via navegador para fotografar o comprovante físico; (5) ler e confirmar a mensagem de conclusão do protocolo em linguagem simplificada[cite: 1].

- **Eventos:** (1) O sistema carrega uma interface minimalista com foco em Call to Action (CTA); (2) ao ser acionado, o sistema ativa o modo "foco", ocultando elementos distratores (notícias e avisos secundários); (3) o sistema valida os dados e gera um protocolo automático; (4) o sistema apresenta uma mensagem de encerramento amigável e em "linguagem cidadã"[cite: 1].

- **Avaliação:** Dona Ivone sente-se empoderada e aliviada. A avaliação foi positiva pois o sistema eliminou a desorientação visual típica do site antigo[cite: 1]. O uso de um padrão de design reconhecido (inspirado no Reclame Aqui) e a ausência de jargão jurídico fizeram com que ela sentisse que o Procon é, de fato, um facilitador de direitos e não uma barreira burocrática[cite: 1].

!!! info "Responsável por este artefato"
    O **Cenário 2** foi elaborado por **Pedro Augusto Macedo Del Castilo**, responsável pela funcionalidade *Botão de Reclamação Rápida* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Análise de Tarefas](analise-tarefas.md).

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
| `1.1` | 03/05/2026 | Elaboração do Cenário 2 | Pedro Macedo | A definir |
| `1.0` | 30/04/2026 | Elaboração do Cenário 1 de interação — Acompanhamento de Reclamação (Persona Laura). | Heitor Macedo Ricardo | A definir |
