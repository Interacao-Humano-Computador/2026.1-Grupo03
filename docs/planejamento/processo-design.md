# Processo de Design

Para compreender o que é um Processo de Design, primeiro é necessário entender o próprio conceito de design. Segundo Barbosa e Silva (2021), o design pode ser organizado em três atividades básicas: análise da situação atual, síntese de uma intervenção e avaliação dessa intervenção.

A **análise da situação atual**, conforme Barbosa e Silva (2021), envolve a compreensão dos elementos presentes no contexto investigado, permitindo interpretar com mais precisão a realidade observada. Em outras palavras, após essa etapa, obtém-se uma visão mais clara das necessidades e oportunidades de melhoria que precisam ser endereçadas.

Já a **síntese de intervenção** corresponde à definição da situação desejada e à elaboração de uma **intervenção** capaz de conduzir a transição entre o estado atual e o estado pretendido.

A **avaliação**, por sua vez, pode ocorrer em diferentes momentos do processo e tem como objetivo verificar se a intervenção proposta está, de fato, transformando a situação atual na direção esperada.

Com base nessas definições, entende-se o Processo de Design como o detalhamento dessas atividades básicas, abrangendo desde a forma de execução de cada etapa até os artefatos produzidos e consumidos ao longo do processo (BARBOSA; SILVA, 2021).

Alguns dos modelos de Processo de Design estudados em sala de aula são citados abaixo:

## Ciclo de Vida Simples

<div align="center">
  <p>Figura 1 - Representação Gráfica do Modelo Simples</p>
  <img src="../images/processo-design/Modelo_Simples.png" alt="Modelo Simples">
  <p markdown><b>Fonte: Barbosa e Silva (2021)</b><sup><a href="#ref-barbosa">[1]</a></sup></p>
</div>

Desenvolvido por Sharp, Preece e Rogers, este é um processo de design centrado no usuário, com uso do desenvolvimento de versões interativas da proposta de solução e da iteração entre atividades, nesse processo as atividades não seguem uma ordem específica, podendo-se retornar para qualquer atividade do processo conforme a necessidade e a iteração entre elas pode ocorrer quantas vezes forem necessárias (BARBOSA; SILVA, 2021).

## Ciclo de Vida em Estrela

<div align="center">
  <p>Figura 2 - Representação Gráfica do Modelo em Estrela</p>
  <img src="../images/processo-design/Modelo_Estrela.png" alt="Modelo em Estrela">
  <p markdown><b>Fonte: Barbosa e Silva (2021)</b><sup><a href="#ref-barbosa">[1]</a></sup></p>
</div>

Desenvolvido por Hix e Hartson, esse processo possui seis atividades, sendo a avaliação a atividade central. A ordem da execução das atividades é de discrição do designer de acordo com a sua intenção (BARBOSA; SILVA, 2021).

Segundo Barbosa e Silva (2021), esse modelo a atividade de síntese é segmentada nas atividades de projeto conceitual e **especificação do design**, **prototipação** e **implementação**.

## Ciclo de Vida Mayhew

<div align="center">
  <p>Figura 3 - Representação Gráfica do Modelo Mayhew</p>
  <img src="../images/processo-design/Modelo_Mayhew.png" alt="Modelo Mayhew">
  <p markdown><b>Fonte: Barbosa e Silva (2021)</b><sup><a href="#ref-barbosa">[1]</a></sup></p>
</div>

Segundo Barbosa e Silva (2021), o ciclo de vida de Mayhew organiza atividades clássicas de IHC em um processo iterativo com três fases: análise de requisitos; design, avaliação e desenvolvimento; e instalação. Essas fases podem ser descritas da seguinte forma:

- **Análise de Requisitos:** Nesta etapa, definem-se metas de usabilidade com base no perfil dos usuários, na análise de tarefas, em princípios gerais de design de IHC e nas limitações da plataforma (BARBOSA; SILVA, 2021).

- **Design, avaliação e desenvolvimento:** Nessa fase, a solução de IHC é elaborada em três níveis (BARBOSA; SILVA, 2021):
  - No primeiro nível, são produzidos e avaliados protótipos de baixa fidelidade.
  - No segundo, são definidos padrões de design e desenvolvidos protótipos de média fidelidade.
  - No terceiro, é elaborado o projeto com interface detalhada e de alta fidelidade.
- **Instalação:** Após o uso, são coletadas opiniões dos usuários para consolidar melhorias no sistema (BARBOSA; SILVA, 2021).

## Processo de Design Selecionado: Engenharia de Usabilidade de Nielsen

Para guiar o desenvolvimento do nosso projeto, selecionamos o ciclo de vida da **Engenharia de Usabilidade de Jakob Nielsen**.

## Justificativa da Escolha:

Optamos por este processo porque ele propõe um conjunto de atividades que ocorrem durante todo o ciclo de vida do produto, com uma forte ênfase na avaliação contínua e no design iterativo. Isso nos permite identificar e corrigir problemas de usabilidade desde os estágios iniciais, garantindo que o sistema final atenda às reais necessidades dos usuários antes de focar apenas na implementação técnica.

<div align="center">
  <p>Figura 4 - Atividades do processo de Engenharia de Usabilidade de Nielsen</p>
  <img src="../images/processo-design/atividades-nielsen.png" alt="Atividades de Nielsen">
  <p markdown><b>Fonte: Nielsen (1994c) apud Barbosa et al. (2021), cap. 6.3.2, p. 102</b><sup><a href="#ref-barbosa">[1]</a></sup></p>
</div>

## Como aplicaremos o processo no nosso projeto:

Nielsen propõe 10 atividades básicas. Para a execução do nosso projeto, organizamos essas atividades nas seguintes fases práticas:

**1. Fase de Descoberta e Planejamento**

- **Conhecer o usuário:** Vamos levantar dados para criar perfis de usuários e personas, focando em suas características, ambiente e objetivos finais com o sistema.
- **Análise competitiva:** Examinaremos sistemas semelhantes ou concorrentes para extrair boas ideias e identificar falhas que não devemos repetir.
- **Definição das metas de usabilidade:** Estabeleceremos quais fatores de qualidade (eficiência, satisfação, facilidade de aprendizado) serão prioridade no nosso design.

<div align="center">
  <p>Figura 5 - Primeira etapa do processo de Engenharia de Usabilidade de Nielsen</p>
  <img src="../images/processo-design/primeira-etapa-nielsen.png" alt="Primeira etapa de Nielsen">
  <p markdown><b>Fonte: Nielsen (1994c) apud Barbosa et al. (2021), cap. 6.3.2, p. 102-103</b><sup><a href="#ref-barbosa">[1]</a></sup></p>
</div>

**2. Fase de Concepção e Design**

- **Designs paralelos e Design participativo:** Membros da equipe criarão alternativas iniciais de design de forma independente. Em seguida, selecionaremos as melhores ideias, mantendo o foco em ouvir o feedback de usuários representativos sempre que possível.
- **Design coordenado da interface:** Padronizaremos a identidade visual, a linguagem e o tom do sistema para garantir consistência.
- **Prototipação:** Desenvolveremos protótipos rápidos e de baixo custo (como protótipos de papel ou _wireframes_) para materializar nossas ideias antes de escrever qualquer código.

<div align="center">
  <p>Figura 6 - Segunda etapa do processo de Engenharia de Usabilidade de Nielsen</p>
  <img src="../images/processo-design/segunda-etapa-nielsen.png" alt="Segunda etapa de Nielsen">
  <p markdown><b>Fonte: Nielsen (1994c) apud Barbosa et al. (2021), cap. 6.3.2, p. 103-104</b><sup><a href="#ref-barbosa">[1]</a></sup></p>
</div>

**3. Fase de Avaliação e Refinamento**

- **Diretrizes e Análise Heurística:** A equipe aplicará as 10 Heurísticas de Nielsen sobre os protótipos para encontrar potenciais violações de usabilidade (Método de Inspeção).
- **Testes empíricos:** Realizaremos sessões de observação com usuários reais interagindo com nossos protótipos para identificar onde eles realmente encontram barreiras.
- **Design iterativo:** Com base nos problemas encontrados nas inspeções e testes, faremos as correções necessárias na interface e repetiremos o ciclo de avaliação até atingirmos nossas metas de usabilidade.

<div align="center">
  <p>Figura 7 - Terceira etapa do processo de Engenharia de Usabilidade de Nielsen</p>
  <img src="../images/processo-design/terceira-etapa-nielsen.png" alt="Terceira etapa de Nielsen">
  <p markdown><b>Fonte: Nielsen (1994c) apud Barbosa et al. (2021), cap. 6.3.2, p. 105</b><sup><a href="#ref-barbosa">[1]</a></sup></p>
</div>

<br>

<div align="center">
  <p>Figura 8 - Processo de Design</p>
  <img src="../images/processo-design/ProcessoDesign.png" alt="Fluxo do Processo de Design">
  <p><b>Fonte: Heitor Macedo</b></p>
</div>

---

## Referências Bibliográficas

<div id="ref-barbosa" markdown>
Barbosa, S. D. J.; Silva, B. S. da; Silveira, M. S.; Gasparini, I.; Darin, T.; Barbosa, G. D. J. (2021) **Interação Humano-Computador e Experiência do usuário**. Autopublicação.
</div>

---

## Agradecimentos à Inteligência Artificial

Agradecimento especial ao **NotebookLM** pelo auxílio na criação da imagem de processo de design que foi utilizada.

---

## Histórico de Versão

| Versão | Data       | Descrição                                                                                                                                                                                                                                           | Autor                 | Revisor       |
| ------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------- |
| 1.2    | 12/04/2026 | Inclusão de imagens de referência para os modelos de ciclo de vida e para o processo de design de Nielsen, com legendas e referências bibliográficas padronizadas.                                                                                       | Pedro Moretti         |        Heitor Macedo Ricardo       |
| 1.1    | 11/04/2026 | Revisão da redação introdutória do Processo de Design e inserção das representações gráficas dos modelos Ciclo de Vida Simples, Ciclo de Vida em Estrela e Ciclo de Vida Mayhew, com legendas padronizadas.                                         | Heloisa Silva         |          Eduardo Valadares     |
| 1.0    | 11/04/2026 | Inclusão do embasamento textual em Nielsen, justificativas, mapeamento de fases do projeto, inserção da imagem do processo e marcação dos espaços faltantes (fotos do livro e referências) para inclusão futura pelos demais integrantes da equipe. | Heitor Macedo RIcardo | Heloisa Silva |
