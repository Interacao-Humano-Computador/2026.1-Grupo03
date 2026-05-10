# Metas de Usabilidade

## 1. Introdução
De acordo com a Engenharia de Usabilidade de Nielsen, descrita por Barbosa e Silva (2021), a definição das metas de usabilidade envolve estabelecer quais fatores de qualidade de uso devem ser priorizados no projeto. Para cada fator escolhido, é necessário definir como ele será avaliado, estabelecendo faixas de valores inaceitáveis, aceitáveis e ideais para os indicadores de interesse.

Com base no Perfil de Usuário levantado para o sistema do PROCON-DF, selecionamos metas focadas na agilidade e na intuição, buscando garantir que os cidadãos e fornecedores consigam utilizar a plataforma sem frustrações e com o mínimo de carga cognitiva.

---

## 2. Razão da Seleção das Metas (Justificativa)
Conforme exigência da verificação do projeto, justificamos abaixo a escolha das metas prioritárias para o PROCON-DF, totalmente alinhadas aos artefatos da Análise de Requisitos:

1. **Eficiência:** Selecionada porque o Grupo de Foco e a Análise de Tarefas (GOMS) revelaram que usuários como Laura (jovem universitária) e Roberto (gerente pragmático) têm aversão a burocracia. O uso do OCR e do preenchimento automático visa acelerar o registro e permitir que as tarefas sejam concluídas rapidamente, poupando o tempo do cidadão e do fornecedor.
2. **Facilidade de Aprendizado:** Selecionada para atender usuários com barreiras tecnológicas, como Ivone (iniciante vulnerável) e Maria Helena (aposentada). Como o uso do portal não é diário, o sistema precisa guiar o usuário passo a passo (ex: Assistente de Triagem Guiada), permitindo que ele deduza o funcionamento logo no primeiro uso, sem ler cartilhas ou manuais.
3. **Satisfação do Usuário:** Selecionada para reverter o atual quadro de frustração. Os relatos indicaram que os usuários desistem do PROCON-DF e migram para sites como "Reclame Aqui" devido à "poluição visual" e desamparo. O redesign foca em um *Clean Design* e em feedback claro para aumentar a confiança no órgão.
4. **Segurança no Uso (Prevenção de Erros):** Inserida devido à alta taxa de erros identificada na Análise Documental (ex: anexos ilegíveis ou faltando). A meta justifica funcionalidades como a validação via OCR e o teste obrigatório de áudio/vídeo antes da sala de conciliação virtual, garantindo que usuários com pouca fluência digital não sejam prejudicados por falhas técnicas.
5. **Facilidade de Recordação (Memorability):** Como o acesso ao PROCON é esporádico (fornecedores como Gustavo acessam anualmente; consumidores, apenas quando lesados), a interface não pode exigir esforço de memorização. Padrões de design universais e visibilidade do status do sistema ajudam o usuário a retomar o controle mesmo após meses sem acessar o portal.

---

## 3. Indicadores e Faixas de Valores
A tabela abaixo define os indicadores numéricos que comprovarão o sucesso do redesign do sistema, estruturados de acordo com as metas estabelecidas:

| Meta de Usabilidade | Indicador de Medição | Valor Inaceitável | Valor Aceitável | Valor Ideal |
| :--- | :--- | :--- | :--- | :--- |
| **Eficiência** | Tempo total gasto pelo usuário para registrar uma reclamação completa (incluindo anexos via OCR). | Mais de 10 minutos | Entre 5 e 10 minutos | Menos de 5 minutos |
| **Eficiência** | Tempo gasto por um fornecedor para visualizar uma notificação de denúncia no sistema. | Mais de 3 minutos | Entre 1 e 3 minutos | Menos de 1 minuto |
| **Facilidade de Aprendizado** | Número de vezes que o usuário aciona a Ajuda/FAQ ou abandona o Assistente de Triagem no 1º uso. | Mais de 2 consultas | 1 ou 2 consultas | Nenhuma consulta (0) |
| **Facilidade de Aprendizado** | Taxa de conclusão com sucesso (ex: enviar a reclamação completa sem desistir). | Menos de 70% | Entre 70% e 90% | Acima de 90% |
| **Satisfação** | Nota média atribuída pelos usuários em uma pesquisa de satisfação CSAT pós-uso (escala 1 a 5). | Nota inferior a 3 | Nota 3 ou 4 | Nota 5 (Excelente) |
| **Segurança no Uso** | Taxa de processos barrados ou atrasados por envio de documentos ilegíveis/faltantes. | Mais de 15% | Entre 5% e 15% | Menos de 5% |
| **Segurança no Uso** | Número de falhas técnicas de áudio/vídeo reportadas na Sala de Conciliação Virtual. | Mais de 3 incidentes/mês | 1 a 3 incidentes/mês | Zero (0) incidentes |
| **Facilidade de Recordação** | Tempo médio para realizar uma tarefa base após 3 meses sem acesso ao sistema. | Mais que o dobro do tempo do 1º uso | Até 50% a mais do tempo do 1º uso | Igual ou menor que o 1º uso |



---

## 4. Comprovação e Referência Bibliográfica
Conforme exigência dos **Itens 13 e 14** da avaliação da Etapa 3, abaixo consta a referência teórica que fundamenta a definição das metas de usabilidade, as razões de seleção e o uso de faixas de valores.

**Referência:** 
> BARBOSA, Simone D. J.; SILVA, Bruno S. da; SILVEIRA, Milene S.; GASPARINI, Isabela; DARIN, Ticianne; BARBOSA, Gabriel D. J. *Interação Humano-Computador e Experiência do Usuário*. 1. ed. Rio de Janeiro: Autopublicação, 2021. (Capítulo 3, Seção 3.2.1, p. 35-36; e Capítulo 6, Seção 6.3.2, p. 103).

**[INSERIR AQUI A FOTO/PRINT DA PÁGINA 103 DO LIVRO BARBOSA E SILVA QUE MOSTRA O GRÁFICO DAS "FAIXAS DE VALORES PARA INDICADORES DE USABILIDADE" (Figura 6.6)]**

**[INSERIR AQUI A FOTO/PRINT DA PÁGINA 35-36 DO LIVRO QUE LISTA OS 5 FATORES DE NIELSEN (Facilidade de aprendizado, Eficiência, etc.)]**

---

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 10/05/2026 | Elaboração das Metas de Usabilidade. | Heitor Macedo Ricardo | Pedro Moretti |