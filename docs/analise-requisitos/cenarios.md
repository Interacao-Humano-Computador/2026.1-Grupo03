# Cenários

## Introdução

Cenários são narrativas textuais ricas em detalhes contextuais que descrevem situações concretas de uso de um sistema, envolvendo personas específicas, seus objetivos, o ambiente em que atuam e a sequência de interações que realizam. Segundo Barbosa e Silva (2021, p. 158), um cenário é uma ferramenta fundamental para explorar ideias de design antes que o sistema seja construído, pois permite avaliar se a solução proposta satisfaz as necessidades reais dos usuários ao situá-los em situações verossímeis do cotidiano. Um bom cenário deve conter sete elementos obrigatórios: **ambiente ou contexto**, **atores**, **objetivos**, **planejamento**, **ações**, **eventos** e **avaliação**.

Os cenários deste projeto foram elaborados com foco na funcionalidade de **Sala de Conciliação Virtual com Mediação Assistida**, integrando as necessidades dos perfis de consumidor e fornecedor identificados nas etapas anteriores.

---

## Cenário 1: Lucas, Gustavo e a Resolução Virtual de Conflito

### Narrativa

Era uma segunda-feira, 10h da manhã. Lucas Silva estava em seu apartamento em Taguatinga, sentado diante de seu setup de alta performance rodando Manjaro Linux. Ele havia agendado uma audiência virtual com a "Panificadora do Guará" para resolver um problema de uma encomenda de grande porte paga via Pix que nunca foi entregue corretamente. Enquanto isso, Gustavo Santos, proprietário da panificadora, estava nos fundos do seu estabelecimento. Em vez de ter que fechar a loja e se deslocar por 40 minutos até o Setor Comercial Sul, ele simplesmente lavou as mãos, abriu o notebook no escritório e clicou no link recebido via e-mail.

Ao entrarem na **Sala de Conciliação Virtual**, ambos passaram por um check‑up automático de hardware. Lucas, sempre atento a questões técnicas, ficou aliviado ao constatar que a sala rodava diretamente no navegador, sem exigir a instalação de plugins. Ele ajustou rapidamente o microfone e a câmera, observando o indicador visual de qualidade da conexão — tudo estável, áudio nítido. O mediador do PROCON-DF iniciou a sessão de vídeo. Lucas, com sua exigência técnica, ficou satisfeito ao ver uma interface limpa, sem os banners de notícias que poluíam o site antigo, e com os nomes e papéis de cada participante fixos na parte inferior da tela.

Quando chegou o momento de apresentar suas evidências, Lucas usou a opção de **compartilhar uma janela específica** — apenas o arquivo com os logs da transação e os e‑mails trocados com o suporte do e‑commerce, mantendo o restante de sua área de trabalho em privacidade. O mediador compartilhou a tela exibindo o "Termo de Acordo" em tempo real. Gustavo explicou que houve uma falha na logística de entrega devido a um problema no forno, mas propôs o estorno imediato de 100% do valor acrescido de um voucher de cortesia.

Lucas concordou. O mediador editou as cláusulas ali mesmo, na frente de ambos. Não houve necessidade de imprimir nada. Um botão azul **"Assinar com Gov.br"** apareceu para os dois. Lucas usou o leitor de digital do seu celular para autenticar a assinatura, enquanto Gustavo fez o mesmo. Em 20 minutos, a audiência foi encerrada. O sistema exibiu o status "Acordo firmado" e enviou o PDF assinado por e‑mail. Lucas voltou ao seu trabalho de desenvolvedor e Gustavo voltou para a linha de produção, sentindo que o sistema finalmente respeitava o tempo de quem produz.

---

### Análise dos Elementos do Cenário

Segundo Barbosa e Silva (2021, p. 158), os 7 elementos obrigatórios do cenário estão presentes na narrativa acima:

- **Ambiente ou contexto:** Lucas em seu home office tecnológico em Taguatinga; Gustavo no escritório de sua panificadora no Guará. Ambos conectados via internet em ambiente profissional/doméstico.
- **Atores:** Lucas Silva (Consumidor Exigente/Persona Primária) e Gustavo Santos (Microempreendedor/Persona Secundária), além do Mediador do PROCON.
- **Objetivos:** Realizar a audiência de conciliação agendada, chegar a um consenso sobre o estorno de um pagamento e formalizar o acordo com validade jurídica.
- **Planejamento:** Ambos se prepararam minutos antes, garantindo conexão estável e acesso aos documentos (comprovante Pix e relatório de entrega) para fundamentar seus argumentos durante a chamada. Lucas, in particular, planejou compartilhar apenas a janela com as evidências, preservando a privacidade de suas outras atividades.
- **Ações:** (1) Acessar o link da sala; (2) realizar teste de periféricos e verificar indicadores de qualidade; (3) expor os fatos via vídeo; (4) compartilhar seletivamente uma janela com evidências; (5) revisar o termo de acordo editado ao vivo; (6) realizar a assinatura digital via Gov.br.
- **Eventos:** (1) O sistema valida a entrada das partes; (2) a plataforma gerencia o fluxo de áudio/vídeo e exibe os indicadores de conexão; (3) o sistema permite o compartilhamento seletivo de tela; (4) o sistema integra o serviço de assinatura eletrônica do Governo Federal; (5) o sistema encerra o protocolo e envia o PDF assinado para os e‑mails.
- **Avaliação:** Lucas sentiu que a interface moderna, a possibilidade de compartilhar apenas uma janela e a estabilidade da transmissão condizem com sua expectativa de eficiência técnica e respeito à privacidade. Gustavo avaliou a experiência como essencial para sua rotina, permitindo resolver pendências jurídicas sem abandonar a gestão física de seu negócio.

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Pedro Augusto Moretti Moreira**, responsável pela [Funcionalidade](funcionalidades.md#2-sala-de-conciliacao-virtual-com-mediacao-assistida), pela técnica de [Perfil de Usuário](perfil-usuario.md#entrevistas-fornecedores), pelas [Personas](personas.md#22-persona-primaria-lucas-o-consumidor-exigente), pelos [Cenários](cenarios.md#cenario-1-lucas-gustavo-e-a-resolucao-virtual-de-conflito) e pela [Análise de Tarefas](analise-tarefas.md#1-analise-hierarquica-de-tarefas-hta).

---

## Cenário 2: Laura e a Conciliação Mobile-First no Intervalo da Aula

### Narrativa

Era uma terça-feira agitada na Universidade de Brasília (UnB). Eram 15h45, e Laura Mendes tinha exatos 15 minutos de intervalo antes de sua próxima aula. Ela precisava resolver uma cobrança indevida de R$ 89,90 que vinha recebendo de sua operadora de telefonia. Caminhando pelos corredores barulhentos do ICC Norte, ela procurou um canto com melhor sinal de rede móvel, colocou seus fones de ouvido para abafar o barulho dos estudantes e aguardou.

No horário agendado, Laura recebeu uma notificação no WhatsApp com um link de acesso direto do PROCON-DF. Com um único toque, sem precisar de senhas complexas ou logins demorados, ela entrou na Sala de Conciliação Virtual. O navegador pediu permissão para usar a câmera e o microfone, que ela concedeu rapidamente. O sistema ajustou perfeitamente a transmissão de vídeo para o modo retrato do seu smartphone.

Na sala, o mediador do PROCON e o representante da operadora já a aguardavam. A conversa foi direta: a operadora reconheceu o erro e ofereceu o estorno imediato do valor nas próximas faturas. Laura escutou atentamente a proposta. O mediador redigiu o termo de acordo e o compartilhou na tela. A interface mobile destacou de forma clara os pontos essenciais do documento, sem letras miúdas ou jargões jurídicos confusos. 

Com a orientação do mediador, que destacou o botão de ação principal na interface de Laura, ela tocou em "Assinar Acordo" e confirmou a assinatura usando a biometria facial do próprio celular. Em menos de 10 minutos, o problema estava resolvido. O sistema enviou imediatamente o comprovante em PDF para o seu WhatsApp. Laura sentiu-se empoderada e aliviada por ter resolvido tudo de forma fluida, a tempo de entrar tranquilamente na sua próxima aula de Administração.

---

### Análise dos Elementos do Cenário

Segundo **Barbosa e Silva (2021, p. 158)**, os 7 elementos obrigatórios de um cenário estão presentes na narrativa acima da seguinte forma:

- **Ambiente ou contexto:** Corredor movimentado e ruidoso do ICC Norte na UnB, durante um breve intervalo entre aulas, às 15h45 de uma terça-feira. A usuária está conectada via smartphone pessoal utilizando rede móvel 4G/5G.
- **Atores:** Laura Mendes (estudante universitária e Persona Primária), o Mediador do PROCON-DF e o Representante da Operadora de telefonia.
- **Objetivos:** Participar de uma audiência de conciliação para resolver uma cobrança indevida de R$ 89,90 de forma rápida, sem necessidade de logins complexos, e formalizar o acordo a tempo de comparecer à próxima aula.
- **Planejamento:** Laura planejou utilizar seus 15 minutos de intervalo acadêmico. Para isso, deslocou-se para um local com melhor sinal e utilizou fones de ouvido para isolar o ruído externo do ambiente universitário.
- **Ações:** (1) Tocar na notificação do link recebido via WhatsApp; (2) conceder permissões de câmera e microfone no navegador mobile; (3) escutar a proposta na videoconferência; (4) ler o resumo do termo de acordo na tela; (5) tocar em "Assinar Acordo" e autenticar a assinatura via biometria facial.
- **Eventos:** (1) O sistema envia automaticamente o link de ingresso pelo WhatsApp; (2) a plataforma adapta a interface de vídeo e visualização de documentos para o modo retrato (mobile-first); (3) o mediador utiliza recursos do sistema para destacar o botão de ação para Laura; (4) o sistema processa a biometria e envia o comprovante de resolução pelo WhatsApp.
- **Avaliação:** Laura sentiu-se empoderada pela eficiência do processo. A ausência de burocracia e de jargões inacessíveis, aliada à fluidez de uma interface otimizada para smartphones, permitiu a resolução de um conflito jurídico de forma rápida, respeitando sua rotina acadêmica.

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Heitor Macedo Ricardo**, responsável pela [Funcionalidade](funcionalidades.md#1-portal-de-acompanhamento-de-reclamacoes-com-notificacoes-ativas), pela técnica de [Perfil de Usuário](perfil-usuario.md#entrevista-consumidor), pelas [Personas](personas.md#21-persona-primaria-laura-a-universitaria-pratica), pelo [Cenário](cenarios.md#cenario-2-laura-e-a-conciliacao-mobile-first-no-intervalo-da-aula) e pela [Análise de Tarefas](analise-tarefas.md#1-analise-hierarquica-de-tarefas-hta).

---

## Cenário 3: Gustavo e o Gerenciamento de Acordos Pós-Conciliação

### Contexto e Ambiente

| Elemento | Descrição |
| :--- | :--- |
| **Ambiente** | Escritório administrativo da Panificadora. |
| **Data/Horário** | Fim do expediente, às 18h30. |
| **Dispositivo** | Computador Desktop (Monitor Philco). |
| **Pré-condições** | Audiência finalizada com sucesso minutos antes. |

### Atores

- **Ator Principal:** Gustavo Santos — Microempreendedor (Persona Secundária).

### Objetivos

- **Objetivo Final:** Arquivar o termo de acordo e programar o estorno financeiro.
- **Objetivos Intermediários:**
    - Fazer o download do termo assinado.
    - Verificar no dashboard se a pendência foi marcada como "Resolvida".

### Planejamento

> Gustavo decidiu organizar a papelada digital antes de fechar a loja. Ele quer garantir que a reclamação não conste mais como ativa no seu CNPJ.

### Sequência de Ações

1. Acessar o "Portal do Fornecedor" no site do PROCON-DF.
2. Filtrar por "Processos Concluídos".
3. Localizar o caso de Lucas Silva.
4. Baixar o arquivo PDF com as assinaturas digitais acopladas.

### Eventos

- O Dashboard atualiza o status do fornecedor em tempo real.
- O sistema gera um log de conformidade que Gustavo pode usar para seu controle contábil.

### Avaliação

> Gustavo sente que o portal agora é uma ferramenta de gestão útil, e não apenas um site de reclamações contra de ele. A clareza das informações reduz sua ansiedade administrativa.

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Pedro Augusto Moretti Moreira**, responsável pela [Funcionalidade](funcionalidades.md#2-sala-de-conciliacao-virtual-com-mediacao-assistida), pela técnica de [Perfil de Usuário](perfil-usuario.md#entrevistas-fornecedores), pelas [Personas](personas.md#22-persona-primaria-lucas-o-consumidor-exigente), pelos [Cenários](cenarios.md#cenario-1-lucas-gustavo-e-a-resolucao-virtual-de-conflito) e pela [Análise de Tarefas](analise-tarefas.md#1-analise-hierarquica-de-tarefas-hta).

---

## Cenário 4: Maria Helena e a Reclamação com OCR

### Contexto e Ambiente

| Elemento | Descrição |
| :--- | :--- |
| **Ambiente** | Sala de estar da residência de Maria Helena, em Ceilândia, após o almoço. |
| **Data/Horário** | Sexta-feira, às 14h20. |
| **Dispositivo** | Smartphone Android com internet móvel. |
| **Pré-condições** | Maria Helena recebeu uma cobrança indevida da operadora de telefonia e decidiu abrir uma reclamação no PROCON-DF anexando a fatura e o comprovante de pagamento. |

### Atores

- **Ator Principal:** Maria Helena Costa — Aposentada e consumidora com baixa familiaridade digital.
- **Ator Secundário:** Sistema do PROCON-DF, que orienta o preenchimento e registra o protocolo.

### Objetivos

- **Objetivo Final:** Registrar a reclamação, anexar os documentos e acompanhar o andamento sem precisar ir a uma unidade física.
- **Objetivos Intermediários:**
    - Encontrar rapidamente o botão de abertura de reclamação.
    - Preencher apenas as informações essenciais, sem linguagem jurídica complexa.
    - Receber confirmação clara de que o protocolo foi gerado com sucesso.

### Planejamento

> Maria Helena separou a fatura, o comprovante de pagamento e deixou o celular carregado ao lado. Como não tem muita prática com sistemas governamentais, ela quer concluir tudo em poucos passos e com instruções simples, sem precisar entender termos técnicos.

### Sequência de Ações

1. Abrir o site do PROCON-DF pelo navegador do celular.
2. Tocar no botão de reclamação visível na página inicial.
3. Preencher os dados básicos do caso e anexar a fatura em PDF.
4. O sistema aplica OCR no arquivo, identifica informações como número da conta e valores cobrados, e verifica se o documento está legível.
5. Caso o comprovante esteja incompleto ou ilegível, o portal informa imediatamente o que precisa ser reenviado.
6. Ler a confirmação final com o número do protocolo.
7. Receber aviso de acompanhamento por mensagem.

### Eventos

- O sistema apresenta botões grandes e textos curtos para facilitar a leitura.
- A plataforma informa quais documentos são aceitos antes do envio.
- O OCR lê automaticamente os dados da fatura e valida se o documento está legível e relacionado à reclamação.
- O protocolo é gerado imediatamente quando o arquivo é aceito, e Maria Helena já sai com a primeira orientação sobre os próximos passos.

### Avaliação

> Maria Helena sente que conseguiu resolver um problema que parecia difícil sem depender de ajuda externa. A linguagem simples, a leitura automática por OCR e a confirmação imediata reduzem a insegurança, evitam retrabalho e diminuem o tempo de espera para o andamento do processo.

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Heloisa Laura Santos da Silva**, responsável pela [Funcionalidade](funcionalidades.md#3-validacao-de-documentos-com-ocr), pela técnica de [Perfil de Usuário](perfil-usuario.md#analise-de-documentos), pela [Persona](personas.md#24-persona-primaria-maria-helena-a-aposentada-pratica), pelo [Cenário](cenarios.md#cenario-4-maria-helena-e-a-reclamacao-com-ocr) e pela [Análise de Tarefas](analise-tarefas.md#1-analise-hierarquica-de-tarefas-hta).

---

## Cenário 5: Roberto e a Eficiência na Resolução

### Contexto e Ambiente

| Elemento | Descrição |
| :--- | :--- |
| **Ambiente** | Escritório da distribuidora onde Roberto trabalha. |
| **Data/Horário** | Segunda-feira, às 09h15. |
| **Dispositivo** | Computador Desktop (Windows). |
| **Pré-condições** | Roberto identificou uma cobrança indevida de seguro no cartão e possui o PDF da fatura. |

### Atores

- **Ator Principal:** Roberto Oliveira — Gerente de Logística (Persona Primária).
- **Ator Secundário:** Sistema do PROCON-DF.

### Objetivos

- **Objetivo Final:** Registrar a contestação da cobrança e obter um comprovante formal com prazo de resposta.
- **Objetivos Intermediários:**
    - Localizar a área de "Assuntos Financeiros".
    - Anexar a fatura do cartão como evidência.
    - Exportar o protocolo em PDF para seu controle pessoal.

### Planejamento

> Roberto reservou o início da manhã para resolver essa pendência. Ele quer um processo rápido e que transmita seriedade, preferindo usar o computador para anexar os arquivos com precisão.

### Sequência de Ações

1. Roberto acessa o portal do PROCON-DF pelo computador.
2. Seleciona a opção de nova reclamação e escolhe a categoria "Assuntos Financeiros".
3. Preenche o formulário detalhando as tentativas de contato prévio com o banco.
4. Faz o upload da fatura do cartão de crédito (PDF).
5. Revisa os dados e clica em "Finalizar Protocolo".
6. O sistema o redireciona para o **Painel de Monitoramento de Prazos**, onde ele visualiza o número do processo e a contagem regressiva para a resposta da empresa.
7. Roberto utiliza a opção "Exportar Dossiê Jurídico" para salvar um resumo em PDF em sua pasta de "Finanças Pessoais".

### Eventos

- O sistema valida o arquivo PDF e confirma o recebimento.
- O portal exibe um cronômetro visual indicando o prazo legal para a resposta da empresa.
- Um e-mail de confirmação é enviado automaticamente para o endereço de Roberto.

### Avaliação

> Roberto sente que o tempo foi bem investido. A interface profissional e a entrega imediata do protocolo em PDF deram a ele a segurança de que o banco agora será obrigado a responder dentro do prazo visível na tela.

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Mateus Rodrigues Barreto**, responsável pela [Funcionalidade](funcionalidades.md#4-painel-de-monitoramento-de-prazos-com-alertas-juridicos), pela [Persona](personas.md#25-persona-primaria-roberto-o-pragmatico), pelo [Cenário](cenarios.md#cenario-5-roberto-e-a-eficiencia-na-resolucao) e pela [Análise de Tarefas](analise-tarefas.md#3-goms-goals-operators-methods-and-selection-rules).

---

## Cenário 6: Dona Ivone e a Superação da Barreira Digital

### Narrativa

Era uma noite de quinta-feira e Dona Ivone estava na cozinha de sua casa em Ceilândia, terminando de guardar a louça enquanto olhava para o balcão vazio onde deveria estar a fritadeira elétrica que comprou há dois meses em um site estrangeiro. Após semanas enfrentando o que ela descrevia como um "atendimento de tortura" — sendo transferida entre múltiplos atendentes que nunca resolviam o sumiço do produto — ela sentia que o prejuízo financeiro era inevitável. Seguindo o conselho de uma vizinha que teve um problema similar, Ivone decidiu que era hora de procurar o Procon, mas o medo de "mexer com essas coisas de internet" ainda a assombrava.

Sentada à mesa da cozinha, ela pegou seu celular com as mãos ainda levemente úmidas do trabalho doméstico. Ivone tinha uma aversão profunda a sites oficiais; para ela, as páginas do governo eram sempre "poluídas", cheias de banners que pareciam "links de vírus" ou "spam". Ao digitar "Procon" no Google, ela respirou fundo e clicou no primeiro resultado, esperando encontrar aquela confusão desorientadora de notícias e textos pequenos que sempre a faziam desistir. No entanto, ao carregar o novo portal, ela não viu o caos habitual. No centro da tela, um botão grande, de cor vibrante e com excelente contraste, exibia apenas duas palavras: **"REGISTRAR RECLAMAÇÃO"**.

"Parece o botão daquele site que o povo fala, o Reclame Aqui", pensou Ivone, sentindo uma pontada de confiança por reconhecer um padrão visual amigável. Ela tocou no botão. Imediatamente, todos os banners de notícias e links externos desapareceram, dando lugar a um fluxo guiado que perguntou, em letras grandes: *"Qual empresa te causou problemas?"*. Ela digitou o nome da loja e, em seguida, o sistema solicitou uma foto do comprovante. Ivone usou a própria câmera do celular, tirou uma foto da nota fiscal que estava sobre a mesa e, com mais dois toques, recebeu o aviso: *"Tudo pronto, Ivone! O Procon já recebeu seu pedido e vai falar com a empresa por você"*. Ela guardou o celular com um sorriso; pela primeira vez, não precisou de um tutorial ou da ajuda dos filhos para exercer seus direitos.

---

### Análise dos Elementos do Cenário

Segundo **Barbosa e Silva (2021, p. 158)**, os 7 elementos obrigatórios de um cenário estão presentes na narrativa acima da seguinte forma:

- **Ambiente ou contexto:** Cozinha da residência em Ceilândia, DF, durante o período noturno. Dona Ivone utiliza um smartphone pessoal de entrada, com tela pequena e conexão Wi-Fi doméstica. O ambiente é doméstico e calmo, mas a usuária possui pressa em resolver o problema devido ao cansaço do dia de trabalho.

- **Atores:** Ivone Maria da Silva — auxiliar de limpeza de 56 anos, Persona Primária do projeto. Possui baixa fluência digital, medo crônico de interfaces poluídas (percepção de "spam") e é leiga em terminologias jurídicas.

- **Objetivos:** Registrar formalmente uma reclamação contra um site de e-commerce internacional por produto não entregue e obter o suporte mediador do Procon sem precisar de deslocamento físico ou auxílio técnico de terceiros.

- **Planejamento:** O planejamento de Ivone foi motivado pela necessidade de reaver seu dinheiro após a falha nos canais diretos da empresa. Sua atividade mental consistiu em superar a desconfiança inicial em relação ao site oficial e buscar um ponto de interação óbvio que confirmasse que ela estava no caminho certo para "reclamar".

- **Ações:** (1) Acessar o portal pelo navegador do celular; (2) identificar e tocar no botão centralizado "Registrar Reclamação"; (3) digitar o nome da empresa fornecedora; (4) acionar a câmera do celular via navegador para fotografar o comprovante físico; (5) ler e confirmar a mensagem de conclusão do protocolo em linguagem simplificada.

- **Eventos:** (1) O sistema carrega uma interface minimalista com foco em Call to Action (CTA); (2) ao ser acionado, o sistema ativa o modo "foco", ocultando elementos distratores (notícias e avisos secundários); (3) o sistema valida os dados e gera um protocolo automático; (4) o sistema apresenta uma mensagem de encerramento amigável e em "linguagem cidadã".

- **Avaliação:** Dona Ivone sente-se empoderada e aliviada. A avaliação foi positiva pois o sistema eliminou a desorientação visual típica do site antigo. O uso de um padrão de design reconhecido (inspirado no Reclame Aqui) e a ausência de jargão jurídico fizeram com que ela sentisse que o Procon é, de fato, um facilitador de direitos e não uma barreira burocrática.

!!! info "Responsável por este artefato"
    Este trecho foi elaborado por **Pedro Augusto Macedo Del Castilo**, responsável pela [Funcionalidade](funcionalidades.md#5-assistente-de-triagem-guiada-para-reclamacoes), pela [Persona](personas.md#23-persona-primaria-ivone-a-iniciante-vulneravel) e pelo [Cenário](cenarios.md#cenario-6-dona-ivone-e-a-superacao-da-barreira-digital).

---

## Material de Apoio

| Documento                                    | Link                                                                                                                                                      |
| :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📃 Termo de Consentimento (TCLE)             | [Abrir TCLE](../atas/TCLE.pdf){: target="\_blank" }                                                                       |                                                                                                                            |
| 📃 Roteiro de Validação dos Cenários 1 e 3     | [Abrir Roteiro](./images/roteiro_validacao_cenarios_moretti.pdf){: target="\_blank" }                                                                       |
| 📊 Relatório de Validação dos Cenários 1 e 3     | [Abrir Relatório](./images/relatorio_validacao_cenarios_Moretti.pdf){: target="\_blank" }                                                                       |
| 🎥 Gravação da Validação dos Cenários 1 e 3                 | [🔗 Assistir no YouTube](https://youtu.be/zkf6aAAHtmg){: target="\_blank" }                                                                               |

---

## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação, redação e detalhamento contextualmente rico dos cenários de interação, garantindo que as dores de Lucas, Laura e Gustavo fossem endereçadas.

---

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Elaboração do Cenário 1 (Persona Laura). | Heitor Macedo Ricardo | Pedro Augusto Moretti |
| `1.1` | 01/05/2026 | Reestruturação completa focada na Sala de Conciliação Virtual e inclusão das personas Lucas e Gustavo. | Pedro Augusto Moretti Moreira | Heloisa Silva |
| `1.2` | 03/05/2026 | Adição do Cenário 4 com Maria Helena. | Heloisa Silva | Heitor Macedo |
| `1.3` | 03/05/2026 | Adição do Cenário 5 com Roberto. | Mateus Rodrigues Barreto | Pedro Augusto Moretti |
| `1.4` | 03/05/2026 | Adição do Cenário 6 com Ivone. | Pedro Macedo | Pedro Augusto Moretti |
| `1.5` | 03/05/2026 | Padronização do Cenário 2 (Laura) para o formato narrativo e estrutural (Barbosa e Silva, 2021). | Heitor Macedo Ricardo | Pedro Augusto Moretti |
| `1.6` | 08/05/2026 | Padronização dos blocos de responsabilidade com hiperlinks de rastreabilidade entre artefatos. | Heitor Macedo Ricardo | Heloisa Silva |

