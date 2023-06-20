import argparse
from pathlib import Path

from pymdocs.markdown_formatter import Formatter, format_package_md
from pymdocs.parsers.ast import parse


class Pymdocs:

    def __init__(
        self,
        source_path: str,
        doc_path: str,
        formatter: type[Formatter] = Formatter
    ):
        self.source_path = source_path
        self.doc_path = doc_path
        self.formatter = formatter

    @staticmethod
    def _save(md: str, path: Path):
        with path.open('w') as f:
            f.write(md)

    def doc(self):
        source_path = Path(self.source_path)
        doc_path = Path(self.doc_path)

        if not source_path.exists():
            raise FileNotFoundError(
                f'Source path {source_path} doesn\'t exist'
            )
        elif source_path.is_file():
            formatter = self.formatter(
                source_path.as_posix(),
                doc_path.as_posix()
            )

            module_def = parse(source_path.as_posix())
            module_md = formatter.module_md(module_def)
            self._save(module_md.render(), doc_path)
        elif source_path.is_dir():
            modules = []
            module_links = []

            base_package_name = source_path.name
            for module_path in source_path.rglob('*.py'):
                relative_path = module_path.relative_to(source_path).parent
                module_name = module_path.name.replace('.py', '')
                if module_name.startswith('_'):
                    continue

                module_package_name = base_package_name

                if relative_path.parts:
                    module_package_name = (
                        module_package_name
                        + '.'
                        + '.'.join(relative_path.parts)
                    )

                formatter = self.formatter(
                    module_path,
                    doc_path,
                    module_package_name
                )

                module_def = parse(module_path.as_posix())
                module_md = formatter.module_md(module_def)

                modules.append(module_md)
                module_links.append(formatter.module_link())

            package_md = format_package_md(
                base_package_name,
                modules,
                module_links
            )

            self._save(package_md.render(), doc_path)


def main():
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
        doc_path=args.DOC_PATH,
        formatter=Formatter
    )

    doc.doc()
