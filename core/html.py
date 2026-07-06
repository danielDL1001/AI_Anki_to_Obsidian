import html2text


def html_to_markdown(text: str) -> str:
    """
    Converte uma string HTML para Markdown.

    Se a entrada estiver vazia, retorna uma string vazia.

    Args:
        text: Conteúdo em HTML.

    Returns:
        Conteúdo convertido para Markdown.
    """
    if not text:
        return ""

    converter = html2text.HTML2Text()

    # Configurações
    converter.body_width = 0          # Não quebrar linhas automaticamente
    converter.ignore_links = False    # Preservar links
    converter.ignore_images = False   # Preservar imagens
    converter.ignore_emphasis = False # Preservar negrito/itálico
    converter.unicode_snob = True     # Preferir Unicode quando possível

    markdown = converter.handle(text)

    return markdown.strip()