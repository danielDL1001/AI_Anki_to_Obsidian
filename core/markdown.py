from core.models import Card

from templates import basic
from templates import cloze
from templates import reversed


# Registro dos templates disponíveis
TEMPLATES = {
    "Basic": basic.render,
    "Basic Reversed": reversed.render,
    "Cloze": cloze.render,
}


def render_card(card: Card) -> str:
    """
    Renderiza um Card utilizando o template correspondente
    ao seu modelo.

    Args:
        card: Cartão a ser convertido.

    Returns:
        Markdown gerado pelo template.
    """

    renderer = TEMPLATES.get(card.model)

    if renderer is None:
        raise ValueError(
            f"Modelo não suportado: {card.model}"
        )

    return renderer(card)