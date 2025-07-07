"""
Autores: Heric da Silva Cruz - 548317,
         Antonio Herik Cosmo Martins - 516098,
         Ezequiel Santos Maia - 521431,
         Vitor Galvan Fernandes da Silva - 428953

[Questão 3] - Conversão para os padrões da árvore
"""

from .config import PATTERNS_INSTRUCTIONS


def get_instructions(patterns: list) -> str:
    reg1, reg2 = 1, 2
    output_lines = []

    for line_num, (node, pattern) in enumerate(reversed(patterns), 1):
        if pattern in {"FP", "TEMP"}:
            continue

        template = PATTERNS_INSTRUCTIONS.get(pattern)
        if not template:
            continue

        line = ""
        if pattern in ["+", "*", "-", "/"]:
            left_val = node.left.get_value(reg1)
            right_val = node.right.get_value(reg2)
            line = template.format(i=reg1, j=left_val, k=right_val)

        elif pattern in ["+ -> CONST", "+ --> CONST", "- --> CONST"]:
            j_val = node.left.get_value(reg2)
            c_val = node.right.get_value()
            line = template.format(i=reg2, j=j_val, c=c_val)

        elif pattern == "CONST":
            c_val = node.get_value()
            line = template.format(i=reg2, c=c_val)

        elif pattern == "MEM":
            j_val = node.left.get_value(reg1)
            line = template.format(i=reg2, j=j_val)

        elif pattern == "MEM -> CONST":
            c_val = node.left.get_value()
            line = template.format(i=reg2, c=c_val)

        elif pattern == "MOVE -> MEM ===> MEM":
            i_val = node.right.get_value(reg2)
            j_val = node.left.get_value(reg1)
            line = template.format(i=i_val, j=j_val)

        if line:
            output_lines.append(f"{line_num}: {line}")

    return "\n".join(output_lines)
