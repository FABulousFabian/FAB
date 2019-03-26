import matplotlib.pyplot as plt
import numpy as np
from math import *

def eulerplot(h, teind, u10, u20, v10, v20, tf, dy, dx):
    nsteps= int(teind/h)
    t= np.zeros(nsteps+1)
    
    u1= np.zeros(nsteps+1)
    u2= np.zeros(nsteps+1)
    
    v1= np.zeros(nsteps+1)
    v2= np.zeros(nsteps+1)
    
    a= np.zeros(nsteps+1)
    b= np.zeros(nsteps+1)
    u1[0]= u10
    u2[0]= u20
    v1[0]= v10
    v2[0]= v20
    a[0]= 2
    b[0]= 4.5
    for i in range(nsteps):
        
        if i*h <= tf:
            a_afg= 0
            b_afg= 0
            u1_afg= 2 + v1[i]*u1[i]**2 - 5.5*u1[i] + dx*(u2[i]-u1[i])
            v1_afg= 4.5*u1[i] - v1[i]*u1[i]**2 + dy*(v2[i]-v1[i])
            u2_afg= 2 + v2[i]*u2[i]**2 - 5.5*u2[i] + dx*(u1[i]-u2[i])
            v2_afg= 4.5*u2[i] - v2[i]*u2[i]**2 + dy*(v1[i]-v2[i])
            t[i+1]= t[i] + h
            a[i+1]= a[i] + h*a_afg
            b[i+1]= b[i] + h*b_afg
            u1[i+1]= u1[i] + h*u1_afg
            v1[i+1]= v1[i] + h*v1_afg
            u2[i+1]= u2[i] + h*u2_afg
            v2[i+1]= v2[i] + h*v2_afg
            print(u1_afg, u2_afg, u1[i]-u2[i]) 
        if i*h > tf:
            a[i]= 2*exp(-(t[i]-tf))
            b_afg= 0
            u1_afg= a[i] + v1[i]*u1[i]**2 - 5.5*u1[i] + dx*(u2[i]-u1[i])
            v1_afg= 4.5*u1[i] - v1[i]*u1[i]**2 + dy*(v2[i]-v1[i])
            u2_afg= a[i] + v2[i]*u2[i]**2 - 5.5*u2[i] + dx*(u1[i]-u2[i])
            v2_afg= 4.5*u2[i] - v2[i]*u2[i]**2 + dy*(v1[i]-v2[i])
            t[i+1]= t[i] + h
            b[i+1]= b[i] + h*b_afg
            u1[i+1]= u1[i] + h*u1_afg
            v1[i+1]= v1[i] + h*v1_afg
            u2[i+1]= u2[i] + h*u2_afg
            v2[i+1]= v2[i] + h*v2_afg
            print(u1_afg, u2_afg, u1[i]-u2[i]) 
    return t, u1, u2, v1, v2

while True:
    print()
    h= float(input('Input stepsize: '))
    if h == 666:
        break
    teind= float(input('Input eindtijd: '))
    u10= float(input('Input u1(0): '))
    v10= float(input('Input v1(0): '))
    u20= float(input('Input u2(0): '))
    v20= float(input('Input v2(0): '))
    tf= float(input('Input tf: '))
    dy= float(input('Input dy: '))
    dx= float(input('Input dx: '))
    t, v1, v2, u1, u2= eulerplot(h, teind, u10, u20, v10, v20, tf, dy, dx)
    plt.plot(t,v1)
    plt.show()
    plt.plot(t,v2)
    plt.show()
    plt.plot(t,u1)
    plt.plot(t,u2)
    
    plt.show()
    plt.close()
    
