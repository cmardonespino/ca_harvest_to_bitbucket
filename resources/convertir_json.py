# -- coding: utf-8 --

import os, sys, json
from datetime import datetime
from variables import (
	servHarv, 
	usuharv, 
	passharv, 
	enHarv, 
	ambHarv, 
	modoHarv,
	path,
)

#################################################################
# Funcion para extraer extensiones de las fuentes descargadas 
extensiones = []
with open(path+'\\output\\datos_fuentes_limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		for word in line.split():
			extensiones.append(word.rpartition('.')[-1])
			break

# Funcion para extraer una unica vez la extensión de las fuentes
extension_n = []
for extension in extensiones:
	if extension in extension_n:
		continue
	else:
		extension_n.append(extension)
#################################################################
# Funcion para extraer los paquetes
packages = []
with open(path+'\\output\\datos_fuentes_limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		for word in line.split():
			#extensiones.append(word.rpartition('.')[-1])
			if 'PG-' in word:
				packages.append(word)

# Funcion para extraer una unica vez los paquetes de las fuentes
packages_n = []
for package in packages:
	if package in packages_n:
		continue
	else:
		packages_n.append(package)

#################################################################
# Funcion para extraer los path
paths = []
with open(path+'\\output\\datos_fuentes_limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		for word in line.split():
			#extensiones.append(word.rpartition('.')[-1])
			if 'weblogic' in word:
				paths.append(word)

# Funcion para extraer una unica vez los paths
paths_n = []
for url_path in paths:
	if url_path in packages_n:
		continue
	else:
		paths_n.append(url_path)
#################################################################
# Funcion para extraer los nombres de archivos
archivos = []
with open(path+'\\output\\datos_fuentes_limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		if line.strip():
			archivos.append(line.split()[0])
		else:
			break
#################################################################
fechas = []
with open(path+'\\output\\datos_fuentes_limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		fechas.append("sig")
		for word in line.split():
			if ';' in word:
				fechas.append(word)

fechas_n = []
aux = []
for n in fechas:
	if n == 'sig':
		fechas_n.append(aux)
		aux = []
	else:
		aux.append(n)

#################################################################
# Genera JSON con los datos de las fuentes
n = open(path+'\\output\\fuentes.json', 'w')
j=0
n.writelines('{\n')
for j in range(len(paths)):
	a = ('"package-'+str(j)+'":[\n\t\t{\n\t\t\t"archivo": "'+archivos[j]+'",\n\t\t\t"extension": "'+
		extensiones[j]+'",\n\t\t\t"paquete": "'+packages[j]+
		'",\n\t\t\t"path": "'+paths[j].replace('\\', '/')+
		'",\n\t\t\t"fecha": "'+str(fechas_n[j+1])+'"\n\t\t}\n\t]')
	n.writelines('\t'+a)
	if j == len(paths)-1:
		n.writelines('\n}')
	else:
		n.writelines(',\n')
n.close()
