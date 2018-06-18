# -- coding: utf-8 --

import os, sys, json
from variables import (
	servHarv, 
	usuharv, 
	passharv, 
	enHarv, 
	ambHarv, 
	modoHarv,
	path,
)

repo = path+"entrada"
bajada = path+"\\bajada"
perso = path+"pers"

empre = path+"empr"
logh = path+"logHarvest"

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

o = 0
for package in packages_n:
	os.system('hco -b '+servHarv+' -usr '+usuharv+' -pw '+
    	passharv+' -en "'+enHarv+'" -st "'+ambHarv+'" -vp '+"\\"+
		' -cp "'+bajada+'\\package-'+str(o)+'" -op pc -pf "'+package+
		'" -pn "'+modoHarv+'" -s *.* -br replace rw -oa '+logh+'\\hco.log')
	o =+ 1
