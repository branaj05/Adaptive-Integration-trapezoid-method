"""
AUSTIN BRANDENBERGER
Python 3.7.7
29 september 2020
"""
import numpy as np
import setuptools
import matplotlib.pyplot as plt

"""GOAL IS TO WRITE CODE THAT USES BOTH THE TRAPEZOID METHOD AND SIMPSON'S RULE TO INTEGRATE SOME TARGET FUNCTION OVER A GIVEN INTERVAL
(a, b)"""

#---------------------------------------------------------------------------------------------------------------------------#
""" STEP 0: DEFINE THE BASE VALUES"""
a = 0
b = 10
n_slices = 100


delt = (b-a)/n_slices #need to determine what my delt, or change is. I need to know how big my interval is, so I know the values to calculate. 
n_points = n_slices+1 #the number of points I need to generate depends on the number of slices I want in the givin range
                      #The number of points will always be 1 greater than the number of slices. If it is drawn out on paper, this becomes obvious.
#---------------------------------------------------------------------------------------------------------------------------#
""" STEP 1: GENERATE SOME DATA"""

def func(x):
    y_func = 100-x**2
    return y_func
#here I am setting up lists to store my function data and introducing x_i, my iteration/integration variable. 
yy = []
xx = []
x_1 = 0
for i in range(n_points): #n_points returns data with n slices, just like I am looking for. I tested it. 
    yy.append(func(x_1))
    xx.append(x_1)
    x_1 += delt
"""
plt.plot(xx, yy)
plt.show()
"""
#---------------------------------------------------------------------------------------------------------------------------#
"""STEP 2: INTEGRATE USING THE TRAPEZOID METHOD"""

def integ(y1, y2, delt):
    integral = 1/2*(delt)*(y1+y2)
    return integral

integ_t = 0
for i in range(n_slices):
    integ_t += integ(yy[i], yy[i+1], delt)

     
#Analytic solution
#integ_value = -np.cos(b)+np.cos(a)

#"error" calculation (difference b/t numberical and analyitic solution
#---------------------------------------------------------------------------------------------------------------------------#
"""STEP 3: BEGIN THE ADAPTIVE APPROACH"""

error_t = 1 #not really the "error". this is just here to initiate my while loop.
err = 10**-6

n1 = n_slices
y_odd = 0
delt = (b-a)/n_slices
error_tlist = []
n2_list = []
while error_t >err:
#while my error value is greater than my target error, this loop will continue to run. 
    n2 = n1*2 #re-defines n2 every loop
     #checks where I am at in my program (this program takes quite a while to finish, so it is better to see where it is in it's progression). 
    delt2 = delt/2 #makes a smaller slice size each loop.
    #I have to re-calculate my actual function values every loop becaues otherwise this method would not work. It depends upon the data points in xx and yy. 
    yy = []
    xx = []
    x_1 = 0
    for i in range(n2+1):
        yy.append(func(x_1))
        xx.append(x_1)
        x_1 += delt2
    #summs up the "odd" terms of yy to be multiplied by my slice size later on. 
    for i in range(1, n2, 2):
        y_odd += yy[i]
        
    i2 = .5*integ_t + delt2*y_odd #this is the main thing that mattters here. this is the value of my integral. 
    error_t = abs(i2-integ_t)*(1/3)
    #this section re-defines my variables for the next iteration in the loop. 
    integ_t = i2
    delt = delt2
    n1 = n2
    y_odd = 0
    error_tlist.append(error_t)
    n2_list.append(n2)
    
print("the number of slices is between", n2_list[-2],"and",n2_list[-1])
print("the error values are between", error_tlist[-2],"and",error_tlist[-1])
print("the estimated value of the integral is", integ_t)


        
 
    
        
    
    


















