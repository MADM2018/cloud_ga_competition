#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:53:27 2019

@author: carlos
"""

import copy



def randomSolution(rnd,i,numNodes,numPods):
    i = [[0 for col in range(numNodes)] for row in range(numPods)]
    i[0][0]=1
    return i




def getFather(rnd,population,obj):
    
    f1 = population[rnd.randint(0,len(population)-1)]
   
    return f1


def crossover(rnd,f1,f2):
    
    c1 = copy.copy(f1)
    c2 = copy.copy(f2)
    
    return c1,c2

def mutate(rnd,c1):
    
    return c1


def addChild(offs,c1,c,a,o):
    
    if c1['constraints'] == True:
        offs.append(c1['child'])
        c.append(c1['cost'])
        a.append(c1['availability'])
        o.append(c1['objective'])
        print("New child in the offspring")
    else:
        offs.append(c1['child'])
        c.append(c1['cost'])
        a.append(c1['availability'])
        o.append(c1['objective'])
        print("New child in the offspring")
        
        
        
def addInitialSolution(population,newSol,constr):
    
    population.append(newSol)
        
def mergePopulations(pop,offs,costpop,availpop,objpop,costoffs,availoffs,objoffs):
    return offs,costoffs,availoffs,objoffs