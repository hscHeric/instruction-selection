"""
Autores: Heric da Silva Cruz - 548317,
         Antonio Herik Cosmo Martins - 516098,
         Ezequiel Santos Maia - 521431,
         Vitor Galvan Fernandes da Silva - 428953

[Questão 1] - Lógica de parsing para construir a árvore e um método para imprimir no terminal
"""

from .node import Node


class Tree:
    def __init__(self, root: Node = None):
        self.root = root
        self.REDUCIBLE_INSTRUCTIONS = {"MOVE", "MEM", "+", "-", "*", "/"}

    def _is_compound_instruction(self, instruction_type: str) -> bool:
        return instruction_type in ["CONST", "TEMP"]

    def draw(self):
        self._draw_recursive(self.root, "", True)

    def _draw_recursive(self, node: Node, indent: str, is_last_child: bool):
        if node is None:
            return

        if indent is not "":
            print(indent + ("`-> " if is_last_child else "|-> ") + node.instruction)
        else:
            print("    " + node.instruction)

        child_indent = indent + ("    " if is_last_child else "|   ")

        children = [child for child in node.get_children() if child]

        for i, child in enumerate(children):
            is_child_last = i == len(children) - 1
            self._draw_recursive(child, child_indent, is_child_last)

    def create_tree(self, linear_code: str):
        formatted_code = (
            linear_code.replace("(", " ( ").replace(")", " ) ").replace(",", " , ")
        )
        tokens = formatted_code.split()

        self.root = self._create_tree_recursive(tokens)

    def _create_tree_recursive(self, tokens: list) -> Node:
        if not tokens:
            return None

        token = tokens.pop(0)

        if self._is_compound_instruction(token) and tokens:
            token += " " + tokens.pop(0)

        node = Node(token)

        instruction_type = token.split()[0]
        if instruction_type in self.REDUCIBLE_INSTRUCTIONS:
            if tokens and tokens[0] == "(":
                tokens.pop(0)

            node.left = self._create_tree_recursive(tokens)

            if tokens and tokens[0] == ",":
                tokens.pop(0)
                node.right = self._create_tree_recursive(tokens)

            if tokens and tokens[0] == ")":
                tokens.pop(0)

        return node
