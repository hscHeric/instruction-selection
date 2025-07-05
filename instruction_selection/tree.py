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
        """Inicia o processo de desenhar a árvore a partir da raiz."""
        self._draw_recursive(self.root)

    def _draw_recursive(self, node: Node, indent_level: int = 0):
        """
        Desenha a árvore recursivamente no terminal.
        """
        if node is not None:
            indent_step = 4

            self._draw_recursive(node.right, indent_level + indent_step)

            print(" " * indent_level + "-> " + node.instruction)

            self._draw_recursive(node.left, indent_level + indent_step)

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
