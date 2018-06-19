# -- coding: utf-8 --

import os, sys, json
from variables import (
	servHarv, 
	usuharv, 
	passharv, 
	enHarv, 
	ambHarv, 
	modoHarv,
	path as path_principal,
)
from limpiar_listado import packages_n

logh = path_principal+"logHarvest"

if os.path.isdir(path_principal+'\\repositorios_harvest') == False:
	os.system('mkdir '+path_principal+'\\repositorios_harvest')

path_repo = path_principal+'\\repositorios_harvest'

for package in packages_n:
	os.system('hco -b '+servHarv+' -usr '+usuharv+' -pw '+
	   	passharv+' -en "'+enHarv+'" -st "'+ambHarv+'" -vp '+"\\"+
		' -cp "'+path_repo+'\\'+package+'" -op pc -pf "'+package+
		'" -pn "'+modoHarv+'" -s *.* -br replace rw -oa '+logh+'\\hco.log')
