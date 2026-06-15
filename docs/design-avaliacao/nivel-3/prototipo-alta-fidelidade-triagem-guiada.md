# Protótipo de Alta Fidelidade — Assistente de Triagem Guiada

## Colaboração

Colaboração referente a [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores      | Contribuiu          |
| ------------ | ------------------- |
| Pedro Macedo | Elaborou o Artefato |

---

## Introdução

Este artefato apresenta o **protótipo de alta fidelidade** desenvolvido para a funcionalidade de **Asistente de Triagem Guiada** do sistema PROCON-DF. O protótipo foi construído em HTML, CSS e JavaScript, seguindo o [Guia de Estilo](../../analise-requisitos/guia-estilo.md) do projeto.

A funcionalidade de Notificação Ativa permite que o cidadão receba uma notificação diretamente no WhatsApp quando há uma atualização em seu processo de reclamação no PROCON-DF, acesse a linha do tempo do processo com um único toque e responda a propostas de acordo com a empresa — incluindo a assinatura digital — de forma completamente remota e sem deslocamento.

Diferentemente do protótipo de papel (baixa fidelidade), este protótipo incorpora:

- **Paleta de cores oficial** — Azul Principal (#4079BC), Amarelo Governo (#FFD200), Verde Sucesso e tons neutros conforme o guia de estilo
- **Tipografia oficial** — Titillium Web (títulos), Open Sans (corpo e UI)
- **Padrões de componentes** — cartões, botões, timeline, campos, pop-ups, conforme especificado no guia de estilo
- **Interações realistas** — fluxo completo de notificação, login, visualização de proposta, aceite, assinatura por biometria e por GOV.BR

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Toque nos elementos para simular a interação do usuário com a funcionalidade.

<div align="center">
  <p><b>Figura 1 - Protótipo de Alta Fidelidade — Assistente de Triagem Guiada PROCON-DF</b></p>
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
    src="../../prototipo-alta-fidelidade/triagem-guiada/triagem-guiada.html"
    width="100%"
    height="820"
    style="border:none;display:block;"
    title="Protótipo de Alta Fidelidade — Assistente de Triagem Guiada PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Pedro Macedo (2026).</i></p></div>

---

## Fluxo Representado

O protótipo cobre o fluxo completo da funcionalidade de Notificação Ativa:

- **Tela 1:** Home do PROCON-DF Limpa — Foco total no grande botão central de alto contraste para iniciar a queixa.
- **Tela 2:** Seleção de Categoria — Cards e ícones grandes que facilitam a classificação do problema por reconhecimento.
- **Tela 3:** Filtro de Contato Prévio — Pergunta direta com botões simples de "Sim" ou "Não" sobre tentativas com a empresa.
- **Tela 4:** Painel de Linguagem Cidadã — Explicação clara do papel do PROCON em tom acolhedor e pedagógico.
- **Tela 5:** Identificação Integrada — Tela de transição e autenticação segura via Gov.br simplificado.
- **Tela 6:** Upload Guiado de Evidências — Área otimizada para capturar fotos de comprovantes diretamente pela câmera do celular.
- **Tela 7:** Tela de Sucesso e Protocolo — Exibição do número de protocolo em destaque e confirmação de envio de alertas via WhatsApp.

---

## Arquitetura do Protótipo

| Camada             | Tecnologia               | Função                                                                             |
| ------------------ | ------------------------ | ---------------------------------------------------------------------------------- |
| **Estrutura**      | HTML5                    | Marcação semântica de cada tela e fluxo de navegação                               |
| **Estilo**         | CSS3                     | Fidelidade visual ao guia de estilo do PROCON-DF (paleta, tipografia, componentes) |
| **Interatividade** | JavaScript (vanilla)     | Gerencia a navegação entre telas e os estados dos componentes interativos          |
| **Distribuição**   | Standalone (single file) | Arquivo HTML autocontido, sem dependências de servidor                             |

---

## Decisões de Design

| Decisão                                              | Justificativa                                                                                                        |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Botão central de alto contraste na home**          | Foco total na ação principal (“Iniciar queixa”), reduzindo carga cognitiva e atrito inicial.                         |
| **Cards com ícones grandes na seleção de categoria** | Facilita o reconhecimento visual e a classificação rápida do problema, especialmente em dispositivos móveis.         |
| **Pergunta direta “Sim/Não” sobre contato prévio**   | Simplifica a triagem e adapta o fluxo à experiência real do usuário (se já tentou resolver ou não).                  |
| **Painel de “linguagem cidadã”**                     | Explica o papel do PROCON de forma acolhedora e sem juridiquês, aumentando a confiança e a compreensão.              |
| **Autenticação integrada via GOV.BR**                | Reutiliza dados oficiais, evita cadastros repetidos e garante segurança com nível de identidade já validado.         |
| **Captura de evidências diretamente pela câmera**    | Otimiza o processo em mobile, eliminando a necessidade de salvar arquivos previamente e reduzindo abandono.          |
| **Exibição do protocolo em destaque**                | Garante que o usuário memorize ou anote o número da reclamação, essencial para acompanhamento futuro.                |
| **Confirmação de envio de alertas via WhatsApp**     | Aproveita o canal de maior penetração e familiaridade entre os cidadãos, mantendo o usuário informado proativamente. |

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. _Interação Humano-Computador e Experiência do usuário_. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data       | Descrição                                                                 | Autor(es)    | Revisor(es)   |
| ------ | ---------- | ------------------------------------------------------------------------- | ------------ | ------------- |
| 1.0    | 15/06/2026 | Criação do documento e adição do protótipo de alta fidelidade interativo. | Pedro Macedo | Heitor Macedo |
