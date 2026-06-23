# Relatos dos Resultados — Nível 3

## Colaboração

Colaboração referente à [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Augusto Moretti Moreira | Elaborou o Artefato |
| Heitor Macedo | Realizou a Triangulação |
| Mateus Barreto | Atualizou consolidação com novo relato |

---

## Introdução

Esta página consolida os relatos de resultados das avaliações conduzidas no **Nível 3** do processo de Design, Avaliação e Desenvolvimento. Os relatos documentam os resultados obtidos nas avaliações dos protótipos de alta fidelidade, incluindo problemas de usabilidade identificados, feedback dos participantes e planejamento de reprojeto. Trata-se de avaliação **somativa**<sup><a href="#figura1">[1]</a></sup>, conduzida sobre protótipo de alta fidelidade — representação próxima à solução final —, por meio de teste de usabilidade com observação direta e protocolo Think Aloud, com o propósito de verificar a conformidade do design com padrões de usabilidade e validar os fluxos de interação antes da entrega final.

---

## Relatos

| Documento | Autor(es) | Objeto Avaliado | Acesso |
|---|---|---|---|
| Relato — Sala de Conciliação Virtual | Pedro Augusto Moretti Moreira | Avaliação do protótipo de alta fidelidade da Sala de Conciliação Virtual | [Acessar](relato-resultados-alta-fidelidade-conciliacao-virtual.md) |
| Relato — Notificação Ativa | Heitor Macedo | Avaliação do protótipo de alta fidelidade da Notificação Ativa | [Acessar](relato-resultados-alta-fidelidade-notificacao-ativa.md) |
| Relato — Assistente de Triagem Guiada | Pedro Macedo | Avaliação do protótipo de alta fidelidade da Triagem Guiada | [Acessar](relato-resultados-alta-fidelidade-triagem-guiada.md) |
| Relato — Painel de Monitoramento de Prazos | Mateus Barreto | Avaliação do protótipo de alta fidelidade do Painel de Monitoramento de Prazos | [Acessar](relato-resultados-alta-fidelidade-painel-prazos.md) |

---

## Triangulação e Consolidação dos Resultados

Esta seção sintetiza, de forma interparticipante e entre funcionalidades, os dados coletados nas avaliações do Nível 3. O objetivo é identificar padrões, convergências e divergências que emergem da leitura conjunta dos quatro relatos — **Sala de Conciliação Virtual** (1 sessão), **Notificação Ativa** (5 sessões), **Assistente de Triagem Guiada** (1 sessão) e **Painel de Monitoramento de Prazos** (3 sessões) —, totalizando **10 sessões com 10 participantes reais**, fornecendo uma visão consolidada do estado de usabilidade do sistema proposto para o PROCON-DF.

---

### Visão Geral das Avaliações

**Tabela — Síntese das sessões de avaliação do Nível 3**

| Funcionalidade | Avaliador | Sessões | Perfis Avaliados | Período | Tarefas por Sessão | Taxa de Conclusão | Problemas (Gravidade ≥ 2) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Sala de Conciliação Virtual | Pedro Moretti | 1 (P1) | Fornecedor — empresária, 40 anos | 12/06/2026 | 3 | 100% (3/3) | 0 |
| Notificação Ativa | Heitor Macedo | 5 (P1–P5) | Consumidores — 18 a 45 anos; professor, universitária, engenheiro elétrico, orientadora educacional | 13–16/06/2026 | 1 (fluxo completo) | 100% (5/5) | 1 (P02, grav. 2) |
| Assistente de Triagem Guiada | Pedro Macedo | 1 (P1) | Consumidor — professor, 60 anos | 16/06/2026 | 1 (fluxo completo) | 100% (1/1) | 0 |
| Painel de Monitoramento de Prazos | Mateus Barreto | 3 (P1–P3) | Consumidores — estudantes universitários (19 a 20 anos) | 20–21/06/2026 | 1 (fluxo completo) | 100% (3/3) | 2 (PB2-1, PB2-2) |

<div align="center">
<p><i>Fonte: Elaborado por Pedro Augusto Moretti Moreira e Heitor Macedo.</i></p>
</div>

Somados, o Nível 3 acumula **10 sessões de avaliação**, **12 tarefas executadas** (3 na Conciliação Virtual, 5 na Notificação Ativa, 1 na Triagem Guiada e 3 no Painel de Monitoramento de Prazos). Nos testes do Painel de Monitoramento de Prazos, foram observados 2 erros cometidos (P2 e P3 confundiram o prazo de conciliação com o de prescrição) e 2 intervenções de ajuda/orientação pelo mediador, todos resolvidos com sucesso durante as sessões sem impedir a conclusão das tarefas.

---

### Convergências entre os Relatos

As avaliações das três funcionalidades, com sete participantes de perfis diversificados (18 a 60 anos; professor, empresária, engenheiro elétrico, universitária, orientadora educacional), revelaram **seis convergências expressivas**, indicando que as decisões de design centrais do sistema foram validadas de forma consistente.

**1. WhatsApp como canal de entrada — validação unânime em todos os fluxos**

O WhatsApp como ponto de entrada foi validado pelos seis participantes da Notificação Ativa e da Conciliação Virtual que interagiram com esse canal. Na Notificação Ativa, os cinco participantes avaliaram positivamente a notificação via WhatsApp — P1 afirmou que "hoje em dia a nossa vida é resumida basicamente tudo através de um celular, através do WhatsApp"; P4 (18 anos, universitária) apontou a razão comportamental mais específica: "às vezes a gente silencia os aplicativos que não interessa, né? E aí no WhatsApp a gente vai ver"; P5 resumiu como "mais viável, mais rápido". Na Triagem Guiada, o participante verbalizou espontaneamente "quero receber alertas no WhatsApp, eu acho importante" ao chegar na tela de configuração de notificações. Na Conciliação Virtual, o link de acesso à sala de audiência enviado pelo WhatsApp foi recebido sem fricção.

**2. Assinatura digital via GOV.BR e biometria — confiança e praticidade reconhecidas**

A integração com o GOV.BR e com biometria para assinatura digital foi avaliada positivamente nas funcionalidades que a incorporam. Na Conciliação Virtual, a participante afirmou que "é muito mais prático, porque você já tem essa senha muito decorada, pela vasta utilização, sem precisar imprimir, depois digitalizar, enviar, o que facilita bastante". Na Notificação Ativa, P3 destacou a redundância segura entre biometria e GOV.BR ("caso haja falha na biometria, ainda tem o SMS"); P5 acrescentou uma dimensão ainda não mencionada pelos demais: "eu acredito também na questão da segurança. Eu acho que são para te dar uma segurança." A convergência entre perfis tão distintos (empresária experiente de 40 anos e orientadora educacional de 45 anos) sobre o valor das assinaturas digitais valida a decisão de adotar múltiplos métodos.

**3. Telas de confirmação e protocolo — fricção necessária percebida como segurança**

Em todos os fluxos que contêm etapas explícitas de confirmação antes de ações definitivas, os participantes as avaliaram como úteis e necessárias — jamais como obstáculo ou excesso. Na Notificação Ativa, P5 expressou a síntese mais enfática: "ele é útil, bom, tem de ter" (sobre o pop-up de irreversibilidade). Na Conciliação Virtual, a participante relatou que o teste prévio de periféricos "fica bem claro e acho uma etapa bem importante porque às vezes entramos em uma reunião e estamos falando sem ser ouvidos". Esse padrão valida a decisão de design de não suprimir confirmações intermediárias em prol da velocidade.

**4. Taxa de conclusão de 100% em todas as tarefas — ausência de barreiras operacionais**

Todos os sete participantes concluíram 100% das tarefas propostas, com 0 erros cometidos e nível de dificuldade 1 ("Muito fácil") em todos os casos. A amostra da Notificação Ativa, com cinco participantes cobrindo faixas etárias de 18 a 45 anos e ocupações distintas, é particularmente relevante: a consistência dos resultados quantitativos ao longo de perfis variados indica que os fluxos de navegação são robustos e acessíveis, não dependendo de familiaridade técnica específica.

**5. Percepção de valor superior ao atendimento presencial**

Em todas as três funcionalidades, os participantes manifestaram espontaneamente que as soluções digitais representam uma melhoria em relação ao atendimento presencial no PROCON-DF. Na Conciliação Virtual, a participante declarou: "com certeza, isso traz uma economia de tempo, de dinheiro, gastos e tranquilidade". Na Notificação Ativa, os cinco participantes validaram unanimemente a notificação via WhatsApp como superior ao SMS ou ao push notification de aplicativo desconhecido. Na Triagem Guiada, o participante validou positivamente cada etapa do fluxo de cadastro de reclamação, confirmando que a experiência guiada e pedagógica é superior à navegação não assistida.

**6. Linguagem de suporte e explicações em texto simples — valorizadas pelos participantes**

Em duas das três funcionalidades, os participantes demonstraram atenção e valorização explícita dos textos de apoio e da linguagem cidadã. Na Notificação Ativa, P5 (45 anos, orientadora educacional) leu em voz alta o texto em linguagem simples da proposta ("em palavras simples, a loja vai devolver todo o valor que você pagou direto na sua conta em até 10 dias úteis após você aceitar"), demonstrando que o recurso cumpre seu papel. Na Triagem Guiada, o participante de 60 anos narrou com precisão o papel do PROCON: "aqui tá comunicando que ele recebe a reclamação, faz a notificação, busca um acordo entre os lados e se não houver acordo orienta para ir pro juizado especial" — evidenciando que a tela de "Painel de Linguagem Cidadã" foi assimilada.

---

### Divergências e Pontos de Atenção

**Tabela — Problemas de usabilidade consolidados do Nível 3**

| Funcionalidade | ID | Tela / Etapa | Descrição do Problema | Gravidade | Frequência | Persistência | Status |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| Notificação Ativa | P01 | Visualização da Proposta | Prazo de crédito (10 dias úteis) sem destaque visual proporcional à sua relevância na decisão do usuário | 1 — Cosmético | 1/5 participantes | Pontual | Correção planejada |
| Notificação Ativa | P02 | Tela de Resposta (Aceitar ou Recusar) | A tela não comunica as consequências da recusa da proposta, gerando hesitação sobre o que acontecerá com a reclamação caso a proposta seja rejeitada | 2 — Pequeno | 1/5 participantes | Pontual | Correção planejada |
| Sala de Conciliação Virtual | — | — | Nenhum problema identificado | — | — | — | — |
| Assistente de Triagem Guiada | P01 | Upload Guiado de Evidências (Tela 6) | Não há opção para o caso de o usuário não possuir nota fiscal ou comprovante de compra, tornando o campo de evidência implicitamente obrigatório | 1 — Cosmético | 1/1 participante | Não verificável (n=1) | Correção planejada |
| Painel de Monitoramento de Prazos | PB1-1 | Visualização de Prazos Legais | Leve hesitação ao procurar o prazo máximo para acionar a justiça. O usuário cogitou procurar na "Linha do tempo" antes de notar a "Prescrição do direito". | 1 — Cosmético | 1/3 participantes | Pontual | Correção planejada |
| Painel de Monitoramento de Prazos | PB2-1 | Visualização de Prazos Legais | Concorrência visual e ambiguidade. O usuário confundiu a "Audiência de conciliação" (15 dias) com o prazo máximo para acionar a justiça (Prescrição). | 3 — Grande | 2/3 participantes | Persistente | Correção planejada |
| Painel de Monitoramento de Prazos | PB2-2 | Orientações do Juizado Especial | Fricção no retrocesso do fluxo. O participante não entendeu como voltar ou se deveria voltar da tela de orientações do juizado. | 2 — Pequeno | 2/3 participantes | Persistente | Correção planejada |

<div align="center">
<p><i>Nota sobre a Gravidade: (1) Cosmético; (2) Pequeno; (3) Grande; (4) Catastrófico — impede o usuário de realizar a tarefa e alcançar seus objetivos.</i></p>
<p><i>Fonte: Elaborado por Pedro Augusto Moretti Moreira e Heitor Macedo.</i></p>
</div>

O Nível 3 acumula seis problemas de usabilidade mapeados em três protótipos distintos. O problema de maior gravidade (PB2-1, Gravidade 3) foi detectado no Painel de Monitoramento de Prazos, onde a proximidade visual levou P2 e P3 a confundirem o prazo administrativo de conciliação do Procon com a prescrição legal para acionamento judicial. Este protótipo também apresentou um atrito de retrocesso de fluxo (PB2-2, Gravidade 2) e uma hesitação visual de P1 em localizar a prescrição (PB1-1, Gravidade 1). O único outro problema de gravidade 2 foi encontrado na Notificação Ativa (P02), relacionado à falta de clareza das consequências de recusa de proposta. Os problemas cosméticos (Notificação Ativa P01, Triagem Guiada P01, Painel Prazos PB1-1) correspondem a detalhes de layout ou caminhos alternativos que não obstruem o fluxo principal. Ressalva-se que a Sala de Conciliação Virtual e o Assistente de Triagem Guiada contaram com apenas uma sessão cada, de modo que a ausência de maiores problemas nesses fluxos deve ser corroborada por testes complementares.

Os três tipos de problema identificados têm naturezas distintas e complementares:
- **Hierarquia visual** (NA P01): informação presente mas com baixa proeminência
- **Lacuna informacional sobre caminhos alternativos** (NA P02, TG P01): o sistema não orienta o usuário sobre o que acontece em um cenário diferente do caminho principal

Essa complementaridade sugere uma oportunidade de revisão transversal: garantir que todos os fluxos do sistema comuniquem explicitamente as consequências de ações alternativas (recusar, pular etapa, não ter comprovante), não apenas as do caminho feliz.

---

### Sugestões de Melhoria Consolidadas

**Tabela — Sugestões levantadas pelos participantes**

| ID | Funcionalidade | Sugestão | Participante | Contexto | Prioridade |
| :---: | :--- | :--- | :---: | :--- | :---: |
| S01 | Notificação Ativa | Adicionar terceira opção de assinatura digital vinculada ao cadastro próprio do portal PROCON-DF | P1 | "Uma assinatura da própria plataforma do PROCON — um cadastro que o usuário fez anteriormente poderia ser uma possibilidade" | Média — aumenta inclusão para usuários sem GOV.BR ativo ou sem biometria |
| S02 | Notificação Ativa | Adicionar e-mail como canal complementar de notificação ativa, além do WhatsApp | P2 | "Também seria uma boa opção [o e-mail]" | Baixa — WhatsApp validado como canal principal pelos 5 participantes |
| S03 | Notificação Ativa | Enviar confirmação por e-mail ou SMS ao usuário após a assinatura do acordo | P3 | "Provavelmente uma recomendação, um envio para o e-mail ou até mesmo por SMS do acordo finalizado" | Média — registra comprovante fora da plataforma e aumenta confiança |
| S04 | Assistente de Triagem Guiada | Tornar o upload de evidência opcional, adicionando caminho alternativo para quem não possui nota fiscal | P1 | "E se eu não tiver a nota fiscal? Muitas vezes a pessoa pode perder essa nota fiscal" | Alta — afeta diretamente a acessibilidade do fluxo de abertura de reclamação |
| S05 | Painel de Monitoramento de Prazos | Adicionar um subtítulo claro como "(Prazo máximo para acionar a justiça)" onde diz "Prescrição do Direito" | P1 | Dificuldade inicial de P1 em reconhecer o termo legal de prescrição na home | Média — melhora o entendimento do termo jurídico |
| S06 | Painel de Monitoramento de Prazos | Separar o bloco de "Prescrição do Direito" da "Linha do tempo" e usar UX Writing mais incisivo como "Seu Direito na Justiça (Prescrição)" | P2, P3 | Usuários P2 e P3 confundiram o prazo de audiência do Procon com o prazo legal de prescrição | Alta — corrige um erro conceitual crítico detectado no fluxo |
| S07 | Painel de Monitoramento de Prazos | Criar botão primário óbvio de retorno ("Voltar para minhas reclamações") na tela de orientações do Juizado e adicionar breadcrumbs de localização | P2, P3 | Usuários manifestaram desorientação sobre como retornar ao painel principal | Alta — remove quebra de fluxo na navegação de retrocesso |

<div align="center">
<p><i>Fonte: Elaborado por Pedro Augusto Moretti Moreira e Heitor Macedo.</i></p>
</div>

Nota-se que S04 (Triagem Guiada) tem a maior prioridade da tabela: a obrigatoriedade implícita de evidência fotográfica pode excluir do fluxo usuários sem comprovante disponível, impactando diretamente a acessibilidade funcional do portal. As sugestões S01 e S03 (Notificação Ativa) reforçam o padrão de múltiplas opções e comprovação externa que emergiu em toda a amostra do Nível 3.

---

### Respostas Consolidadas às Perguntas de Pesquisa do Nível 3

| Pergunta de Pesquisa | Evidência Consolidada |
| :--- | :--- |
| Os protótipos validaram os conceitos visuais e o comportamento das interações planejadas? | Sim — os três protótipos tiveram fluxos completos navegados sem erros por todos os 7 participantes, com feedback positivo sobre design visual e componentes em todas as sessões |
| Foram identificados problemas que impeçam ou dificultem a conclusão de tarefas? | Não — nenhum dos três problemas identificados impediu a conclusão; P02 (Notificação Ativa, gravidade 2) é o de maior impacto e afeta a qualidade da decisão, não a operabilidade |
| As soluções de design atendem às necessidades e expectativas dos usuários? | Sim — em todas as avaliações, os participantes validaram as escolhas centrais de design (WhatsApp, GOV.BR/biometria, confirmações explícitas, timelines, linguagem cidadã) |
| O usuário consegue operar os sistemas de forma autônoma e eficiente? | Sim — taxa de conclusão de 100% em todas as 8 tarefas executadas, dificuldade 1/5 em todos os casos, sem erros e com apenas 1 pedido de clarificação (P5, Notificação Ativa) |
| Foram observadas sugestões de refinamento? | Sim — 4 sugestões registradas: S01–S03 na Notificação Ativa (assinatura adicional, e-mail como canal, confirmação pós-assinatura) e S04 na Triagem Guiada (evidência opcional) |

<div align="center">
<p><i>Fonte: Elaborado por Pedro Augusto Moretti Moreira e Heitor Macedo.</i></p>
</div>

---

### Conclusão

Os resultados do Nível 3 são positivos em sua totalidade, consolidados sobre uma base de **7 sessões, 3 funcionalidades e perfis de usuário que cobrem de 18 a 60 anos**. As avaliações dos protótipos de alta fidelidade da **Sala de Conciliação Virtual**, da **Notificação Ativa** e do **Assistente de Triagem Guiada** indicam que o design proposto pela equipe está alinhado com as necessidades dos usuários do PROCON-DF — tanto do perfil Fornecedor quanto do perfil Consumidor Reclamante.

A amostra expandida da Notificação Ativa (5 participantes) produziu resultados tanto quantitativos — tempo médio de execução, desvio padrão e taxa de conclusão — quanto qualitativos, e foi decisiva para revelar o problema P02, que não teria sido identificado com apenas uma sessão. A Sala de Conciliação Virtual e o Assistente de Triagem Guiada, avaliados com n = 1, forneceram exclusivamente resultados qualitativos — identificação de problemas de interação e feedback do usuário —, conforme a distinção entre os dois tipos de resultado de teste de usabilidade descrita em Barbosa et al. (2021, Cap. 12). Os resultados positivos observados nessas sessões únicas não devem ser interpretados como certificação definitiva de conformidade, mas como indícios encorajadores que precisam ser corroborados por ao menos uma sessão adicional antes que se possa afirmar a ausência de problemas com maior confiança. Os dois problemas cosméticos e o único problema de gravidade 2 identificados na Notificação Ativa possuem correções planejadas de baixa complexidade, sem necessidade de redesenho estrutural.

As três funcionalidades apresentam direção de design promissora e podem avançar à etapa de implementação, desde que as funcionalidades com apenas uma sessão sejam submetidas a avaliações complementares para fortalecer a base empírica das conclusões.

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 12/06/2026 | Criação da página de consolidação dos relatos do Nível 3. | Pedro Augusto Moretti Moreira | Heitor Macedo |
| 1.1 | 14/06/2026 | Adição do relato de Notificação Ativa e atualização da colaboração. | Heitor Macedo | Heitor Macedo |
| 1.2 | 14/06/2026 | Adição da seção de Triangulação e Consolidação dos Resultados do Nível 3. | Heitor Macedo | Heitor Macedo |
| 1.3 | 16/06/2026 | Adição do relato do Assistente de Triagem Guiada 3. | Pedro Macedo | Heitor Macedo |
| 1.4 | 16/06/2026 | Atualização completa da seção de Triangulação e Consolidação dos Resultados: expansão para 7 sessões (5 Notificação Ativa, 1 Conciliação Virtual, 1 Triagem Guiada), atualização da tabela síntese, convergências, tabela de problemas consolidados (incluindo NA P02, gravidade 2), sugestões S02–S04 e respostas às perguntas de pesquisa. | Heitor Macedo | Heitor Macedo |
| 1.5 | 23/06/2026 | Consolidação dos resultados e relatos do Painel de Monitoramento de Prazos (expansão para 10 sessões, inclusão de PB1-1, PB2-1 e PB2-2, novas sugestões S05–S07 e atualização da análise). | Mateus Barreto | Heitor Macedo |

## Notas de Rodapé e Referências de Imagens

<div id="figura1" align="center">
  <p>Figura 1 - Definição de avaliação somativa</p>
  <a href="../../images/avaliacaosomativa.png" target="_blank"><img src="../../images/avaliacaosomativa.png" alt="Definição de avaliação somativa — Barbosa et al. (2021, Cap. 11.3, p. 251)" width="700"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, Cap. 11.3, p. 251).</p>
</div>

<div id="figura2" align="center">
  <p>Figura 2 - Tabela 12.11 — Caracterização dos métodos de avaliação de IHC</p>
  <a href="../../images/tabela1211.png" target="_blank"><img src="../../images/tabela1211.png" alt="Tabela 12.11 — Métodos de avaliação de IHC — Barbosa et al. (2021, Cap. 12, p. 308)" width="700"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, Cap. 12, p. 308).</p>
</div>
