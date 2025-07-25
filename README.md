# Seleção de Instruções para Arquitetura Jouett

Este projeto implementa um selecionador de instruções para uma arquitetura hipotética, como parte de um trabalho da disciplina de Compiladores. O programa lê uma representação intermediária de código em formato linear, constrói árvores de expressão, aplica um algoritmo de programação dinâmica para selecionar os melhores padrões de instrução e, por fim, gera o código Assembly correspondente.

## Autores

* **Heric da Silva Cruz** - 548317
* **Antonio Herik Cosmo Martins** - 516098
* **Ezequiel Santos Maia** - 521431
* **Vitor Galvan Fernandes da Silva** - 428953

## Funcionalidades

O projeto está dividido em três partes principais, correspondendo às questões do trabalho:

1. **Construção e Impressão da Árvore**: Converte a entrada linear em uma árvore de expressão e a exibe no terminal.
2. **Seleção de Instruções e Cálculo de Custo**: Utiliza programação dinâmica (travessia em pós-ordem) para encontrar os padrões de instrução de menor custo.
3. **Geração de Código Assembly**: Traduz os padrões selecionados para o código de máquina equivalente da arquitetura Jouett.

## Como Executar

1. Certifique-se de que o arquivo `data/source.txt` contém as instruções em formato linear que você deseja processar.
2. Abra um terminal na pasta raiz do projeto.
3. Execute o script principal:

    ```bash
    python main.py
    ```

4. A saída será impressa no terminal, mostrando a árvore, os padrões, o custo e o código Assembly para cada linha do arquivo de entrada.
# instruction-selection
