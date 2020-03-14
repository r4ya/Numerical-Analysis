# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:52:42 2020

@author: ryavu
"""
#%%
import math
def regulaFalsi(function,lower,upper,MAXN):
    i = 0
    fa = function(lower)
    fb = function(upper)
    print("f({0}) = {1} and f({2}) = {3}".format(lower,fa,upper,fb))
    if (fa*fb)>0:
        print ("There is iteration root in {0} and {1}".format(lower,upper))      
        return
    
    print("Iter","Point","   Function",sep='       ')
    while( i < MAXN ):
        c = lower-(fa*(upper-lower)/(fb-fa))
        fc = function(c)
        print((i+1),"%.10f"%c,"%.10f"%fc,sep='     ')
        i = i+1
        if fa*fc > 0:
            lower = c
            fa = fc
        else:
            upper = c
            fb = fc
    print ("After", MAXN, "The value of root is: ","%.10f"%c)
    return c
#%%
function = lambda x: math.cos(x)-x
regulaFalsi(function,0,5,7)
regulaFalsi(function,-5,5,7)
regulaFalsi(function,-1,1,10)
print("Function value is %.10f"%function(regulaFalsi(function,-1,1,10)))