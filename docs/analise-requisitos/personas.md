# Personas

## Introdução

Personas são personagens fictícios criados para representar os diferentes tipos de usuários dentro de um grupo demográfico que poderá usar o sistema de modo similar. Segundo Barbosa e Silva (2021), personas são definidas principalmente por seus objetivos, determinados por um processo de refinamento a partir de dados do perfil de usuário. Um elenco de personas deve cobrir os principais grupos de usuários do sistema para que o designer foque seus esforços nos usuários mais importantes.

O elenco de personas deste projeto foi construído a partir dos dados coletados no Perfil de Usuário, com base nos resultados do Grupo de Foco realizado em 30/04/2026, na Entrevista e na Análise Documental. O elenco é composto por **7 personas** ao total: **5 personas primárias**, **1 persona secundária** e **1 antipersona**.

---

## Elenco de Personas

---

### 2.1. Persona Primária: Laura, a Universitária Prática

<p align="center">
  <img src="../images/Personas-Laura.png" width="180" alt="Foto de Laura Mendes"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #1976d2; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 1 — Laura Mendes. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | Laura Mendes |
| **Idade** | 22 anos |
| **Gênero** | Feminino |
| **Localidade** | Brasília, DF — Asa Norte |
| **Escolaridade** | Ensino Superior incompleto (5º semestre de Administração — UnB) |
| **Ocupação** | Estudante universitária e estagiária em marketing digital |
| **Status** | <span style="background-color: #1976d2; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Persona Primária</span> |

**Objetivos:**

- **Pessoal:** Resolver qualquer problema burocrático de forma rápida e sem burocracia — "sem enrolação". Para ela, tempo é o recurso mais escasso.
- **Prático:** Acompanhar o andamento da sua reclamação contra uma operadora de internet (que a cobrou indevidamente por um mês) sem precisar entrar no site do Procon-DF todos os dias para descobrir se houve alguma atualização.
- **De experiência:** Ser tratada pelo sistema com a mesma fluidez e clareza que ela espera de um app de delivery ou de rastreio de encomendas — status visível, linguagem simples, notificação automática.

**Habilidades:**

- **Alta fluência digital:** Usa smartphone como extensão do corpo. Navega em múltiplos apps simultaneamente, posta conteúdo nas redes sociais, faz compras, paga contas e resolve serviços bancários 100% pelo celular, sem nunca abrir um computador.
- **Perfil explorador:** Aprende novas ferramentas por tentativa e erro; não lê manuais nem tutoriais. Se a interface não for autoexplicativa, ela abandona e busca outra solução.
- **Leiga em Direito do Consumidor:** Desconhece completamente termos como "fornecedor", "SAC", "carta de resposta" ou os prazos legais previstos no CDC. Para ela, "entrar no Procon" é um território desconhecido e intimidador.

**Tarefas:**

- Consultar o status atual da sua reclamação — *frequência: diária (ou sempre que lembrar)*
- Verificar se precisa enviar algum documento ou resposta ao Procon — *frequência: eventual*
- Receber confirmação de que a reclamação foi registrada com sucesso — *frequência: única, no início do processo*
- Ser alertada quando um prazo crítico estiver se aproximando — *frequência: conforme o processo avança*

**Relacionamentos:**

- Mora em um apartamento compartilhado com duas colegas de faculdade na Asa Norte. É a "expert em tecnologia" da república: resolve o Wi-Fi, configura os aplicativos das amigas e é sempre a primeira a testar novidades.
- Quando tem dúvida sobre seus direitos como consumidora, pergunta ao pai (advogado aposentado) por mensagem no WhatsApp, pois não tem paciência para pesquisar legislação por conta própria.
- Compartilhou a experiência ruim com a operadora de internet no grupo da turma e foi encorajada pelas amigas a "ir ao Procon".

**Requisitos:**

- **Notificações proativas obrigatórias:** O sistema deve enviar automaticamente uma mensagem (WhatsApp, SMS ou e-mail) sempre que o status do processo mudar — ela não deve ser obrigada a logar para descobrir novidades.
- **Sem jargão jurídico:** Toda comunicação deve usar linguagem do cotidiano, sem termos legais que exijam conhecimento prévio em Direito.
- **Interface Mobile-First:** Toda a experiência de acompanhamento deve funcionar perfeitamente no smartphone, sem precisar "apertar" ou rolar para lados.
- **Status sem login (básico):** Consulta básica do status deve ser possível com apenas o número de protocolo, sem exigir criação de conta ou autenticação a cada acesso.
- **CTA claro na entrada:** O botão "Acompanhar minha reclamação" deve estar visível logo na página inicial, sem necessidade de explorar menus.

**Expectativas:**

- Espera que a tela de acompanhamento funcione como o rastreamento de um pedido no iFood ou na Amazon: **linha do tempo visual** mostrando cada etapa (Reclamação registrada → Notificada à empresa → Empresa respondeu → Em análise → Resolvida).
- Espera que o sistema a avise **proativamente** — via notificação push, SMS ou e-mail — sem que ela precise lembrar de abrir o aplicativo ou o site.
- Espera **linguagem humana e simples**: em vez de "Aguardando manifestação do fornecedor dentro do prazo estipulado em lei", quer ler algo como "A empresa tem até 10 dias para responder. Te avisamos quando chegar uma resposta."
- Espera que o design seja **limpo e sem poluição visual** — sem banners, sem menus escondidos, sem excesso de texto.

!!! info "Responsável por este artefato"
    A **Persona Primária Laura** foi criada por **Heitor Macedo Ricardo**, responsável pela funcionalidade *Portal de Acompanhamento de Reclamações com Notificações Ativas* na Etapa 2 do projeto. Integra o conjunto de artefatos da funcionalidade: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Cenários](cenarios.md) · [Análise de Tarefas](analise-tarefas.md).

---

### 2.2. Persona Primária: Lucas, o Consumidor Exigente

<p align="center">
  <img src="../images/persona_lucas.jpeg" width="180" alt="Foto de Lucas Silva"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #1976d2; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 2 — Lucas Silva. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | Lucas Silva |
| **Idade** | 24 anos |
| **Gênero** | Masculino |
| **Localidade** | Brasília, DF — Taguatinga |
| **Escolaridade** | Ensino Superior Completo (Ciência da Computação — UnB) |
| **Ocupação** | Desenvolvedor Júnior em uma Fintech |
| **Status** | <span style="background-color: #1976d2; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Persona Primária</span> |

**Objetivos:**

- **Pessoal:** Não ser lesado por empresas que negligenciam o suporte ao cliente. Para ele, registrar uma reclamação e levá-la até uma solução é um ato de "higiene digital" e exercício de cidadania.
- **Prático:** Após registrar uma reclamação contra um e-commerce internacional, **participar ativamente da audiência de conciliação virtual** para expor suas evidências técnicas e negociar diretamente com o fornecedor, sem sair de casa.
- **De experiência:** Utilizar uma interface de videoconferência que siga padrões modernos de UX, livre de travamentos, com controles responsivos e sem a necessidade de instalar plugins obsoletos.

**Habilidades:**

- **Alta Literacia Tecnológica:** Usuário avançado de Linux, competidor de programação. Identifica rapidamente falhas de latência, má qualidade de vídeo e problemas de segurança.
- **Uso Híbrido:** Embora utilize o smartphone para monitorar processos, prefere seu desktop com múltiplos monitores para participar de audiências — assim pode manter as evidências abertas em uma tela enquanto vê o mediador na outra.
- **Autossuficiência:** Prefere caminhos diretos (CTAs claros) e detesta interfaces que o forçam a assistir tutoriais ou ler avisos institucionais antes de acessar a sala virtual.

**Tarefas:**

- Receber o link da audiência e **testar a configuração de áudio/vídeo** antes da sessão — *frequência: única por audiência*
- **Participar da audiência virtual**, ativando/desativando microfone conforme necessário e compartilhando trechos de logs ou capturas de tela como prova — *frequência: durante a sessão*
- **Assinar digitalmente o termo de acordo** (se houver) ou entender os próximos passos caso a conciliação não resulte em acordo — *frequência: única ao final da audiência*

**Relacionamentos:**

- É o "expert" do seu círculo social; frequentemente ajuda amigos a coletarem evidências para processos e os incentiva a usar os canais oficiais do governo.
- Crítico da burocracia estatal, compartilha suas experiências de usabilidade — inclusive de audiências virtuais — em fóruns de tecnologia e redes sociais profissionais.

**Requisitos:**

- **Sala virtual sem instalação:** A audiência deve rodar diretamente no navegador (WebRTC), sem exigir plugins ou aplicativos externos.
- **Estabilidade e qualidade:** O sistema deve se adaptar automaticamente à largura de banda para evitar congelamentos, mantendo o áudio sempre nítido.
- **Segurança transparente:** Confirmação de que a sala é criptografada e de que a assinatura digital tem validade jurídica.
- **Feedback técnico claro:** Indicadores visuais de qualidade da conexão, microfone silenciado e compartilhamento de tela ativo.

**Expectativas:**

- Espera que a sala virtual funcione tão bem quanto uma chamada no Google Meet ou Zoom, com controles familiares e sem atrasos.
- Espera que o sistema permita **compartilhar apenas uma janela específica** (não a tela inteira), preservando sua privacidade.
- Acredita que, ao final da audiência, o processo não fique "em suspensão" — quer um status claro (acordo firmado ou prosseguimento da reclamação) e um comprovante digital do que foi decidido.
- Espera que a interface da sala mostre o nome e o papel de cada participante de forma fixa, para não precisar deduzir quem é quem durante o debate.

!!! info "Responsável por este artefato"
    A **Persona Primária Lucas** foi criada por **Pedro Augusto Moretti Moreira** e **Heitor Macedo Ricardo**, com base nos dados consolidados do Grupo de Foco. Adaptada para refletir a participação de Lucas na funcionalidade *Sala de Conciliação Virtual com Mediação Assistida*, garantindo que o perfil técnico do usuário seja contemplado no design da experiência de audiência remota.

---

### 2.3. Persona Primária: Ivone, a Iniciante Vulnerável

<p align="center">
  <img src="../images/personas/persona2.png" width="180" alt="Foto de Ivone"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #1976d2; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 3 — Ivone Maria da Silva. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | Ivone Maria da Silva |
| **Idade** | 56 anos |
| **Gênero** | Feminino |
| **Localidade** | Ceilândia, DF |
| **Escolaridade** | Ensino Fundamental incompleto |
| **Ocupação** | Auxiliar de Limpeza |
| **Status** | <span style="background-color: #1976d2; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Persona Primária</span> |

**Objetivos:**
- **Resolver conflitos sem medo:** Registrar uma reclamação sobre uma compra não entregue sem sentir que o site é pouco confiável ou "perigoso".
- **Independência digital:** Conseguir finalizar o processo pelo celular sem depender de terceiros para navegar em uma interface "poluída".

**Habilidades:**
- **Uso básico de tecnologia:** Utiliza o celular para WhatsApp e chamadas. Associa layouts excessivamente carregados a "spam" ou vírus.
- **Leitura funcional:** Prefere ícones e botões grandes a blocos densos de texto pequeno.

**Tarefas:**
- Localizar o ponto de partida para reclamação na home — *frequência: única*.
- Tirar foto e anexar comprovantes de pagamento — *frequência: eventual*.
- Diferenciar se seu problema é caso de Procon ou Justiça — *frequência: raro*.

**Relacionamentos:**
- Busca o Procon por recomendação de vizinhos após sofrer um "atendimento de tortura" por parte de uma loja online.

**Expectativas:**
- Espera encontrar um **botão central e destacado** (estilo Reclame Aqui) para registrar sua queixa imediatamente.
- Espera que o site a guie passo a passo, eliminando a necessidade de pesquisar no Google "como usar o site do Procon".

**Requisitos:**
- **Clean Design:** Redução de banners e notícias que criam uma estética de "spam".
- **CTA de Alto Contraste:** O botão de reclamação deve ser o elemento mais visível da página.
- **Foco em Mobile:** A interface deve ser totalmente adaptada para uso em smartphones, evitando menus escondidos.

!!! info "Responsável por este artefato"
    A **Persona Primária Ivone** foi criada por **Pedro Augusto Macedo Del Castilo**, responsável pela funcionalidade *Botão de Reclamação Rápida*.

---

### 2.4. Persona Primária: Maria Helena, a Aposentada Prática

<p align="center">
  <img src="../images/persona_MariaHelena.png" width="180" alt="Foto de Maria Helena Costa"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #1976d2; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 4 — Maria Helena Costa. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | Maria Helena Costa |
| **Idade** | 67 anos |
| **Gênero** | Feminino |
| **Localidade** | Brasília, DF — Ceilândia |
| **Escolaridade** | Ensino Médio Completo |
| **Ocupação** | Aposentada |
| **Status** | <span style="background-color: #1976d2; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Persona Primária</span> |

**Objetivos:**

- Resolver problemas de consumo sem depender de deslocamentos frequentes.
- Acompanhar reclamações contra empresas de telefonia e serviços financeiros com clareza e sem burocracia.
- Entender rapidamente o que precisa fazer quando houver retorno do PROCON-DF.

**Habilidades:**

- Usa WhatsApp diariamente para se comunicar com a família.
- Consegue acessar serviços básicos no celular, mas se perde em formulários longos e telas cheias de informação.
- Prefere instruções diretas, com passo a passo simples.

**Tarefas:**

- Consultar o andamento de uma reclamação — *frequência: eventual, principalmente quando recebe nova notificação*.
- Enviar documentos simples, como fatura e comprovante de pagamento — *frequência: quando solicitado*.
- Ler avisos sobre prazo de resposta da empresa — *frequência: conforme o processo avança*.

**Relacionamentos:**

- Mora com o marido, também aposentado, e recorre à filha quando precisa resolver algo mais complicado no celular.
- Costuma compartilhar problemas com vizinhas e amigas do bairro, que também já passaram por situações parecidas com empresas de telefonia e bancos.

**Expectativas:**

- Espera uma página inicial clara, com acesso rápido ao serviço de reclamação.
- Espera mensagens simples sobre o que aconteceu e o que ela deve fazer em seguida.
- Espera conseguir resolver boa parte do processo pelo celular.

**Requisitos:**

- Interface com linguagem simples e botões bem destacados.
- Notificações proativas sobre andamento da reclamação.
- Consulta de protocolo sem excesso de etapas ou campos obrigatórios.

!!! info "Responsável por este artefato"
    A **Persona Primária Maria Helena Costa** foi criada por **Heloisa Laura Santos da Silva** com base nos dados da análise documental, que indicam maior concentração de atendimentos em faixas etárias mais altas, predominância de reclamações ou denúncias e participação feminina mais elevada.

---

### 2.5. Persona Primária: Roberto, o Pragmático

<p align="center">
  <img src="../images/persona_roberto.png" width="180" alt="Foto de Roberto Oliveira"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #1976d2; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 5 — Roberto Oliveira. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | Roberto Oliveira |
| **Idade** | 52 anos |
| **Gênero** | Masculino |
| **Localidade** | Brasília, DF — Águas Claras |
| **Escolaridade** | Ensino Superior Completo (Logística) |
| **Ocupação** | Gerente de Logística em uma distribuidora |
| **Status** | <span style="background-color: #1976d2; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Persona Primária</span> |

**Objetivos:**

- **Pessoal:** Resolver conflitos financeiros sem perder tempo de trabalho.
- **Prático:** Contestar uma cobrança de seguro não contratado em seu cartão de crédito após várias tentativas frustradas via SAC.
- **De experiência:** Encontrar um fluxo direto, com evidências claras de que sua reclamação foi aceita e que o banco será notificado formalmente.

**Habilidades:**

- **Fluência Tecnológica Média:** Utiliza ferramentas de ERP e planilhas no trabalho. No dia a dia, usa o smartphone para bancos e e-mails, mas prefere o desktop para preencher formulários longos.
- **Perfil Pragmático:** Foca na eficiência. Se o sistema exige muitos cliques ou informações que ele considera irrelevantes, ele se irrita, mas persiste por ser um direito seu.
- **Conhecimento Básico de Direitos:** Sabe que tem direito ao estorno, mas não quer ler o código de defesa do consumidor inteiro para fazer a denúncia.

**Tarefas:**

- Registrar uma reclamação detalhada anexando fatura do cartão — *frequência: única no registro*
- Acompanhar o prazo de resposta da instituição financeira — *frequência: semanal*
- Exportar o protocolo em PDF para ter uma prova documental — *frequência: eventual*

**Relacionamentos:**

- Casado, pai de dois filhos. É o responsável por gerir as contas da casa e não tolera cobranças indevidas que afetem o orçamento familiar.
- Valoriza a indicação de amigos sobre serviços que "realmente funcionam" e evita burocracias desnecessárias.

**Expectativas:**

- Espera que o portal do PROCON seja uma ferramenta de resolução e não apenas um canal de registro, preferencialmente com um **Painel de Monitoramento de Prazos** centralizado.
- Espera clareza sobre os prazos: "Quanto tempo o banco tem para me responder?".
- Espera um design sóbrio e profissional, que transmita credibilidade institucional.

**Requisitos:**

- **Feedback de Prazos:** Indicação visual clara de quantos dias restam para a resposta do fornecedor.
- **Upload Estruturado:** Espaço dedicado para anexar faturas e prints de protocolos de SAC.
- **Resumo Executivo:** Um resumo do status da reclamação logo após o login.

!!! info "Responsável por este artefato"
    A **Persona Primária Roberto Oliveira** foi criada por **Mateus Rodrigues Barreto**, baseada nos dados da análise documental que apontam os "Assuntos Financeiros" como a maior causa de atendimentos (47,62%) e o perfil da Geração X como um dos mais presentes no sistema.

---

### 2.6. Persona Secundária: Gustavo, o Microempreendedor

<p align="center">
  <img src="../images/persona_gustavo.jpeg" width="180" alt="Foto de Gustavo Santos"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #2e7d32; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 6 — Gustavo Santos. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | Gustavo Santos |
| **Idade** | 20 anos |
| **Gênero** | Masculino |
| **Localidade** | Brasília, DF — Guará |
| **Escolaridade** | Ensino Superior Incompleto (Gastronomia) |
| **Ocupação** | Proprietário de Panificadora Artesanal |
| **Status** | <span style="background-color: #2e7d32; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Persona Secundária</span> |

**Objetivos:**

- **Pessoal:** Manter a conformidade legal da sua empresa sem que isso tome o tempo dedicado à produção e às vendas.
- **Prático:** Responder a notificações de reclamações e participar de mediações de forma remota, evitando deslocamentos até o centro da cidade.
- **De gestão:** Ter um canal claro para entender quais normas de consumo sua padaria precisa seguir, evitando multas por desconhecimento.

**Habilidades:**

- **Multitarefa Administrativa:** Gerencia estoque, funcionários e finanças simultaneamente via smartphone e computador desktop da padaria.
- **Leigo no Domínio Jurídico:** Sente-se intimidado por termos como "manifestação do fornecedor" ou "autos do processo". Prefere uma linguagem direta e orientada à ação.
- **Pragmatismo Digital:** Valoriza ferramentas que permitem resolver problemas em "janelas de 15 minutos" entre uma tarefa e outra da produção.

**Tarefas:**

- Consultar se existem novas pendências administrativas contra sua empresa — *frequência: eventual*
- Upload de documentos de defesa e comprovantes de resolução — *frequência: conforme demanda*
- Participar de audiências virtuais de conciliação — *frequência: agendada*

**Relacionamentos:**
- Responsável direto pela reputação de um negócio local e familiar. Interage com a comunidade do Guará e preza por resolver conflitos de forma amigável para não perder clientes.
- Busca o equilíbrio entre ser um "empresário moderno" e cumprir as exigências burocráticas tradicionais.

**Expectativas:**

- Espera um "Portal do Lojista" ou área dedicada ao fornecedor que seja visualmente distinta da área do consumidor.
- Espera que o sistema o guie sobre "o que fazer agora" quando recebe uma notificação, em vez de apenas exibir um texto jurídico longo.
- Espera que as reuniões de conciliação funcionem sem a necessidade de instalar novos softwares, rodando direto no navegador.

**Requisitos:**

- **Dashboard de Pendências:** Uma visão clara de reclamações ativas vs. resolvidas.
- **Notificações em Tempo Real:** Alertas via e-mail ou WhatsApp para não perder prazos administrativos críticos.
- **Simplificação Terminológica:** Uso de linguagem acessível que traduza os termos do CDC para a realidade do pequeno lojista.

!!! info "Responsável por este artefato"
    A **Persona Secundária Gustavo** foi criada por **Pedro Augusto Moretti Moreira**, baseada na entrevista semiestruturada realizada com o perfil de proprietário de estabelecimento comercial.

---

### Antipersona — Hugo Rocha

<p align="center">
  <img src="../images/hugo_persona.jpeg" width="180" alt="Foto de Hugo Rocha"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #2e7d32; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 6 — Hugo Rocha. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | Hugo Rocha |
| **Idade** | 8 anos |
| **Ocupação** | Estudante do Fundamental |
| **Status** | <span style="background-color: #b71c1c; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Antipersona</span> |

**Por que não é o público-alvo:**
- Hugo não possui capacidade civil plena para registrar reclamações de forma autônoma e não possui transações comerciais de alto valor que exijam a intervenção direta do PROCON-DF.

---

### Antipersona — Seu José, o Consumidor Excluído

<p align="center">
  <img src="../images/persona_SeuJose.png" width="180" alt="Foto de Seu José"
       style="border-radius: 50%; object-fit: cover; width: 180px; height: 180px; border: 4px solid #b71c1c; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
  <br><em>Figura 9 — Seu José. Fonte: Elaborado pelos autores (2026).</em>
</p>

| Atributo | Descrição |
| :--- | :--- |
| **Nome** | José Alves dos Santos ("Seu José") |
| **Idade** | 71 anos |
| **Gênero** | Masculino |
| **Localidade** | Planaltina, DF |
| **Escolaridade** | Ensino Fundamental incompleto |
| **Ocupação** | Aposentado (ex-agricultor) |
| **Status** | <span style="background-color: #b71c1c; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">Antipersona</span> |

**Por que não é o público-alvo:**

Seu José representa o perfil de consumidor para o qual o sistema **não foi projetado** em sua forma digital atual — e cujas barreiras estruturais o excluem da experiência de uso autônomo. Seu perfil é documentado para orientar o design a **não agravar sua exclusão** e para indicar canais alternativos (presencial, telefone) que devem coexistir com o portal digital.

#### 1. Identidade e Contexto Digital

- **Barreira Digital:** Não possui conta no portal gov.br ou tem dificuldade em realizar validações biométricas e acessos em múltiplos fatores.
- **Navegação:** Sente-se confuso com a ruptura visual e técnica ao ser redirecionado para sistemas externos como o SPE (`sistemas.df.gov.br`) ou subsites como o da Escola do Procon.
- **Equipamento:** Possui um smartphone antigo ou acesso limitado à internet, o que torna o processo de "peticionamento eletrônico" frustrante e lento.

#### 2. Letramento e Comunicação

- **Conhecimento Jurídico:** Não compreende termos como "polo passivo", "jurisprudência dominante" ou "destinatário final". Sem exemplos práticos, ele não consegue decidir se seu problema é uma "relação de consumo".
- **Suporte:** Depende do FAQ (Perguntas Frequentes) para tirar dúvidas simples, mas encontra o serviço inacessível ou instável, ficando sem nenhum roteiro de apoio.

#### 3. Comportamento e Esforço

- **Baixa Tolerância à Complexidade:** Não tem disposição ou tempo para ler de 3 a 5 páginas de normas e exclusões antes de iniciar uma reclamação.
- **Risco de Desistência:** Ao encontrar as 13 categorias de exclusão apenas no final do processo (ou após leitura densa), ele tende a abandonar o sistema por cansaço cognitivo.

#### 4. Privacidade e Segurança

- **Insegurança com Dados:** Sente-se intimidado ao saber que seus dados pessoais (nome, CPF, endereço) serão compartilhados automaticamente com a empresa reclamada, sem entender as implicações legais disso devido à linguagem técnica da política de privacidade.

!!! info "Responsável por este artefato"
    A **Antipersona Seu José** foi criada por **Heitor Macedo Ricardo**, com base nos dados do Perfil de Usuário e nas barreiras de acessibilidade digital identificadas na análise documental do portal do PROCON-DF.

---

## Agradecimentos à IA

Agradecimento ao **Gemini 3 Flash** pela ajuda na criação e estruturação das personas deste documento.

---

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Criação do documento com Persona Primária Laura, baseada nos dados reais do Grupo de Foco (Etapa 2). | Heitor Macedo Ricardo | Pedro Augusto Moretti |
| `1.1` | 01/05/2026 | Adição e expansão profunda das personas Lucas e Gustavo e da Antipersona Hugo com base nos dados consolidados. | Pedro Augusto Moretti Moreira | Heloisa Silva |
| `1.2` | 03/05/2026 | Inclusão da Persona Primária Maria Helena com base na análise documental. | Heloisa Silva | Heitor Macedo |
| `1.3` | 03/05/2026 | Criação da persona Ivone (Etapa 2). | Pedro Macedo | Heitor Macedo |
| `1.4` | 03/05/2026 | Inclusão da Persona Primária Roberto Oliveira. | Mateus Rodrigues Barreto | Pedro Moretti |
| `1.5` | 03/05/2026 | Padronização da imagem da Persona Laura para o padrão `<p align="center"><img>` das demais personas; adição da Antipersona Seu José com foto, tabela de atributos e 4 seções temáticas. | Heitor Macedo Ricardo | Pedro Moretti |
