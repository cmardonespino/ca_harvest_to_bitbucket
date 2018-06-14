# -- coding: utf-8 --

import os, sys
from variables import (
	servHarv, 
	usuharv, 
	passharv, 
	enHarv, 
	ambHarv, 
	modoHarv,
	path_principal as path,
)

repo = path+"/entrada"
bajada = path+"/"
perso = path+"/pers"

empre = path+"/empr"
logh = path+"/logHarvest"

#fechar = %date:~-4%-%date:~3,2%-%date:~0,2%
#fechor = %fechar%_%time:~0,2%_%time:~3,2%_%time:~6,2%

# Crea archivo con el listado de packages con sus nombes, fechas, etc
os.system('hsv -b '+servHarv+' -en "'+enHarv+'" -vp '+"\\"+
	' -usr '+usuharv+' -pw '+passharv+' -st "'+ambHarv+
	'" -id nd 40 -s *.* -o '+path+'/output/allnd40.txt')
