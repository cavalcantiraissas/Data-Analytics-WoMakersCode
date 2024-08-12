# Atividade 1 :
# O cliente que teve acidente abaixo da média nos últimos 2 anos,
# ganhará um desconto no seu seguro. Identifique-os.

import numpy as np

acidentes = np.array([[1, 3, 2],
                      [0, 1, 0],
                      [2, 1, 4],
                      [0, 0, 0],
                      [1, 1, 0]])

media_acidentes = np.mean(acidentes[:, 1:], axis=1)

clientes_desconto = acidentes[media_acidentes < np.mean(media_acidentes)]
print(clientes_desconto)

# Atividade 2 :
# Qual cliente teve pelo menos 2 anos sem cometer acidentes?

clientes_sem_acidente = np.sum(acidentes[:, 1:] == 0, axis=1) >= 2
print(acidentes[clientes_sem_acidente])

# Atividade 3 :
# Uma professora quer que seus alunos apliquem a função (3x + 2y + x*y)
#  em um conjunto de dados. Ela dá dois arrays aos estudantes e pede que 
# seja feita essa operação.

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

resultado = 3*x + 2*y + x*y
print(resultado)

# Atividade 4:
# A mesma professora percebeu que houve um erro em todas as provas dos estudantes e esqueceu
#  de anotar a nota de trabalhos apresentados durante o semestre. Já que foi feito em 
# grupo, ela vai adicionar a mesma nota para todos os estudantes.
#  No array cada estudante representa uma linha e cada coluna uma prova. 
# Adicione para cada prova de cada estudante os valores: 1, 2, 1.

notas = np.array([[7, 8, 9],
                  [6, 7, 8],
                  [5, 6, 7]])

notas_ajustadas = notas + np.array([1, 2, 1])
print(notas_ajustadas)
