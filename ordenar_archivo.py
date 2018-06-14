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

labels = ['html', 'path', 'numero', 'letra', 
	'numeroMayor', 'nombre', 'usuario', 'fechaLlegada', 
	'usuarioDenuevo', 'fechaInicio', 'fechaTermino'
	]

e = open(path+"ordenado.txt","w")
cont = 0
'''
with open(path+'limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		for word in line.split():
			if cont==11:
				cont=0
			e.writelines('{ '+labels[cont]+': '+word+' }\n')
			cont += 1
'''

# Funcion para extraer extensiones de las fuentes descargadas
extensiones = []
with open(path+'limpiado.txt','r') as archivo_leido:
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

'''
with open(path+'limpiado.txt','r') as archivo_leido:
	for line in archivo_leido:
		for word in line.split():
			if word.endswith('.html'):
				print("html")
			elif word.endswith('.java'):
				print("java")
			elif word.endswith('.xhtml'):
				print("xhtml")
			elif word.endswith('.jsp'):
				print("jsp")
			elif word.endswith('.png'):
				print("png")
			elif word.endswith('.wsdl'):
				print("wsdl")
			elif word.endswith('.xsd'):
				print("xsd")
			elif word.endswith('.txt'):
				print("txt")
			elif word.endswith('.parametros'):
				print("parametros")

'''

'''
with open(path+'limpiado.txt','r') as archivo_leido:
    for line in archivo_leido:
    	for word in line.split():
        	print(str(cont)+'\n')
        	cont += 1
'''
