# -- coding: utf-8 --

import os, sys
from variables import path

with open(path+"\\output\\datos_fuentes_limpiado.txt") as f:
    seen = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line)
        else:
            seen.add(line_lower)
