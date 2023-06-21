import os
from pathlib import Path

import pymdocs.formatters.markdown_constructor as md
from pymdocs.parsers.ast import AstWrapper


def module_line_path_link(
    element: AstWrapper,
    text: str,
    doc_path: str
) -> md.Link:
    """
    Returns reference Markdown link to object

    Args:
        element: AstWrapper, element needed to reference
        text: str, reference link text
        doc_path: str, path to documentation file

    Returns:
        Link: reference link to object
    """

    relpath = Path(
        os.path.relpath(
            element.path,
            os.path.dirname(doc_path)
        )
    ).as_posix()

    pos = element.lineno

    if pos is not None:
        relpath += f'#L{pos}'

    return md.Link(text, relpath)
