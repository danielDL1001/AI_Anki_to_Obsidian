
from core.models import Card


def render(card: Card) -> str:
    """
    Gera o Markdown de um cartão do modelo Basic.

    Args:
        card: Objeto Card contendo os dados do flashcard.

    Returns:
        Uma string em Markdown compatível com o Obsidian_to_Anki.
    """

    lines = []

    # Frente
    lines.append(card.front)
    lines.append("?")

    # Verso
    lines.append(card.back)

    # Áudios
    if card.audio_front:
        lines.append("")
        lines.append(card.audio_front)

    if card.audio_back:
        lines.append(card.audio_back)

    # Tags
    if card.tags:
        lines.append("")
        lines.append(
            "Tags: " + " ".join(f"#{tag}" for tag in card.tags)
        )

    return "\n".join(lines).strip()