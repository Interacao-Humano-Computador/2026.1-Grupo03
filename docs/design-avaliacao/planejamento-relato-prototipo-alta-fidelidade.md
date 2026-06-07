# Planejamento da Avaliação do Protótipo de Alta Fidelidade — Assistente de Triagem Guiada

## Colaboração
Colaboração referente à [Etapa 6](../planejamento/cronograma-executado.md)


| Autores | Contribuiu |
|---|---|
| Pedro Augusto Macedo Del Castilo | Elaborou o Artefato |

---

## Introdução

O teste de usabilidade com um protótipo de alta fidelidade permite avaliar a interação, a navegação, o design visual e a clareza da interface em um ambiente que simula o comportamento do sistema final, mas sem a necessidade de codificação no *back-end*. Segundo Barbosa e Silva (2011), essa avaliação com usuários reais é indispensável para coletar percepções subjetivas, identificar barreiras remanescentes de acessibilidade e refinar elementos de IHC antes da etapa final de desenvolvimento.

Este artefato documenta o planejamento detalhado para a avaliação do **Assistente de Triagem Guiada para Reclamações** do PROCON-DF em sua versão de alta fidelidade (desenvolvida em ferramenta de design interativo), com foco na validação das escolhas de *Clean Design* e Linguagem Cidadã implementadas para mitigar a sobrecarga cognitiva de usuários com pouca familiaridade tecnológica.

---

## Metodologia

Para estruturar este planejamento, adota-se o framework **DECIDE** (BARBOSA; SILVA, 2011), que orienta a avaliação de forma sistemática através de seis etapas sequenciais detalhadas na Tabela 1.


**Tabela 1** – Framework DECIDE e suas definições

| Letra | Definição |
| :---: | --- |
| **D** | Determinar os objetivos da avaliação. |
| **E** | Explorar perguntas a serem respondidas com a avaliação. |
| **C** | Escolher os métodos de avaliação a serem utilizados. |
| **I** | Identificar e administrar as questões práticas da avaliação. |
| **D** | Decidir como lidar com as questões éticas. |
| **E** | Avaliar, interpretar e apresentar os dados. |

Fonte: Barbosa e Silva (2011).

---

### D - Determinar os Objetivos da Avaliação <sup><a href="#fig-d">[1]</a></sup>
Esta avaliação tem como objetivo geral validar a usabilidade, a acessibilidade e a aceitabilidade do fluxo interativo do Assistente de Triagem Guiada em alta fidelidade. Os objetivos específicos compreendem:
- Avaliar se usuários com diferentes níveis de letramento digital conseguem concluir o registro de uma queixa de ponta a ponta sem auxílio externo;
- Verificar o impacto da substituição de jargões jurídicos por linguagem cidadã na compreensão das instruções do órgão;
- Identificar gargalos de navegação ou problemas de legibilidade na interface mobile.
---
### E - Explorar Perguntas a serem Respondidas <sup><a href="#fig-d">[2]</a></sup>

Com base nos objetivos delineados e nas diretrizes de Barbosa e Silva (2011), foram formuladas as seguintes perguntas de pesquisa para guiar a análise dos avaliadores:

1. O usuário compreendeu imediatamente o propósito do botão central de alto contraste na tela inicial?
2. A categorização por *cards* visuais grandes permitiu ao usuário identificar seu problema por reconhecimento, reduzindo a necessidade de digitação?
3. A barra de progresso no estilo *wizard* forneceu feedback adequado sobre a localização do usuário no fluxo?
4. O usuário demonstrou hesitação, confusão ou insegurança em relação à segurança do ambiente (especialmente na transição para o Gov.br e upload de documentos)?
5. As mensagens escritas em linguagem cidadã foram interpretadas corretamente ou causaram alguma ambiguidade?

---

### C - Escolher os Métodos de Avaliação <sup><a href="#fig-d">[3]</a></sup>

O método selecionado é o **Teste de Usabilidade**, combinado de forma complementar com a técnica de **Observação Direta** e o protocolo de **Pensar em Voz Alta (*Think Aloud*)**.

A escolha fundamenta-se na natureza estritamente **qualitativa** definida para esta avaliação. Ao solicitar que o usuário verbalize seus pensamentos, dúvidas e sentimentos enquanto interage presencialmente com o smartphone, a equipe conseguirá capturar com precisão as nuances de frustração, alívio ou confusão, fornecendo insumos ricos para ajustes finos de design emocional e cognitivo.

---
### I - Identificar Questões Práticas da Avaliação <sup><a href="#fig-d">[4]</a></sup>

#### Recrutamento e Perfil dos Participantes
O teste contará com uma amostra de **3 a 5 participantes**. Embora o foco prioritário do design seja atender às necessidades da persona primária, o recrutamento abrangerá perfis diversificados de cidadãos do Distrito Federal para assegurar que a simplificação do fluxo também beneficie usuários gerais e de outros segmentos demográficos, mantendo o processo inclusivo e abrangente.

#### Preparação do Ambiente e Equipamentos
As sessões ocorrerão de forma **presencial**. O avaliador disponibilizará um smartphone configurado com o protótipo de alta fidelidade. O ambiente de teste deverá ser silencioso e confortável para o participante. Um segundo dispositivo será posicionado para registrar as reações e as verbalizações do usuário, mediante autorização prévia.

#### Roteiro de Tarefas a Executar
O participante receberá um cenário fictício: *"Você comprou uma mercadoria pela internet que não foi entregue e a empresa não responde mais suas mensagens. Você decidiu abrir uma reclamação oficial no PROCON-DF usando o celular"*. A partir disso, ele deverá realizar as 4 tarefas detalhadas a seguir:

* **Tarefa 1: Iniciar a queixa e classificar o problema**
    * *Objetivo:* Avaliar a clareza da tela inicial e a eficácia dos cartões de categoria por reconhecimento.
    * *Ação esperada:* Localizar o botão de início e selecionar a categoria "Produto com defeito ou não entregue".
* **Tarefa 2: Responder à triagem e passar pelo painel pedagógico**
    * *Objetivo:* Validar a interação com a pergunta sobre contato prévio e a recepção do painel explicativo.
    * *Ação esperada:* Clicar em "Sim" na tela de filtro e ler as orientações em linguagem cidadã, avançando para a etapa de cadastro.
* **Tarefa 3: Realizar a autenticação fictícia e o upload do documento**
    * *Objetivo:* Verificar a sensação de segurança na tela do Gov.br e a usabilidade do botão de acionamento de câmera para anexar evidências.
    * *Ação esperada:* Clicar em avançar no campo do CPF e acionar a área tracejada simulando a captura da foto da nota fiscal/comprovante.
* **Tarefa 4: Concluir o fluxo e validar o encerramento**
    * *Objetivo:* Analisar o sentimento de fechamento e o alívio cognitivo ao receber o número de protocolo destacado.
    * *Ação esperada:* Clicar em "Enviar Reclamação", conferir os dados finais na tela de sucesso e clicar em "Fechar e Sair".

#### Custos e Prazos
A avaliação será executada sem custos diretos para os participantes ou para a equipe, fazendo uso de equipamentos próprios dos estudantes. As sessões presenciais serão distribuídas conforme o cronograma provável apresentado na Tabela 2.


**Tabela 2** – Cronograma provável das sessões de teste

| Avaliador(es) | Participante | Perfil Resumido | Data | Horário | Local |
| :--- | :--- | :--- | :---: | :---: | :--- |
| Pedro Castilo | Participante 1 | Idoso / Baixo letramento | 15/06/2026 | 14:00 - 14:30 | Presencial |
| Pedro Castilo | Participante 2 | Adulto / Usuário médio | 15/06/2026 | 15:00 - 15:30 | Presencial |
| Pedro Castilo | Participante 3 | Jovem / Mobile-first | 16/06/2026 | 10:00 - 10:30 | Presencial |
| Pedro Castilo | Participante 4 | Adulto / Baixo letramento | 16/06/2026 | 11:00 - 11:30 | Presencial |

Fonte: elaborado pelo autor (2026).

---
### D - Decidir como Lidar com as Questões Éticas <sup><a href="#fig-d">[5]</a></sup>

Antes do início de qualquer atividade, o avaliador fará a leitura detalhada do Termo de Consentimento Livre e Esclarecido (TCLE). Será enfatizado ao participante que a interface está sendo testada, e não as suas habilidades individuais, assegurando um ambiente livre de pressão. O teste só prosseguirá após a assinatura física ou concordância verbal gravada do termo, garantindo o anonimato dos dados e o direito de interrupção a qualquer momento.

---

### E - Avaliar, Interpretar e Apresentar os Dados <sup><a href="#fig-d">[6]</a></sup>

Por se tratar de uma coleta qualitativa baseada em observação e técnica *think aloud*, os dados serão consolidados através de uma análise de conteúdo descritiva após o término das rodadas. O avaliador anotará:
- Os pontos exatos da tela onde os usuários manifestaram dúvidas ou hesitações em voz alta;
- Padrões visuais ou textuais que causaram erros de interpretação;
- Expressões corporais e faciais associadas à satisfação ou estresse.

Os resultados obtidos serão tabulados em um relatório final categorizando os problemas de usabilidade encontrados por níveis de severidade (leve, moderado ou grave), acompanhados das respectivas propostas de correção de design a serem implementadas na entrega final do sistema.

---

## Planejamento do Teste Piloto

Conforme recomendado pela literatura de IHC (BARBOSA; SILVA, 2011), o teste piloto serve para avaliar a consistência do próprio planejamento, verificando se o roteiro de tarefas é compreensível, se as ferramentas interativas funcionam perfeitamente no dispositivo e se o tempo estimado por sessão é condizente. O avaliador conduzirá o teste piloto simulando rigorosamente uma sessão padrão.

---

## Referência Bibliográfica

> BARBOSA, S. D. J.; SILVA, B. S. **Interação Humano-Computador**. Rio de Janeiro: Elsevier, 2011.

---

## Agradecimento a IA

Agradecimento ao **Gemini** pela estruturação, seguindo as normas ABNT, do documento.

## Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 07/06/2026 | Elaboração inicial do planejamento da avaliação em alta fidelidade com framework DECIDE. | Pedro Macedo | Heitor Macedo |

## Notas de Rodapé e Referências de Imagens

<div id="fig-d"></div>

**Figura 1** - D: Determinar os objetivos da avaliação.

![Determinar os objetivos](./images/decide-d.png)
<div></div>
Fonte: BARBOSA et al. (2021, p. 264).<sup><a href="#ref1">[1]</a></sup>

<div id="fig-e"></div>

**Figura 2** - E: Explorar perguntas a serem respondidas.

![Explorar perguntas](./images/decide-e.png)
<div></div>
Fonte: BARBOSA et al. (2021, p. 264).<sup><a href="#ref1">[1]</a></sup>

<div id="fig-c"></div>

**Figura 3** - C: Escolher os métodos de avaliação.

![Escolher métodos](./images/decide-c.png)
<div></div>
Fonte: BARBOSA et al. (2021, p. 264).<sup><a href="#ref1">[1]</a></sup>

<div id="fig-i"></div>

**Figura 4** - I: Identificar e administrar as questões práticas.

![Identificar questões práticas](./images/decide-i.png)
<div></div>
Fonte: BARBOSA et al. (2021, p. 264).<sup><a href="#ref1">[1]</a></sup>

<div id="fig-d2"></div>

**Figura 5** - D: Decidir como lidar com as questões éticas.

![Decidir questões éticas](./images/decide-d2.png)
<div></div>
Fonte: BARBOSA et al. (2021, p. 264).<sup><a href="#ref1">[1]</a></sup>

<div id="fig-e2"></div>

**Figura 6** - E: Avaliar (Evaluate), interpretar e apresentar os dados.

![Avaliar dados](./images/decide-e2.png)
<div></div>
Fonte: BARBOSA et al. (2021, p. 264).<sup><a href="#ref1">[1]</a></sup>
