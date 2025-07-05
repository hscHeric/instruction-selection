"""
Autores: Heric da Silva Cruz - 548317,
Antonio Herik Cosmo Martins - 516098,
Ezequiel Santos Maia - 521431
Vitor Galvan Fernandes da Silva - 428953

Este script executa a seleção de instruções para uma representação intermediária.
Ele lê um arquivo fonte, constrói uma árvore de expressão para cada linha,
identifica padrões de instrução, calcula o custo e gera o código Assembly correspondente.

Uso:
    python main.py
"""

import os
from instruction_selection.tree import Tree
from instruction_selection.patterns import traverse_tree, calculate_cost
from instruction_selection.instructions import get_instructions


def main():
    source_path = os.path.join("data", "source.txt")

    try:
        with open(source_path, "r") as file:
            instruction_counter = 1
            for line in file:
                line = line.strip()
                if not line:
                    continue

                print(f" Instrução {instruction_counter} ")

                # 1. Criar a Árvore
                print("\nÁrvore: ")
                tree = Tree()
                tree.create_tree(line)
                tree.draw()

                print("\nPadrões e Custos: \n")
                patterns = traverse_tree(tree.root)
                for _, pattern_name in patterns:
                    print(pattern_name)

                cost = calculate_cost(patterns)
                print(f"\nCusto total = {cost}")

                print("\nInstruções Assembly: \n")
                assembly_instructions = get_instructions(patterns)
                print(assembly_instructions)
                print("\n")

                instruction_counter += 1

    except FileNotFoundError:
        print(f"Erro: O arquivo '{source_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
