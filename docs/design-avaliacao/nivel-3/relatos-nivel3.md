# Relatos dos Resultados — Nível 3

## Colaboração

Colaboração referente à [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Moretti | Elaborou o Artefato |
| Heitor Macedo | Realizou a Triangulação |

---

## Introdução

Esta página consolida os relatos de resultados das avaliações conduzidas no **Nível 3** do processo de Design, Avaliação e Desenvolvimento. Os relatos documentam os resultados obtidos nas avaliações dos protótipos de alta fidelidade, incluindo problemas de usabilidade identificados, feedback dos participantes e planejamento de reprojeto.

---

## Relatos

| Documento | Autor(es) | Objeto Avaliado | Acesso |
|---|---|---|---|
| Relato — Sala de Conciliação Virtual | Pedro Moretti | Avaliação do protótipo de alta fidelidade da Sala de Conciliação Virtual | [Acessar](relato-resultados-alta-fidelidade-conciliacao-virtual.md) |
| Relato — Notificação Ativa | Heitor Macedo | Avaliação do protótipo de alta fidelidade da Notificação Ativa | [Acessar](relato-resultados-alta-fidelidade-notificacao-ativa.md) |

---

## Triangulação e Consolidação dos Resultados

Esta seção sintetiza, de forma interparticipante e entre funcionalidades, os dados coletados nas avaliações do Nível 3. O objetivo é identificar padrões, convergências e divergências que emergem da leitura conjunta dos dois relatos, fornecendo uma visão consolidada do estado de usabilidade do sistema proposto para o PROCON-DF.

---

### Visão Geral das Avaliações

**Tabela — Síntese das sessões de avaliação do Nível 3**

| Funcionalidade | Avaliador | Participante | Perfil | Data | Nº de Tarefas | Taxa de Conclusão | Problemas (Gravidade ≥ 2) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Sala de Conciliação Virtual | Pedro Moretti | P1 | Fornecedor (empresária, 40 anos) | 12/06/2026 | 3 | 100% | 0 |
| Notificação Ativa | Heitor Macedo | P1 | Consumidor (professor, 44 anos) | 13/06/2026 | 1 (fluxo completo) | 100% | 0 |

<div align="center">
<p><i>Fonte: Elaborado por Pedro Moretti e Heitor Macedo.</i></p>
</div>

---

### Convergências entre os Relatos

As avaliações das duas funcionalidades revelaram **cinco convergências expressivas**, indicando que as decisões de design centrais do sistema foram validadas por perfis de usuário distintos.

**1. WhatsApp como canal de entrada — validação unânime**

Ambas as funcionalidades utilizam o WhatsApp como ponto de entrada (notificação com link direto), e em ambas as avaliações os participantes validaram essa escolha com ênfase. O participante da Notificação Ativa afirmou que "hoje em dia a nossa vida é resumida basicamente tudo através de um celular, através do WhatsApp", corroborando a premissa de design adotada pela equipe. A participante da Conciliação Virtual também confirmou a praticidade do canal ao receber o link de acesso à sala de audiência.

**2. Assinatura digital via GOV.BR — confiança e praticidade reconhecidas**

A integração com o GOV.BR para assinatura digital foi avaliada positivamente por ambos os participantes. Na Conciliação Virtual, a participante afirmou que "é muito mais prático" que assinar fisicamente, pois "a senha do Gov.br já é amplamente utilizada e decorada". Na Notificação Ativa, o participante validou as opções de assinatura disponíveis (biometria e GOV.BR) e sugeriu adicionar uma terceira via vinculada ao cadastro PROCON-DF.

**3. Telas de confirmação e protocolo — segurança percebida como valor**

Em ambos os fluxos, telas que confirmam e registram ações importantes (pop-ups de irreversibilidade, telas de protocolo com número, data e horário) foram avaliadas como úteis e necessárias — não como fricção ou obstáculo. Isso valida a decisão de design de manter etapas explícitas de confirmação antes de ações definitivas.

**4. Conclusão de todas as tarefas sem erros e sem ajuda**

Todos os participantes concluíram 100% das tarefas propostas com nível de dificuldade máximo de 1 ("Muito fácil"), sem cometer erros e sem solicitar auxílio ao avaliador. Esse dado quantitativo indica que os fluxos de navegação propostos são eficientes e não apresentam barreiras operacionais significativas.

**5. Percepção de valor superior ao processo presencial**

Em ambas as avaliações, os participantes manifestaram espontaneamente que as funcionalidades representam uma alternativa superior ao atendimento presencial no PROCON-DF — seja pela economia de tempo, de deslocamento ou pela praticidade do acesso remoto.

---

### Divergências e Pontos de Atenção

**Tabela — Problemas de usabilidade consolidados do Nível 3**

| Funcionalidade | ID | Tela / Etapa | Descrição do Problema | Gravidade | Frequência | Status |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: |
| Notificação Ativa | P01 | Visualização da Proposta | Prazo de crédito (10 dias úteis) sem destaque visual proporcional à sua relevância na decisão | 1 | 1/1 | Correção planejada |
| Sala de Conciliação Virtual | — | — | Nenhum problema identificado | — | — | — |

<div align="center">
<p><i>Nota sobre a Gravidade: (1) Cosmético; (2) Pequeno; (3) Grande; (4) Catastrófico.</i></p>
<p><i>Fonte: Elaborado por Pedro Moretti e Heitor Macedo.</i></p>
</div>

O único problema identificado em todo o Nível 3 é de **gravidade cosmética (1)**: na tela de visualização da proposta da Notificação Ativa, o prazo de crédito de 10 dias úteis não possui destaque visual proporcional à sua relevância para a decisão do usuário. A informação está presente, mas não é percebida de imediato.

A ausência de problemas na Sala de Conciliação Virtual e a presença de apenas um problema cosmético na Notificação Ativa indicam que os protótipos de alta fidelidade do Nível 3 estão em estado avançado de maturidade para os dois perfis de usuário avaliados.

---

### Sugestões de Melhoria Consolidadas

**Tabela — Sugestões levantadas pelos participantes**

| ID | Funcionalidade | Sugestão | Origem | Prioridade |
| :---: | :--- | :--- | :---: | :---: |
| S01 | Notificação Ativa | Adicionar terceira opção de assinatura digital vinculada ao cadastro próprio do portal PROCON-DF | P1 (pós-tarefa) | Média |

<div align="center">
<p><i>Fonte: Elaborado por Pedro Moretti e Heitor Macedo.</i></p>
</div>

A sugestão S01 está alinhada com a convergência identificada no ponto 2 (valorização de múltiplas opções de assinatura) e pode ser avaliada para implementação em iterações futuras, aumentando a inclusão digital para usuários sem conta GOV.BR ativa ou sem biometria disponível no dispositivo.

---

### Respostas Consolidadas às Perguntas de Pesquisa do Nível 3

| Pergunta de Pesquisa | Evidência Consolidada |
| :--- | :--- |
| Os protótipos validaram os conceitos visuais e o comportamento das interações planejadas? | Sim — ambos os protótipos tiveram fluxos completos navegados sem erros e com feedback positivo sobre design visual e componentes |
| Foram identificados problemas que impeçam ou dificultem a conclusão de tarefas? | Não — o único problema (P01, cosmético) não impede a execução da tarefa nem causa confusão operacional |
| As soluções de design atendem às necessidades e expectativas dos usuários? | Sim — em ambas as avaliações, os participantes validaram as escolhas centrais de design (WhatsApp, GOV.BR, confirmações explícitas, timelines) |
| O usuário consegue operar os sistemas de forma autônoma e eficiente? | Sim — taxa de conclusão de 100% em todas as tarefas, dificuldade máxima de 1/5, sem pedidos de ajuda |
| Foram observadas sugestões de refinamento? | Sim — 1 sugestão (S01): adicionar terceira opção de assinatura digital na Notificação Ativa |

<div align="center">
<p><i>Fonte: Elaborado por Pedro Moretti e Heitor Macedo.</i></p>
</div>

---

### Conclusão

Os resultados do Nível 3 são positivos em sua totalidade. As avaliações dos protótipos de alta fidelidade da **Sala de Conciliação Virtual** e da **Notificação Ativa** demonstram que o design proposto pela equipe está alinhado com as necessidades dos usuários do PROCON-DF — tanto do perfil Fornecedor quanto do perfil Consumidor Reclamante. O único problema identificado é cosmético e possui correção planejada de baixa complexidade. As duas funcionalidades estão prontas para avançar à etapa de implementação, com base nos dados coletados neste ciclo de avaliação.

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 12/06/2026 | Criação da página de consolidação dos relatos do Nível 3. | Pedro Moretti | Heitor Macedo |
| 1.1 | 14/06/2026 | Adição do relato de Notificação Ativa e atualização da colaboração. | Heitor Macedo | Heitor Macedo |
| 1.2 | 14/06/2026 | Adição da seção de Triangulação e Consolidação dos Resultados do Nível 3. | Heitor Macedo | Heitor Macedo |
