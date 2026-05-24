# Metas de Usabilidade

## Colaboração
Colaboração referente a [Etapa 3](../planejamento/cronograma-executado.md)

| Autores | Contribuiu |
|---|---|
| Heitor Macedo | Elaboração do Artefato  |
| Mateus Rodrigues Barreto | Inserção das imagens de comprovação bibliográfica |

## 1. Introdução
De acordo com a Engenharia de Usabilidade de Nielsen, descrita por Barbosa e Silva (2021) <sup><a href="#figura1">[1]</a></sup>, a definição das metas de usabilidade envolve estabelecer quais fatores de qualidade de uso devem ser priorizados no projeto. Para cada fator escolhido, é necessário definir como ele será avaliado, estabelecendo faixas de valores inaceitáveis, aceitáveis e ideais para os indicadores de interesse <sup><a href="#figura2">[2]</a></sup>.

Com base no Perfil de Usuário levantado para o sistema do PROCON-DF, selecionamos metas focadas na agilidade e na intuição, buscando garantir que os cidadãos e fornecedores consigam utilizar a plataforma sem frustrações e com o mínimo de carga cognitiva.

---

## 2. Razão da Seleção das Metas (Justificativa)
Conforme exigência da verificação do projeto, justificamos abaixo a escolha das metas prioritárias para o PROCON-DF, baseadas em evidências empíricas e totalmente alinhadas aos artefatos da Análise de Requisitos:

1. **Eficiência:** Selecionada pois o Grupo de Foco e a Análise de Tarefas (GOMS) evidenciaram uma forte aversão à burocracia excessiva e à alta carga cognitiva exigida na interface atual. O uso de tecnologias como OCR e o autocompletar visa maximizar a eficiência de entrada de dados, reduzindo o tempo de execução e a probabilidade de falhas operacionais, otimizando o fluxo de interação para cidadãos e fornecedores.
   > **Princípio Geral de Projeto Associado:** Promoção da Eficiência do Usuário; Simplicidade nas Estruturas das Tarefas.
2. **Facilidade de Aprendizado *(Learnability)*:** Fundamental para mitigar barreiras tecnológicas enfrentadas por perfis como Ivone (iniciante vulnerável) e Maria Helena (aposentada). Dado o caráter esporádico de uso do portal, a interface deve possuir um modelo conceitual claro e autoexplicativo (ex: Assistente de Triagem Guiada), permitindo que o usuário construa um mapa mental correto logo no primeiro acesso, eliminando a necessidade de treinamento prévio ou leitura de extensa documentação técnica.
   > **Princípio Geral de Projeto Associado:** Correspondência com as Expectativas dos Usuários; Conteúdo Relevante e Expressão Adequada.
3. **Satisfação do Usuário *(Satisfaction)*:** Escolhida para combater o atual quadro de elevada insatisfação e abandono do portal. O excesso de informações (poluição visual) e a ausência de amparo do sistema levam os usuários a optarem por alternativas privadas como o "Reclamje Aqui"(veja mais). Plataformas como esta oferecem uma experiência de usuário (UX) manifestamente superior, caracterizada por linguagem natural, *clean design* e *feedback* contínuo de status, atributos que elevam a percepção de valor, a confiança e a sensação de resolutividade. O redesign deve incorporar esses elementos para restaurar a credibilidade institucional do PROCON-DF.
   > **Princípio Geral de Projeto Associado:** Conteúdo Relevante e Expressão Adequada; Visibilidade e Reconhecimento.
4. **Segurança no Uso (Prevenção de Erros):** Inserida em decorrência da elevada taxa de erros documentada na Análise Documental (ex: anexos ilegíveis ou documentação incompleta). Essa meta fundamenta o desenvolvimento de mecanismos heurísticos de prevenção, como a validação automatizada via OCR e a testagem compulsória de periféricos (áudio/vídeo) antecedendo a sala de conciliação virtual. O objetivo é estabelecer restrições preventivas que resguardem usuários com menor fluência digital contra falhas sistêmicas ou operacionais.
   > **Princípio Geral de Projeto Associado:** Projeto para Erros; Antecipação das Necessidades do Usuário.
5. **Facilidade de Recordação *(Memorability)*:** Tendo em vista o acesso episódico ao PROCON-DF (fornecedores como Gustavo acessam anualmente; consumidores, apenas em episódios de lesão consumerista), o sistema não deve impor uma alta carga de memorização na memória de curto prazo do usuário. A aplicação de padrões de design universais (consistência interna e externa) e a clara visibilidade do estado do sistema asseguram que o usuário possa retomar e inferir processos com facilidade, mesmo após longos hiatos de interação, favorecendo o reconhecimento em vez da recordação.
   > **Princípio Geral de Projeto Associado:** Consistência e Padronização; Visibilidade e Reconhecimento; Equilíbrio entre Controle e Liberdade do Usuário.

---

## 3. Indicadores e Faixas de Valores
A tabela abaixo define os indicadores numéricos que comprovarão o sucesso do redesign do sistema, estruturados de acordo com as metas estabelecidas:

| Meta de Usabilidade | Princípio Geral Associado | Indicador de Medição | Valor Inaceitável | Valor Aceitável | Valor Ideal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Eficiência** | Promoção da Eficiência do Usuário | Tempo total gasto pelo usuário para registrar uma reclamação completa (incluindo anexos via OCR). | Mais de 10 minutos | Entre 5 e 10 minutos | Menos de 5 minutos |
| **Eficiência** | Simplicidade nas Estruturas das Tarefas | Tempo gasto por um fornecedor para visualizar uma notificação de denúncia no sistema. | Mais de 3 minutos | Entre 1 e 3 minutos | Menos de 1 minuto |
| **Facilidade de Aprendizado** | Correspondência com as Expectativas dos Usuários | Número de vezes que o usuário aciona a Ajuda/FAQ ou abandona o Assistente de Triagem no 1º uso. | Mais de 2 consultas | 1 ou 2 consultas | Nenhuma consulta (0) |
| **Facilidade de Aprendizado** | Conteúdo Relevante e Expressão Adequada | Taxa de conclusão com sucesso (ex: enviar a reclamação completa sem desistir). | Menos de 70% | Entre 70% e 90% | Acima de 90% |
| **Satisfação** | Visibilidade e Reconhecimento | Nota média atribuída pelos usuários em uma pesquisa de satisfação CSAT pós-uso (escala 1 a 5). | Nota inferior a 3 | Nota 3 ou 4 | Nota 5 (Excelente) |
| **Segurança no Uso** | Projeto para Erros | Taxa de processos barrados ou atrasados por envio de documentos ilegíveis/faltantes. | Mais de 15% | Entre 5% e 15% | Menos de 5% |
| **Segurança no Uso** | Antecipação das Necessidades do Usuário | Número de falhas técnicas de áudio/vídeo reportadas na Sala de Conciliação Virtual. | Mais de 3 incidentes/mês | 1 a 3 incidentes/mês | Zero (0) incidentes |
| **Facilidade de Recordação** | Consistência e Padronização | Tempo médio para realizar uma tarefa base após 3 meses sem acesso ao sistema. | Mais que o dobro do tempo do 1º uso | Até 50% a mais do tempo do 1º uso | Igual ou menor que o 1º uso |


---

## Metas de Usabilidade: Análise do PROCON-DF 
<div><a href="#"> </a></div>

A análise a seguir examina os principais fatores que levam usuários a abandonar o portal oficial do
[PROCON-DF](https://www.procon.df.gov.br/) em favor de alternativas como o
[Reclame Aqui](https://www.reclameaqui.com.br/) ou os canais de atendimento das próprias lojas online.
Essa avaliação é fundamentada nas metas de usabilidade propostas por Nielsen (1994 apud Barbosa et al., 2021) e Sharp, Rogers e Preece (2019 apud Barbosa et al., 2021), aplicadas à experiência de registro de reclamações no site avaliado.

---

### 1. Facilidade de Aprendizado *(Learnability)*

O menu principal do portal mistura itens institucionais ("Perfil do Diretor", "Agenda do Diretor-Geral"),
seções restritas a servidores públicos (SEI, SIGMANET, SIAPMED) e os serviços ao cidadão  todos no mesmo
nível hierárquico. Um usuário que acessa o site pela primeira vez com o objetivo de registrar uma reclamação
precisa de um esforço cognitivo considerável apenas para localizar o caminho correto.

Em contraste, o Reclame Aqui apresenta na página inicial um único campo de busca com a instrução direta
*"Pesquise a empresa e reclame"*, eliminando qualquer ambiguidade sobre o que o sistema permite fazer.

---

### 2. Eficiência *(Efficiency)*

O serviço de peticionamento eletrônico  equivalente ao "abrir reclamação"  está acessível apenas por meio
de `Serviços > Peticionamento Eletrônico`, uma nomenclatura técnico-burocrática que não corresponde ao
vocabulário do usuário comum. Além disso, o fluxo depende de autenticação via sistema externo do GDF (SEI),
impondo uma barreira de entrada que plataformas privadas eliminaram.

As lojas online como Mercado Livre e Amazon, por sua vez, oferecem o fluxo de reclamação embutido na própria
jornada de compra, com histórico do pedido, nota fiscal e conversa centralizados no mesmo ambiente 
reduzindo ao mínimo o esforço necessário para agir.

---

### 3. Facilidade de Memorização *(Memorability)*

Por não possuir um fluxo padronizado e reconhecível, o portal exige que o usuário reapenda o caminho a cada
novo acesso. A ausência de um *call-to-action* destacado na página inicial  como um botão "Registre sua
reclamação"  impede que o sistema seja reconhecido em vez de recordado, violando diretamente o heurístico
de Nielsen de *reconhecimento em vez de recordação*.

---

### 4. Baixa Taxa de Erros *(Errors)*

A ausência de feedback claro após o envio de uma reclamação  sem confirmação visual, prazo estimado ou
próximos passos em linguagem acessível  aumenta a probabilidade de o usuário abandonar o processo antes de
concluí-lo ou repetir ações por incerteza. O portal também apresentou, na análise do código-fonte,
vulnerabilidades que permitiram a injeção de links externos maliciosos (sites de apostas e conteúdo
inadequado), o que compromete diretamente a **confiança percebida** pelo usuário.

---

### 5. Satisfação *(Satisfaction)*

A percepção de eficácia é determinante para a satisfação. O Reclame Aqui utiliza a **exposição pública da
reputação das empresas** como mecanismo de pressão, gerando respostas mais rápidas e visíveis. Para o
usuário, isso representa resultado concreto e imediato  enquanto o rito administrativo do PROCON-DF é
percebido como lento e de desfecho incerto.

Essa diferença na **satisfação percebida** é o principal fator que orienta a escolha do usuário para fora do
canal oficial, independentemente da autoridade legal do órgão.

---

### Síntese

| Meta de Usabilidade | Situação no PROCON-DF |
|---|---|
| Facilidade de aprendizado | Arquitetura da informação voltada à estrutura institucional, não às tarefas do usuário |
| Eficiência | Fluxo burocrático com múltiplos passos e autenticação externa |
| Memorabilidade | Ausência de padrão reconhecível e de *call-to-action* visível |
| Baixa taxa de erros | Falta de feedback pós-envio e vulnerabilidades de segurança ativas |
| Satisfação | Percepção de lentidão e ineficácia em relação às alternativas privadas |

> O abandono do canal oficial não decorre de desconhecimento dos direitos do consumidor, mas de uma
> experiência de uso que não atende às metas básicas de usabilidade. Plataformas que reduzem fricção,
> entregam feedback imediato e criam pressão visível sobre as empresas conquistam a preferência do usuário
> independentemente da autoridade legal do órgão.

---
## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação deste documento e auxílio na análise do reclame aqui.


## Referência:
> BARBOSA, S. D. J. et al. **Interação Humano-Computador e Experiência do Usuário**. 1. ed. Rio de Janeiro: Autopublicação, 2021. ISBN 978-65-00-19677-1.

---

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.2` | 21/05/2026 | Formatação do documento. | Heitor Macêdo Ricardo | Pedro Moretti |
| `1.1` | 11/05/2026 | Inserção das imagens de comprovação bibliográfica. | Mateus Rodrigues Barreto | Pedro Moretti |
| `1.0` | 10/05/2026 | Elaboração das Metas de Usabilidade. | Heitor Macedo Ricardo | Pedro Moretti |

## Notas de Rodapé e Referências de Imagens

<br>

<div id="figura1" align="center">
  <p>Figura 1 - Fatores de Usabilidade de Nielsen</p>
  <img src="../fatores_de_nielsen.png" alt="Fatores de Usabilidade de Nielsen" width="800">
  <p><b>Fonte:</b> BARBOSA, S. D. J. et al. (2021, p. 35).</p>
</div>

<br>

<div id="figura2" align="center">
  <p>Figura 2 - Faixas de Valores para Indicadores de Usabilidade</p>
  <img src="../faixas_de_valores.png" alt="Faixas de Valores para Indicadores de Usabilidade" width="800">
  <p><b>Fonte:</b> BARBOSA, S. D. J. et al. (2021, p. 103).</p>
</div>