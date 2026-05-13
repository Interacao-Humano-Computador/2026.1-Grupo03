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
| 4. <a href="#interacao">Elementos de interação</a> | Paradigmas de interação e acessibilidade. |
| 5. <a href="#acao">Elementos de ação</a> | Padrões de formulários, botões e estados de ativação. |
| 6. <a href="#vocabulario">Vocabulário e padrões</a> | Nomenclatura técnica, tipos de tela e fluxos de diálogo. |

### 1.3 Público‑alvo

*   **Desenvolvedores front-end:** Devem usar as classes CSS documentadas sem recriar estilos.
*   **Gestores de conteúdo (WordPress):** Devem respeitar os padrões de nomenclatura e estrutura de páginas.
*   **Designers de interface:** Devem consultar este guia antes de propor qualquer alteração visual.
*   **Gerentes e equipe de suporte:** Referência para entender decisões já tomadas e justificá-las.

### 1.4 Como utilizar e manter o guia

**Em produção:** Antes de criar um novo componente, verifique se já existe uma classe CSS que atenda à necessidade. Reutilize; não recrie.

**Em manutenção:** Qualquer alteração em valores de cor, tipografia ou espaçamento deve ser refletida neste documento, registrando o **design rationale** (justificativa da mudança), preservando o rastreamento sugerido por **Mayhew (1999)** *apud* **Barbosa e Silva (2021)**.

---

## 2. <a name="analise"></a>2 Resultados de Análise

### 2.1 Fontes de dados e artefatos técnicos

A análise de IHC baseou‑se na extração direta de dados e na engenharia reversa do portal oficial do **Instituto de Defesa do Consumidor do Distrito Federal (PROCON-DF)**. Os artefatos técnicos analisados são:

1.  <a href="../images/procon-bootstrap.css" target="_blank">`procon‑bootstrap.css`</a>: Estrutura de grid responsivo (Bootstrap 3).
2.  <a href="../images/procon-style1.css" target="_blank">`procon‑style1.css`</a>: Folha principal (GDF Theme).
3.  <a href="../images/procon-style2.css" target="_blank">`procon‑style2.css`</a>: Componentes internos (IcoMoon Library).
4.  <a href="../images/procon-icomoon.css" target="_blank">`procon‑icomoon.css`</a>: Biblioteca de ícones institucionais do governo.
5.  <a href="../images/procon-zci-styles.css" target="_blank">`procon‑zci‑styles.css`</a>: Grid de categorias de serviços.

### 2.2 Ambiente de trabalho do usuário

O Procon‑DF é um portal governamental acessado por cidadãos buscando direitos e servidores operando sistemas internos. O perfil é heterogêneo, exigindo que a **performance** e a **acessibilidade (e‑MAG)** sejam requisitos centrais (**BARBOSA; SILVA, 2021**).

---

## 3. <a name="interface"></a>3 Elementos de Interface

**Marcus (1991** *apud* **BARBOSA; SILVA, 2021)** considera os elementos desta seção os pilares da comunicação visual.

### 3.1 Disposição espacial e grid

O layout adota a metáfora de “blocos de serviço” sobre o sistema de 12 colunas do Bootstrap 3.

<figure align="center">
  <img src="../images/main-grid.png" alt="Grade Principal do Portal" width="600">
  <figcaption align="center">
    <b>Figura 1:</b> O seguinte exemplo de disposição espacial prioriza o conteúdo de destaque ladeado por uma barra lateral de acesso rápido.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

**Espaçamentos utilitários (Rationale: Manter ritmo vertical consistente):**
*   `.margin‑top‑10` a `.margin‑top‑80`
*   `.margin‑bottom‑20` a `.margin‑bottom‑80`
*   `.padding‑10`

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
| `card-com-foto` | bg: white, border: 1px solid **#E0E0E0**, min-height: 470px, radius: 0 |
| `card-com-foto` (hover) | border: 1px solid **#CBCBCB**, box-shadow: 10px 10px 20px **#DFDFDF** |
| `card-sem-foto` | height: 400px, padding: 100px 30px 30px 30px |
| `box-servicos` | **border-radius: 10px**, height: 263px |

<figure align="center">
  <img src="../images/external-services.png" alt="Box de serviços" width="600">
  <figcaption align="center">
    <b>Figura 3:</b> O seguinte exemplo de box de serviços demonstra a organização de informações por categorias.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/news-grid.png" alt="Cards com foto" width="600">
  <figcaption align="center">
    <b>Figura 3:</b> O seguinte exemplo de cards com foto demonstra a organização de informações por categorias.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.3 Tipografia

**Tabela 2 – Escala e Papéis Tipográficos**

| Família | Papel IHC | Importação |
| :--- | :--- | :--- |
| **Titillium Web** | Títulos (h1–h5) e Identidade | Google Fonts (300) |
| **Open Sans** | Corpo de texto, parágrafos e legendas | Google Fonts |
| **Montserrat** | UI: Botões, menus e labels | Google Fonts |

<figure align="center">
  <img src="../images/nav-items.png" alt="Itens de Menu" width="300">
  <figcaption align="center">
    <b>Figura 3:</b> O seguinte exemplo de tipografia Montserrat aplicada em submenus garante clareza na leitura de itens de navegação interna.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.4 Paleta de cores

**Tabela 3 – Camadas Funcionais de Cor**

| Nome | Hexadecimal | Uso Principal |
| :--- | :--- | :--- |
| **Azul Principal** | **#4079BC** | Links, botões secundários e títulos. |
| **Magenta (CTA)** | **#A93D8E** | Botões primários (Classes `.btn-verde`). |
| **Amarelo Menu** | **#FFD200** | Identidade GDF no menu de navegação. |
| **Verde Sucesso** | **#29BCB6** | Feedback positivo e botões de envio. |

<figure align="center">
  <img src="../images/navbar.png" alt="Barra de Navegação" width="600">
  <figcaption align="center">
    <b>Figura 4:</b> O seguinte exemplo de barra de navegação utiliza o amarelo institucional para reforçar a identidade do governo local.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 3.5 Simbolismo: ícones e Identidade

*   **Conjunto 1 (GDF Institucional):** Identidade e acessibilidade (`.icon-brasao_gdf`, `.icon-contraste`, `.icon-aumenta_fonte`).
*   **Conjunto 2 (Procon Específico):** Ações diretas (`.icon-denuncia-icone`, `.icon-reclamacao-icone`, `.icon-sugestao-icone`).

<figure align="center">
  <img src="../images/gdf-logo.png" alt="Logotipo GDF" width="200">
  <figcaption align="center">
    <b>Figura 5:</b> O seguinte exemplo de logotipo estabelece a autoridade governamental no topo da interface.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## 4. <a name="interacao"></a>4 Elementos de Interação

### 4.1 Estilos de interação

O portal prioriza a interação por **apontar e clicar**.

<figure align="center">
  <img src="../images/breadcrumb.png" alt="Trilha de Navegação" width="1000">
  <figcaption align="center">
    <b>Figura 6:</b> O seguinte exemplo de trilha de navegação indica a localização exata do usuário dentro da hierarquia do portal.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

### 4.2 Seleção de um estilo

Conforme **Mayhew (1999** *apud* **BARBOSA; SILVA, 2021)**, os estilos minimizam a carga de memória:

1.  **Navegação Principal:** Seleção por menus no topo para visibilidade imediata.
2.  **Consumo de Informação:** Manipulação direta via Cards para varredura rápida.
3.  **Tarefas de Entrada:** Preenchimento de formulários em áreas de reclamação.

### 4.3 Aceleradores (Acessibilidade)

Seguindo a **WCAG 2.1**, o sistema oferece:

*   **Ajuste de Fonte:** Slider range com thumb **#01A453**.
*   **VLibras:** Widget fixo de tradução.

<figure align="center">
  <img src="../images/acessibility.png" alt="Controles de Acessibilidade" width="400">
  <figcaption align="center">
    <b>Figura 7:</b> O seguinte exemplo de painel de acessibilidade permite ao usuário customizar a interface para suas necessidades visuais.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/libras.png" alt="Widget VLibras" width="200">
  <figcaption align="center">
    <b>Figura 8:</b> O seguinte exemplo de widget garante suporte à comunidade surda através da tradução para Libras.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## 5. <a name="acao"></a>5 Elementos de Action

### 5.1 Preenchimento de campos e seleção

*   **Inputs:** `border: 1px solid #E0E0E0`, `border-radius: 4px`.
*   **Select:** `appearance: none`, fundo **#E0E0E0** com seta SVG customizada.

### 5.2 Ativação — Catálogo de botões

| Classe | Cor Fundo | Hover | Uso |
| :--- | :--- | :--- | :--- |
| `.btn-verde-grande` | **#A93D8E** | **#CB5599** | CTA principal (Anatomia: 15px 10px, Montserrat, radius 10px). |
| `.btn-azul-medio` | **#4079BC** | **#346399** | Ações secundárias importantes. |

<figure align="center">
  <img src="../images/cta-button.png" alt="Botão CTA" width="400">
  <figcaption align="center">
    <b>Figura 9:</b> O seguinte exemplo de CTA principal utiliza a cor magenta para guiar o usuário rumo à conversão do serviço.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/most-searched.png" alt="Serviços Mais Procurados" width="600">
  <figcaption align="center">
    <b>Figura 10:</b> O seguinte exemplo de blocos de interação destaca as tarefas mais comuns com feedback visual de inversão de cores.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/search-button.png" alt="Botão de Busca" width="100">
  <figcaption align="center">
    <b>Figura 11:</b> O seguinte exemplo de funcionalidade de busca utiliza alto contraste cromático para rápida localização pelo usuário.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## 6. <a name="vocabulario"></a>6 Vocabulário e Padrões

### 6.1 Terminologia e nomenclatura

Convenção **BEM Simplificada**:

*   **box-**: Caixas temáticas (`.box-diario-oficial`).
*   **btn-**: Elementos de ativação.
*   **area-**: Sub-regiões (`.area-textual`).

### 6.2 Sequências de diálogo e Rodapé

*   **Feedback de Erro:** Borda **#EA4D3C** (classe `.input-erro`).
*   **Confirmação de Envio:** Botão `.btnEnviar` (**#29BCB6**).

<figure align="center">
  <img src="../images/footer.png" alt="Rodapé do Portal" width="600">
  <figcaption align="center">
    <b>Figura 12:</b> O seguinte exemplo de rodapé consolida as informações institucionais e canais de contato de forma clara.<br>
    Fonte: DISTRITO FEDERAL (2026).
  </figcaption>
</figure>

---

## Apêndice A – Design Rationale Consolidado

| Decisão | Justificativa |
| :--- | :--- |
| **Magenta para CTA** | Contraste intencional com o azul institucional para guiar a conversão. |
| **Border-radius 10px** | Modernidade sem perda de seriedade governamental. |
| **Duas fontes IcoMoon** | Independência entre ícones GDF (globais) e Procon (específicos). |

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
| `1.2` | 13/05/2026 | Consolidação visual com inclusão de artefatos de interface e rationale. | Pedro Moretti | Heitor Macedo |

<br>

---

<figure id="ref-barbosa" align="center">
  <img src="../images/guia-estilo-1.png" alt="Referência Barbosa 1" width="500">
  <figcaption align="center">
    <i><b>Figura 13:</b> Principais elementos e considerações do design (BARBOSA; SILVA, 2021, cap. 10.5, p. 241).</i><a href="#ref-barbosa"><sup>1</sup></a>
  </figcaption>
</figure>

<figure align="center">
  <img src="../images/guia-estilo-2.png" alt="Referência Barbosa 2" width="500">
  <figcaption align="center">
    <i><b>Figura 14:</b> Estrutura proposta para um Guia de Estilo (BARBOSA; SILVA, 2021, cap. 10.5, p. 242).</i><a href="#ref-barbosa"><sup>2</sup></a>
  </figcaption>
</figure>