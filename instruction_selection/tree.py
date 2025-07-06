"""
Autores: Heric da Silva Cruz - 548317,
         Antonio Herik Cosmo Martins - 516098,
         Ezequiel Santos Maia - 521431,
         Vitor Galvan Fernandes da Silva - 428953

[Questão 1] - Contém a lógica de parsing para construir a árvore e um método
para imprimi-la no terminal em um formato hierárquico, atendendo aos
requisitos da Questão 1.
"""

from .node import Node


class Tree:
    """Representa e gerencia a árvore de expressão."""

    def __init__(self, root: Node = None):
        """Inicializa a árvore."""
        self.root = root
        self.REDUCIBLE_INSTRUCTIONS = {"MOVE", "MEM", "+", "-", "*", "/"}

    def _is_compound_instruction(self, instruction_type: str) -> bool:
        """Verifica se a instrução é composta (ex: 'CONST 1')."""
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

        # Remove os nós-filho vazios
        children = [child for child in node.get_children() if child]
        
        for i, child in enumerate(children):
            is_child_last = (i == len(children) - 1)
            self._draw_recursive(child, child_indent, is_child_last)

    def create_tree(self, linear_code: str):
        """
        Cria a árvore a partir de uma representação de código linear.
        """
        formatted_code = (
            linear_code.replace("(", " ( ").replace(")", " ) ").replace(",", " , ")
        )
        tokens = formatted_code.split()

        self.root = self._create_tree_recursive(tokens)

    def _create_tree_recursive(self, tokens: list) -> Node:
        """
        Função auxiliar recursiva que constrói a árvore consumindo a lista de tokens.
        """
        if not tokens:
            return None

        token = tokens.pop(0)

        if self._is_compound_instruction(token) and tokens:
            token += " " + tokens.pop(0)

        node = Node(token)

        instruction_type = token.split()[0]
        if instruction_type in self.REDUCIBLE_INSTRUCTIONS:
            if tokens and tokens[0] == "(":
                tokens.pop(0)  # Consome o '('

            node.left = self._create_tree_recursive(tokens)

            if tokens and tokens[0] == ",":
                tokens.pop(0)  # Consome a ','
                node.right = self._create_tree_recursive(tokens)

            if tokens and tokens[0] == ")":
                tokens.pop(0)  # Consome o ')'

        return node
