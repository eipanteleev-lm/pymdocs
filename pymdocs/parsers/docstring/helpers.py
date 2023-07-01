import re
from typing import Iterator, Optional, Tuple


def iter_split(
    pattern: re.Pattern,
    text: str
) -> Iterator[Tuple[Optional[re.Match], str, int, int]]:
    """
    Iterates through pattern matches and yiedls text between them

    Args:
        pattern: re.Pattern, pattern to search
        text: str, text to search pattern

    Yields:
        tuple[(re.Match | None), str, int, int]: tuple of match,
            text till next metch or text end, start of match and end of text
    """
    pos = 0
    last_group: Optional[re.Match] = None

    for group in pattern.finditer(text):
        last_group_end = group.start()
        last_group_start = (
            0 if last_group is None
            else last_group.start()
        )

        yield (
            last_group,
            text[pos:last_group_end],
            last_group_start,
            last_group_end
        )

        pos = group.end()
        last_group = group

    last_group_end = len(text)
    last_group_start = (
        0 if last_group is None
        else last_group.start()
    )

    yield (
        last_group,
        text[pos:last_group_end],
        last_group_start,
        last_group_end
    )
