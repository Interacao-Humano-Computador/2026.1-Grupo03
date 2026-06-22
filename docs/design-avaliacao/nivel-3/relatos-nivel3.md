# Relatos dos Resultados — Nível 3

## Colaboração

Colaboração referente à [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Augusto Moretti Moreira | Elaborou o Artefato |
| Heitor Macedo | Realizou a Triangulação |

---

## Introdução

Esta página consolida os relatos de resultados das avaliações conduzidas no **Nível 3** do processo de Design, Avaliação e Desenvolvimento. Os relatos documentam os resultados obtidos nas avaliações dos protótipos de alta fidelidade, incluindo problemas de usabilidade identificados, feedback dos participantes e planejamento de reprojeto.

---

## Relatos

| Documento | Autor(es) | Objeto Avaliado | Acesso |
|---|---|---|---|
| Relato — Sala de Conciliação Virtual | Pedro Augusto Moretti Moreira | Avaliação do protótipo de alta fidelidade da Sala de Conciliação Virtual | [Acessar](relato-resultados-alta-fidelidade-conciliacao-virtual.md) |
| Relato — Notificação Ativa | Heitor Macedo | Avaliação do protótipo de alta fidelidade da Notificação Ativa | [Acessar](relato-resultados-alta-fidelidade-notificacao-ativa.md) |
| Relato — Assistente de Triagem Guiada | Pedro Macedo | Avaliação do protótipo de alta fidelidade da Notificação Ativa | [Acessar](relato-resultados-alta-fidelidade-triagem-guiada.md) |

---

## Triangulação e Consolidação dos Resultados

Esta seção sintetiza, de forma interparticipante e entre funcionalidades, os dados coletados nas avaliações do Nível 3. O objetivo é identificar padrões, convergências e divergências que emergem da leitura conjunta dos três relatos — **Sala de Conciliação Virtual** (1 sessão), **Notificação Ativa** (5 sessões) e **Assistente de Triagem Guiada** (1 sessão) —, totalizando **7 sessões com 7 participantes reais**, fornecendo uma visão consolidada do estado de usabilidade do sistema proposto para o PROCON-DF.

---

### Visão Geral das Avaliações

**Tabela — Síntese das sessões de avaliação do Nível 3**

| Funcionalidade | Avaliador | Sessões | Perfis Avaliados | Período | Tarefas por Sessão | Taxa de Conclusão | Problemas (Gravidade ≥ 2) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Sala de Conciliação Virtual | Pedro Moretti | 1 (P1) | Fornecedor — empresária, 40 anos | 12/06/2026 | 3 | 100% (3/3) | 0 |
| Notificação Ativa | Heitor Macedo | 5 (P1–P5) | Consumidores — 18 a 45 anos; professor, universitária, engenheiro elétrico, orientadora educacional | 13–16/06/2026 | 1 (fluxo completo) | 100% (5/5) | 1 (P02, grav. 2) |
| Assistente de Triagem Guiada | Pedro Macedo | 1 (P1) | Consumidor — professor, 60 anos | 16/06/2026 | 1 (fluxo completo) | 100% (1/1) | 0 |

<div align="center">
<p><i>Fonte: Elaborado por Pedro Augusto Moretti Moreira e Heitor Macedo.</i></p>
</div>

Somados, o Nível 3 acumula **7 sessões de avaliação**, **8 tarefas executadas** (3 na Conciliação Virtual, 5 na Notificação Ativa e 1 na Triagem Guiada) e **0 erros cometidos** por qualquer participante. Apenas P5 (Notificação Ativa) pediu ajuda ao avaliador — uma vez, sobre uma dúvida conceitual do fluxo —, sem impacto na conclusão da tarefa.

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

| Funcionalidade | ID | Tela / Etapa | Descrição do Problema | Gravidade | Frequência | Status |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: |
| Notificação Ativa | P01 | Visualização da Proposta | Prazo de crédito (10 dias úteis) sem destaque visual proporcional à sua relevância na decisão do usuário | 1 — Cosmético | 1/5 participantes | Correção planejada |
| Notificação Ativa | P02 | Tela de Resposta (Aceitar ou Recusar) | A tela não comunica as consequências da recusa da proposta, gerando hesitação sobre o que acontecerá com a reclamação caso a proposta seja rejeitada | 2 — Pequeno | 1/5 participantes | Correção planejada |
| Sala de Conciliação Virtual | — | — | Nenhum problema identificado | — | — | — |
| Assistente de Triagem Guiada | P01 | Upload Guiado de Evidências (Tela 6) | Não há opção para o caso de o usuário não possuir nota fiscal ou comprovante de compra, tornando o campo de evidência implicitamente obrigatório | 1 — Cosmético | 1/1 participante | Correção planejada |

<div align="center">
<p><i>Nota sobre a Gravidade: (1) Cosmético; (2) Pequeno; (3) Grande; (4) Catastrófico.</i></p>
<p><i>Fonte: Elaborado por Pedro Augusto Moretti Moreira e Heitor Macedo.</i></p>
</div>

O Nível 3 acumula três problemas identificados em dois protótipos distintos. O único problema de gravidade 2 (Pequeno) foi encontrado na Notificação Ativa (P02): a tela de resposta comunica claramente as consequências do aceite, mas omite as do rejeite — uma assimetria informacional que pode induzir viés decisório em usuários que não conhecem seus direitos pós-recusa. Os dois problemas cosméticos (NA P01, TG P01) correspondem a lacunas de visibilidade de informação (prazo de crédito) e de cobertura de caminho alternativo (ausência de evidência), nenhum dos quais impede a conclusão da tarefa. Ressalva-se que a Sala de Conciliação Virtual e o Assistente de Triagem Guiada contaram com apenas uma sessão cada; portanto, não foram identificados problemas nessas funcionalidades, mas a amostra reduzida recomenda cautela — sessões adicionais poderiam revelar obstáculos não observados na avaliação singular.

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

A amostra expandida da Notificação Ativa (5 participantes) foi decisiva para revelar o problema P02 — que não teria sido identificado com apenas 1 sessão —, demonstrando o valor de múltiplas sessões de teste para funcionalidades de decisão crítica. Essa constatação impõe uma ressalva importante para as funcionalidades avaliadas com apenas uma sessão (Conciliação Virtual e Triagem Guiada): os resultados positivos observados em suas sessões únicas não devem ser interpretados como certificação definitiva de conformidade, mas como indícios encorajadores que precisam ser corroborados por ao menos uma sessão adicional antes que se possa afirmar a ausência de problemas com maior confiança. Os dois problemas cosméticos e o único problema de gravidade 2 identificados na Notificação Ativa possuem correções planejadas de baixa complexidade, sem necessidade de redesenho estrutural.

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
