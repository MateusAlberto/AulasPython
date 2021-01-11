import numpy as np

km = np.loadtxt(fname = 'carros-km.txt')
anos = np.loadtxt(fname = 'carros-anos.txt', dtype = int)
valor = np.loadtxt(fname = 'carros-valor.txt')

dataset = np.column_stack((anos, km, valor))
# print(dataset)
print(dataset.shape)

# média de um conjunto de dados
media_km = np.mean(dataset[:, 1])
print(media_km)
media_valores = np.mean(dataset[:, 2])
print(media_valores)

# desvio padrão de um conjunto de dados
dp_km = np.std(dataset[:, 1])
print(dp_km)
dp_valores = np.std(dataset[:, 2])
print(dp_valores)

# somatório de conjuntos de dados
somatorio = np.sum(dataset, axis = 0)
print(somatorio)
somatorio_valores = np.sum(dataset[:, 2])
print(somatorio_valores)