from abc import ABC, abstractmethod
from pathlib import Path

from core.models import Card


class BaseImporter(ABC):
    """
    Classe base para todos os importadores.

    Todo importador deve implementar o método parse(),
    retornando uma lista de objetos Card.
    """

    @abstractmethod
    def parse(self, file_path: Path) -> list[Card]:
        raise NotImplementedError


def parse_file(file_path: Path, importer: BaseImporter) -> list[Card]:
    """
    Executa o importador informado.

    Args:
        file_path: Caminho do arquivo.
        importer: Instância de um importador.

    Returns:
        Lista de objetos Card.
    """

    return importer.parse(file_path)