# Protótipo de Papel — Notificação Ativa

## Colaboração
Colaboração referente a [Etapa 5](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Heitor Macedo | Elaborou o Artefato |

---

## Introdução

O protótipo de papel é um método de prototipação de baixa fidelidade que permite explorar ideias de design de forma rápida e econômica, sem a necessidade de implementação. Segundo Barbosa et al. (2021), o método consiste em simular a interface com o usuário por meio de esboços em papel (ou equivalentes digitais de baixa fidelidade), possibilitando identificar problemas de usabilidade e comparar alternativas de design antes do investimento em soluções de maior fidelidade.

Este artefato apresenta o protótipo de papel desenvolvido para a funcionalidade de **Notificação Ativa de Reclamação** do sistema PROCON-DF. A funcionalidade visa eliminar a necessidade de consulta manual ao portal, enviando notificações automáticas (WhatsApp/SMS/e-mail) ao consumidor sempre que o status de sua reclamação for atualizado, acompanhadas de um painel visual de progresso em linguagem simples.

O protótipo foi elaborado com base na análise de tarefas (HTA e CTT), nos cenários de uso e na persona **Laura** — universitária de 22 anos, mobile-first, que precisa acompanhar sua reclamação nos intervalos de aula sem jargão jurídico.

---

## Fluxo Representado

O protótipo cobre as seguintes telas e interações:

1. **Notificação recebida** — mensagem ativa chegando ao dispositivo do usuário (WhatsApp/SMS)
2. **Tela de acesso** — autenticação simplificada ao portal
3. **Painel de reclamações** — lista com indicador de nova atualização
4. **Linha do tempo** — barra de progresso com etapas nomeadas e etapa atual destacada
5. **Visualização da proposta** — texto em linguagem simples com prazo de resposta
6. **Tela de decisão** — botões "Aceitar" e "Recusar" com modal de confirmação
7. **Confirmação** — tela de sucesso ou encaminhamento para próxima etapa

---

## Fotos do Protótipo de Papel

As imagens abaixo registram o protótipo de papel físico elaborado para a funcionalidade de Notificação Ativa, utilizado nas sessões de avaliação com usuários.

<div align="center">
  <p><b>Figura 2 — Protótipo de Papel (1/9)</b></p>
  <img src="../../images/IMG_3047.png" alt="Protótipo de papel - foto 1" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 3 — Protótipo de Papel (2/9)</b></p>
  <img src="../../images/IMG_3048.png" alt="Protótipo de papel - foto 2" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 4 — Protótipo de Papel (3/9)</b></p>
  <img src="../../images/IMG_3049.png" alt="Protótipo de papel - foto 3" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 5 — Protótipo de Papel (4/9)</b></p>
  <img src="../../images/IMG_3050.png" alt="Protótipo de papel - foto 4" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 6 — Protótipo de Papel (5/9)</b></p>
  <img src="../../images/IMG_3051.png" alt="Protótipo de papel - foto 5" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 7 — Protótipo de Papel (6/9)</b></p>
  <img src="../../images/IMG_3052.png" alt="Protótipo de papel - foto 6" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 8 — Protótipo de Papel (7/9)</b></p>
  <img src="../../images/IMG_3053.png" alt="Protótipo de papel - foto 7" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 9 — Protótipo de Papel (8/9)</b></p>
  <img src="../../images/IMG_3054.png" alt="Protótipo de papel - foto 8" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 10 — Protótipo de Papel (9/9)</b></p>
  <img src="../../images/IMG_3055.png" alt="Protótipo de papel - foto 9" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Heitor Macedo, 2026.</i></p></div>

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Clique nas telas para avançar no fluxo e simular a interação do usuário com a funcionalidade de Notificação Ativa.

<div align="center">
  <p><b>Figura 1 - Protótipo de Baixa Fidelidade — Notificação Ativa</b></p>
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
    src="../../Notificacao%20Ativa%20-%20Wireframe%20(standalone).html"
    width="100%"
    height="720"
    style="border:none;display:block;"
    title="Protótipo de Papel — Notificação Ativa PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Elaborado por Heitor Macedo com auxílio da ferrmante de inteligência artificial Claude.</i></p></div>

---

## Decisões de Design

As principais escolhas de design refletidas no protótipo são:

- **Canal de entrada via WhatsApp/SMS** — canal preferido pelo usuário identificado na análise de tarefas (HTA operação 0.0), com deep link direto para o portal
- **Barra de progresso estilo rastreamento** — analogia com rastreamento de pedido (iFood/Amazon), conforme expectativa da persona Laura
- **Linguagem simples** — sem jargão jurídico, conforme heurística de correspondência com o mundo real (Nielsen)
- **Modal de confirmação** — antes de qualquer ação irreversível (aceitar/recusar proposta), conforme recomendação IHC da HTA operação 3.0
- **Fallback de autenticação** — PIN ou código SMS caso a biometria falhe, conforme recomendação da HTA operação 3.1

---

## Referência

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Agradecimentos

Este artefato contou com o apoio do assistente de IA **Claude** (Anthropic), que colaborou nas seguintes frentes:

| Contribuição | Descrição |
|---|---|
| Estrutura e formatação do artefato | Organização das seções segundo as convenções do projeto (Colaboração, Introdução, Fluxo, Decisões de Design, Referência, Histórico de Versão) |
| Integração do protótipo via iframe | Identificação e correção do caminho relativo (`../`) considerando o `use_directory_urls` do MkDocs, adição da barra com botão de tela cheia |
| Apoio na codificação do HTML do protótipo | Suporte na estruturação do wireframe interativo em HTML — fluxo de telas, lógica de navegação e estilo visual de baixa fidelidade |

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 31/05/2026 | Criação do documento e adição do protótipo interativo. | Heitor Macedo | Pedro Augusto Moretti Moreira |
