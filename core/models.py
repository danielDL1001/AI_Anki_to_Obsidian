from dataclasses import dataclass, field
from typing import Any


@dataclass
class Card:
    """
    Representa um flashcard importado do Anki.

    Esta classe é independente do formato de entrada (TXT, APKG,
    collection.anki2 etc.) e também do formato de saída (Markdown,
    JSON, HTML...).

    Os demais módulos trabalham apenas com objetos Card.
    """

    # Identificação
    id: str = ""
    deck: str = ""
    model: str = "Basic"

    # Conteúdo principal
    front: str = ""
    back: str = ""

    # Mídias
    audio_front: str = ""
    audio_back: str = ""
    images: list[str] = field(default_factory=list)

    # Organização
    tags: list[str] = field(default_factory=list)

    # Campos extras para modelos personalizados
    fields: dict[str, Any] = field(default_factory=dict)

    # Informações adicionais
    metadata: dict[str, Any] = field(default_factory=dict)