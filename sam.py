# -*- coding: utf-8 -*-
"""
Sampling Theorem
"""
import numpy as np
import matplotlib.pyplot as plt

F=500
t = np.linspace(0,0.01)
a = np.cos(2*np.pi*F*t)

plt.plot(t,a)
plt.title('input signal')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()


Fs1 = 1.3*F
n1 = np.arange(0,0.01,step = 1/Fs1)
x1 = np.cos(2*np.pi*F*n1)
plt.stem(n1,x1,use_line_collection=True)
plt.title('Undersampled signal')
plt.show()

Fs2 = 2*F
n2 = np.arange(0,0.01,step = 1/Fs2)
x2 = np.cos(2*np.pi*F*n2)
plt.stem(n2,x2,use_line_collection=True)
plt.title('Critically sampled signal')
plt.show()


Fs3 = 10*F
n3 = np.arange(0,0.01,step = 1/Fs3)
x3 = np.cos(2*np.pi*F*n3)
plt.stem(n3,x3,use_line_collection=True)
plt.title('Over sampled signal')
plt.show()
#aa=np.interp(x1,fp=n1)
