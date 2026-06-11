# Protótipo de Papel — Painel de Monitoramento de Prazos com Alertas Jurídicos

## Colaboração
Colaboração referente a [Etapa 5](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Mateus | Elaborou o Artefato |

---

## Introdução

O protótipo de papel é um método de prototipação de baixa fidelidade que permite explorar ideias de design de forma rápida e econômica, sem a necessidade de implementação. Segundo Barbosa et al. (2021), o método consiste em simular a interface com o usuário por meio de esboços em papel (ou equivalentes digitais de baixa fidelidade), possibilitando identificar problemas de usabilidade e comparar alternativas de design antes do investimento em soluções de maior fidelidade.

Este artefato apresenta o protótipo de papel desenvolvido para a funcionalidade de **Painel de Monitoramento de Prazos com Alertas Jurídicos** do sistema PROCON-DF. A funcionalidade visa oferecer ao consumidor um painel inteligente que exibe, em linguagem simples, todos os prazos legais vinculados à sua reclamação — incluindo o prazo de resposta da empresa (CDC, art. 49), datas de audiência, contagem regressiva do prazo de prescrição (CDC, art. 27) e encaminhamento automático ao Juizado Especial quando o prazo expira sem resolução.

O protótipo foi elaborado com base na análise de tarefas (HTA e CTT), nos cenários de uso e na persona **Carlos** — servidor público de 45 anos, pouco familiarizado com jargão jurídico, que precisa acompanhar sua reclamação de forma clara e ser avisado proativamente sobre vencimentos sem precisar consultar o portal manualmente.

---

## Fluxo Representado

O protótipo cobre as seguintes telas e interações:

1. **Painel principal (semáforo)** — visão geral com indicador de urgência colorido (🔴/🟡/🟢), prazo em destaque e cards de atalho para cada prazo relevante
2. **Linha do tempo** — barra de progresso do CDC e sequência visual de etapas (concluída / em andamento / futura), com botão de acionamento ao Juizado quando o prazo expira
3. **Prazo de prescrição** — contagem regressiva em dias com explicação em linguagem simples e base legal (art. 27 CDC)
4. **Acionar Juizado Especial** — orientação passo a passo sobre documentos necessários e localização do fórum mais próximo
5. **Alertas recebidos** — histórico de notificações push enviadas ao consumidor por WhatsApp/e-mail

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Clique nas telas para avançar no fluxo e simular a interação do usuário com a funcionalidade de Monitoramento de Prazos.

<div align="center">
  <p><b>Figura 1 - Protótipo de Baixa Fidelidade — Painel de Prazos com Alertas Jurídicos</b></p>
</div>

<div id="prototipo-wrapper" style="width:100%;border:2px solid #2b2b2b;border-radius:12px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.15);position:relative;">
  <div style="background:#2b2b2b;padding:8px 12px;display:flex;justify-content:flex-end;">
    <button
      onclick="(function(){var w=document.getElementById('prototipo-wrapper');var f=document.getElementById('prototipo-iframe');if(!document.fullscreenElement){w.requestFullscreen().then(function(){f.style.height='100vh';w.style.borderRadius='0';});} else {document.exitFullscreen().then(function(){f.style.height='720px';w.style.borderRadius='12px';});}})();"
      style="background:transparent;border:1px solid rgba(255,255,255,0.4);color:#fff;padding:4px 14px;border-radius:6px;cursor:pointer;font-size:13px;display:flex;align-items:center;gap:6px;">
      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" y1="3" x2="14" y2="10"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg>
      Tela cheia
    </button>
  </div>
  <iframe
    id="prototipo-iframe"
    src="../../Painel%20Prazos%20-%20Wireframe%20(standalone).html"
    width="100%"
    height="720"
    style="border:none;display:block;"
    title="Protótipo de Papel — Painel de Prazos PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Elaborado por Mateus.</i></p></div>

---

## Decisões de Design

As principais escolhas de design refletidas no protótipo são:

- **Semáforo de urgência (🔴/🟡/🟢)** — indicador visual imediato do nível de criticidade do prazo dominante, sem necessidade de leitura; inspirado em interfaces de rastreamento e apps de saúde
- **Contagem em dias em destaque** — número grande e legível como foco principal do painel, conforme heurística de visibilidade do status do sistema (Nielsen)
- **Linha do tempo estilo rastreamento** — analogia com rastreamento de encomenda (iFood/Correios), tornando etapas jurídicas compreensíveis para usuários sem formação legal
- **Linguagem simples sem jargão jurídico** — termos como "seu direito de ação caduca" em vez de "prazo prescricional extintivo", conforme heurística de correspondência com o mundo real (Nielsen)
- **Base legal sempre visível** — referência ao artigo do CDC exibida em cada prazo, permitindo verificação pelo usuário mais avançado sem poluir a interface principal
- **Botão "Acionar Juizado Especial" condicionado** — aparece apenas quando o prazo de resposta da empresa expira, evitando ação prematura e conforme recomendação da HTA (operação de encaminhamento)
- **Orientação passo a passo no Juizado** — lista de documentos e localização do fórum reduzem barreira de acesso à Justiça para usuários com baixa familiaridade jurídica
- **Histórico de alertas** — registro das notificações recebidas, mantendo o usuário orientado mesmo quando retorna ao app dias depois

---

## Referência

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Agradecimentos

Este artefato contou com o apoio do assistente de IA **Claude** (Anthropic), que colaborou nas seguintes frentes:

| Contribuição | Descrição |
|---|---|
| Estrutura e formatação do artefato | Organização das seções segundo as convenções do projeto (Colaboração, Introdução, Fluxo, Decisões de Design, Referência, Histórico de Versão) |
| Integração do protótipo via iframe | Identificação do caminho relativo considerando o `use_directory_urls` do MkDocs, adição da barra com botão de tela cheia |
| Apoio na codificação do HTML do protótipo | Suporte na estruturação do wireframe interativo em HTML — fluxo de telas, lógica de navegação, semáforo de urgência e estilo visual de baixa fidelidade |

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 31/05/2026 | Criação do documento e adição do protótipo interativo. | Mateus Barreto | — |
