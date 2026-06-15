# Protótipos de Alta Fidelidade

## Colaboração

Colaboração referente à [Etapa 7](../../planejamento/cronograma-executado.md)

| Autores       | Contribuiu          |
| ------------- | ------------------- |
| Pedro Moretti | Elaborou o Artefato |
| Heitor Macedo | Elaborou o Artefato |
| Pedro Macedo  | Elaborou o Artefato |

---

## Introdução

Esta página consolida todos os **protótipos de alta fidelidade** desenvolvidos para o sistema PROCON-DF. Cada protótipo implementa uma funcionalidade específica do sistema em HTML, CSS e JavaScript, seguindo o [Guia de Estilo](../../analise-requisitos/guia-estilo.md) do projeto — incluindo paleta de cores oficial, tipografia e padrões de componentes.

Os protótipos são interativos e navegáveis diretamente no navegador, permitindo simular o fluxo completo de interação do usuário.

---

## Protótipos Disponíveis

| Funcionalidade               | Descrição                                                                                                              | Fluxo                                   | Acesso                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------- |
| Sala de Conciliação Virtual  | Videoconferência com mediação assistida, chat de evidências e assinatura digital                                       | 8 telas (notificação → encerramento)    | [Acessar protótipo](prototipo-alta-fidelidade-conciliacao.md)       |
| Notificação Ativa            | Recebimento de notificação via WhatsApp, acompanhamento da linha do tempo e resposta à proposta com assinatura digital | 11 telas (notificação → acordo firmado) | [Acessar protótipo](prototipo-alta-fidelidade-notificacao-ativa.md) |
| Assistente de Triagem Guiada | Reclamação de algum objeto                                                                                             | 7 telas (reclamação → notificação)      | [Acessar protótipo](prototipo-alta-fidelidade-triagem-guiada.md)    |

### Sala de Conciliação Virtual

Cobre o fluxo completo de uma audiência de conciliação virtual: o cidadão recebe uma notificação no WhatsApp, entra na sala de espera, testa periféricos, participa da videoconferência, troca documentos no chat de evidências, revisa e assina digitalmente o termo de acordo via Gov.br, e finaliza com a tela de encerramento.

### Notificação Ativa

Cobre o fluxo completo da funcionalidade de notificação ativa: o cidadão recebe uma notificação diretamente no WhatsApp sobre uma atualização em sua reclamação, realiza login, acessa a lista de reclamações, visualiza a linha do tempo do processo, revisa a proposta da empresa, aceita-a e assina digitalmente por biometria ou GOV.BR, finalizando com a tela de acordo firmado.

---

## Protótipos Planejados

Os seguintes protótipos de alta fidelidade estão previstos com base nos [protótipos de papel](../nivel-2/prototipo-conciliacao.md) existentes:

| Funcionalidade                    | Protótipo de Papel                         |
| --------------------------------- | ------------------------------------------ |
| Notificação Ativa                 | [Acessar](../nivel-2/prototipo.md)         |
| Validação por OCR                 | [Acessar](../nivel-2/prototipo-ocr.md)     |
| Painel de Monitoramento de Prazos | [Acessar](../nivel-2/prototipo-prazos.md)  |
| Assistente de Triagem Guiada      | [Acessar](../nivel-2/prototipo-triagem.md) |

---

## Resultados Consolidados

A avaliação do protótipo de alta fidelidade segue o framework DECIDE, conforme detalhado no [planejamento de avaliação](planejamento-avaliacao-prototipo-alta-fidelidade.md). Os resultados serão registrados seguindo a estrutura definida no [planejamento do relato de resultados](planejamento-relato-resultados-paf.md).

| Funcionalidade              | Status da Avaliação | Principais Achados                                                                                             |
| --------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------- |
| Sala de Conciliação Virtual | ✅ Concluída        | Sem problemas identificados — protótipo validado integralmente                                                 |
| Notificação Ativa           | ✅ Concluída        | 1 problema cosmético (baixa visibilidade do prazo de crédito) + 1 sugestão (3ª opção de assinatura via PROCON) |

---

## Agradecimentos à IA

Agradecimento ao **DeepSeek** pelo auxílio na estruturação deste arquivo.

---

## Referências

> BARBOSA, S. D. J.; SILVA, B. S.; SILVEIRA, M. S.; GASPARINI, I.; DARIN, T.; BARBOSA, G. D. J. _Interação Humano-Computador e Experiência do usuário_. Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data       | Descrição                                                                           | Autor(es)     | Revisor(es)   |
| ------ | ---------- | ----------------------------------------------------------------------------------- | ------------- | ------------- |
| 1.0    | 11/06/2026 | Criação da página de consolidação dos protótipos de alta fidelidade.                | Pedro Moretti | Heitor Macedo |
| 1.1    | 14/06/2026 | Adição do protótipo de Notificação Ativa e atualização dos resultados consolidados. | Heitor Macedo | Heitor Macedo |
