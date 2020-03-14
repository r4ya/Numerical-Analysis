# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:10:35 2020

@author: ryavu
"""
import math
def fixedpoint(function,xo,TOL,MAXN):
    i = 0
    error=1
    print("Iter","Point","   Function","Error",sep='       ')
    while((error > TOL) and (i < MAXN)):
        x = function(xo)
        error = abs(x-xo)
        print((i+1),"%.10f"%xo,"%.10f"%x,"%.10f"%error,sep='     ')
        xo = x
        i = i + 1
    return x,xo,error

function = lambda x: x-2
fixedpoint(function,2.25,0.001,10)