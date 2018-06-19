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

if os.path.isdir(path+'\\output') == False:
	os.system('mkdir '+path+'\\output')

path_output = path+'\\output'

# Crea archivo con el listado de packages con sus nombes, fechas, etc

os.system('hsv -b '+servHarv+' -en "'+enHarv+'" -vp '+"\\"+
	' -usr '+usuharv+' -pw '+passharv+' -st "'+ambHarv+
	'" -id nd 40 -s *.* -o '+path_output+'\\datos_fuentes.txt')
# Descarga los ultimos paquetes dentro de los 40 días
