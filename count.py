#!/usr/bin/python
#-*-coding:utf-8-*-
# Filename: count.py

import os
import sys

path = "F:\Study\python\data"
listfile = os.listdir(path)
newlist = []
for names in listfile:
  if names.endswith(".dat"):
    newlist.append(names)
print newlist

def getCountsByFile(filename):
    fp = open(filename)
    content = fp.read()
    fp.close()
    
    matchdata = re.compile(r'([a-z0-9]{32})')
    data = re.findall(matchdata,content)
    if data:
        return len(data)/2
    else:
        return 0