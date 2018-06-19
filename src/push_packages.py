# -- coding: utf-8 --

import os, sys
from variables import (
	NAME_ORGANIZATION_BITBUCKET,
	path as path_principal,
)

path_repo = path_principal+'\\repositorios_harvest'

carpetas_en_el_directorio = os.listdir(path_repo)

ID_ORIGEN = 0

for name in carpetas_en_el_directorio:
	os.chdir(path_principal+"\\repositorios_harvest\\"+name)
	'''
	os.system("git remote add origin-"+str(ID_ORIGEN)+" git@bitbucket.org:"+NAME_ORGANIZATION_BITBUCKET+"/"+name.lower())
	os.system("git push origin-"+str(ID_ORIGEN)+" --mirror")
	'''
	os.chdir(path_principal)
	ID_ORIGEN += 1