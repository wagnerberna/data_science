import numpy

vetor = numpy.array([1, -3, 4.2, 5])
print(type(vetor))
print(vetor)
print(vetor[0])
print(vetor[1])

# criar uma matriz no formato array com 2 linhas e 3 colunas
# matriz de 2L x 3C
#  .ones(preenche com o número 1)
matriz = numpy.ones((2, 3))
print(type(matriz))
print(matriz)

# valores do array preenchem de uma diagonal a outra da matriz
# matriz 5l X 5c
matriz_diagonal = numpy.diag((2, 4, 6, 8, 10))
print(matriz_diagonal)
