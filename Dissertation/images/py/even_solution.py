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

fig = plt.figure(figsize=(5,4))
ax = []
ax.append(fig.add_subplot(1,1,1))


ax[0].set_xlim(0,10)
ax[0].set_ylim(0,2)

ax[0].set_xlabel('$t$')
ax[0].set_ylabel("$p$")

ax[0].plot(t, p1(t), label="$p_1(t)$")
ax[0].plot(t, p2(t), label="$p_2(t)$")
ax[0].plot(t, np.ones_like(t)*pinfty, "--", label="$p_{\\infty}$")


yticks = np.append(np.linspace(0, max(p10,p20), num=9), np.array([pinfty, p10, p20]))
ax[0].axes.set_yticks(yticks)

#ax[0].axes.set_xticks(ax.get_xticks())
#print(ax[0].get_xticks())
xts = list(ax[0].get_xticks())
xlabel = ["" for xt in xts]



ylabel = []

for yt in yticks:
    if (abs(yt - p10) < 1e-5):
        ylabel.append("$p_1^0$")
    elif (abs(yt - p20) < 1e-5):
        ylabel.append("$p_2^0$")
    elif (abs(yt - pinfty) < 1e-5):
        ylabel.append("$p_{\\infty}$")
    elif (abs(yt) < 1e-5):
        ylabel.append("0")
    else:
        ylabel.append("")


ax[0].set_yticklabels( ylabel )
ax[0].set_xticklabels( xlabel )

ax[0].set_xlim(0,10)
ax[0].set_ylim(0,2)

for a in ax:
    a.grid(True)
    a.legend(loc='best')  
    
plt.show() 