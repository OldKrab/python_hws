from typing import Any


def table_to_tex(table: list[list[Any]]) -> str:
    def row_to_tex(row: list[Any]) -> str:
        return " & ".join(str(elem) for elem in row) + r" \\"

    cols_count = len(table[0]) if len(table) > 0 else 1
    cols_def = "|" + "|".join("c"*cols_count) + "|"
    content = "\n\\hline\n".join(row_to_tex(row) for row in table)
    return Rf"""
\begin{{table}}[h!]
\centering
\begin{{tabular}}{{ {cols_def} }}
\hline
{content}
\hline
\end{{tabular}}
\end{{table}}
"""


def image_to_tex(image_path: str) -> str:
    return fr"\includegraphics[width=\textwidth]{{ {image_path} }}"

