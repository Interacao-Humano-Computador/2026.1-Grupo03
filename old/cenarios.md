# Cenários

## Introdução

Cenários são narrativas textuais ricas em detalhes contextuais que descrevem situações concretas de uso de um sistema, envolvendo personas específicas, seus objetivos, o ambiente em que atuam e a sequência de interações que realizam. Segundo Barbosa e Silva (2021, p. 158), um cenário é uma ferramenta fundamental para explorar ideias de design antes que o sistema seja construído, pois permite avaliar se a solução proposta satisfaz as necessidades reais dos usuários ao situá-los em situações verossímeis do cotidiano. Um bom cenário deve conter sete elementos obrigatórios: **ambiente ou contexto**, **atores**, **objetivos**, **planejamento**, **ações**, **eventos** e **avaliação**.

Os cenários deste projeto foram elaborados com foco na funcionalidade de **Sala de Conciliação Virtual com Mediação Assistida**, integrando as necessidades dos perfis de consumidor e fornecedor identificados nas etapas anteriores.

---

## Cenário 1: Lucas, Gustavo e a Resolução Virtual de Conflito

### Narrativa

Era uma segunda-feira, 10h da manhã. Lucas Silva estava em seu apartamento em Taguatinga, sentado diante de seu setup de alta performance rodando Manjaro Linux. Ele havia agendado uma audiência virtual com a "Panificadora do Guará" para resolver um problema de uma encomenda de grande porte paga via Pix que nunca foi entregue corretamente. Enquanto isso, Gustavo Santos, proprietário da panificadora, estava nos fundos do seu estabelecimento. Em vez de ter que fechar a loja e se deslocar por 40 minutos até o Setor Comercial Sul, ele simplesmente lavou as mãos, abriu o notebook no escritório e clicou no link recebido via e-mail.

Ao entrarem na **Sala de Conciliação Virtual**, ambos passaram por um check-up automático de hardware. O mediador do PROCON-DF iniciou a sessão de vídeo. Lucas, com sua exigência técnica, ficou satisfeito ao ver uma interface limpa, sem os banners de notícias que poluíam o site antigo. O mediador compartilhou a tela exibindo o "Termo de Acordo" em tempo real. Gustavo explicou que houve uma falha na logística de entrega devido a um problema no forno, mas propôs o estorno imediato de 100% do valor acrescido de um voucher de cortesia.

Lucas concordou. O mediador editou as cláusulas ali mesmo, na frente de ambos. Não houve necessidade de imprimir nada. Um botão azul **"Assinar com Gov.br"** apareceu para os dois. Lucas usou o leitor de digital do seu celular para autenticar a assinatura, e Gustavo fez o mesmo. Em 20 minutos, a audiência foi encerrada. Lucas voltou ao seu trabalho de desenvolvedor e Gustavo voltou para a linha de produção, sentindo que o sistema finalmente respeitava o tempo de quem produz.

---

### Análise dos Elementos do Cenário

Segundo Barbosa e Silva (2021, p. 158), os 7 elementos obrigatórios do cenário estão presentes na narrativa acima:

- **Ambiente ou contexto:** Lucas em seu home office tecnológico em Taguatinga; Gustavo no escritório de sua panificadora no Guará. Ambos conectados via internet em ambiente profissional/doméstico.
- **Atores:** Lucas Silva (Consumidor Exigente/Persona Primária) e Gustavo Santos (Microempreendedor/Persona Secundária), além do Mediador do PROCON.
- **Objetivos:** Realizar a audiência de conciliação agendada, chegar a um consenso sobre o estorno de um pagamento e formalizar o acordo com validade jurídica.
- **Planejamento:** Ambos se prepararam minutos antes, garantindo conexão estável e acesso aos documentos (comprovante Pix e relatório de entrega) para fundamentar seus argumentos durante a chamada.
- **Ações:** (1) Acessar o link da sala; (2) realizar teste de periféricos; (3) expor os fatos via vídeo; (4) revisar o termo de acordo editado ao vivo; (5) realizar a assinatura digital via Gov.br.
- **Eventos:** (1) O sistema valida a entrada das partes; (2) a plataforma gerencia o fluxo de áudio/vídeo e o chat de documentos; (3) o sistema integra o serviço de assinatura eletrônica do Governo Federal; (4) o sistema encerra o protocolo e envia o PDF assinado para os e-mails.
- **Avaliação:** Lucas sentiu que a interface moderna e a agilidade do fluxo condizem com sua expectativa de eficiência tecnológica. Gustavo avaliou a experiência como essencial para sua rotina, permitindo resolver pendências jurídicas sem abandonar a gestão física de seu negócio.

!!! info "Responsável por este artefato"
    O **Cenário 1** foi elaborado por **Pedro Augusto Moretti Moreira**, responsável pela funcionalidade *Sala de Conciliação Virtual com Mediação Assistida*. Integra o conjunto de artefatos da funcionalidade: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Análise de Tarefas](analise-tarefas.md).

---

## Cenário 2: Laura e a Conciliação Mobile-First no Intervalo da Aula

### Contexto e Ambiente

| Elemento | Descrição |
| :--- | :--- |
| **Ambiente** | Corredor do ICC Norte na UnB (ambiente ruidoso). |
| **Data/Horário** | Terça-feira, às 15h45 (durante o intervalo entre aulas). |
| **Dispositivo** | Smartphone pessoal (conexão 4G/5G). |
| **Pré-condições** | Reclamação prévia contra operadora de telefonia com audiência marcada. |

### Atores

- **Ator Principal:** Laura Mendes — Estudante Universitária (Persona Primária).
- **Ator Secundário:** Mediador do PROCON e Representante da Operadora.

### Objetivos

- **Objetivo Final:** Resolver cobrança indevida de R$ 89,90.
- **Objetivos Intermediários:**
    - Entrar na sala virtual sem precisar de login complexo.
    - Ouvir a proposta da empresa via áudio.
    - Aceitar e assinar o acordo rapidamente antes da próxima aula.

### Planejamento

> Laura planejou usar os 15 minutos de intervalo para resolver a pendência. Ela se posicionou em um local com melhor sinal de rede e usou fones de ouvido para mitigar o barulho ambiente.

### Sequência de Ações

1. Tocar na notificação do WhatsApp que contém o link de acesso direto.
2. Permitir acesso à câmera e microfone no navegador do celular.
3. Participar da discussão rápida mediada pelo agente do PROCON.
4. Visualizar o resumo do acordo na tela otimizada para mobile.
5. Clicar em "Assinar Acordo" e autenticar via biometria facial.

### Eventos

- O sistema adapta a interface de vídeo para o modo retrato do smartphone.
- O mediador destaca os botões de ação para a usuária.
- O sistema envia o comprovante de resolução imediatamente via WhatsApp.

### Avaliação

> Laura sente-se empoderada pela facilidade. A ausência de termos jurídicos complexos e a fluidez do sistema mobile permitiram que ela resolvesse um problema que parecia impossível sem comprometer sua rotina acadêmica.

---

## Cenário 3: Gustavo e o Gerenciamento de Acordos Pós-Conciliação

### Contexto e Ambiente

| Elemento | Descrição |
| :--- | :--- |
| **Ambiente** | Escritório administrativo da Panificadora. |
| **Data/Horário** | Fim do expediente, às 18h30. |
| **Dispositivo** | Computador Desktop (Monitor Philco). |
| **Pré-condições** | Audiência finalizada com sucesso minutos antes. |

### Atores

- **Ator Principal:** Gustavo Santos — Microempreendedor (Persona Secundária).

### Objetivos

- **Objetivo Final:** Arquivar o termo de acordo e programar o estorno financeiro.
- **Objetivos Intermediários:**
    - Fazer o download do termo assinado.
    - Verificar no dashboard se a pendência foi marcada como "Resolvida".

### Planejamento

> Gustavo decidiu organizar a papelada digital antes de fechar a loja. Ele quer garantir que a reclamação não conste mais como ativa no seu CNPJ.

### Sequência de Ações

1. Acessar o "Portal do Fornecedor" no site do PROCON-DF.
2. Filtrar por "Processos Concluídos".
3. Localizar o caso de Lucas Silva.
4. Baixar o arquivo PDF com as assinaturas digitais acopladas.

### Eventos

- O Dashboard atualiza o status do fornecedor em tempo real.
- O sistema gera um log de conformidade que Gustavo pode usar para seu controle contábil.

### Avaliação

> Gustavo sente que o portal agora é uma ferramenta de gestão útil, e não apenas um site de reclamações contra ele. A clareza das informações reduz sua ansiedade administrativa.

---

## Cenário 4: Maria Helena e a Simplicidade do Sistema

### Contexto e Ambiente

| Elemento | Descrição |
| :--- | :--- |
| **Ambiente** | Sala de estar em sua casa em Ceilândia. |
| **Data/Horário** | Quinta-feira, às 10h00. |
| **Dispositivo** | Smartphone pessoal (Android). |
| **Pré-condições** | Notificação de que o PROCON solicitou um documento complementar. |

### Atores

- **Ator Principal:** Maria Helena Costa — Aposentada (Persona Primária).
- **Ator Secundário:** Filha de Maria Helena (apoio técnico pontual).

### Objetivos

- **Objetivo Final:** Enviar a foto da fatura de telefone contestada.
- **Objetivos Intermediários:**
    - Acessar o sistema via link simplificado.
    - Localizar a opção "Anexar Documento".
    - Tirar a foto e confirmar o envio.

### Planejamento

> Maria Helena recebeu um aviso pelo WhatsApp. Ela decidiu resolver logo para não esquecer. Ela chamou sua filha para ficar por perto, caso o site fosse "difícil", mas tentou fazer sozinha primeiro.

### Sequência de Ações

1. Maria Helena clica no link recebido na mensagem do PROCON.
2. O site abre direto na tela de sua reclamação, com um botão grande escrito "Enviar Foto do Documento".
3. Ela clica no botão, e o sistema pergunta se quer "Tirar Foto" ou "Escolher da Galeria".
4. Ela escolhe "Tirar Foto", aponta para a fatura sobre a mesa e clica no ícone da câmera.
5. O sistema mostra uma prévia da foto e pergunta: "A foto está legível?". Ela clica em "Sim, Enviar".

### Eventos

- O sistema otimiza o tamanho da imagem automaticamente para não consumir muito bônus de dados.
- O sistema exibe um check verde gigante com a mensagem: "Documento recebido com sucesso! Não precisa fazer mais nada."

### Avaliação

> Maria Helena ficou surpresa por não precisar de senhas complicadas ou navegar por menus confusos. Ela disse para a filha: "Dessa vez foi fácil, nem precisei da sua ajuda!". Ela se sente segura de que o processo está andando.

!!! info "Responsável por este artefato"
    O **Cenário 4** foi elaborado por **Mateus Rodrigues Barreto**, focado na jornada de acessibilidade para idosos (Persona Maria Helena). Integra o conjunto de artefatos: [Funcionalidade](funcionalidades.md) · [Perfil de Usuário](perfil-usuario.md) · [Personas](personas.md) · [Análise de Tarefas](analise-tarefas.md).

---

## Agradecimentos à IA

Agradecimento ao **Gemini** pela ajuda na estruturação, redação e detalhamento contextualmente rico dos cenários de interação, garantindo que as dores de Lucas, Laura e Gustavo fossem endereçadas.

---

## Referências

> 1. BARBOSA, Simone Diniz Junqueira; SILVA, Bruno Santana da. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021.

---

## Histórico de Versão

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| `1.0` | 30/04/2026 | Elaboração do Cenário 1 (Persona Laura). | Heitor Macedo Ricardo | A definir |
| `1.1` | 01/05/2026 | Reestruturação completa focada na Sala de Conciliação Virtual e inclusão das personas Lucas e Gustavo. | Pedro Augusto Moretti Moreira | A definir |
| `1.2` | 03/05/2026 | Adição do Cenário 4 focado na Persona Maria Helena. | Mateus Rodrigues Barreto | A definir |