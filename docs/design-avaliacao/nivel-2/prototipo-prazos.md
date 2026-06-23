# Protótipo de Papel — Painel de Monitoramento de Prazos com Alertas Jurídicos

## Colaboração
Colaboração referente a [Etapa 5](../../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Mateus | Elaborou o Artefato |

---

## Introdução

O protótipo de papel é um método de prototipação de baixa fidelidade que permite explorar ideias de design de forma rápida e econômica, sem a necessidade de implementação. Segundo Barbosa et al. (2021), o método consiste em simular a interface com o usuário por meio de esboços em papel (ou equivalentes digitais de baixa fidelidade), possibilitando identificar problemas de usabilidade e comparar alternativas de design antes do investimento em soluções de maior fidelidade.

Este artefato apresenta o protótipo de papel desenvolvido para a funcionalidade de **Painel de Monitoramento de Prazos com Alertas Jurídicos** do sistema PROCON-DF. A funcionalidade visa oferecer ao consumidor um painel inteligente que exibe, em linguagem simples, todos os prazos legais vinculados à sua reclamação — incluindo o prazo de resposta da empresa (CDC, art. 49), datas de audiência, contagem regressiva do prazo de prescrição (CDC, art. 27) e encaminhamento ao Juizado Especial quando o prazo expira sem resolução. O protótipo também cobre a autenticação do consumidor no portal, etapa anterior ao acesso ao painel.

O protótipo foi elaborado com base na análise de tarefas (HTA e CTT), nos cenários de uso e na persona **Carlos** — servidor público de 45 anos, pouco familiarizado com jargão jurídico, que precisa acompanhar sua reclamação de forma clara e ser avisado proativamente sobre vencimentos sem precisar consultar o portal manualmente.

---

## Fluxo Representado

O protótipo cobre as seguintes telas e interações:

1. **Login** — autenticação por CPF e senha ou por biometria facial, com validação visual de campos e fallback em caso de falha no reconhecimento
2. **Minhas Reclamações** — tela intermediária exibida logo após o login, listando todas as reclamações do consumidor (em andamento e encerradas) com badges de status; permite selecionar qual reclamação acompanhar ou adicionar um protocolo existente
3. **Adicionar Protocolo** — tela para vincular uma reclamação já registrada no PROCON-DF à conta do usuário, com campo de busca por número de protocolo, estados de "buscando" e "encontrado/não encontrado" simulados e dica de onde localizar o número
4. **Painel principal (semáforo)** — visão geral com indicador de urgência colorido, prazo em destaque e lista com atalho para cada prazo relevante
5. **Linha do tempo** — sequência visual de etapas (concluída / em andamento / futura), com botão de acionamento ao Juizado quando o prazo de resposta da empresa expira
6. **Prazo de prescrição** — contagem regressiva em dias com explicação em linguagem simples e base legal (art. 27 CDC)
7. **Acionar Juizado Especial** — checklist interativo de documentos necessários, com confirmação obrigatória de cada item antes da liberação do botão de salvar orientações, e localização do fórum mais próximo
8. **Alertas recebidos** — histórico de notificações push enviadas ao consumidor por WhatsApp/e-mail

---

## Fotos do Protótipo de Papel

As imagens abaixo registram o protótipo de papel físico elaborado para a funcionalidade de Monitoramento de Prazos, utilizado nas sessões de avaliação com usuários.

<div align="center">
  <p><b>Figura 2 — Protótipo de Papel (1/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-1.jpg" alt="Protótipo de papel - foto 1" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 3 — Protótipo de Papel (2/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-2.jpg" alt="Protótipo de papel - foto 2" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 4 — Protótipo de Papel (3/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-3.jpg" alt="Protótipo de papel - foto 3" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 5 — Protótipo de Papel (4/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-4.jpg" alt="Protótipo de papel - foto 4" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 6 — Protótipo de Papel (5/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-5.jpg" alt="Protótipo de papel - foto 5" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 7 — Protótipo de Papel (6/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-6.jpg" alt="Protótipo de papel - foto 6" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 8 — Protótipo de Papel (7/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-7.jpg" alt="Protótipo de papel - foto 7" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

---

<div align="center">
  <p><b>Figura 9 — Protótipo de Papel (8/8)</b></p>
  <img src="../../images/pp_telas/pp-painel-8.jpg" alt="Protótipo de papel - foto 8" style="max-width:700px;width:100%;border-radius:8px;">
</div>

<div align="center"><p><i>Fonte: Mateus Barreto, 2026.</i></p></div>

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

- **Autenticação com dois caminhos** — CPF/senha ou biometria facial, com fallback explícito em caso de falha no reconhecimento, conforme recomendação da HTA quanto à flexibilidade de acesso para diferentes perfis de usuário
- **Tela de seleção de reclamação pós-login** — em vez de exibir diretamente um único painel, o fluxo passa por uma lista de reclamações do usuário, tornando o protótipo mais realista para consumidores com múltiplos registros ativos; a tela distingue visualmente reclamações em andamento (com badge de urgência) e encerradas
- **Adição de protocolo existente** — fluxo dedicado para vincular reclamações já registradas no PROCON-DF, com feedback de "buscando", "não encontrado" e "encontrado" para demonstrar os estados possíveis da operação
- **Semáforo de urgência** — indicador visual imediato do nível de criticidade do prazo dominante, sem necessidade de leitura; inspirado em interfaces de rastreamento e apps de saúde
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
| 1.1 | 17/06/2026 | Adição de novas telas ao protótipo. | Mateus Barreto | — |
| 1.2 | 19/06/2026 | Adição das telas "Minhas Reclamações" e "Adicionar Protocolo"; login passa a redirecionar para seleção de reclamação. | Mateus Barreto | — |
| 1.3 | 22/06/2026 | Adição das imagens do protótipo de papel e reestruturação do layout do artefato. | Mateus Barreto | — |