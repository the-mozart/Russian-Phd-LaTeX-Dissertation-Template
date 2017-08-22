#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:14:45 2017

@author: anton
"""
import matplotlib.pyplot as plt
import numpy as np

# Включение русского языка
from matplotlib import rc 
rc('font',**{'family':'serif'}) 
rc('text', usetex=True) 
rc('text.latex',unicode=True) 
rc('text.latex',preamble='\\usepackage[utf8]{inputenc}') 
rc('text.latex',preamble='\\usepackage[russian]{babel}')


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 14}
rc('font', **font)

def p1(t):
    return ((p10+alfa*p20)-alfa*(p20-p10)*np.exp(-K*(1+alfa)*t))/(1+alfa)
    
def p2(t):
    return ((p10+alfa*p20)+(p20-p10)*np.exp(-K*(1+alfa)*t))/(1+alfa)
    
    
alfa = 0.5
K = 0.4
p20 = 2
p10 = 0.25

pinfty = (p10+alfa*p20)/(1+alfa)   

t = np.linspace(0, 10, num=100) 

fig = plt.figure(figsize=(7,5))
ax = []
ax.append(fig.add_subplot(1,1,1))

ax[0].set_xlabel('$t$')
ax[0].set_ylabel("$p$")
ax[0].plot(t, p1(t), label="$p_1(t)$")
ax[0].plot(t, p2(t), label="$p_2(t)$")
ax[0].plot(t, np.ones_like(t)*pinfty, "--", label="$p_{\\infty}$")

y = [0.25, 2]
labels = ["0", "$p_2^0$", "", "","","","","", "$p_1^0$"]

ax[0].set_xlim(0,10)
ax[0].set_ylim(0,2)

#ax[0].annotate("$p_{\\infty}$", xy=(0, pinfty),
## xytext=(0, pinfty),
##            arrowprops=dict(facecolor='black', shrink=0.05),
#            )

ax[0].set_yticklabels( labels )


#ax[0].set_xticks(range(10), ["","","","","","","","","",""] )

for a in ax:
    a.grid(True)
    a.legend(loc='best')  
    
plt.show() 