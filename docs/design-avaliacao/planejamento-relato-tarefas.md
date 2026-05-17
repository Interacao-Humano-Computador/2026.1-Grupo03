## 1. Introdução
Esta página descreve como será estruturado o documento de relato dos resultados após a realização da avaliação da Análise de Tarefas do sistema do PROCON-DF. O foco deste documento é estritamente o planejamento prévio, garantindo que todas as informações relevantes sejam abordadas de maneira clara e padronizada. Isso facilitará a compreensão e o uso dos dados coletados durante as sessões de avaliação do fluxo das tarefas, captando melhorias viáveis para a arquitetura e interface do sistema.

**Autor:** Heitor Macedo Ricardo

---

## 2. Metodologia
O planejamento do relato dos resultados foi fundamentado na literatura oficial de Interação Humano-Computador. Segundo Barbosa *et al.* (2021, p. 263)<sup><a href="#figura0">[1]</a></sup>, após a consolidação dos dados (análise interparticipante), os avaliadores devem relatar os resultados consolidados seguindo uma estrutura padronizada de tópicos, que abrange desde os objetivos iniciais até o planejamento para o reprojeto.

A documentação do relato final da nossa avaliação da análise de tarefas deverá conter obrigatoriamente os seguintes tópicos delineados abaixo.

---

## 3. Tópicos do Relato dos Resultados

### 3.1. Objetivos e escopo da avaliação
Nesta etapa, o redator do documento deverá explicar a razão pela qual a avaliação está sendo realizada e descrever o objetivo prático que o grupo pretende alcançar ao validar os modelos de tarefas (HTA, CTT, etc.) com os usuários. Isso envolve justificar a importância da avaliação, esclarecer as expectativas, as metas estabelecidas e fornecer uma visão geral das tarefas que foram o escopo da avaliação.

### 3.2. Método de avaliação empregado
Esta etapa do relato deverá conter uma breve descrição do método utilizado (Observação com Simulação de Uso e Entrevistas). O redator deve descrever como o fluxo da tarefa foi apresentado ao usuário e como a sessão foi conduzida pelo avaliador, mantendo o documento harmônico e conciso.

### 3.3. Número e perfil de avaliadores e dos participantes
O relato deverá justificar a seleção dos entrevistados, comprovando que eles se encaixam no Perfil de Usuário / Personas (ex: Consumidor Reclamante, Fornecedor) do PROCON-DF definidos no projeto. Deve apresentar uma tabela descrevendo quantos usuários reais participaram e quais membros do grupo atuaram como avaliadores (mediadores e observadores).

### 3.4. Tarefas executadas pelos participantes
O avaliador deverá descrever os fluxos e os passos que o usuário foi instruído a seguir (com base nos diagramas de Análise de Tarefas como o HTA) ao simular a interação.

### 3.5. Sumário dos dados coletados

Os dados quantitativos coletados durante a observação da execução das tarefas serão padronizados e consolidados através de tabelas de medição de desempenho. O formato abaixo será utilizado para registrar o tempo, os erros e a taxa de sucesso de cada participante, permitindo a comparação estatística e a verificação das Metas de Usabilidade.

**Tabela 1 - Sumário quantitativo da execução das tarefas**

| Participante | Tarefa Solicitada | Tempo de Execução | Concluída? (Sim/Não) | Qtd. de Erros Cometidos | Pediu Ajuda? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Participante 1 | Acompanhar Reclamação | 02 min 15 seg | Sim | 1 | Não |
| Participante 2 | Acompanhar Reclamação | 04 min 30 seg | Sim | 3 | Sim |
| Participante 3 | Acompanhar Reclamação | 07 min 00 seg | Não (Desistiu) | 5 | Sim |

<div align="center">
<p><i>Fonte: Elaborado por Heitor Macedo Ricardo.</i></p>
</div>

### 3.6. Relato da interpretação e análise dos dados
O documento deverá apresentar a análise e interpretação conjunta dos dados. O avaliador descreverá as tendências de comportamento observadas nas atitudes dos participantes avaliados ao tentarem seguir o fluxo das tarefas propostas para o PROCON-DF, fazendo a distinção entre características comuns do grupo e dificuldades individuais.

### 3.7. Lista dos problemas encontrados

Os dados qualitativos e as observações de barreiras de interação serão consolidados em um quadro de problemas. Esta padronização visa facilitar o repasse das falhas para a equipe de design e desenvolvimento, classificando a gravidade do problema para priorizar o reprojeto.

**Quadro 1 - Padronização e priorização dos problemas identificados**

| ID | Local / Passo na Tarefa | Descrição do Problema | Gravidade (1 a 4) | Sugestão de Correção |
| :--- | :--- | :--- | :--- | :--- |
| P1 | Tela de Login | O usuário não entendeu que o CPF precisava de pontuação, gerando erro. | 3 (Problema Grande) | Inserir máscara automática no campo de CPF. |
| P2 | Dashboard | O usuário não encontrou o botão de "Ver Notificações". | 4 (Catastrófico) | Mudar a cor do ícone do sino para dar mais contraste. |

<div align="center">
<p><i>Nota sobre a Gravidade: (1) Problema cosmético; (2) Problema pequeno; (3) Problema grande; (4) Catastrófico (impede a conclusão da tarefa).</i></p>
<p><i>Fonte: Elaborado por Heitor Macedo Ricardo.</i></p>
</div>

### 3.8. Planejamento para o reprojeto do sistema
É importante que o grupo documente o planejamento de melhorias com base nos problemas identificados no modelo de tarefas. O avaliador tem a responsabilidade de **priorizar a correção dos problemas não resolvidos**, baseando-se na gravidade do impacto que eles causaram no desempenho do usuário. Além disso, o relato deve propor soluções para corrigir os gargalos nos fluxos das tarefas, oferecendo ideias para as próximas fases de prototipação da interface.

---

## 4. Comprovação Teórica e Referência Bibliográfica
Conforme exigência do plano de ensino, a estrutura deste planejamento de relato reflete exatamente as diretrizes listadas na bibliografia oficial da disciplina.

## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação deste documento.

## Referência:
> BARBOSA, Simone D. J.; SILVA, Bruno S. da; SILVEIRA, Milene S.; GASPARINI, Isabela; DARIN, Ticianne; BARBOSA, Gabriel D. J. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021. (Capítulo 11: Planejamento da Avaliação de IHC, Seção 11.7.5 - Consolidação e Relato dos Resultados, p. 263-264).

---

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 17/05/2026 | Criação do Planejamento do Relato dos Resultados da Análise de Tarefas. | Heitor Macedo Ricardo | Pedro Moretti |

<div id="figura0" align="center">
  <p>Figura 1 - Consolidação e Relato dos Resultados</p>
  <a href="../images/consolidacao.png" target=_blank><img src="../images/consolidacao.png" alt="Seção 11.7.5 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 263).</p>
</div>