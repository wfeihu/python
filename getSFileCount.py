# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:05:19 2017

@author: lpy
"""

import os
import re
import time
#import argparse
import sys

def getCountsByFile(filename):
    #print("getCountsByFile:"+filename)
    fp = open(filename)
    content = fp.read()
    #time.sleep(1)
    fp.close()
    
    matchdata = re.compile(r'([a-z0-9]{32})')
    data = re.findall(matchdata,content)
    if data:
        return len(data)/2
    else:
        return 0
    
#/PFSData/SFiles2/vdtimg/bimg/data/20170801/19_0/indexFile/000003.log

# 201708021300
def test1(date1):
    if len(date1)!=12:
        pass
    else:
        path_head = "/PFSData/SFiles2/vdtimg/bimg/data/"
        path_bottom = "/indexFile/000003.log"
    

def test2(date1, date2):
    if (len(date1)!=12) or (len(date2)!=12):
        pass
    else:
        pass

def test_all():
    #print("test_all")
    res = os.popen('find /PFSData/SFiles2/vdtimg/bimg/data/ -name 000003.log')
    arr = res.read()
    arr = arr.split('\n')
    arr.sort()
    del arr[0]
    #print(arr)
    for aaa in arr:
        #print("test_all:"+aaa)
        count = getCountsByFile(aaa)
        print(aaa[33:45]+","+str(count))


if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("date")
    
    args = parser.parse_args()
    '''
    print(sys.argv)
    
    if len(sys.argv)==3:
        test1()
    elif len(sys.argv)==4:
        test2()
    elif len(sys.argv)==1:
        #print("error!")
        test_all()
    else:
	print("error!")
    
    

