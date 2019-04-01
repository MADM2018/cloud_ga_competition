#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:17:36 2019

@author: carlos
"""

import pickle
import matplotlib.pyplot as plt


f = open('reinier.pckl', 'rb')
reinier = pickle.load(f)
f.close()


f = open('carlos2.pckl', 'rb')
carlos2 = pickle.load(f)
f.close()


plt.plot(reinier,color='g',label='reinier')
plt.plot(carlos2,color='b',label='carlos2')
plt.legend(loc='upper right')
plt.xlabel('Num. de generaciones')
plt.ylabel('Valor de fitness')
plt.show()