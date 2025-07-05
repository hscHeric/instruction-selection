"""
Autores: Heric da Silva Cruz - 548317,
         Antonio Herik Cosmo Martins - 516098,
         Ezequiel Santos Maia - 521431,
         Vitor Galvan Fernandes da Silva - 428953

[Questão 2 e 3] -Esse arquivo apresenta os custos de cada padrão de instrução,
conforme definido na Questão 2, e os templates de código Assembly para cada
padrão, necessários para a geração de código da Questão 3.
"""

INSTRUCTION_COSTS = {
    "TEMP": 0,
    "FP": 1,
    "+": 1,
    "*": 1,
    "-": 1,
    "/": 1,
    "+ -> CONST": 1,
    "+ --> CONST": 1,
    "CONST": 1,
    "- --> CONST": 1,
    "MEM -> + --> CONST": 1,
    "MEM -> + -> CONST": 1,
    "MEM -> CONST": 1,
    "MEM": 1,
    "MOVE -> MEM -> + --> CONST": 1,
    "MOVE -> MEM -> + -> CONST": 1,
    "MOVE -> MEM -> CONST": 1,
    "MOVE -> MEM": 1,
    "MOVE -> MEM ===> MEM": 2,
}

# [Questão 3]
PATTERNS_INSTRUCTIONS = {
    "+": "ADD r{i} <- {j} + {k}",
    "*": "MUL r{i} <- {j} * {k}",
    "-": "SUB r{i} <- {j} - {k}",
    "/": "DIV r{i} <- {j} / {k}",
    "+ -> CONST": "ADDI r{i} <- {j} + {c}",
    "+ --> CONST": "ADDI r{i} <- {j} + {c}",
    "CONST": "ADDI r{i} <- r0 + {c}",
    "- --> CONST": "SUBI r{i} <- {j} - {c}",
    "MEM -> + --> CONST": "LOAD r{i} <- M[{j} + {c}]",
    "MEM -> + -> CONST": "LOAD r{i} <- M[{j} + {c}]",
    "MEM -> CONST": "LOAD r{i} <- M[r0 + {c}]",
    "MEM": "LOAD r{i} <- M[{j}]",
    "MOVE -> MEM -> + --> CONST": "STORE M[{j} + {c}] <- r{i}",
    "MOVE -> MEM -> + -> CONST": "STORE M[{j} + {c}] <- r{i}",
    "MOVE -> MEM -> CONST": "STORE M[r0 + {c}] <- r{i}",
    "MOVE -> MEM": "STORE M[{j}] <- r{i}",
    "MOVE -> MEM ===> MEM": "MOVEM M[{j}] <- M[{i}]",
}
