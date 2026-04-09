# Documentação do Projeto (IHC - Grupo 03)

Este repositório contém a documentação gerada e hospedada via **MkDocs** com a customização altamente visual do **Material for MkDocs**, direcionada aos registros da disciplina de Interação Humano-Computador (2026.1).

A documentação conta com efeitos visuais pesonalizados (Grid avançado, Dark/Light mode com controle de acessibilidade textual, Hero Headers) nativos construídos para a equipe não se preocupar com infraestrutura visual complexa na hora de redigir o conteúdo.

---

## 🚀 Como testar localmente na sua máquina

Para testar ou visualizar o site na sua máquina de forma idêntica à web, basta abrir o terminal na pasta deste repositório e executar:

1. **Instale as dependências** (se for o primeiro uso):
   ```bash
   pip install -r requirements.txt
   ```
2. **Inicie o servidor de pré-visualização ao vivo**:
   ```bash
   python -m mkdocs serve
   ```
O site estará disponível no seu navegador no endereço: `http://127.0.0.1:8000`. Alterações feitas em qualquer lado serão rapidamente e automaticamente atualizadas.

---

## 📂 Organização do Repositório

Entenda de onde vêm os botões principais da infraestrutura:

- `docs/` 👉 **A Alma do Projeto.** Tudo que é texto (.md) ou imagem fica aqui.
  - `docs/images/`: Onde ficam os avatares redondos da equipe ou capturas de tela do sistema.
  - `docs/stylesheets/extra.css`: Toda a estilização premium das cores em Hexadecimal de hover, sombras e contornos de cartões estão aqui isoladas, sem estragar o tema primário.
- `overrides/` 👉 **Templates Injetados.** A mágica do botão verde do GitHub não funciona para layout na raiz, logo fizemos um override da `main.html`. O *Hero* da página inicial e os 4 botões ficam ali.
- `mkdocs.yml` 👉 **Painel Principal.** Arquivo central que gerencia menus hierárquicos e extensões Markdown.
- `.github/workflows/deploy.yml` 👉 **Action Automática**. O deploy está todo configurado — ao dar _push_ na branch `main`, em menos de 1 minuto o repositório é compilado invisivelmente e disponibilizado publicamente no **GitHub Pages**.

---

## 📝 Como Adicionar ou Editar Campos

### 1. Criar uma página nova (Subaba)
1. Crie um arquivo `sua-pagina.md` e jogue dentro da pasta `docs/`.
2. Escreva todo o conteúdo nela usando títulos `##` e Markdown puramente.
3. **PASSO PRINCIPAL:** Abra o `mkdocs.yml`, role até o bloco `nav:`, ache a aba superior que pertence (`- Projeto:` ou `- Planejamento:`) e declare o anexo dela como nas atuais. Exemplo:
    ```yaml
      - A Equipe:
          - Equipe: equipe.md
          - Tópico Extra: sua-pagina.md
    ```

### 2. Editar os Cartões Grandes de Botão na Home Inicial
Como a home tem o layout que esconde a sidebar (A Landing Page central com gradient blur), o conteúdo não está no `index.md`.
Para alterar ou plugar um novo título na home inteira:
1. Acesse: `overrides/main.html`
2. Modifique os títulos das divs como `<div class="feature-title">Equipe</div>`, os ícones SGV e descrições dos paragráfos contidas nesse arquivo de visualização.

### 3. Editar a página da Equipe
Ela foge do layout rígido por conta das fotos em bolhas exclusivas e da remoção do índice sequencial. Para preencher suas bios:
1. Abra `docs/equipe.md`.
2. Troque as imagens no formato `![Seu Nome](sua_foto.png){ .team-avatar }`. Suba ela antes para pasta `images/`.
3. Preencha as propriedades dentro das `<div class="bio" markdown>`! Atenção para não trocar por `###` pois ativaria a quebra da extensão de numeração (`1.0.2...`). Sempre que quiser títulos bonitos aí dentro, use `<div class="team-name">...</div>`. Tudo já está padronizado, é só trocar texto por texto!

---

**Equipe 03 - 2026.1 IHC**
