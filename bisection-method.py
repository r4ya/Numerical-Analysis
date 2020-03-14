# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:51:08 2020

@author: ryavu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:56:44 2020

@author: ryavu
"""
#%% B I S E C T I O N M E T H O D
import math

def bisection(function,lower,upper,TOL,MAXN):
    i=0
    if(function(lower)*function(upper) >= 0):
        print("You have not assumed right",lower,"and",upper)
        return 1
    c=lower
    print("Input","Number of iterations.",sep='                            ')
    while( (abs(upper-lower) >= TOL ) and ( i < MAXN) ):    
        c=(upper+lower)/2
        if( function(c) == 0.0):
            break
        if( function(c)*function(lower) < 0):
            upper=c
        else:
            lower=c
        i=i+1
        print("(","%.10f"%upper,",","%.10f"%lower,")",i)    
    print("The value of root is: ","%.10f"%c)
    return c
#%% 
function = lambda x: (x-1)*(x-1)*(x-1)-2*x*x+10-math.sin(x)
first = bisection(function,-10,10,(0.0001),10)
second = bisection(function,-2,1,(0.000001),100)
third = bisection(function,-2,1,(0.00000000000001),100)
print('\nComparison of Result')
print('first c = ',first)
print('second c = ',second)
print('third c = ',third)
#%%
function = lambda x: (x*x*x)*math.cos(x)-x*x-math.sinh(x)+3
first = bisection(function,-10,10,(0.0001),10)
second = bisection(function,1,10,(0.000001),100)
third = bisection(function,1,2,(0.00000000000001),100)
print('\nComparison of Result')
print('first c = ',first)
print('second c = ',second)
print('third c = ',third)