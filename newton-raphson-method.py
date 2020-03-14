# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:45:00 2020

@author: ryavu
"""
#%%
import math
def newtonMethod(function,point,TOL,MAXN):
    i = 0
    pc = point
    print("f({0}) = {1}".format(point,function(point)))
    print("Iter","Function",sep='        ')
    while i <= MAXN:
        p = pc - function(pc)/derive(function,point)
        print((i+1),"%.10f"%p,sep='        ')
        if abs(pc-p)<TOL:
            return i,p
        i = i+1
        pc = p
    print ("After", MAXN, "The value of root is: ","%.10f"%p)
    return p
#%%
function = lambda x: x*x - math.cos(2*x) + math.sin(x)    
def derive(function, point):
    h = 0.00000000001 #h=value of epsilon--->limit
    derivative = (function(point + h) - function(point))/h
    return float("%.3f" %derivative)
newtonMethod(function,2,0.0000001,10)