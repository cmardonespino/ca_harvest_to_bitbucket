# -- coding: utf-8 --

import os, sys
from variables import path

# limpiar archivo
f = open(path+"allnd40.txt","r")
e = open(path+"limpiado.txt","w")
lines = f.readlines()
del lines[0:3]

e.writelines(lines)

f.close()
e.close()
