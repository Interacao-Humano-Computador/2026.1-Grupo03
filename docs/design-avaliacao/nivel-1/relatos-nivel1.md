# Relatos dos Resultados — Nível 1

## Colaboração

Colaboração referente à [Etapa 5](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Augusto Moretti Moreira | Elaborou o Artefato |
| Heitor Macedo | Realizou a triangulação |

---

## Introdução

Esta página consolida os relatos de resultados das avaliações conduzidas no **Nível 1** do processo de Design, Avaliação e Desenvolvimento. Os relatos documentam os resultados obtidos nas avaliações dos storyboards e da análise de tarefas, incluindo problemas de usabilidade identificados, feedback dos participantes e planejamento de reprojeto. Trata-se de avaliação **formativa**<sup><a href="#figura1">[1]</a></sup>, conduzida sobre representações parciais da solução — modelos de tarefas (HTA e CTT) e storyboards — antes de qualquer implementação interativa, com o propósito de identificar problemas e orientar o refinamento do design nas fases iniciais do desenvolvimento.

---

## Relatos

| Documento | Autor(es) | Objeto Avaliado | Acesso |
|---|---|---|---|
| Relato dos Resultados — Storyboard | Heitor Macedo, Pedro Augusto Moretti Moreira, Heloisa Silva | Avaliação dos storyboards das funcionalidades do PROCON-DF | [Acessar](relato-resultados-storyboard.md) |
| Relato dos Resultados — Análise de Tarefas | Heitor Macedo, Pedro Augusto Moretti Moreira | Avaliação dos modelos de tarefas (HTA e CTT) | [Acessar](relato-resultados-analise-tarefas.md) |

---

## Triangulação e Consolidação dos Resultados

Esta seção sintetiza, de forma interparticipante e entre métodos de avaliação, os dados coletados nas avaliações do Nível 1. O objetivo é identificar padrões, convergências e divergências que emergem da leitura conjunta dos dois relatos — Storyboard e Análise de Tarefas —, fornecendo uma visão consolidada do estado de usabilidade do sistema proposto para o PROCON-DF.

---

### Visão Geral das Avaliações

**Tabela — Síntese das sessões de avaliação do Nível 1**

| Método | Avaliadores | Participantes | Perfis | Nº de Avaliações | Taxa de Conclusão | Problemas (Gravidade ≥ 2) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Storyboard | Heitor Macedo, Pedro Augusto Moretti Moreira, Heloisa Silva | P1, P2, P3 | Universitária (18), Empresário (40), Aposentada (67) | 3 | 100% | 0 |
| Análise de Tarefas (HTA + CTT) | Heitor Macedo, Pedro Augusto Moretti Moreira | P1, P2 | Universitária (18), Empresário (40) | 2 | 100% | 5 |

<div align="center">
<p><i>Fonte: Elaborado por Heitor Macedo.</i></p>
</div>

---

### Convergências entre os Relatos

As avaliações do Nível 1 revelam **cinco convergências expressivas** entre os dois métodos e os três perfis de usuário avaliados.

**1. Validação unânime da proposta de valor das funcionalidades**

Nos três storyboards avaliados (Notificação Ativa, Sala de Conciliação Virtual, Reconhecimento de Documentos por OCR), todos os participantes — de perfis radicalmente distintos (18 a 67 anos, universitária a aposentada) — responderam "Sim" a todas as cinco perguntas de validação, incluindo clareza do cenário, identificação com a situação e praticidade da solução digital. Isso indica que a proposta de valor do sistema tem apelo transversal de público.

**2. Modelos de tarefa HTA percebidos como compreensíveis e corretos**

Em ambas as avaliações da Análise de Tarefas, os participantes classificaram os diagramas HTA como "muito fáceis" (dificuldade 1/5), indicando que a decomposição hierárquica das tarefas de "Acompanhar reclamação" e "Participar de conciliação virtual" reflete com fidelidade o modelo mental dos usuários para essas atividades.

**3. Lacuna documental como problema transversal**

O manuseio e visualização de documentos foi identificado como ponto de fricção em dois problemas independentes: PB2 (instruções insuficientes para envio de documentos na Análise de Tarefas de P1) e PB4 (ausência de tela de visualização de documentos na Conciliação Virtual, identificado por P2). Ambos emergiram em contextos de avaliação diferentes (Notificação Ativa e Conciliação Virtual), sugerindo que a gestão de evidências e documentos é uma lacuna sistêmica do design.

**4. Alternativa digital reconhecida como superior ao presencial**

Em ambos os métodos, os participantes manifestaram espontaneamente preferência pela alternativa digital frente ao atendimento presencial no PROCON-DF, seja pela economia de tempo, eliminação de deslocamento ou praticidade do acesso remoto. Esse padrão aparece na satisfação dos storyboards (notas 5/5) e nos comentários durante a análise de tarefas.

**5. Fluxos propostos concluídos sem necessidade de ajuda**

Em todas as avaliações do Nível 1, os participantes concluíram as tarefas sem solicitar auxílio ao avaliador, independentemente do perfil ou método. Isso valida que os fluxos conceituais propostos são coerentes e navegáveis para os perfis de usuário do PROCON-DF.

---

### Divergências e Pontos de Atenção

**Tabela — Problemas de usabilidade consolidados do Nível 1**

| Método | ID | Objeto Avaliado | Descrição do Problema | Gravidade | Freq. | Persistência | Status |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| Análise de Tarefas | PB1 | CTT — Notificação Ativa | Notação CTT não intuitiva para participantes sem formação técnica | 2 | 1/2 | Pontual | Correção planejada |
| Análise de Tarefas | PB2 | HTA — Notificação Ativa | Etapas de envio de documentos são excessivamente genéricas, sem instruções claras | 2 | 1/2 | Estrutural | Correção planejada |
| Análise de Tarefas | PB3 | Site PROCON-DF atual | Navegação até "Registrar Reclamação" não é intuitiva — usuário cometeu 2 erros | 3 | 1/2 | Recorrente | Correção planejada |
| Análise de Tarefas | PB4 | CTT — Conciliação Virtual | Ausência de tela de visualização de documentos no fluxo de conciliação | 2 | 1/2 | Estrutural | Correção planejada |
| Análise de Tarefas | PB5 | HTA/CTT — Conciliação Virtual | Falta de representação explícita da transição para atendimento presencial | 2 | 2/2 | Estrutural | Correção planejada |
| Storyboard | — | Todos os storyboards | Nenhum problema identificado | — | — | — | — |

<div align="center">
<p><i>Nota sobre a Gravidade: (1) Cosmético; (2) Pequeno; (3) Grande; (4) Catastrófico — impede o usuário de realizar a tarefa e alcançar seus objetivos.</i></p>
<p><i>Fonte: Elaborado por Heitor Macedo.</i></p>
</div>

**Divergência de perfil: impacto da familiaridade tecnológica**

O único ponto de divergência relevante entre os participantes está na dificuldade percebida com o CTT: P1 (universitária, 18 anos) classificou o diagrama como "muito difícil" (4/5), enquanto P2 (empresário, 40 anos) o classificou como "muito fácil" (1/5). Essa divergência não reflete problemas no design proposto, mas indica que a notação CTT pressupõe letramento técnico não garantido em usuários leigos — recomendando-se a adição de legenda explicativa nos diagramas.

**PB3 como problema de maior gravidade (3 — Grande)**

O único problema de gravidade 3 identificado no Nível 1 refere-se à navegação no site atual do PROCON-DF para localizar a funcionalidade de registro de reclamação: a participante P1 cometeu dois erros de navegação antes de encontrar o caminho correto. Esse problema é independente das funcionalidades propostas pela equipe, mas afeta diretamente a percepção de usabilidade do sistema como um todo e deve ser considerado como requisito de arquitetura de informação nos protótipos.

---

### Respostas Consolidadas às Perguntas de Pesquisa do Nível 1

| Pergunta de Pesquisa | Evidência Consolidada |
| :--- | :--- |
| Os storyboards comunicam cenários realistas e identificáveis pelos usuários? | Sim — todos os participantes (3/3) identificaram-se com os cenários e validaram as situações como pertinentes |
| As funcionalidades propostas apresentam valor percebido pelos usuários? | Sim — todos os perfis reconheceram espontaneamente a vantagem das soluções digitais sobre o atendimento presencial |
| Os modelos de tarefas (HTA e CTT) refletem adequadamente o modelo mental dos usuários? | Parcialmente — HTA foi validado por ambos os perfis; CTT gerou dificuldade para o perfil menos técnico (P1) |
| Existem problemas que impeçam ou dificultem a execução das tarefas propostas? | Sim — PB3 (gravidade 3): navegação no site atual não é intuitiva; os demais problemas são de gravidade 2 e não impedem a conclusão das tarefas |
| Quais aspectos do design precisam de ajuste antes do protótipo de papel? | Gestão de documentos (PB2, PB4), legenda do CTT (PB1), transição presencial (PB5) e arquitetura de navegação do portal (PB3) |

<div align="center">
<p><i>Fonte: Elaborado por Heitor Macedo.</i></p>
</div>

---

### Conclusão

Os resultados do Nível 1 são positivos no que se refere à validação conceitual das funcionalidades: os storyboards foram aprovados unanimemente por três perfis de usuário distintos, sem nenhum problema identificado. No entanto, as avaliações da Análise de Tarefas revelam cinco pontos de melhoria, concentrados principalmente na gestão de documentos e na arquitetura de navegação do site atual do PROCON-DF. O problema de maior impacto (PB3, gravidade 3) afeta a jornada de entrada no sistema e deve ser tratado com prioridade no protótipo de papel (Nível 2). Os demais problemas (PB1, PB2, PB4, PB5, gravidade 2) são correções de médio impacto que refinam a completude e clareza dos fluxos propostos.

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 11/06/2026 | Criação da página de consolidação dos relatos do Nível 1. | Pedro Augusto Moretti Moreira | Heitor Macedo |
| 1.1 | 14/06/2026 | Adição da seção de Triangulação e Consolidação dos Resultados do Nível 1 e atualização da colaboração. | Heitor Macedo | Heitor Macedo |

## Notas de Rodapé e Referências de Imagens

<div id="figura1" align="center">
  <p>Figura 1 - Definição de avaliação formativa</p>
  <a href="../../images/avaliacaoformativa.png" target="_blank"><img src="../../images/avaliacaoformativa.png" alt="Definição de avaliação formativa — Barbosa et al. (2021, Cap. 11.3, p. 251)" width="700"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, Cap. 11.3, p. 251).</p>
</div>

<div id="figura2" align="center">
  <p>Figura 2 - Tabela 12.11 — Caracterização dos métodos de avaliação de IHC</p>
  <a href="../../images/tabela1211.png" target="_blank"><img src="../../images/tabela1211.png" alt="Tabela 12.11 — Métodos de avaliação de IHC — Barbosa et al. (2021, Cap. 12, p. 308)" width="700"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, Cap. 12, p. 308).</p>
</div>
