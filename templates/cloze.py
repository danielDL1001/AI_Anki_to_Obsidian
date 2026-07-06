from core.models import Card


def render(card: Card) -> str:
    """
    Renderiza um cartão do modelo Cloze.

    O conteúdo da frente deve conter as marcações
    {{c1::...}}, {{c2::...}}, etc., que serão
    interpretadas posteriormente pelo Anki.
    """

    lines = []

    # Texto com as marcações Cloze
    lines.append(card.front)

    # Alguns exportadores armazenam conteúdo adicional
    if card.back:
        lines.append("")
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