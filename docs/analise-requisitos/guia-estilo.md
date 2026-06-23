# Guia de Estilo — Procon-DF

---

## Colaboração
Colaboração referente a [Etapa 3](../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Augusto Moretti Moreira | Elaboração do Artefato |

## 1. <a name="introducao"></a>1 Introdução

### 1.1 Objetivo do Guia de Estilo

Este guia constitui o registro formal das principais decisões de design da interface do portal Procon‑DF. Segundo **Barbosa e Silva (2021)**<sup><a href="#ref-barbosa">[1]</a></sup>, o guia de estilo é uma ferramenta essencial para garantir que as diretrizes de IHC sejam efetivamente incorporadas no produto final, atuando como canal de comunicação entre designers e desenvolvedores.

O propósito não é apenas restringir a criatividade por meio de regras, mas apoiar o trabalho coletivo por intermédio de um processo reflexivo de design (**BARBOSA; SILVA, 2021**), evitando que decisões fundamentais se percam em manutenções futuras.

### 1.2 Organização e Conteúdo

A estrutura segue a padronização proposta por **Marcus (1991)** e **Mayhew (1999)**, ambos *apud* **Barbosa e Silva (2021)**, organizada conforme a Tabela 1.

**Tabela 1 – Estrutura do guia de estilo**

| Seção | Conteúdo |
| :--- | :--- |
| 1. <a href="#introducao">Introdução</a> | Objetivos, público‑alvo e governança do guia. |
| 2. <a href="#analise">Resultados de análise</a> | Descrição do ambiente de uso e fontes técnicas. |
| 3. <a href="#interface">Elementos de interface</a> | Grid, tipografia, cores, ícones e animações. |
| 4. <a href="#interacao">Elementos de interação</a> | Paradigmas de interação, acessibilidade e aceleradores. |
| 5. <a href="#acao">Elementos de ação</a> | Padrões de formulários, botões e estados de ativação. |
| 6. <a href="#vocabulario">Vocabulário e padrões</a> | Nomenclatura técnica, tipos de tela, fluxos de diálogo e rodapé. |

### 1.3 Público‑alvo

*   **Desenvolvedores front-end:** Devem usar as classes documentadas sem recriar estilos.
*   **Gestores de conteúdo (WordPress):** Devem respeitar os padrões de nomenclatura e estrutura de páginas.
*   **Designers de interface:** Devem consultar este guia antes de propor qualquer alteração visual.
*   **Gerentes e equipe de suporte:** Referência para entender decisões já tomadas e justificá-las.

### 1.4 Como utilizar e manter o guia

**Em produção:** Antes de criar um novo componente, verifique se já existe um padrão que atenda à necessidade. Reutilize; não recrie.

**Em manutenção:** Qualquer alteração em valores de cor, tipografia ou espaçamento deve ser refletida neste documento, registrando a justificativa da mudança (**design rationale**), preservando o rastreamento sugerido por **Mayhew (1999)** *apud* **Barbosa e Silva (2021)**.

---

## 2. <a name="analise"></a>2 Resultados de Análise

### 2.1 Fontes de dados e artefatos técnicos

A análise de IHC baseou‑se na extração direta de dados e na engenharia reversa do portal oficial do **Instituto de Defesa do Consumidor do Distrito Federal (PROCON-DF)**. Os artefatos técnicos analisados incluem a estrutura de grade responsiva, a folha de estilos principal do tema governamental, bibliotecas de componentes internos e de ícones institucionais.

1. <a href="../images/procon-bootstrap.css" target=_blank>`procon‑bootstrap.css`</a>: Estrutura de grid responsivo (Bootstrap 3).
2. <a href="../images/procon-style1.css" target=_blank>`procon‑style1.css`</a>: Folha principal (GDF Theme).
3. <a href="../images/procon-style2.css" target=_blank>`procon‑style2.css`</a>: Componentes internos (IcoMoon Library).
4. <a href="../images/procon-icomoon.css" target=_blank>`procon‑icomoon.css`</a>: Biblioteca de ícones institucionais do governo.
5. <a href="../images/procon-zci-styles.css" target=_blank>`procon‑zci‑styles.css`</a>: Grid de categorias de serviços.

### 2.2 Ambiente de trabalho do usuário

O Procon‑DF é um portal governamental acessado por cidadãos buscando direitos e servidores operando sistemas internos. O perfil é heterogêneo, exigindo que a **performance** e a **acessibilidade (e‑MAG)** sejam requisitos centrais (**BARBOSA; SILVA, 2021**).

---

## 3. <a name="interface"></a>3 Elementos de Interface

**Marcus (1991** *apud* **BARBOSA; SILVA, 2021)** considera os elementos desta seção os pilares da comunicação visual.

### 3.1 Disposição espacial e grid

O layout adota a metáfora de “blocos de serviço” sobre o sistema de 12 colunas.

Como pode ser observado na Figura 1, a estrutura prioriza o conteúdo de destaque com barra lateral de acesso rápido.

<figure align="center">
  <figcaption align="center">
    <b>Figura 1:</b> O seguinte exemplo de disposição espacial prioriza o conteúdo de destaque ladeado por uma barra lateral de acesso rápido.
  </figcaption>
  <img src="../images/main-grid.png" alt="Grade Principal do Portal" width="600">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

**Espaçamentos utilitários (Rationale: Manter ritmo vertical consistente):**
Os espaçamentos seguem uma escala definida para margens superiores (variando de 10 a 80 pixels), margens inferiores (de 20 a 80 pixels) e preenchimento interno padrão de 10 pixels.

Conforme ilustrado na Figura 2, a grade de notícias usa categorias coloridas para segmentar tipos de informação.

<figure align="center">
  <figcaption align="center">
    <b>Figura 2:</b> O seguinte exemplo de componente de grade utiliza categorias coloridas para segmentar tipos de informação, como Fiscalização e Erratas.
  </figcaption>
  <img src="../images/news-grid.png" alt="Grid de Notícias" width="600">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.2 Janelas e Cartões (Cards)

| Componente | Propriedades visuais |
| :--- | :--- |
| Cartão com foto | Fundo branco, borda sólida cinza claro de 1 pixel, altura mínima de 470 pixels e bordas retas (sem arredondamento). |
| Cartão com foto (ao passar o mouse) | Borda sólida cinza de 1 pixel e sombra projetada suave na cor cinza claro. |
| Cartão sem foto | Altura fixa de 400 pixels e preenchimento interno de 100 pixels no topo e 30 pixels nas demais laterais. |
| Caixa de serviços | Bordas arredondadas de 10 pixels e altura de 263 pixels. |

Como apresentado na Figura 3, a caixa de serviços organiza informações por categorias gráficas.

<figure align="center">
  <figcaption align="center">
    <b>Figura 3:</b> O seguinte exemplo de caixa de serviços demonstra a organização de informações por categorias gráficas.
  </figcaption>
  <img src="../images/external-services.png" alt="Box de serviços" width="600">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

Como pode ser observado na Figura 4, os cartões com fotografia aplicam preenchimentos e bordas padronizadas.

<figure align="center">
  <figcaption align="center">
    <b>Figura 4:</b> O seguinte exemplo de cartões com fotografia demonstra a aplicação de preenchimentos e bordas padronizadas.
  </figcaption>
  <img src="../images/news-grid.png" alt="Cards com foto" width="600">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.3 Tipografia

**Tabela 2 – Escala e Papéis Tipográficos**

| Família | Papel IHC | Escala e Detalhes |
| :--- | :--- | :--- |
| **Titillium Web** | Títulos e Identidade | Tamanhos variando entre 24 e 60 pixels na cor cinza escuro. |
| **Open Sans** | Corpo de texto e parágrafos | Tamanho de 16 pixels com altura de linha entre 1,4 e 1,7 vezes o tamanho da fonte. |
| **Montserrat** | Botões, menus e rótulos | Utilizada em elementos de interação; metadados em 14 pixels. |

Na Figura 5, apresenta-se a aplicação da família Titillium Web em títulos para assegurar hierarquia visual.

<figure align="center">
  <figcaption align="center">
    <b>Figura 5:</b> O seguinte exemplo da família Titillium Web aplicada em títulos garante o impacto visual e a legibilidade da hierarquia.
  </figcaption>
  <img src="../images/titulo-fonte.png" alt="Tipografia Titillium Web" width="300">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

Conforme ilustrado na Figura 6, a tipografia Montserrat aparece em submenus para facilitar a leitura de itens de navegação.

<figure align="center">
  <figcaption align="center">
    <b>Figura 6:</b> O seguinte exemplo da tipografia Montserrat aplicada em submenus garante clareza na leitura de itens de navegação interna.
  </figcaption>
  <img src="../images/nav-items.png" alt="Itens de Menu" width="300">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.4 Paleta de cores

**Tabela 3 – Camadas Funcionais de Cor**

| Nome | Amostra | Hexadecimal | Uso Principal |
| :--- | :---: | :--- | :--- |
| **Azul Principal** | 🟦 | #4079BC | Links, botões secundários e títulos. |
| **Magenta (Chamada para Ação)** | 🟪 | #A93D8E | Botões de alta prioridade e destaque. |
| **Amarelo Menu** | 🟨 | #FFD200 | Identidade visual do governo no menu de navegação superior. |
| **Verde Sucesso** | 🟩 | #29BCB6 | Mensagens de confirmação positiva e botões de envio. |

> Nota: na implementação final do documento, os emojis devem ser substituídos por amostras gráficas exatas (amostras de cor) para fidelidade cromática.

Como pode ser observado na Figura 7, a barra de navegação utiliza o amarelo institucional para reforçar a identidade do governo local.

<figure align="center">
  <figcaption align="center">
    <b>Figura 7:</b> O seguinte exemplo de barra de navegação utiliza o amarelo institucional para reforçar a identidade do governo local.
  </figcaption>
  <img src="../images/navbar.png" alt="Barra de Navegação" width="600">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.5 Simbolismo: ícones e Identidade

A interface utiliza dois conjuntos de símbolos: um focado na identidade e acessibilidade governamental (contraste, ajuste de fonte) e outro voltado para ações específicas do órgão (denúncias, reclamações).

Na Figura 8, observa-se o logotipo institucional que estabelece a autoridade governamental no topo da interface.

<figure align="center">
  <figcaption align="center">
    <b>Figura 8:</b> O seguinte exemplo de logotipo institucional estabelece a autoridade governamental no topo da interface.
  </figcaption>
  <img src="../images/gdf-logo.png" alt="Logotipo GDF" width="200">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.6 Animações e transições

Para garantir previsibilidade e fluidez na interface, adotam-se os seguintes comportamentos:

- **Transições em botões e cartões:** Movimentos suaves e lineares aplicados a todas as propriedades, com duração entre 0,1 e 0,2 segundos.
- **Galeria e grades:** Duração de 0,3 segundos para transformações visuais.
- **Indicadores de estado:** Botões no topo sofrem aumento de escala de 3%; imagens em grades aumentam em 5%; e galeria tem redução de brilho em 20% ao passar o mouse.
- **Indicadores de espera:** Exibição de um elemento giratório azul ou efeito de "tela esqueleto" com fundo cinza pulsante.

---

## 4. <a name="interacao"></a>4 Elementos de Interação

### 4.1 Estilos de interação

O portal prioriza a interação por **apontar e clicar**. Botões apresentam um efeito tátil ao serem clicados, deslocando-se 1 pixel para baixo. Menus com itens internos desabilitam o clique no nível superior para forçar a abertura do submenu, que apresenta fundo cinza escuro ao passar o mouse.

Como pode ser observado na Figura 9, a trilha de navegação indica a localização do usuário na hierarquia do portal.

<figure align="center">
  <figcaption align="center">
    <b>Figura 9:</b> O seguinte exemplo de trilha de navegação indica a localização exata do usuário dentro da hierarquia do portal.
  </figcaption>
  <img src="../images/breadcrumb.png" alt="Trilha de Navegação" width="1000">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 4.2 Seleção de um estilo

Conforme **Mayhew (1999** *apud* **BARBOSA; SILVA, 2021)**, os estilos minimizam a carga de memória através de navegação visível, manipulação direta de cartões e formulários claros para tarefas de entrada.

### 4.3 Acessibilidade e adaptações da interface

Seguindo a **WCAG 2.1**, o sistema oferece ajuste de tamanho de fonte via controle deslizante e tradução automática para Libras.

Conforme ilustrado na Figura 10, o painel de acessibilidade permite ao usuário customizar a interface para necessidades visuais.

<figure align="center">
  <figcaption align="center">
    <b>Figura 10:</b> O seguinte exemplo de painel de acessibilidade permite ao usuário customizar a interface para suas necessidades visuais.
  </figcaption>
  <img src="../images/acessibility.png" alt="Controles de Acessibilidade" width="400">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

Na Figura 11, observa-se a ferramenta assistiva de tradução para Libras para suporte a usuarios surdos.

<figure align="center">
  <figcaption align="center">
    <b>Figura 11:</b> O seguinte exemplo de ferramenta assistiva garante suporte à comunidade surda através da tradução para Libras.
  </figcaption>
  <img src="../images/libras.png" alt="Widget VLibras" width="200">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## 5. <a name="acao"></a>5 Elementos de Ação

### 5.1 Preenchimento de campos e seleção

Os campos de formulário obedecem às seguintes regras:

*   **Campos de entrada:** Borda sólida cinza claro de 1 pixel e bordas levemente arredondadas de 4 pixels.
*   **Seleção (Dropdown):** Estilo de seta customizado sobre fundo cinza claro.

**Estados dos campos:**

| Estado | Aparência Visual |
| :--- | :--- |
| Padrão | Borda sólida cinza claro de 1 pixel. |
| Em Foco | Borda sólida azul de 1 pixel acompanhada de uma suave auréola externa azul transparente. |
| Erro | Borda sólida vermelha de 1 pixel com ícone de alerta e mensagem explicativa. |
| Sucesso | Borda sólida verde de 1 pixel acompanhada de ícone de confirmação. |
| Desabilitado | Redução da opacidade para 50% e bloqueio total de interações. |

### 5.2 Ativação — Catálogo de botões

| Tipo de Botão | Estilo Visual | Uso Sugerido |
| :--- | :--- | :--- |
| Principal (Grande) | Fundo magenta, tipografia Montserrat e bordas arredondadas de 10 pixels com preenchimento interno generoso. | Chamada principal para ação (CTA). |
| Secundário (Médio) | Fundo azul sólido com mudança para tom mais escuro ao passar o mouse. | Ações de suporte importantes. |

Como pode ser observado na Figura 12, o botão de chamada principal utiliza a cor magenta para orientar a conclusão do serviço.

<figure align="center">
  <figcaption align="center">
    <b>Figura 12:</b> O seguinte exemplo de botão de chamada principal utiliza a cor magenta para guiar o usuário rumo à conclusão do serviço.
  </figcaption>
  <img src="../images/cta-button.png" alt="Botão CTA" width="400">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

Conforme ilustrado na Figura 13, os blocos de interação destacam tarefas comuns com inversao de cores no feedback.

<figure align="center">
  <figcaption align="center">
    <b>Figura 13:</b> O seguinte exemplo de blocos de interação destaca as tarefas mais comuns com feedback visual de inversão de cores.
  </figcaption>
  <img src="../images/most-searched.png" alt="Serviços Mais Procurados" width="600">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

Na Figura 14, a funcionalidade de busca aparece com alto contraste para facilitar a localizacao imediata.

<figure align="center">
  <figcaption align="center">
    <b>Figura 14:</b> O seguinte exemplo de funcionalidade de busca utiliza alto contraste de cor para permitir uma localização imediata.
  </figcaption>
  <img src="../images/search-button.png" alt="Botão de Busca" width="100">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## 6. <a name="vocabulario"></a>6 Vocabulário e Padrões

### 6.1 Terminologia e nomenclatura

Utiliza-se uma convenção simplificada para nomear caixas temáticas, elementos de ativação e sub-regiões textuais.

### 6.2 Sequências de diálogo

Considerando que o portal Procon‑DF possui poucas ações executadas internamente — visto que a maior parte das funcionalidades consiste em redirecionamentos para sistemas externos — não se observa uma grande variedade de sequências de diálogo para análise aprofundada neste guia.

### 6.3 Tipos de tela

Para facilitar a criação de novas páginas e manter a coerência visual, definem‑se os seguintes gabaritos:

| Tipo de tela | Finalidade | Componentes básicos |
| :--- | :--- | :--- |
| Página inicial | Acesso rápido a serviços e notícias | Menu superior, carrossel, grade de serviços, rodapé |
| Resultado de busca | Listagem de itens encontrados | Campo de busca, filtros laterais, lista de cartões |
| Detalhe de serviço | Leitura completa de um serviço | Trilha de navegação, título, conteúdo, botão de ação principal |
| Formulário | Entrada de dados pelo cidadão | Etapas (se necessário), campos com validação, botão de envio |
| Página de confirmação | Agradecimento e número de protocolo | Mensagem de sucesso, protocolo, opção de voltar ao início |

### 6.4 Rodapé

Como pode ser observado na Figura 15, o rodape consolida informações institucionais e canais de contato de forma organizada.

<figure align="center">
  <figcaption align="center">
    <b>Figura 15:</b> O seguinte exemplo de rodapé consolida as informações institucionais e canais de contato de forma clara e organizada.
  </figcaption>
  <img src="../images/footer.png" alt="Rodapé do Portal" width="600">
  <figcaption align="center">
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## Apêndice A – Design Rationale Consolidado

| Decisão | Justificativa |
| :--- | :--- |
| **Magenta para CTA** | Contraste intencional para guiar a conversão. |
| **Bordas arredondadas (10px)** | Modernidade sem perda de seriedade governamental. |
| **Estados de campo definidos** | Redução da incerteza do usuário durante a interação. |

---

## Agradecimentos

Agradecimento ao **Gemini** pelo auxílio na estruturação e redação da análise de IHC que subsidiou este documento.

---

## Referências

BARBOSA, S. D. J.; SILVA, B. S. da. **Interação Humano‑Computador e Experiência do Usuário**. 1. ed. Rio de Janeiro: Autopublicação, 2021.

DISTRITO FEDERAL. Instituto de Defesa do Consumidor (PROCON-DF). **Portal oficial**. Brasília, 2026. Disponível em: <https://www.procon.df.gov.br/>. Acesso em: 13 maio 2026.

MARCUS, A. **Graphic Design for Electronic Documents and User Interfaces**. ACM Press, 1991. *Apud* BARBOSA; SILVA, 2021.

MAYHEW, D. J. **The Usability Engineering Lifecycle**. Morgan Kaufmann, 1999. *Apud* BARBOSA; SILVA, 2021.

W3C. **Web Content Accessibility Guidelines (WCAG) 2.1**. 2018. Disponível em: <a href="https://www.w3.org/TR/WCAG21/" target="_blank">https://www.w3.org/TR/WCAG21/</a>. Acesso em: 11 maio 2026.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor | Revisor |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 11/05/2026 | Estruturação inicial baseada em Barbosa e Silva (2021). | Pedro Augusto Moretti Moreira | Heitor Macedo |
| `1.3` | 13/05/2026 | Conversão de termos técnicos de estilos para descrições explicativas e consolidação visual. | Pedro Augusto Moretti Moreira | Heitor Macedo |
| `1.4` | 13/05/2026 | Inclusão de hexadecimais na paleta de cores, expansão das sequências de diálogo, adição de tipos de tela e reorganização da seção 6. | Pedro Augusto Moretti Moreira | Heitor Macedo |

## Notas de Rodapé e Referências de Imagens


<br>
---

Conforme ilustrado na Figura 16, apresentam-se os principais elementos e consideracoes de design discutidos na referencia.

<figure id="ref-barbosa" align="center">
  <figcaption align="center">
    <i><b>Figura 16:</b> Principais elementos e considerações do design.</i>
  </figcaption>
  <img src="../images/guia-estilo-1.png" alt="Referência Barbosa 1" width="500">
  <figcaption align="center">
    Fonte: (BARBOSA; SILVA, 2021, cap. 10.5, p. 241).
  </figcaption>
</figure>

Na Figura 17, observa-se a estrutura proposta para um guia de estilo segundo Barbosa e Silva.

<figure align="center">
  <figcaption align="center">
    <i><b>Figura 17:</b> Estrutura proposta para um Guia de Estilo.</i>
  </figcaption>
  <img src="../images/guia-estilo-2.png" alt="Referência Barbosa 2" width="500">
  <figcaption align="center">
    Fonte: (BARBOSA; SILVA, 2021, cap. 10.5, p. 242).
  </figcaption>
</figure>
