from pathlib import Path


class MarkdownExporter:
    """
    Responsável por escrever arquivos Markdown.
    """

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_single_file(
        self,
        filename: str,
        markdown_cards: list[str],
    ) -> Path:
        """
        Exporta todos os cartões para um único arquivo.
        """

        output_file = self.output_dir / filename

        content = "\n\n---\n\n".join(markdown_cards)

        output_file.write_text(
            content,
            encoding="utf-8",
        )

        return output_file

    def export_one_file_per_card(
        self,
        markdown_cards: list[str],
        prefix: str = "card",
    ) -> list[Path]:
        """
        Exporta um arquivo Markdown para cada cartão.
        """

        files: list[Path] = []

        for index, markdown in enumerate(markdown_cards, start=1):
            file_path = self.output_dir / f"{prefix}_{index}.md"

            file_path.write_text(
                markdown,
                encoding="utf-8",
            )

            files.append(file_path)

        return files