# Protótipo de Papel — Sala de Conciliação Virtual

## Colaboração
Colaboração referente a [Etapa 5](../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Pedro Moretti | Elaborou o Artefato |

---

## Introdução

O protótipo de papel é um método de prototipação de baixa fidelidade que permite explorar ideias de design de forma rápida e econômica, sem a necessidade de implementação. Segundo Barbosa et al. (2021), o método consiste em simular a interface com o usuário por meio de esboços em papel (ou equivalentes digitais de baixa fidelidade), possibilitando identificar problemas de usabilidade e comparar alternativas de design antes do investimento em soluções de maior fidelidade.

Este artefato apresenta o protótipo de papel desenvolvido para a funcionalidade de **Sala de Conciliação Virtual com Mediação Assistida** do sistema PROCON-DF. A funcionalidade visa eliminar a necessidade de deslocamento físico para audiências de conciliação, oferecendo um ambiente de videoconferência integrado com chat de evidências, mediação assistida e assinatura digital de acordos.

O protótipo foi elaborado com base na análise de tarefas (HTA e CTT), nos cenários de uso e nas personas **Lucas** — consumidor exigente, 34 anos, que valoriza eficiência técnica e privacidade — e **Gustavo** — microempreendedor que precisa resolver pendências sem fechar seu negócio.

---

## Fluxo Representado

O protótipo cobre as seguintes telas e interações:

1. **Notificação recebida** — mensagem ativa no WhatsApp com link direto para a sala virtual
2. **Sala de espera** — pré-chamada com contagem regressiva e lista de participantes
3. **Teste de periféricos** — verificação guiada de câmera e microfone com indicadores visuais
4. **Videoconferência** — sala principal com vídeo dos participantes, nomes/papéis fixos e controles de mídia
5. **Chat de evidências** — painel de troca de documentos com confirmação de entrega
6. **Termo de acordo** — minuta elaborada pelo mediador em linguagem simples
7. **Assinatura digital** — autenticação via Gov.br ou biometria facial
8. **Encerramento** — tela de sucesso (acordo firmado) ou comunicação de encerramento sem acordo

---

## Protótipo Interativo

O protótipo abaixo é navegável diretamente no navegador. Clique nas telas para avançar no fluxo e simular a interação do usuário com a funcionalidade de Sala de Conciliação Virtual.

<div align="center">
  <p><b>Figura 1 - Protótipo de Baixa Fidelidade — Sala de Conciliação Virtual</b></p>
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
    src="../Conciliacao%20Virtual%20-%20Wireframe%20(standalone).html"
    width="100%"
    height="720"
    style="border:none;display:block;"
    title="Protótipo de Papel — Sala de Conciliação Virtual PROCON-DF"
    allow="fullscreen">
  </iframe>
</div>

<div align="center"><p><i>Fonte: Elaborado por Pedro Moretti.</i></p></div>

---

## Decisões de Design

As principais escolhas de design refletidas no protótipo são:

- **Canal de entrada via WhatsApp** — notificação no canal preferencial, com deep link direto para a sala (HTA operação 1.1)
- **Sala de espera com contagem regressiva** — reduz ansiedade e informa o usuário sobre o horário, conforme recomendação HTA operação 2.1
- **Teste de periféricos obrigatório** — checklist visual de câmera e microfone antes da entrada, prevenindo falhas técnicas durante a audiência (HTA operação 2.2, heurística de prevenção de erros)
- **Nome e papel fixos nos vídeos** — etiquetas permanentes identificando Consumidor, Fornecedor e Mediador, conforme heurística de reconhecimento em vez de recordação (Nielsen)
- **Botões grandes de microfone/câmera** — controles sempre visíveis para mutar/desmutar, seguindo recomendação HTA operação 3.2
- **Chat de evidências integrado** — troca de documentos com confirmação de entrega e miniatura, conforme HTA operação 3.3
- **Termo em linguagem simples** — sem jargão jurídico, destacando valor e prazo (heurística de correspondência com o mundo real)
- **Assinatura digital via Gov.br ou biometria** — dupla opção de autenticação para diferentes perfis de usuário, conforme HTA operação 4.1
- **Próximo passo claro pós-encerramento** — tanto em caso de acordo quanto sem acordo, evitando sensação de abandono (HTA operação 4.2)

---

## Referência

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. *Interação Humano-Computador e Experiência do usuário*. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 31/05/2026 | Criação do documento e adição do protótipo interativo. | Pedro Moretti | Mateu Barreto |

