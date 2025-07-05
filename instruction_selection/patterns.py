"""
Autores: Heric da Silva Cruz - 548317,
         Antonio Herik Cosmo Martins - 516098,
         Ezequiel Santos Maia - 521431,
         Vitor Galvan Fernandes da Silva - 428953

[Questão 2] - implementa a fase de Seleção de Instrução.
Ele utiliza uma abordagem de programação dinâmica (percorrendo a árvore em
pós-ordem) para encontrar os melhores padrões de instrução (tiling) e
calcular o custo da solução, conforme especificado na Questão 2.
"""

from .node import Node
from .config import INSTRUCTION_COSTS


def calculate_cost(patterns: list) -> int:
    """
    Calcula o custo total a partir de uma lista de padrões e seus custos.
    """
    total_cost = 0
    for _, pattern_name in patterns:
        total_cost += INSTRUCTION_COSTS.get(pattern_name, 0)
    return total_cost


def traverse_tree(node: Node) -> list:
    """
    Percorre a árvore em pós-ordem para extrair os padrões de forma otimizada.
    Este método de travessia garante que um nó só seja processado após
    seus filhos, o que é a base para a solução com programação dinâmica.

    Retorna:
        Uma lista de tuplas contendo o nó e o nome do padrão correspondente.
    """
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
    """
    Identifica o maior padrão de instrução (maximal munch) para um nó.
    """
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
