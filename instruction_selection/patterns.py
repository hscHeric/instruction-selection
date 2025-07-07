"""
Autores: Heric da Silva Cruz - 548317,
         Antonio Herik Cosmo Martins - 516098,
         Ezequiel Santos Maia - 521431,
         Vitor Galvan Fernandes da Silva - 428953

[Questão 2] - Implementação da seleção de instruções
"""

from .node import Node
from .config import INSTRUCTION_COSTS


def calculate_cost(patterns: list) -> int:
    total_cost = 0
    for _, pattern_name in patterns:
        total_cost += INSTRUCTION_COSTS.get(pattern_name, 0)
    return total_cost


def traverse_tree(node: Node) -> list:
    patterns = []

    def post_order_traversal(n: Node):
        if n is None or n.is_used:
            return

        post_order_traversal(n.left)
        post_order_traversal(n.right)

        pattern = find_pattern_for_node(n)
        if pattern:
            patterns.append((n, pattern))

    post_order_traversal(node)
    return patterns


def find_pattern_for_node(node: Node) -> str:
    if node.is_used:
        return ""

    instr_type = node.instruction.split()[0]

    if instr_type == "MOVE":
        if (
            node.left
            and node.left.instruction.split()[0] == "MEM"
            and node.right
            and node.right.instruction.split()[0] == "MEM"
        ):
            node.is_used = True
            node.left.is_used = True
            node.right.is_used = True
            return "MOVE -> MEM ===> MEM"

    elif instr_type == "MEM":
        if node.left:
            child = node.left
            child_instr_type = child.instruction.split()[0]

            if child_instr_type == "CONST":
                node.is_used = True
                child.is_used = True
                return "MEM -> CONST"

            elif (
                child_instr_type == "+"
                and child.right
                and child.right.instruction.split()[0] == "CONST"
            ):
                node.is_used = True
                child.is_used = True
                child.left.is_used = True
                child.right.is_used = True
                return "MEM -> + --> CONST"

    node.is_used = True
    return instr_type
