# Relatório de Avaliação de IHC: Sites Governamentais

Este documento detalha a análise de usabilidade e interface de três sistemas distintos, utilizando métodos de inspeção e investigação baseados em frameworks consolidados na literatura de IHC.

---
## Histórico de Versão

| Versão | Data       | Descrição                                      | Autor        |
|--------|------------|-----------------------------------------------|--------------|
| 1.0    | 2026-04-11 | Criação do documento inicial                  | Pedro Augusto |

---

## 1. Agenda DF (Serviço de Agendamentos do Distrito Federal)

**Foco:** Agendamento para doação de sangue (Fundação Hemocentro de Brasília)  
**Objetivo:** Identificar problemas que dificultam o alcance de objetivos do usuário, avaliando a frequência e gravidade desses obstáculos.  
**Método:** Avaliação Heurística de Nielsen  

### Conclusões

- **Integração Positiva:** O sistema utiliza o SSO do GOV.br para autenticação, garantindo segurança e familiaridade no acesso.  
- **Lacunas de Ajuda:** Apesar de possuir uma seção de FAQ (Perguntas Frequentes), o site carece de um guia de uso ou tutorial passo a passo para novos usuários.  
- **Perfil do Usuário:** Público equilibrado entre gêneros, predominantemente acima de 29 anos (65%), exigindo uma interface clara e direta para diferentes níveis de literacia digital.  

---

## 2. Fala.BR (Plataforma de Ouvidoria e Acesso à Informação)

**Foco:** Fluxo de registro de elogio direcionado ao INEP  
**Objetivo:** Garantir que tarefas críticas sejam concluídas sem erros graves e entender pontos fortes e fracos da jornada do usuário.  
**Método:** Framework DECIDE  

### Conclusões

- **Eficiência e Eficácia:** Avaliação do tempo necessário para completar o elogio e da quantidade de erros durante o processo.  
- **Pontos de Irritação:** Campos específicos ou telas intermediárias podem causar confusão, exigindo feedback mais claro após cada ação.  
- **Necessidade de Suporte:** O sistema deve ser autossuficiente, permitindo que o usuário registre uma manifestação simples sem precisar de ajuda externa.  

---

## 3. Portal de Passaporte (Polícia Federal)

**Foco:** Fluxo de solicitação e consulta de passaportes  
**Objetivo:** Analisar conformidade com padrões de usabilidade e tratamento de erros.  
**Método:** Framework DECIDE aliado à Inspeção Heurística  

### Conclusões

- **Severidade de Erros:** Foram detectados 11 problemas, sendo 4 catastróficos. Destaque para uso do botão "voltar" e ausência de validação em tempo real.  
- **Rigidez do Fluxo:** O sistema impõe uma curva de aprendizado desnecessária, dificultando navegação entre etapas sem perda de dados.  
- **Excesso de Texto:** Interface poluída por conteúdo textual excessivo, dificultando a localização de informações críticas.  

### Recomendação

- Modernizar o tratamento de erros  
- Permitir navegação livre entre etapas  
- Implementar salvamento automático (rascunhos)  

---

## Tabela Comparativa de Problemas

| Site          | Principal Barreira                          | Gravidade               | Recomendação                                      |
|--------------|--------------------------------------------|------------------------|--------------------------------------------------|
| Agenda DF    | Falta de guia de auxílio ao usuário         | Baixa                  | Implementar tutoriais de uso                     |
| Fala.BR      | Feedback de conclusão incerto               | Média                  | Melhorar mensagens de confirmação de status      |
| Passaporte PF| Perda de dados ao navegar/voltar            | Alta (Catastrófica)    | Permitir navegação livre e salvar rascunhos      |

---

## Nota Metodológica

Todas as avaliações basearam-se na obra *"Interação Humano-Computador e Experiência do Usuário"* de Barbosa e Silva (2021).

Os relatórios completos com análises aprofundadas estão disponíveis nos arquivos abaixo:

- 📄 Agenda DF: `./agendadf-analise.pdf`
- 📄 Fala.BR: `./falabr-analise.pdf`
- 📄 Passaporte PF: `./passaportepf-analise.pdf`