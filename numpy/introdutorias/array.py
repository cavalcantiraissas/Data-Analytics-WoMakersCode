# Atividade 01 :
# Crie um array com 4 linhas e 3 colunas com valores aleatórios.

import numpy as np

array1 = np.random.rand(4, 3)
print(array1)

# Atividade 02 :
# Crie um array com valores inteiros, 3 linhas e 5 colunas com valores aleatórios.

array2 = np.random.randint(1, 100, size=(3, 5))
print(array2)

# Atividade 03 :
# Crie um array com 5 colunas e 10 linhas inicializados com zeros.

array3 = np.zeros((10, 5))
print(array3)

# Atividade 04 :
# Crie um array que vá entre 0 e 90 pulando de 4 em 4.

array4 = np.arange(0, 91, 4)
print(array4)

# Atividade 05 :
# Reduza o array (5,7) a apenas uma dimensão.

array5 = np.random.rand(5, 7)

array5_flattened = array5.flatten()
print(array5_flattened)

# Atividade 06 :
# Considerando que você é uma organizadora de um jogo de bingo.
# Crie um array que irá representar a cartilha desses jogos de bingo. 
# Os números das suas cartelas variam entre 1 e 30, e você terá 10 participantes.
# Cada cartela terá 12 números (4, 3). Crie um array que representa esse jogo.

cartelas = np.random.randint(1, 31, size=(10, 4, 3))
print(cartelas)

# Atividade 07 : 
# Faça o reshape das suas cartelas para que haja 5 cartelas de 4 linhas e 6 colunas.

cartelas_reshaped = cartelas.reshape(5, 4, 6)
print(cartelas_reshaped)
