# Protótipo de Papel — Validação de Documentos por OCR

## Colaboração
Colaboração referente a [Etapa 5](../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Heloisa Silva | Elaborou o Artefato |

---

## Introdução

O protótipo de papel é um método de prototipação de baixa fidelidade que permite explorar ideias de design de forma rápida e econômica, sem a necessidade de implementação. Este artefato apresenta o protótipo de papel desenvolvido para a funcionalidade de **Validação de Documentos por OCR** do sistema PROCON-DF. A funcionalidade visa permitir que usuários enviem documentos (foto ou PDF), processem OCR localmente/na nuvem, revejam campos extraídos e corrijam dados com indicadores de confiabilidade.

---

## Fluxo Representado

O protótipo cobre as seguintes telas e interações:

1. **Formulário de envio** — usuário preenche dados básicos e inicia o upload
2. **Upload / Pré-visualização** — confirmação da imagem/PDF antes do processamento
3. **Dados extraídos** — revisão dos campos extraídos com índices de confiança e edição manual
4. **Confirmação** — envio dos dados ao PROCON-DF e tela de sucesso

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Clique nas telas para avançar no fluxo e simular a interação do usuário com a funcionalidade de Validação por OCR.

<div align="center">
  <p><b>Figura - Protótipo de Baixa Fidelidade — Validação por OCR</b></p>
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
    src="../OCR%20validacao%20-%20Wireframe%20(standalone).html"
    width="100%"
    height="720"
    style="border:none;display:block;"
    title="Protótipo de Papel — Validação por OCR PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Elaborado por Heloisa Silva.</i></p></div>

---

## Decisões de Design

As principais escolhas de design refletidas no protótipo são:

- **Feedback de confiabilidade** — mostrar índices de confiança por campo para orientar revisão manual
- **Pré-visualização do documento** — permitir ao usuário confirmar imagem/PDF antes do processamento
- **Edição inline** — facilitar correção de campos com baixa confiança
- **Privacidade e segurança** — orientar sobre tratamento de dados sensíveis e limite de exposição
- **Simplicidade no fluxo** — manter passos claros: enviar → verificar → confirmar

---

## Referência

Documento desenvolvido como parte do projeto de IHC.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 31/05/2026 | Criação do documento e adição do protótipo interativo. | Heloisa Silva | — |
