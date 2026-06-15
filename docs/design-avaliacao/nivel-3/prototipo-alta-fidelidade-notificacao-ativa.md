# Protótipo de Alta Fidelidade — Notificação Ativa

## Colaboração
Colaboração referente a [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Heitor Macedo | Elaborou o Artefato |

---

## Introdução

Este artefato apresenta o **protótipo de alta fidelidade** desenvolvido para a funcionalidade de **Notificação Ativa** do sistema PROCON-DF. O protótipo foi construído em HTML, CSS e JavaScript, seguindo o [Guia de Estilo](../../analise-requisitos/guia-estilo.md) do projeto.

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
  <p><b>Figura 1 - Protótipo de Alta Fidelidade — Notificação Ativa PROCON-DF</b></p>
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
    src="../../prototipo-alta-fidelidade/notificacao-ativa/Notifica%C3%A7%C3%A3o%20Ativa%20PROCON-DF%20%28standalone%29.html"
    width="100%"
    height="820"
    style="border:none;display:block;"
    title="Protótipo de Alta Fidelidade — Notificação Ativa PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Heitor Macedo (2026).</i></p></div>

---

## Fluxo Representado

O protótipo cobre o fluxo completo da funcionalidade de Notificação Ativa:

1. **Notificação recebida no WhatsApp** — mensagem ativa com botão de acesso direto ao processo
2. **Tela de Login** — autenticação com CPF e senha (simulada no protótipo)
3. **Lista de Reclamações** — visão geral das reclamações abertas, com destaque para aquelas com atualizações pendentes
4. **Linha do Tempo (Timeline)** — exibição cronológica das etapas do processo com datas e status
5. **Visualização da Proposta da Empresa** — detalhamento do valor proposto, prazo e condições
6. **Tela de Resposta** — confirmação de aceite ou recusa da proposta
7. **Pop-up de Confirmação** — advertência sobre a irreversibilidade da decisão
8. **Tela de Protocolo** — número de protocolo, data e horário do aceite, chamada para assinatura
9. **Escolha do Método de Assinatura** — biometria ou GOV.BR
10. **Inserção de Código de Verificação** — código enviado por SMS para confirmação biométrica
11. **Tela de Sucesso** — acordo firmado e assinado, linha do tempo encerrada

---

## Arquitetura do Protótipo

| Camada | Tecnologia | Função |
|---|---|---|
| **Estrutura** | HTML5 | Marcação semântica de cada tela e fluxo de navegação |
| **Estilo** | CSS3 | Fidelidade visual ao guia de estilo do PROCON-DF (paleta, tipografia, componentes) |
| **Interatividade** | JavaScript (vanilla) | Gerencia a navegação entre telas e os estados dos componentes interativos |
| **Distribuição** | Standalone (single file) | Arquivo HTML autocontido, sem dependências de servidor |

---

## Decisões de Design

| Decisão | Justificativa |
|---|---|
| **Notificação via WhatsApp** | Canal de comunicação com maior penetração e familiaridade entre os usuários do PROCON-DF |
| **Timeline visual** | Recurso inexistente no portal atual; facilita o acompanhamento do processo sem necessidade de contato com a ouvidoria |
| **Pop-up de confirmação irreversível** | Prevenção de erros: o usuário deve estar ciente de que o aceite não pode ser desfeito |
| **Múltiplos métodos de assinatura** | Inclusão digital: biometria para usuários com dispositivos modernos, GOV.BR como alternativa acessível |
| **Login sem redigitação de dados** | No protótipo, CPF e senha são pré-preenchidos para simular sessão já autenticada |

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 14/06/2026 | Criação do documento e adição do protótipo de alta fidelidade interativo. | Heitor Macedo | Heitor Macedo |
