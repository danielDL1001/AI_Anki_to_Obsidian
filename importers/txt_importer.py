from pathlib import Path
import csv

from core.models import Card
from core.parser import BaseImporter


class TXTImporter(BaseImporter):
    """
    Importa cartões a partir de um arquivo TXT exportado pelo Anki.
    """

    def parse(self, file_path: Path) -> list[Card]:
        separator = "\t"
        cards: list[Card] = []

        with file_path.open(
            "r",
            encoding="utf-8",
            newline=""
        ) as file:

            lines = file.readlines()

        data_lines = []

        # Processa cabeçalhos do Anki
        for line in lines:
            line = line.rstrip("\n")

            if line.startswith("#separator:"):
                value = line.split(":", 1)[1].strip()

                if value == "tab":
                    separator = "\t"
                elif value == "semicolon":
                    separator = ";"
                elif value == "comma":
                    separator = ","

                continue

            if line.startswith("#"):
                continue

            if line.strip():
                data_lines.append(line)

        reader = csv.reader(
            data_lines,
            delimiter=separator
        )

        for row in reader:

            if len(row) < 2:
                continue

            front = row[0].strip()
            back = row[1].strip()

            audio_front = row[2].strip() if len(row) > 2 else ""
            audio_back = row[3].strip() if len(row) > 3 else ""

            tags = []

            if len(row) > 4 and row[4].strip():
                tags = row[4].split()

            cards.append(
                Card(
                    front=front,
                    back=back,
                    audio_front=audio_front,
                    audio_back=audio_back,
                    tags=tags,
                )
            )

        return cards