# Análise de Design Tokens — Procon-DF

**Site:** https://www.procon.df.gov.br/  
**Captura:** 2026-06-14 · emulação iPhone 12 (390×844 px, deviceScaleFactor 3, isMobile, hasTouch)

> **Aviso:** Os tokens aqui extraídos servem de referência e inspiração.
> Não copie textos, imagens ou logotipos do site original.

---

## Screenshot mobile

`screenshot_mobile_fullpage.png` — captura full-page em viewport 390 px.

---

## Paleta de cores

| Token | Hex | Uso observado |
|---|---|---|
| `--color-primary` | `#4079BC` | Botão navbar, links principais |
| `--color-primary-dark` | `#346398` | Borda/hover do botão |
| `--color-accent` | `#FFD200` | Amarelo de destaque |
| `--color-text` | `#515151` | Texto geral |
| `--color-text-muted` | `#777777` | Texto secundário/meta |
| `--color-bg-subtle` | `#F8F8F8` | Fundo do nav |
| `--color-bg-light` | `#F5F5F5` | Seções alternadas |
| `--color-border` | `#E7E7E7` | Borda do nav |
| `--color-border-input` | `#E0E0E0` | Borda de inputs |
| `--color-accent` | `#FFD200` | Destaques |

**Nota:** a paleta é conservadora — azul institucional + branco/cinza + amarelo de alerta.
Sem gradientes ou cores vibrantes no conteúdo principal.

---

## Tipografia

| Fonte | Papel |
|---|---|
| **Titillium Web** | Headings (h1–h4), menu de navegação |
| **Open Sans** | Body, botões, inputs, spans, footer |

### Escala

| Tag | Tamanho | Peso | Line-height |
|---|---|---|---|
| h1 / h2 | 36 px | 500 | 39.6 px (1.1×) |
| h3 / h4 | 24 px | 500 | 26.4 px (1.1×) |
| p | 18 px | 700 | 18 px |
| a / link | 14 px | 700 | 20 px (1.43×) |
| button / span | 16 px | 400 | 16 px |
| input | 14 px | 400 | — |

---

## Espaçamento

O ritmo base é **15 px**. Os valores mais frequentes:

| Valor | Frequência | Contexto |
|---|---|---|
| `15px` | 56× | padding lateral geral |
| `0px 20px 0px 0px` | 7× | margem-right de ícones/itens |
| `0px 15px` | 5× | padding horizontal |
| `9px 20px` | 1× | padding do botão |

Escala de espaçamento WordPress preset (disponível via CSS var):
`0.44rem · 0.67rem · 1rem · 1.5rem · 2.25rem · 3.38rem · 5.06rem`

---

## Componentes

### Botão (navbar-toggle)
```css
background-color: #4079BC;
color: #fff;
border: 1px solid #346398;
border-radius: 0;
padding: 9px 20px;
font-family: "Open Sans", sans-serif;
font-size: 16px;
font-weight: 400;
```

### Input (campo-pesquisa)
```css
background-color: #fff;
color: #515151;
border: 1px solid #E0E0E0;
border-radius: 0;
padding: 15px 12px;
font-family: "Open Sans", sans-serif;
font-size: 14px;
```

### Nav / Header
```css
background-color: #F8F8F8;
border: 1px solid #E7E7E7;
color: #515151;
font-family: "Open Sans", sans-serif;
font-size: 16px;
```

### Footer (.servicos-rodape)
```css
color: #515151;
font-family: "Open Sans", sans-serif;
font-size: 16px;
padding: 0px 15px;
margin: 30px 0px 40px;
```
> Nota: o footer é um `<div class="rodape">`, não uma tag `<footer>` semântica.

### Card (menu item)
> O seletor `[class*='card']` capturou um `<li>` de menu. Cards de conteúdo
> precisam de inspeção manual — o site usa listas `<ul>/<li>` e `.post` classes.

---

## Limitações

- Animações, estados `:hover`, `:focus` e `:active` não são capturados por estilos computados — inspecione manualmente.
- O footer real usa classe `.rodape` (WordPress customizado), não a tag `<footer>`.
- Cards de notícias exigem scroll e seletor refinado (`.post`, `.entry`).
- Fidelidade de cor depende do perfil de cor do monitor; use os valores hex como referência.
