# Relatos dos Resultados — Nível 2

## Colaboração

Colaboração referente à [Etapa 5](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Moretti | Elaborou o Artefato |
| Heitor Macedo | Realizou a triangulação |
| Mateus Barreto | Atualizou consolidação com novo relato |

---

## Introdução

Esta página consolida os relatos de resultados das avaliações conduzidas no **Nível 2** do processo de Design, Avaliação e Desenvolvimento. Os relatos documentam os resultados obtidos nas avaliações dos protótipos de papel, incluindo problemas de usabilidade identificados, feedback dos participantes e planejamento de reprojeto.

---

## Relatos

| Documento | Autor(es) | Objeto Avaliado | Acesso |
|---|---|---|---|
| Relato — Sala de Conciliação Virtual | Pedro Moretti | Avaliação do protótipo de papel da Sala de Conciliação Virtual | [Acessar](relato-resultados-conciliacao-virtual.md) |
| Relato — Notificação Ativa | Heitor Macedo Ricardo | Avaliação do protótipo de papel da Notificação Ativa | [Acessar](relato-resultados-notificacao-ativa.md) |
| Relato — Painel de Monitoramento de Prazos | Mateus Barreto | Avaliação do protótipo de papel do Painel de Monitoramento de Prazos | [Acessar](relato-resultados-prazos.md) |

---

## Triangulação e Consolidação dos Resultados

Esta seção sintetiza, de forma interparticipante e entre funcionalidades, os dados coletados nas avaliações do Nível 2. O objetivo é identificar padrões, convergências e divergências que emergem da leitura conjunta dos dois relatos de protótipo de papel, fornecendo uma visão consolidada sobre a qualidade de interação dos designs propostos para o PROCON-DF.

---

### Visão Geral das Avaliações

**Tabela — Síntese das sessões de avaliação do Nível 2**

| Funcionalidade | Avaliador | Participante | Perfil | Data | Nº de Tarefas | Taxa de Conclusão | Problemas (Gravidade ≥ 2) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Sala de Conciliação Virtual | Pedro Moretti | P1 | Fornecedor (empresária, 40 anos) | 05/06/2026 | 1 (fluxo completo) | 100% | 0 |
| Notificação Ativa | Heitor Macedo | P1 | Consumidor (universitária, ~18 anos) | 05/06/2026 | 1 (fluxo completo) | 100% | 0 |
| Painel de Monitoramento de Prazos | Mateus Barreto | P1 | Consumidor (psicóloga, 45 anos) | 20/06/2026 | 1 (fluxo completo) | 100% | 2 (PB1, PB2) |
| Painel de Monitoramento de Prazos | Mateus Barreto | P2 | Consumidor (professor, 46 anos) | 20/06/2026 | 1 (fluxo completo) | 100% | 1 (PB2) |
| Painel de Monitoramento de Prazos | Mateus Barreto | P3 | Consumidor (empresária, 48 anos) | 21/06/2026 | 1 (fluxo completo) | 100% | 0 |

<div align="center">
<p><i>Fonte: Elaborado por Heitor Macedo.</i></p>
</div>

---

### Convergências entre os Relatos

As avaliações das três funcionalidades revelam **convergências expressivas**, indicando que as decisões centrais de design dos protótipos de papel foram validadas por perfis de usuário distintos.

**1. Alta taxa de conclusão e resolução bem-sucedida**

Todos os participantes concluíram 100% das tarefas propostas. Embora na funcionalidade de Painel de Monitoramento de Prazos tenha havido necessidade de intervenção do mediador para orientar o acesso à Linha do Tempo (para P1 e P2), a taxa final de sucesso permaneceu em 100% em todas as avaliações do Nível 2. Isso demonstra que as interfaces, após as orientações pontuais de navegação, guiam os usuários de forma lógica ao seu objetivo final.

**2. GOV.BR como mecanismo de assinatura digital — validação por dois perfis distintos**

Ambas as funcionalidades integram o GOV.BR como método de assinatura digital, e em ambas as avaliações os participantes validaram essa escolha positivamente. A participante da Conciliação Virtual afirmou que o uso da assinatura digital do Governo Federal é "muito prático" e um "facilitador", pois "todos já usamos essa assinatura". A participante da Notificação Ativa reconheceu e utilizou a opção sem dificuldade, levantando apenas uma consideração cosmética sobre alternativas de assinatura.

**3. Ausência de necessidade de guias ou instruções adicionais**

Nenhum participante sentiu falta de orientação textual adicional nas interfaces. A participante da Notificação Ativa chegou a afirmar que instruções extras poderiam até confundir, pois a interface já indica visualmente onde clicar. Esse padrão valida a abordagem de design minimalista e orientado por ação adotada em ambos os protótipos.

**4. Percepção de valor superior ao processo presencial**

Em ambas as avaliações, os participantes manifestaram espontaneamente que as funcionalidades representam uma alternativa superior ao atendimento presencial no PROCON-DF. A participante da Conciliação Virtual afirmou se sentir "muito confortável" e classificou a proposta como uma "ideia válida para a resolução de muitas questões de uma maneira simples e sem precisar se deslocar". A participante da Notificação Ativa também confirmou conforto com o fluxo e reconheceu o valor prático da solução.

**5. Clareza das consequências e confirmações de ações irreversíveis**

Ambos os protótipos incluem telas de confirmação antes de ações definitivas (aceite de proposta na Notificação Ativa; assinatura do termo na Conciliação Virtual). Em ambos os casos, os participantes compreenderam corretamente o caráter irreversível dessas ações sem necessidade de esclarecimento adicional, validando a decisão de design de manter etapas explícitas de confirmação.

---

### Divergências e Pontos de Atenção

**Tabela — Problemas de usabilidade consolidados do Nível 2**

| Funcionalidade | ID | Tela / Etapa | Descrição do Problema | Gravidade | Freq. | Status |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: |
| Notificação Ativa | PB1 | Tela: Acordo Aceito — Assinatura | Participante demonstrou incerteza sobre a validade jurídica da assinatura biométrica como forma de formalização contratual | 1 | 1/1 | Correção planejada |
| Painel de Monitoramento de Prazos | PB1 | Tela: Prazo Expirado — Juizado Especial | Quebra de modelo mental na transição digital-físico (dúvida sobre ir a um local físico) | 2 | 1/3 | Correção planejada |
| Painel de Monitoramento de Prazos | PB2 | Tela: Painel Principal / Linha do Tempo | Ausência de sinalização de clique no cartão de prazo para acessar a linha do tempo (identificado em P1 e P2; P3 não foi solicitada a realizar esta ação) | 2 | 2/2 | Correção planejada |
| Sala de Conciliação Virtual | — | — | Nenhum problema identificado | — | — | — |

<div align="center">
<p><i>Nota sobre a Gravidade: (1) Cosmético; (2) Pequeno; (3) Grande; (4) Catastrófico.</i></p>
<p><i>Fonte: Elaborado por Heitor Macedo.</i></p>
</div>

Os problemas identificados no Nível 2 são de gravidade reduzida: um de **gravidade cosmética (1)** na Notificação Ativa (dúvida sobre a validade jurídica da biometria) e dois de **gravidade pequena (2)** no Painel de Monitoramento de Prazos (quebra de modelo mental na transição digital-físico e dificuldade em localizar de cara o botão para a linha do tempo). Esses problemas não impediram a conclusão das tarefas nem geraram confusão operacional grave.

A ausência de problemas na Conciliação Virtual e a presença de problemas de baixa gravidade nas demais funcionalidades indicam que os protótipos de papel do Nível 2 estão bem alinhados com as necessidades e expectativas dos usuários.

---

### Sugestões de Melhoria Consolidadas

**Tabela — Sugestões levantadas pelos participantes**

| ID | Funcionalidade | Sugestão | Origem | Prioridade |
| :---: | :--- | :--- | :---: | :---: |
| S01 | Notificação Ativa | Incluir nota explicativa sobre validade jurídica da assinatura biométrica (ex.: referência à Lei nº 14.063/2020) e/ou oferecer método alternativo de assinatura manuscrita | P1 (pós-tarefa) | Baixa |
| S02 | Painel de Monitoramento de Prazos | Facilitar transição lógica entre esfera digital (PROCON) e física (Juizado), incluindo checklist visível de documentos na tela de prazo expirado | P1 (pós-tarefa) | Média |
| S03 | Painel de Monitoramento de Prazos | Adicionar indicação visual explícita de clique nos cartões de prazo para acessar a linha do tempo | P1 e P2 (durante teste) | Média |

<div align="center">
<p><i>Fonte: Elaborado por Heitor Macedo.</i></p>
</div>

Não foram registradas sugestões de melhoria na avaliação da Conciliação Virtual — a participante declarou o sistema completo e adequado em todos os aspectos.

---

### Respostas Consolidadas às Perguntas de Pesquisa do Nível 2

| Pergunta de Pesquisa | Evidência Consolidada |
| :--- | :--- |
| Os protótipos de papel permitiram explorar os conceitos de design? | Sim — os fluxos completos foram simulados e validados em todas as avaliações |
| Foram observadas sugestões de melhoria para os protótipos? | Sim — 3 sugestões: S01 (Notificação Ativa) e S02, S03 (Painel de Prazos) |
| As interfaces propostas estão em conformidade com padrões de usabilidade? | Sim — participantes navegaram em conformidade, identificando padrões de biometria, login e termos legais |
| Foram identificados problemas de usabilidade preliminares? | Sim — identificados 3 problemas (1 cosmético na Notificação Ativa; 2 de gravidade 2 no Painel de Prazos) |
| O usuário consegue operar os sistemas representados nos protótipos? | Sim — taxa de conclusão de 100% em todas as avaliações, com desvios resolvidos na hora |
| Que parte da interface ou do fluxo deixa o usuário insatisfeito ou confuso? | Dúvidas pontuais sobre transição física externa (Juizado) e localização do botão de acesso à linha do tempo |
| O usuário entende o que significa e para que serve cada elemento de interface? | Sim — todos os elementos básicos foram devidamente compreendidos nos três protótipos |
| Quais barreiras o usuário encontra para atingir seus objetivos? | Dificuldade de localização do link/botão para a linha do tempo no painel de prazos |

<div align="center">
<p><i>Fonte: Elaborado por Heitor Macedo.</i></p>
</div>

---

### Conclusão

Os resultados do Nível 2 são amplamente positivos. As avaliações dos protótipos de papel da **Sala de Conciliação Virtual**, da **Notificação Ativa** e do **Painel de Monitoramento de Prazos** demonstram que os designs propostos pela equipe estão alinhados com as necessidades e expectativas dos perfis de usuário avaliados. Os problemas identificados são de gravidade reduzida (um cosmético e dois pequenos de gravidade 2) e possuem correções planejadas simples de layout e navegabilidade. Todos os protótipos estão prontos para avançar ao Nível 3, com base nos dados coletados neste ciclo de avaliação.

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 11/06/2026 | Criação da página de consolidação dos relatos do Nível 2. | Pedro Moretti | Heitor Macedo |
| 1.1 | 14/06/2026 | Adição da seção de Triangulação e Consolidação dos Resultados do Nível 2 e atualização da colaboração. | Heitor Macedo | Heitor Macedo |
| 1.2 | 22/06/2026 | Integração do relato de prazos e atualização da consolidação de resultados (refinamento de problemas/sugestões). | Mateus Barreto | Heitor Macedo |
