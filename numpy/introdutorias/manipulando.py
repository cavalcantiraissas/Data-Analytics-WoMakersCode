# Atividade 01 - a : 
# Selecione a segunda coluna com a quantidade de espécies 
# encontradas e adicione em um array as qtd_especies.

import numpy as np

especies = np.array([
    [747, 89, 33, 5],
    [623, 123, 32, 13],
    [501, 22, 49, 2],
    [116, 101, 42, 10],
    [297, 56, 69, 22],
    [613, 64, 27, 7],
    [295, 84, 29, 14],
    [692, 105, 72, 16],
    [229, 103, 35, 5],
    [374, 124, 70, 1]
])

qtd_especies = especies[:, 1]
print(qtd_especies)

# Atividade 01 - b :
# De qtd_especies selecione apenas as primeiras 3 quantidades e print.

primeiras_3 = qtd_especies[:3]
print(primeiras_3)

# Atividade 01 - c :
# Print as 5 últimas quantidades de espécies.

ultimas_5 = qtd_especies[-5:]
print(ultimas_5)

# Atividade 01 - d :
# Crie um array que contenha apenas os tamanhos das espécies e ordene por ordem crescente.

tamanhos = especies[:, 2]

tamanhos_ordenados = np.sort(tamanhos)
print(tamanhos_ordenados)

# Atividade 02 - a :
# Usando um index boolean, crie um array que contém os dados da maior espécie encontrada 
# (considerando o seu tamanho), esse valor corresponde ao valor 22.

maior_especie = especies[especies[:, 3] == 22]
print(maior_especie)

# Atividade 02 - b :
# Usando fancy index, faça um array que contém apenas dados da espécie com ID 297.

especie_297 = especies[especies[:, 0] == 297]
print(especie_297)

# Atividade 02 - c :
# Usando np.where(), faça um array com a linha com dados correspondentes à 
# espécie com 105 representantes encontrados.

linha_105 = especies[np.where(especies[:, 1] == 105)]
print(linha_105)

# Atividade 02 - d :
# Considere a profundidade em que a espécie foi encontrada e 
# substitua valores maiores que 60 com "Profundo”.

profundidade = especies[:, 2]
profundidade_modificada = np.where(profundidade > 60, "Profundo", profundidade)
print(profundidade_modificada)

# Atividade 03 - a :
# Adicione mais 2 espécies ao array: [[204, 10, 40, 12], [392, 11, 81, 11]].

novas_especies = np.array([[204, 10, 40, 12], [392, 11, 81, 11]])
especies = np.vstack((especies, novas_especies))
print(especies)

# Atividade 03 - b :
# Adicione mais uma coluna no array original agora com o número de espécies 
# encontradas que indica se o animal enxerga ou não: [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0].

enxerga = np.array([0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0])
especies = np.column_stack((especies, enxerga))
print(especies)
