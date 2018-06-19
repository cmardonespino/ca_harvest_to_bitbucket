# -- coding: utf-8 --

import os, sys
from variables import path

# limpiar archivo

f = open(path+"\\output\\datos_fuentes.txt","r")
e = open(path+"\\output\\datos_fuentes_limpiado.txt","w")
lines = f.readlines()
# elimina las primeras 3 lineas y la ultima linea
lines = lines[3:-1]
e.writelines(lines)

f.close()

packages = []
with open(path+'\\output\\datos_fuentes_limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		line = (" ".join(line.split()[:-5]))
		line = (" ".join(line.split()[5:]))
		packages.append(line)

e.close()

# Funcion para extraer una unica vez los paquetes de las fuentes
h = open(path+"\\output\\packages_limpiado.txt","w")
packages_n = []
for package in packages:
	if package in packages_n:
		continue
	else:
		packages_n.append(package)
		h.writelines(package+'\n')

h.close()
