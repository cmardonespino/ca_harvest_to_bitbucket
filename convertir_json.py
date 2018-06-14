# -- coding: utf-8 --

import os, sys, json, csv
from variables import (
	servHarv, 
	usuharv, 
	passharv, 
	enHarv, 
	ambHarv, 
	modoHarv,
	path,
)

txt = open(path+'ordenado.txt', 'r')
jsonfile = open(path+'file.json', 'w')

data = json.loads(txt)

'''
import csv
import json

csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
'''