# anki-to-obsidian

Uma ferramenta em Python para migrar coleções do Anki para um fluxo de estudo baseado no Obsidian.

O objetivo deste projeto é transformar o **Obsidian** na principal fonte de edição dos flashcards, utilizando o **Anki** apenas como mecanismo de revisão espaçada.

Fluxo proposto:

```
Anki (coleção antiga)
        │
        ▼
anki-to-obsidian
        │
        ▼
Obsidian (.md)
        │
        ▼
Obsidian_to_Anki
        │
        ▼
Anki (revisão)
```

Após a migração inicial, toda a edição dos cartões pode ser feita diretamente no Obsidian.

---

# 🤖 Aviso sobre o desenvolvimento

Este projeto foi desenvolvido com auxílio de Inteligência Artificial durante todo o processo de arquitetura, planejamento e implementação do código.

O mantenedor do projeto coordenou o desenvolvimento, definiu os requisitos, revisou as decisões técnicas e conduziu a evolução do projeto, enquanto a IA foi utilizada como ferramenta de apoio na geração e refinamento do código.

A transparência sobre esse processo faz parte da filosofia deste projeto.

---

# Funcionalidades (MVP)

* Importação de arquivos TXT exportados pelo Anki
* Conversão de HTML para Markdown
* Preservação de:

  * Frente
  * Verso
  * Áudio
  * Tags
* Exportação em Markdown
* Arquitetura modular para futuras expansões

---

# Roadmap

## MVP

* [x] Importar TXT
* [x] Converter HTML
* [x] Gerar Markdown
* [x] Preservar áudios
* [x] Preservar tags

## Futuro

* Importar APKG
* Importar collection.anki2
* Copiar mídia automaticamente
* Interface de linha de comando (CLI)
* Interface gráfica
* Novos exportadores
* Novos templates
* Suporte a imagens
* Suporte a modelos personalizados

---

# Estrutura do projeto

```
anki-to-obsidian/

converter.py
config.json
requirements.txt
README.md

core/
importers/
templates/
input/
output/
```

---

# Requisitos

* Python 3.10 ou superior

---

# Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd anki-to-obsidian
```

Crie um ambiente virtual:

Linux/macOS:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Exportando cartões do Anki

No Anki:

```
Arquivo
→ Exportar
→ Texto simples (*.txt)
```

Exporte sua coleção para um arquivo `.txt`.

---

# Preparando os arquivos

Crie a pasta:

```
input/
```

Coloque o arquivo exportado dentro dela.

Exemplo:

```
input/
    meus_flashcards.txt
```

---

# Configuração

Edite o arquivo `config.json`.

Exemplo:

```json
{
    "input": "./input",
    "output": "./output",
    "convertHtml": true,
    "exportMode": "singleFile"
}
```

---

# Executando

Basta executar:

```bash
python converter.py
```

O resultado será gerado em:

```
output/
```

---

# Estrutura da arquitetura

```
TXT
 │
 ▼
Importer
 │
 ▼
Card
 │
 ▼
Conversão HTML
 │
 ▼
Template
 │
 ▼
Markdown
 │
 ▼
Exporter
 │
 ▼
Arquivo .md
```

---

# Filosofia do projeto

Este projeto busca seguir alguns princípios:

* Código limpo
* Responsabilidade única por módulo
* Arquitetura modular
* Fácil manutenção
* Fácil expansão
* Preparado para novos formatos de importação e exportação

O objetivo não é ser apenas um script de conversão, mas uma ferramenta reutilizável para migração entre Anki e Obsidian.

---

# Contribuições

Contribuições são bem-vindas.

Caso encontre algum problema ou tenha sugestões de melhoria, abra uma Issue ou envie um Pull Request.


# Licença

Este projeto está licenciado sob a licença MIT.
