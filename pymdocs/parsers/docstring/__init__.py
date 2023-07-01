from enum import Enum
from typing import Callable, Dict

import pymdocs.parsers.docstring.google as google
import pymdocs.parsers.docstring.numpy as numpy
from pymdocs.parsers.docstring.base import Docstring


class DocstringStyle(int, Enum):
    GOOGLE = 1
    NUMPY = 2


DOCSTRING_STYLE_MAP: Dict[DocstringStyle, Callable[[str], Docstring]] = {
    DocstringStyle.GOOGLE: google.parse,
    DocstringStyle.NUMPY: numpy.parse
}


def parse(docstring: str) -> Docstring:
    best_fit: Docstring
    n_sections = 0
    for _, parse_func in DOCSTRING_STYLE_MAP.items():
        result = parse_func(docstring)
        if len(result._attributes) >= n_sections:
            best_fit = result
            n_sections = len(result._attributes)

    return best_fit
