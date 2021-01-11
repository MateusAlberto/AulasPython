import numpy as np

# Trabalhando com arrays NumPy
km = np.loadtxt('carros-km.txt')
print(km)

anos = np.loadtxt('carros-anos.txt', dtype = int)
print(anos)

km_media = km / (2019 - anos)
print(km_media)