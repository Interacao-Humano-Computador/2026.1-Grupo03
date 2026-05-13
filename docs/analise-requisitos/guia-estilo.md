# Guia de Estilo — Procon-DF

---

## 1. <a name="introducao"></a>1 Introdução

### 1.1 Objetivo do Guia de Estilo

Este guia constitui o registro formal das principais decisões de design da interface do portal Procon‑DF. Segundo **Barbosa e Silva (2021)**, o guia de estilo é uma ferramenta essencial para garantir que as diretrizes de IHC sejam efetivamente incorporadas no produto final, atuando como canal de comunicação entre designers e desenvolvedores.

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

### 2.2 Ambiente de trabalho do usuário

O Procon‑DF é um portal governamental acessado por cidadãos buscando direitos e servidores operando sistemas internos. O perfil é heterogêneo, exigindo que a **performance** e a **acessibilidade (e‑MAG)** sejam requisitos centrais (**BARBOSA; SILVA, 2021**).

---

## 3. <a name="interface"></a>3 Elementos de Interface

**Marcus (1991** *apud* **BARBOSA; SILVA, 2021)** considera os elementos desta seção os pilares da comunicação visual.

### 3.1 Disposição espacial e grid

O layout adota a metáfora de “blocos de serviço” sobre o sistema de 12 colunas.

<figure align="center">
  <img src="../images/main-grid.png" alt="Grade Principal do Portal" width="600">
  <figcaption align="center">
    <b>Figura 1:</b> O seguinte exemplo de disposição espacial prioriza o conteúdo de destaque ladeado por uma barra lateral de acesso rápido.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

**Espaçamentos utilitários (Rationale: Manter ritmo vertical consistente):**
Os espaçamentos seguem uma escala definida para margens superiores (variando de 10 a 80 pixels), margens inferiores (de 20 a 80 pixels) e preenchimento interno padrão de 10 pixels.

<figure align="center">
  <img src="../images/news-grid.png" alt="Grid de Notícias" width="600">
  <figcaption align="center">
    <b>Figura 2:</b> O seguinte exemplo de componente de grade utiliza categorias coloridas para segmentar tipos de informação, como Fiscalização e Erratas.<br>
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

<figure align="center">
  <img src="../images/external-services.png" alt="Box de serviços" width="600">
  <figcaption align="center">
    <b>Figura 3:</b> O seguinte exemplo de caixa de serviços demonstra a organização de informações por categorias gráficas.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/news-grid.png" alt="Cards com foto" width="600">
  <figcaption align="center">
    <b>Figura 4:</b> O seguinte exemplo de cartões com fotografia demonstra a aplicação de preenchimentos e bordas padronizadas.<br>
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

<figure align="center">
  <img src="../images/titulo-fonte.png" alt="Tipografia Titillium Web" width="300">
  <figcaption align="center">
    <b>Figura 5:</b> O seguinte exemplo da família Titillium Web aplicada em títulos garante o impacto visual e a legibilidade da hierarquia.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/nav-items.png" alt="Itens de Menu" width="300">
  <figcaption align="center">
    <b>Figura 6:</b> O seguinte exemplo da tipografia Montserrat aplicada em submenus garante clareza na leitura de itens de navegação interna.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.4 Paleta de cores

**Tabela 3 – Camadas Funcionais de Cor**

| Nome | Amostra | Uso Principal |
| :--- | :---: | :--- |
| **Azul Principal** | 🟦 | Links, botões secundários e títulos. |
| **Magenta (Chamada para Ação)** | 🟪 | Botões de alta prioridade e destaque. |
| **Amarelo Menu** | 🟨 | Identidade visual do governo no menu de navegação superior. |
| **Verde Sucesso** | 🟩 | Mensagens de confirmação positiva e botões de envio. |

> Nota: na implementação final do documento, os emojis devem ser substituídos por amostras gráficas exatas (amostras de cor) para fidelidade cromática.

<figure align="center">
  <img src="../images/navbar.png" alt="Barra de Navegação" width="600">
  <figcaption align="center">
    <b>Figura 7:</b> O seguinte exemplo de barra de navegação utiliza o amarelo institucional para reforçar a identidade do governo local.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.5 Simbolismo: ícones e Identidade

A interface utiliza dois conjuntos de símbolos: um focado na identidade e acessibilidade governamental (contraste, ajuste de fonte) e outro voltado para ações específicas do órgão (denúncias, reclamações).

<figure align="center">
  <img src="../images/gdf-logo.png" alt="Logotipo GDF" width="200">
  <figcaption align="center">
    <b>Figura 8:</b> O seguinte exemplo de logotipo institucional estabelece a autoridade governamental no topo da interface.<br>
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

<figure align="center">
  <img src="../images/breadcrumb.png" alt="Trilha de Navegação" width="1000">
  <figcaption align="center">
    <b>Figura 9:</b> O seguinte exemplo de trilha de navegação indica a localização exata do usuário dentro da hierarquia do portal.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 4.2 Seleção de um estilo

Conforme **Mayhew (1999** *apud* **BARBOSA; SILVA, 2021)**, os estilos minimizam a carga de memória através de navegação visível, manipulação direta de cartões e formulários claros para tarefas de entrada.

### 4.3 Acessibilidade e adaptações da interface

Seguindo a **WCAG 2.1**, o sistema oferece ajuste de tamanho de fonte via controle deslizante e tradução automática para Libras.

<figure align="center">
  <img src="../images/acessibility.png" alt="Controles de Acessibilidade" width="400">
  <figcaption align="center">
    <b>Figura 10:</b> O seguinte exemplo de painel de acessibilidade permite ao usuário customizar a interface para suas necessidades visuais.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/libras.png" alt="Widget VLibras" width="200">
  <figcaption align="center">
    <b>Figura 11:</b> O seguinte exemplo de ferramenta assistiva garante suporte à comunidade surda através da tradução para Libras.<br>
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

<figure align="center">
  <img src="../images/cta-button.png" alt="Botão CTA" width="400">
  <figcaption align="center">
    <b>Figura 12:</b> O seguinte exemplo de botão de chamada principal utiliza a cor magenta para guiar o usuário rumo à conclusão do serviço.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/most-searched.png" alt="Serviços Mais Procurados" width="600">
  <figcaption align="center">
    <b>Figura 13:</b> O seguinte exemplo de blocos de interação destaca as tarefas mais comuns com feedback visual de inversão de cores.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/search-button.png" alt="Botão de Busca" width="100">
  <figcaption align="center">
    <b>Figura 14:</b> O seguinte exemplo de funcionalidade de busca utiliza alto contraste de cor para permitir uma localização imediata.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## 6. <a name="vocabulario"></a>6 Vocabulário e Padrões

### 6.1 Terminologia e nomenclatura

Utiliza-se uma convenção simplificada para nomear caixas temáticas, elementos de ativação e sub-regiões textuais.

### 6.2 Sequências de diálogo e Rodapé

Fluxos críticos (sucesso, erro, confirmação de exclusão) devem exibir mensagens claras em locais previsíveis da tela.

<figure align="center">
  <img src="../images/footer.png" alt="Rodapé do Portal" width="600">
  <figcaption align="center">
    <b>Figura 15:</b> O seguinte exemplo de rodapé consolida as informações institucionais e canais de contato de forma clara e organizada.<br>
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
| `1.0` | 11/05/2026 | Estruturação inicial baseada em Barbosa e Silva (2021). | Pedro Moretti | Heitor Macedo |
| `1.3` | 13/05/2026 | Conversão de termos técnicos de estilos para descrições explicativas e consolidação visual. | Pedro Moretti | Heitor Macedo |

<br>

---

<figure id="ref-barbosa" align="center">
  <img src="../images/guia-estilo-1.png" alt="Referência Barbosa 1" width="500">
  <figcaption align="center">
    <i><b>Figura 16:</b> Principais elementos e considerações do design.<br></i>
    Fonte: (BARBOSA; SILVA, 2021, cap. 10.5, p. 241).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/guia-estilo-2.png" alt="Referência Barbosa 2" width="500">
  <figcaption align="center">
    <i><b>Figura 17:</b> Estrutura proposta para um Guia de Estilo.<br></i>
    Fonte: (BARBOSA; SILVA, 2021, cap. 10.5, p. 242).
  </figcaption>
</figure>