import argparse
import os
from typing import Optional

from pymdocs.formatters.common_formatter import Formatter
from pymdocs.parsers.ast import parse


class Pymdocs:
    """
    Class for rendering Markdown documentation

    Attributes:
        source_path: str, path to Python source code
        doc_path: str, path to documentation file
        formatter: Formatter, markdown formatter
    """

    def __init__(
        self,
        source_path: str,
        doc_path: str,
        formatter: Optional[Formatter] = None
    ):
        self.source_path = source_path
        self.doc_path = doc_path

        self.formatter = formatter or Formatter()

    @staticmethod
    def _save(md: str, path: str) -> None:
        """
        Saves markdown to documentation file

        Args:
            md: str, markdown text
            path: str, path to target file
        """
        with open(path, 'w') as f:
            f.write(md)

    def doc(self) -> None:
        """Generates Code Reference for python code"""
        if not os.path.exists(self.source_path):
            raise FileNotFoundError(
                f'Source path {self.source_path} doesn\'t exist'
            )

        definition = parse(self.source_path)
        if definition is None:
            raise ValueError(
                f'{self.source_path} is not a python package or module'
            )

        md = self.formatter.format(definition, doc_path=self.doc_path)
        self._save(md.render(), self.doc_path)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'SOURCE_PATH',
        help='Path to Python source code'
    )

    parser.add_argument(
        'DOC_PATH',
        help='Path to documentation folder'
    )

    args = parser.parse_args()

    doc = Pymdocs(
        source_path=args.SOURCE_PATH,
        doc_path=args.DOC_PATH
    )

    doc.doc()
