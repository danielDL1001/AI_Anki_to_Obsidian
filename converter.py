from pathlib import Path
import json

from core.html import html_to_markdown
from core.markdown import render_card
from core.exporter import MarkdownExporter
from core.parser import parse_file

from importers.txt_importer import TXTImporter


def load_config(path: str = "config.json") -> dict:
    """
    Carrega o arquivo de configuração.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    config = load_config()

    input_dir = Path(config["input"])
    output_dir = Path(config["output"])

    exporter = MarkdownExporter(output_dir)

    markdown_cards = []

    for txt_file in input_dir.glob("*.txt"):

        cards = parse_file(
            txt_file,
            TXTImporter(),
        )

        for card in cards:

            if config.get("convertHtml", True):
                card.front = html_to_markdown(card.front)
                card.back = html_to_markdown(card.back)

            markdown_cards.append(
                render_card(card)
            )

    export_mode = config.get("exportMode", "singleFile")

    if export_mode == "singleFile":
        exporter.export_single_file(
            filename="anki.md",
            markdown_cards=markdown_cards,
        )

    elif export_mode == "oneFilePerCard":
        exporter.export_one_file_per_card(
            markdown_cards
        )

    else:
        raise ValueError(
            f"Modo de exportação inválido: {export_mode}"
        )


if __name__ == "__main__":
    main()