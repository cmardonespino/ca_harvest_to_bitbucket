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
'''
os.system('hsv -b '+servHarv+' -en "'+enHarv+'" -vp '+"\\"+
	' -usr '+usuharv+' -pw '+passharv+' -st "'+ambHarv+
	'" -id nd 40 -s *.* -o '+path+'/output/allnd40.txt')

os.system('hco -b %servHarv% -usr %usuharv% -pw %passharv% -en "%enHarv%" 
	-st "%ambHarv%" -vp "\\"  -cp "%bajada%\%fechar%" -op pc -pf "%%x" 
	-pn "%modoHarv%" -s *.* -br -oa %logh%\hco.log
'''
'''
k  = open(path+'file.json', 'w')
with open(path+'limpiado.txt','r') as f:
    for line in f:
        for word in line.split():
           json.dump(word, k)   
'''

'''
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
'''
'''
k.close()
f.close()
'''
