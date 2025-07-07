"""
Autores: Heric da Silva Cruz - 548317,
         Antonio Herik Cosmo Martins - 516098,
         Ezequiel Santos Maia - 521431,
         Vitor Galvan Fernandes da Silva - 428953

[Questão 1, 2 e 3] - Node para árvore de expressão
"""


class Node:
    """Representa um nó na árvore de expressão."""

    def __init__(self, instruction: str):
        """
        Inicializa um nó.

        Args:
            instruction: A instrução associada a este nó.
        """
        self.instruction = instruction
        self.parent = None
        self.left = None
        self.right = None
        self.is_used = False

    def get_children(self):
        """Retorna os filhos do nó (esquerdo, direito)."""
        return (self.left, self.right)

    def get_value(self, reg: int = 0) -> str:
        """
        Obtém o valor ou registrador associado a uma instrução.

        Args:
            reg: O número do registrador a ser usado como padrão.

        Returns:
            O valor ou nome do registrador como uma string.
        """
        parts = self.instruction.split()
        instr_type = parts[0]

        if instr_type == "CONST":
            return parts[1]
        elif instr_type == "FP":
            return "fp"
        elif instr_type == "TEMP":
            return f"r{parts[1]}"
        else:
            return f"r{reg}"
