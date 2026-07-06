from core.models import Card


def _render_single(front: str, back: str) -> str:
    """
    Renderiza um único cartão no formato Basic.
    """

    lines = [
        front,
        "?",
        "",
        back,
    ]

    return "\n".join(lines)


def render(card: Card) -> str:
    """
    Renderiza um cartão do modelo Basic Reversed.

    Gera dois cartões:
    - Frente -> Verso
    - Verso -> Frente
    """

    normal = _render_single(card.front, card.back)

    reversed_card = _render_single(card.back, card.front)

    sections = [
        normal,
        "---",
        reversed_card,
    ]

    if card.audio_front or card.audio_back:
        sections.extend([
            "",
            card.audio_front,
            card.audio_back,
        ])

    if card.tags:
        sections.extend([
            "",
            "Tags: " + " ".join(f"#{tag}" for tag in card.tags)
        ])

    return "\n".join(
        line for line in sections if line != ""
    ).strip()