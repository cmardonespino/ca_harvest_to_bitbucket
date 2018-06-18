# -- coding: utf-8 --

import os, sys
from variables import (
	servHarv, 
	usuharv, 
	passharv, 
	enHarv, 
	ambHarv,
	path,
)
#print(path+"\\output")
#print(path+'\\output\\datos_fuentes.txt')

if os.path.isdir(path+"\\output") == False:
	os.system('mkdir '+path+'\\output')

# Crea archivo con el listado de packages con sus nombes, fechas, etc

os.system('hsv -b '+servHarv+' -en "'+enHarv+'" -vp '+"\\"+
	' -usr '+usuharv+' -pw '+passharv+' -st "'+ambHarv+
	'" -id nd 40 -s *.* -o '+path+'\\output\\datos_fuentes.txt')
