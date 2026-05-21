# Princípios Gerais do Projeto

## Colaboração
Colaboração referente a [Etapa 3](../planejamento/cronograma-executado.md)
| Autores | Contribuiu |
|---|---|
| Heitor Macedo | Elaborou o Artefato  |

## 1. Introdução
Para que um modelo conceitual atenda às necessidades de um determinado usuário e permita um aprendizado de forma natural e rápida, a interface deve seguir Princípios e Diretrizes Gerais de Interação Humano-Computador (IHC). Segundo Barbosa *et al.* (2021)<sup><a href="#figura0">[1]</a></sup>, a aplicação adequada de boa parte dos princípios depende do conhecimento do designer acerca do domínio do problema, dos usuários e de suas atividades. 

Sendo assim, o design deve facilitar a determinação de quais ações são possíveis, o esclarecimento visual do estado do sistema e a avaliação das consequências das ações do usuário.

**Autor:** Heitor Macedo Ricardo

---

## 2. Metodologia
Para a definição dos princípios que guiarão o reprojeto do PROCON-DF, buscou-se levantar as vicissitudes presentes no site atual que violam os Princípios Gerais de Projeto exigidos na literatura. O documento foi estruturado em tópicos contendo a **Definição** teórica do princípio e a **Violação** encontrada no sistema atual. A análise foi realizada com base no perfil de usuário e nas dores relatadas durante as pesquisas de campo.

---

## 3. Análise dos Princípios e Violações

### 3.1 Correspondência com as expectativas dos usuários
- **Definição:** Segundo Barbosa *et al.* (2021)<sup><a href="#figura1">[2]</a></sup>, o designer deve explorar os mapeamentos naturais e utilizar o idioma do usuário, com palavras, expressões e conceitos que lhe são familiares, em vez de utilizar termos orientados ao sistema ou jargões. O sistema deve seguir as convenções do mundo real.

- **Violação no PROCON-DF:** No site atual, o vocabulário é altamente técnico e voltado para advogados ou servidores públicos (o chamado "juridiquês"). Há uma violação direta desse princípio quando o cidadão comum (Perfil Primário) tenta registrar uma reclamação e se depara com termos complexos, o que quebra sua expectativa de um atendimento acessível e de fácil compreensão.
- **Proposta de Melhoria:** Substituir termos técnicos institucionais por uma linguagem natural e acessível, trocando jargões como "Peticionamento Eletrônico" por comandos claros como "Registrar Reclamação", alinhando o vocabulário à vivência do cidadão.

**Meta de Usabilidade Associada:** Facilidade de Aprendizado *(Learnability)*


<div id="figura11" align="center">
  <p>Figura 1 - Violação da Correspondência com as expectativas</p>
  <img src="../images/violacao1.png" alt="Violação da Correspondência com as expectativas" width="800">
</div>

---

### 3.2 Simplicidade nas estruturas das tarefas
- **Definição:** Este princípio recomenda simplificar a estrutura das tarefas, reduzindo a quantidade de planejamento e resolução de problemas que elas requerem. Tarefas desnecessariamente complexas devem ser reestruturadas para não sobrecarregar a memória de curto prazo do usuário (Barbosa *et al.*, 2021)<sup><a href="#figura3">[3]</a></sup>.

- **Violação no PROCON-DF:** A tarefa de registrar uma reclamação no site ou qualquer outra tarefa no site atual viola este princípio ao exigir o preenchimento de formulários longos, e as funcionalidades dicilmentes encontradas nos botoes de ação, exigindo que o usuário deduza onde deve clicar para realizar uma ação e a falta de um passo a passo claro (step-by-step).
- **Proposta de Melhoria:** Disponibilizar um formulário particionado (Wizard) com atalhos claros e objetivos para as funcionalidades primárias, reduzindo o esforço de dedução do usuário.

**Meta de Usabilidade Associada:** Eficiência


<div id="figura12" align="center">
  <p>Figura 2 - Violação da Simplicidade nas tarefas</p>
  <img src="../images/violacao2.png" alt="Violação da Simplicidade nas tarefas" width="800">
</div>

---

### 3.3 Equilíbrio entre controle e liberdade do usuário
- **Definição:** Os usuários frequentemente realizam ações equivocadas no sistema e precisam de uma "saída de emergência" claramente marcada para sair de um estado indesejado. A interface deve permitir que o usuário cancele, desfaça e refaça suas ações, mantendo-o no controle (Barbosa *et al.*, 2021)<sup><a href="#figura4">[4]</a></sup>.

- **Violação no PROCON-DF:** Durante a navegação nas cartilhas ou no registro de atendimento, muitas vezes o usuário se vê sem opções claras para cancelar uma ação ou voltar à tela anterior sem perder os dados já preenchidos. A falta de botões claros de "Voltar" ou "Cancelar" tira o controle das mãos do usuário.
- **Proposta de Melhoria:** Inserir botões consistentes e visíveis de "Voltar" e "Cancelar" em todas as etapas de cadastro e navegação, assegurando que o usuário possa reverter ações sem perder o progresso já realizado.

**Meta de Usabilidade Associada:** Facilidade de Recordação *(Memorability)*


<div id="figura13" align="center">
  <p>Figura 3-1 - Violação do Equilíbrio entre Controle e Liberdade do Usuário</p>
  <img src="../images/violocao3-1.png" alt="Violação do Equilíbrio entre Controle e Liberdade do Usuário" width="800">
</div>
<div id="figura14" align="center">
  <p>Figura 3-2 - Violação do Equilíbrio entre Controle e Liberdade do Usuário</p>
  <img src="../images/violocao3-2.png" alt="Violação do Equilíbrio entre Controle e Liberdade do Usuário" width="800">
</div>

---

### 3.4 Consistência e padronização
- **Definição:** Os usuários não devem ter de se perguntar se palavras, situações ou ações diferentes significam a mesma coisa. O designer deve padronizar as ações, os resultados das ações e o layout dos diálogos, seguindo convenções consistentes em toda a interface (Barbosa *et al.*, 2021)<sup><a href="#figura5">[5]</a></sup>.

- **Violação no PROCON-DF:** O site atual apresenta falhas severas de consistência visual. A navegação muda de padrão dependendo do link clicado (alguns abrem novas abas, outros mudam o menu lateral). Elementos interativos (links e botões) não possuem um padrão claro de cores, confundindo o usuário sobre onde ele pode ou não clicar.
- **Proposta de Melhoria:** Estabelecer um Guia de Estilo robusto que unifique a paleta de cores, tipografia, estilos de botões e comportamentos de navegação, criando uma identidade visual sólida e previsível.

**Meta de Usabilidade Associada:** Facilidade de Recordação *(Memorability)*


<div id="figura15" align="center">
  <p>Figura 4 - Violação de Consistência e Padronização</p>
  <img src="../images/violacao4.png" alt="Violação de Consistência e Padronização" width="800">
</div>

---

### 3.5 Promoção da eficiência do usuário
- **Definição:** O sistema deve promover a economia de tempo e esforço. Aceleradores — imperceptíveis aos usuários novatos — podem tornar a interação do usuário experiente mais rápida e eficiente. O sistema deve evitar que o usuário espere desnecessariamente (Barbosa *et al.*, 2021)<sup><a href="#figura6">[6]</a></sup>.

- **Violação no PROCON-DF:** Não há promoção de eficiência na entrada de dados. O sistema peca por não oferecer preenchimento automático (como buscar o endereço automaticamente ao digitar o CEP) ou máscaras de formatação nos campos de CPF e telefone, forçando o usuário a digitar tudo manualmente com grande margem para erros de digitação.
- **Proposta de Melhoria:** Implementar máscaras de formatação em campos numéricos (CPF, Telefone) e integração via API para autocompletar endereços através do CEP, minimizando o esforço mecânico de digitação.

**Meta de Usabilidade Associada:** Eficiência


<div id="figura16" align="center">
  <p>Figura 5 - Violação da Promoção da Eficiência</p>
  <img src="../images/violacao5.png" alt="Violação da Promoção da Eficiência" width="800">
</div>

---

### 3.6 Antecipação das necessidades do usuário
- **Definição:** As aplicações devem tentar prever o que o usuário quer e precisa, em vez de esperar que ele busque as ferramentas. O designer deve fornecer todas as informações necessárias para cada passo do processo e definir valores padrão (defaults) adequados (Barbosa *et al.*, 2021)<sup><a href="#figura7">[7]</a></sup>.

- **Violação no PROCON-DF:** O sistema não antecipa a documentação necessária para uma denúncia. O usuário só descobre que precisa de uma foto do RG ou da Nota Fiscal quando já está no meio do processo ou ao final, obrigando-o a interromper a tarefa. O sistema deveria antecipar essa necessidade avisando logo na tela inicial.
- **Proposta de Melhoria:** Incluir uma tela inicial explicativa antes do início do processo, informando de antemão quais documentos físicos (RG, Nota Fiscal) serão necessários para que o usuário os tenha em mãos.

**Meta de Usabilidade Associada:** Segurança no Uso (Prevenção de Erros)


<div id="figura17" align="center">
  <p>Figura 6 - Violação da Antecipação de Necessidades</p>
  <img src="../images/violacao6.png" alt="Violação da Antecipação de Necessidades" width="800">
</div>

---

### 3.7 Visibilidade e reconhecimento
- **Definição:** O estado do sistema, os objetos, as ações e as opções devem estar atualizados e facilmente perceptíveis. O usuário não deve ter de se lembrar de informações de uma parte da aplicação quando tiver passado para outra (reconhecimento em vez de memorização) (Barbosa *et al.*, 2021)<sup><a href="#figura8">[8]</a></sup>.

- **Violação no PROCON-DF:** Durante o registro de uma manifestação (que possui várias etapas), o site falha em fornecer uma barra de progresso (status) clara. O usuário não sabe em qual etapa está, o que já preencheu ou quantas etapas faltam para finalizar, sobrecarregando sua memória.
- **Proposta de Melhoria:** Incorporar um indicador de progresso (Stepper ou Barra de Progresso) persistente na interface, ilustrando em qual passo o usuário se encontra e quantas etapas restam para a finalização do processo.

**Meta de Usabilidade Associada:** Satisfação do Usuário *(Satisfaction)* e Facilidade de Recordação


<div id="figura18" align="center">
  <p>Figura 7 - Violação da Visibilidade e Reconhecimento</p>
  <img src="../images/violacao7.png" alt="Violação da Visibilidade e Reconhecimento" width="800">
</div>
<div id="figura19" align="center">
  <p>Figura 8 - Violação da Visibilidade e Reconhecimento</p>
  <img src="../images/violacao6.png" alt="Violação da Visibilidade e Reconhecimento" width="800">
</div>
---

### 3.8 Conteúdo relevante e expressão adequada
- **Definição:** Diálogos não devem conter informações irrelevantes ou raramente necessárias (design estético e minimalista). Cada unidade extra de informação em uma interface compete com as unidades relevantes de informação e reduz sua visibilidade relativa (Barbosa *et al.*, 2021)<sup><a href="#figura9">[9]</a></sup>.

- **Violação no PROCON-DF:** A página inicial do Procon-DF está sobrecarregada de informações, notícias institucionais e banners que poluem a visão. Isso dificulta imensamente o acesso à função principal (que é registrar ou acompanhar uma reclamação), violando a premissa do minimalismo e do conteúdo relevante.
- **Proposta de Melhoria:** Aplicar o conceito de Clean Design na interface, ocultando informações institucionais secundárias em menus de apoio e centralizando a atenção do usuário no fluxo principal de denúncias e orientações.

**Meta de Usabilidade Associada:** Satisfação do Usuário *(Satisfaction)* e Facilidade de Aprendizado


<div id="figura20" align="center">
  <p>Figura 9 - Violação de Conteúdo Relevante (Excesso de informação)</p>
  <img src="../images/violacao2.png" alt="Violação de Conteúdo Relevante" width="800">
</div>

---

### 3.9 Projeto para erros
- **Definição:** O designer deve assumir que qualquer erro potencial será cometido e projetar para evitá-los (prevenção). Quando ocorrerem, as mensagens de erro devem ser expressas em linguagem simples, indicando precisamente o problema e sugerindo uma solução de forma construtiva (Barbosa *et al.*, 2021)<sup><a href="#figura10">[10]</a></sup>.

- **Violação no PROCON-DF:** O sistema peca ao não fazer validações ativas de erro. Ao preencher algo incorretamente, o sistema frequentemente recarrega a página apagando os dados, a mensagem de correção dos campos é apresentada apenas ao fim do formulário quando realizado a tentativa de submissão, e não aponta os erros diretamente.
- **Proposta de Melhoria:** Adicionar validações *inline* nos campos de formulário (feedback imediato ao preencher um campo incorretamente) em vez de exibir erros apenas na submissão, utilizando mensagens amigáveis e indicativas.

**Meta de Usabilidade Associada:** Segurança no Uso (Prevenção de Erros)


<div id="figura21" align="center">
  <p>Figura 10 - Violação de Projeto para Erros (Excesso de informação)</p>
  <img src="../images/violacao8.png" alt="Violação de Projeto para Erros" width="800">
</div>

---

## 4. Comprovação Teórica e Bibliográfica
Conforme exigência do **Item 11 e 12** do Plano de Ensino da disciplina, a fundamentação que baseia a análise destes 9 Princípios Gerais de Projeto (Definições) foi extraída integralmente do Capítulo 10 da bibliografia oficial.

---

## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação deste documento ao montar o padrão de seções e formatação de texto.

## Referência:
> BARBOSA, Simone D. J.; SILVA, Bruno S. da; SILVEIRA, Milene S.; GASPARINI, Isabela; DARIN, Ticianne; BARBOSA, Gabriel D. J. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021. (Capítulo 10: Princípios e Diretrizes para o Design de IHC, Seção 10.2).



---

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.4 | 21/05/2026 | Formatação do documento | Heitor Macêdo Ricardo | Pedro Moretti |
| 1.3 | 17/05/2026 | Formatação das Referências | Heitor Macedo Ricardo | Pedro Moretti |
| 1.2 | 10/05/2026 | Correção das referências por imagem | Heitor Macedo Ricardo | Pedro Macedo |
| 1.1 | 10/05/2026 | Adição das imagens na referencia e agradecimento a IA | Pedro Macedo | Heitor Macedo Ricardo |
| 1.0 | 10/05/2026 | Criação dos Princípios Gerais de Projeto. | Heitor Macedo Ricardo | Pedro Macedo |

<br>
<div id="figura0" align="center">
  <p>Figura 1 - Início da Seção 10.2: Princípios e Diretrizes Gerais</p>
  <a href="../images/principiosgerais.png" target=_blank><img src="../images/principiosgerais.png" alt="Seção 10.2.1 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 222).</p>
</div>
<div id="figura1" align="center">
  <p>Figura 2 - Seção 10.2.1: Correspondecia com usuário</p>
  <a href="../images/Correspondenciacomusuario1.png" target=_blank><img src="../images/Correspondenciacomusuario1.png" alt="Seção 10.2.1 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 222).</p>
</div>
<div id="figura2" align="center">
  <p>Figura 3 - Seção 10.2.1: Correspondência com o Usuário</p>
  <a href="../images/Correspondenciacomusuario2.png" target=_blank><img src="../images/Correspondenciacomusuario2.png" alt="Seção 10.2.1 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 222).</p>
</div>
<div id="figura3" align="center">
  <p>Figura 4 - Seção 10.2.2: Simplicidade nas Estruturas das Tarefas</p>
  <a href="../images/simplicidade.png" target=_blank><img src="../images/simplicidade.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 223).</p>
</div>
<div id="figura4" align="center">
  <p>Figura 5 - Seção 10.2.3: Equilibrio entre controle e Liberdade do Usuário</p>
  <a href="../images/equilibrio.png" target=_blank><img src="../images/equilibrio.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 224).</p>
</div>
<div id="figura5" align="center">
  <p>Figura 6 - Seção 10.2.4: Consistência e Padronização</p>
  <a href="../images/consistencia.png" target=_blank><img src="../images/consistencia.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 226).</p>
</div>
<div id="figura6" align="center">
  <p>Figura 7 - Seção 10.2.5: Promovendo a Eficiência do Usuário</p>
  <a href="../images/promocao.png" target=_blank><img src="../images/promocao.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 226).</p>
</div>
<div id="figura7" align="center">
  <p>Figura 8 - Seção 10.2.6: Antecipação</p>
  <a href="../images/antecipacao.png" target=_blank><img src="../images/antecipacao.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 227).</p>
</div>
<div id="figura8" align="center">
  <p>Figura 9 - Seção 10.2.7: Visibilidade e Reconhecimento</p>
  <a href="../images/visibilidade.png" target=_blank><img src="../images/visibilidade.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 226).</p>
</div>
<div id="figura9" align="center">
  <p>Figura 10 - Seção 10.2.8: Conteúdo Relevante e Expressão Adequada</p>
  <a href="../images/conteudo.png" target=_blank><img src="../images/conteudo.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 230).</p>
</div>
<div id="figura10" align="center">
  <p>Figura 11 - Seção 10.2.9: Projeto para Erros</p>
  <a href="../images/projeto.png" target=_blank><img src="../images/projeto.png" alt="Seção 10.2 do livro Barbosa e Silva"></a>
  <p><b>Fonte:</b> BARBOSA et al. (2021, p. 231).</p>
</div>
