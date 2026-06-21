# Listas Compostas: Notas de Alunos em Python

Projeto de estudo desenvolvido em Python que permite cadastrar alunos, armazenar suas notas em listas compostas, calcular a média e consultar as notas individuais pelo nome.

## Objetivo do projeto

Praticar conceitos fundamentais da linguagem Python, como:

- Listas simples e listas compostas
- Entrada de dados pelo terminal
- Estruturas de repetição (`while` e `for`)
- Estruturas condicionais (`if` e `elif`)
- Uso de `enumerate()`
- Acesso a elementos por índice
- Cálculo de média
- Formatação de saída com `f-string`
- Comparação de strings com `.upper()`
- Controle de fluxo com `break`

## Funcionalidades

- Solicita o nome do aluno
- Solicita duas notas para cada aluno
- Armazena cada aluno em uma lista interna
- Armazena todos os alunos em uma lista principal
- Exibe uma tabela com número, nome e média
- Permite consultar as notas de um aluno pelo nome
- Permite encerrar a consulta digitando `999`

## Tecnologias utilizadas

- Python 3
- Execução via terminal ou IDE (PyCharm, VS Code, etc.)

## Exemplo de uso

```text
----------------------- CADASTRO DE ALUNO -----------------------

Digite o nome do aluno: João
Digite a primeira nota do aluno: 8
Digite a segunda nota do aluno: 9
Deseja continuar? S/N: S

----------------------- CADASTRO DE ALUNO -----------------------

Digite o nome do aluno: Maria
Digite a primeira nota do aluno: 7
Digite a segunda nota do aluno: 8
Deseja continuar? S/N: N

----------------------- TABELA DE MÉDIAS -----------------------

Nº    | Nome       | Média
0     | João       | 8.50
1     | Maria      | 7.50

----------------------- CONSULTA DE NOTAS -----------------------

Digite o nome do aluno que você quer ver as notas (999 interrompe): João
As notas de João foram 8.0, 9.0

Digite o nome do aluno que você quer ver as notas (999 interrompe): 999
