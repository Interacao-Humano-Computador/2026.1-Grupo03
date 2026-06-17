# Protótipo de Alta Fidelidade — Painel de Monitoramento de Prazos com Alertas Jurídicos

## Colaboração
Colaboração referente a [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Mateus Rodrigues Barreto | Elaborou o Artefato |

---

## Introdução

Este artefato apresenta o **protótipo de alta fidelidade** desenvolvido para a funcionalidade de **Painel de Monitoramento de Prazos com Alertas Jurídicos** do sistema PROCON-DF. O protótipo foi construído em HTML, CSS e JavaScript, seguindo o [Guia de Estilo](../../analise-requisitos/guia-estilo.md) do projeto.

A funcionalidade visa oferecer ao consumidor um painel inteligente que exibe, em linguagem simples, todos os prazos legais vinculados à sua reclamação — incluindo o prazo de resposta da empresa (CDC, art. 49), datas de audiência, contagem regressiva do prazo de prescrição (CDC, art. 27) e encaminhamento ao Juizado Especial quando o prazo expira sem resolução. O protótipo também cobre a autenticação do consumidor no portal.

Diferentemente do protótipo de papel (baixa fidelidade), este protótipo incorpora:

- **Paleta de cores oficial** — Azul Principal, Amarelo Governo, Verde Sucesso e tons neutros conforme o guia de estilo
- **Tipografia oficial** — Titillium Web (títulos), Open Sans (corpo e UI), Montserrat
- **Padrões de componentes** — cartões, botões, timeline, campos de entrada, pop-ups, conforme especificado no guia de estilo
- **Interações realistas** — fluxo completo de login, validação de campos, simulação de biometria facial, navegação por abas e interação com a linha do tempo e checklist.

O protótipo foi elaborado com base na análise de tarefas (HTA e CTT), nos cenários de uso e na persona **Roberto** — gerente de logística de 52 anos, pragmático, com conhecimento básico de seus direitos, que precisa de um painel centralizado para acompanhar os prazos de resposta do fornecedor de forma clara e objetiva.

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Toque nos elementos para simular a interação do usuário com a funcionalidade.

<div align="center">
  <p><b>Figura 1 - Protótipo de Alta Fidelidade — Painel de Prazos PROCON-DF</b></p>
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
    src="../../prototipo-alta-fidelidade/painel-prazos/painel-prazos.html"
    width="100%"
    height="820"
    style="border:none;display:block;"
    title="Protótipo de Alta Fidelidade — Painel de Prazos PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Mateus Rodrigues Barreto (2026).</i></p></div>

---

## Fluxo Representado

O protótipo cobre o fluxo completo da funcionalidade de Painel de Prazos:

1. **Login** — autenticação por CPF e senha ou por biometria facial, com validação visual de campos e *fallback* em caso de falha no reconhecimento.
2. **Painel principal (Hero de status)** — visão geral com indicador de urgência colorido (que substitui o "semáforo" da versão em papel), prazo em destaque e lista com atalho para cada prazo relevante.
3. **Linha do tempo** — sequência visual de etapas (concluída / em andamento / futura), com alerta sobre o que ocorrerá quando o prazo de resposta da empresa expirar.
4. **Acionar Juizado Especial** — botão que simula a disponibilização de encaminhamento ao Juizado Especial e apresenta um checklist interativo de documentos necessários e localização do fórum mais próximo.
5. **Prazo de prescrição** — contagem regressiva em dias com explicação em linguagem simples e base legal (art. 27 CDC).
6. **Alertas recebidos** — histórico de notificações *push* enviadas ao consumidor por WhatsApp/e-mail, ajudando-o a se manter orientado.

---

## Arquitetura do Protótipo

| Camada | Tecnologia | Função |
|---|---|---|
| **Estrutura** | HTML5 | Marcação semântica de cada tela e fluxo de navegação |
| **Estilo** | CSS3 | Fidelidade visual ao guia de estilo do PROCON-DF (paleta, tipografia, componentes) |
| **Interatividade** | JavaScript (vanilla) | Gerencia a navegação entre telas, os estados dos componentes interativos (checagem de lista, simulação biométrica) e os pop-ups |
| **Distribuição** | Standalone (single file) | Arquivo HTML autocontido, sem dependências de servidor |

---

## Decisões de Design

As principais escolhas de design refletidas no protótipo de alta fidelidade são:

| Decisão | Justificativa |
|---|---|
| **Biometria facial na entrada** | Flexibiliza a autenticação e reduz o atrito, ideal para usuários com dificuldade de memorizar senhas, possuindo alternativa de fallback (CPF/senha) em caso de erro de leitura. |
| **Hero de status colorido** | Indicador visual imediato do nível de criticidade do prazo dominante, sem necessidade de leitura detalhada (substitui o semáforo de urgência da baixa fidelidade). |
| **Checklist interativo de documentos** | A lista de documentos obriga a marcação antes de liberar as próximas etapas, induzindo a preparação correta para o acesso ao Juizado Especial. |
| **Linha do tempo estilo rastreamento** | Analogia com rastreamento de encomendas que simplifica o entendimento das etapas processuais. |
| **Linguagem direta e não jurídica** | O jargão é minimizado ("seu direito de ação caduca" ao invés de termos como "decadência/prescrição"), enquanto as bases legais são mantidas discretas no canto da interface (Ex: "art. 27 CDC"). |

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
|---|---|---|---|---|
| 1.0 | 17/06/2026 | Criação do documento e adição do protótipo de alta fidelidade interativo. | Mateus Rodrigues Barreto | — |
