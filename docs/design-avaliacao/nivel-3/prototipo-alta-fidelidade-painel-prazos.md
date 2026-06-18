# Protótipo de Alta Fidelidade — Painel de Monitoramento de Prazos com Alertas Jurídicos

## Colaboração
Colaboração referente a [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Mateus Barreto | Elaborou o Artefato |

---

## Introdução

Este artefato apresenta o **protótipo de alta fidelidade** desenvolvido para a funcionalidade de **Painel de Monitoramento de Prazos com Alertas Jurídicos** do sistema PROCON-DF. O protótipo foi construído em HTML, CSS e JavaScript, seguindo o [Guia de Estilo](../../analise-requisitos/guia-estilo.md) do projeto.

A funcionalidade permite que o cidadão acompanhe, em linguagem simples, todos os prazos legais vinculados à sua reclamação — incluindo o prazo de resposta da empresa (CDC, art. 49), datas de audiência, contagem regressiva do prazo de prescrição (CDC, art. 27) e o encaminhamento ao Juizado Especial quando o prazo expira sem resolução, sem necessidade de consulta manual ao portal.

Diferentemente do protótipo de papel (baixa fidelidade), este protótipo incorpora:

- **Paleta de cores oficial** — Azul Principal (#4079BC), Amarelo Governo (#FFD200), Verde (#29BCB6), Magenta (#A93D8E) e Vermelho (#CF2E2E), conforme o guia de estilo
- **Tipografia oficial** — Titillium Web (títulos), Open Sans (corpo) e Montserrat (elementos de interface)
- **Padrões de componentes** — cartões de destaque, badges de status, linha do tempo com indicadores de progresso, checklist interativo, modal de confirmação, conforme especificado no guia de estilo
- **Interações realistas** — fluxo completo de login (CPF/senha ou biometria), navegação entre prazos, acionamento condicionado do Juizado Especial e confirmação de documentos via checklist

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Toque nos elementos para simular a interação do usuário com a funcionalidade.

<div align="center">
  <p><b>Figura 1 - Protótipo de Alta Fidelidade — Painel de Prazos PROCON-DF</b></p>
</div>

<div id="prototipo-wrapper" style="width:100%;border:1px solid #E2E8F0;border-radius:12px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.1);position:relative;">
  <div style="background:#2D3748;padding:8px 12px;display:flex;justify-content:flex-end;">
    <button
      onclick="(function(){var w=document.getElementById('prototipo-wrapper');var f=document.getElementById('prototipo-iframe');if(!document.fullscreenElement){w.requestFullscreen().then(function(){f.style.height='100vh';w.style.borderRadius='0';});} else {document.exitFullscreen().then(function(){f.style.height='900px';w.style.borderRadius='12px';});}})();"
      style="background:transparent;border:1px solid rgba(255,255,255,0.4);color:#fff;padding:4px 14px;border-radius:6px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:6px;">
      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" y1="3" x2="14" y2="10"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg>
      Tela cheia
    </button>
  </div>
  <iframe
    id="prototipo-iframe"
    src="../../prototipo-alta-fidelidade/painel-prazos/painel-prazos.html"
    width="100%"
    height="900"
    style="border:none;display:block;"
    title="Protótipo de Alta Fidelidade — Painel de Prazos PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Mateus Barreto (2026).</i></p></div>

---

## Fluxo Representado

O protótipo cobre o fluxo completo da funcionalidade de Painel de Prazos:

1. **Tela de Login** — autenticação com CPF e senha, com máscara automática de formatação e alternativa de biometria facial
2. **Painel Principal** — destaque do prazo mais urgente em cartão colorido por nível de criticidade, seguido da lista completa de prazos da reclamação
3. **Linha do Tempo** — exibição cronológica das etapas do processo (concluídas, em andamento e futuras), com indicadores visuais de progresso
4. **Prazo de Prescrição** — contagem regressiva em dias até a caducidade do direito de ação, com explicação em linguagem simples e base legal
5. **Acionar Juizado Especial** — tela exibida quando o prazo de resposta da empresa expira, com checklist interativo de documentos necessários e localização do fórum
6. **Modal de Confirmação** — pop-up de sucesso ao salvar as orientações do Juizado Especial
7. **Alertas Recebidos** — histórico de notificações enviadas ao consumidor por WhatsApp e e-mail

---

## Arquitetura do Protótipo

| Camada | Tecnologia | Função |
|---|---|---|
| **Estrutura** | HTML5 | Marcação semântica de cada tela e fluxo de navegação |
| **Estilo** | CSS3 | Fidelidade visual ao guia de estilo do PROCON-DF (paleta, tipografia, componentes) |
| **Interatividade** | JavaScript (vanilla) | Gerencia a navegação entre telas, validação de campos, checklist interativo e estado do modal |
| **Distribuição** | Standalone (single file) | Arquivo HTML autocontido, sem dependências de servidor |

---

## Decisões de Design

| Decisão | Justificativa |
|---|---|
| **Cartão de destaque colorido por criticidade** | Substitui o "semáforo" do protótipo de papel por um componente de maior fidelidade visual, mantendo a comunicação imediata do nível de urgência sem necessidade de leitura |
| **Biometria com falha simulada na primeira tentativa** | Representa o fluxo de fallback de autenticação de forma realista, permitindo observar a reação do usuário diante de uma falha de reconhecimento |
| **Um único caminho para o Juizado Especial** | O botão "Acionar Juizado Especial" existe apenas na Linha do Tempo, vinculado exclusivamente à expiração do prazo de resposta da empresa, evitando que o usuário confunda esse gatilho com o da Prescrição |
| **Checklist interativo com botão condicionado** | Cada documento necessário deve ser marcado individualmente; o botão de confirmação só é liberado quando todos os itens são conferidos, reforçando a prevenção de erros antes de uma ação importante |
| **Modal de confirmação ao salvar orientações** | Fornece feedback explícito de sucesso da ação, em vez de apenas navegar silenciosamente para outra tela |
| **Base legal sempre visível** | Referência ao artigo do CDC exibida em cada prazo, permitindo verificação pelo usuário mais avançado sem poluir a interface principal |

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 18/06/2026 | Criação do documento e adição do protótipo de alta fidelidade interativo. | Mateus Barreto | — |