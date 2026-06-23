# Protótipo de Alta Fidelidade — Sala de Conciliação Virtual

## Colaboração
Colaboração referente a [Etapa 5](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Augusto Moretti Moreira | Elaborou o Artefato |

---

## Introdução

Este artefato apresenta o **protótipo de alta fidelidade** desenvolvido para a funcionalidade de **Sala de Conciliação Virtual com Mediação Assistida** do sistema PROCON-DF. O protótipo foi construído em HTML, CSS (Tailwind) e JavaScript, seguindo o [Guia de Estilo](../../analise-requisitos/guia-estilo.md) do projeto.

Diferentemente do protótipo de papel (baixa fidelidade), este protótipo incorpora:

- **Paleta de cores oficial** — Azul Principal (#4079BC), Magenta CTA (#A93D8E), Amarelo Governo (#FFD200), Verde Sucesso (#29BCB6)
- **Tipografia oficial** — Titillium Web (títulos), Open Sans (corpo), Montserrat (botões e UI)
- **Padrões de componentes** — cartões, botões, campos, conforme especificado no guia de estilo
- **Interações realistas** — toggle de microfone/câmera, fluxo de assinatura Gov.br

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Toque nos elementos para simular a interação do usuário com a funcionalidade.

<div align="center">
  <p><b>Figura 1 - Protótipo de Alta Fidelidade — Sala de Conciliação Virtual</b></p>
</div>

<div id="prototipo-wrapper" style="width:100%;border:1px solid #E2E8F0;border-radius:12px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.1);position:relative;">
  <div style="background:#2D3748;padding:8px 12px;display:flex;justify-content:flex-end;">
    <button
      onclick="(function(){var w=document.getElementById('prototipo-wrapper');var f=document.getElementById('prototipo-iframe');if(!document.fullscreenElement){w.requestFullscreen().then(function(){f.style.height='100vh';w.style.borderRadius='0';});} else {document.exitFullscreen().then(function(){f.style.height='820px';w.style.borderRadius='12px';});}})();"
      style="background:transparent;border:1px solid rgba(255,255,255,0.4);color:#fff;padding:4px 14px;border-radius:6px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:6px;">
      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" y1="3" x2="14" y2="10"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg>
      Tela cheia
    </button>
  </div>
  <iframe
    id="prototipo-iframe"
    src="../../prototipo-alta-fidelidade/conciliacao-virtual/index.html"
    width="100%"
    height="820"
    style="border:none;display:block;"
    title="Protótipo de Alta Fidelidade — Sala de Conciliação Virtual PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Pedro Augusto Moretti Moreira (2026).</i></p></div>

---

## Fluxo Representado

O protótipo cobre as mesmas 8 telas do fluxo de conciliação:

1. **Notificação recebida** — mensagem no WhatsApp com link direto para a sala virtual
2. **Sala de espera** — pré-chamada com contagem regressiva e lista de participantes
3. **Teste de periféricos** — verificação guiada de câmera e microfone com indicadores visuais
4. **Videoconferência** — sala principal com vídeo dos participantes, nomes/papéis fixos e controles de mídia
5. **Chat de evidências** — painel de troca de documentos com confirmação de entrega
6. **Termo de acordo** — minuta elaborada pelo mediador em linguagem simples
7. **Assinatura digital** — autenticação via Gov.br
8. **Encerramento** — tela de sucesso (acordo firmado) ou comunicação de encerramento sem acordo

---

## Arquitetura do Protótipo

O protótipo foi construído com a seguinte pilha tecnológica:

| Camada | Tecnologia | Função |
|---|---|---|
| **Estrutura** | HTML5 | Marcação semântica de cada tela e componentes de interface |
| **Estilo** | CSS3 + Tailwind (CDN) | CSS customizado para componentes reutilizáveis. Tailwind via CDN para utilitários de layout, espaçamento e tipografia |
| **Interatividade** | JavaScript (vanilla) | Gerencia navegação entre as 8 telas, controle de estados (microfone ativo/desligado, câmera) e atualização dos controles de avanço/retrocesso |
| **Tipografia** | Google Fonts | Titillium Web (títulos), Open Sans (corpo), Montserrat (botões e UI) — conforme [guia de estilo](../../analise-requisitos/guia-estilo.md) |
| **Embutimento** | iframe aninhado | Cada tela é uma página HTML independente carregada via iframe no `index.html`, que simula um dispositivo móvel com moldura de telefone |

A opção por **Tailwind via CDN** eliminou a necessidade de configuração de build (webpack/vite), agilizando a prototipagem. O **CSS customizado** garantiu fidelidade visual ao guia de estilo do PROCON-DF. O **JavaScript vanilla** manteve o protótipo leve e sem dependências externas.

---

## Decisões de Design

| Decisão | Justificativa |
|---|---|
| **Magenta para CTA** | Conforme guia de estilo, contraste intencional para guiar a conversão |
| **Cartões sem bordas arredondadas** | Padrão do portal PROCON-DF — cartões com bordas retas |
| **Amarelo no topo gov** | Identidade visual do governo no topo da interface (guia de estilo, seção 3.4) |
| **Titillium Web em títulos** | Hierarquia visual com impacto e legibilidade (guia de estilo, seção 3.3) |
| **Montserrat em botões** | Elementos de interação com tipografia clara (guia de estilo, seção 3.3) |
| **Transições de 0,12s a 0,15s** | Movimentos suaves conforme guia de estilo, seção 3.6 |

---

## Agradecimentos

Agradecimento ao **DeepSeek** pelo auxílio na estruturação do design do protótipo de alta fidelidade em HTML/CSS/JavaScript, seguindo as diretrizes do guia de estilo do PROCON-DF.

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 11/06/2026 | Criação do documento e adição do protótipo de alta fidelidade interativo. | Pedro Augusto Moretti Moreira | — |
| 1.1 | 11/06/2026 | Adição da seção de arquitetura do protótipo (HTML, CSS, Tailwind, JS). | Pedro Augusto Moretti Moreira | — |
