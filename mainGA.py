# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import copy
import time

import reinier as competidor


def solutionCost(p):
    
    totalCost = 0
    for node in range(numNodes):
        for pod in range(numPods):
            if p[pod][node] == 1:
                break
        if p[pod][node] == 1:
            totalCost += nodes[node]['cost']
    return totalCost
    

def calculateCost(pop,c):
    
    for p in pop:
        solCost = solutionCost(p)
        c.append(solCost)
        
        
    
    
def solutionAvailability(p):
    totalScale = 0
    for pod in range(numPods):
        podScale = sum(p[pod])
        totalScale += podScale
    totalScale = float(float(totalScale))/float(len(p))
    return totalScale

def calculateAvailability(pop,a):
    for p in pop:
        solAvailability = solutionAvailability(p)
        a.append(solAvailability)


def constrScale(p):
    for pod in range(numPods):
        if sum(p[pod]) < 1:
            return False
    return True

def constrUsage(p):
    for node in range(numNodes):
        totalCPU = 0
        totalMEM = 0
        for pod in range(numPods):
            if p[pod][node] == 1:
                totalCPU += pods[pod]['cpu']
                totalMEM += pods[pod]['mem']
        if totalCPU > nodes[node]['cpu']:
            return False
        if totalMEM > nodes[node]['mem']:
            return False
    return True


def checkConstrains(p):
    
    if not constrUsage(p):
        return False
    if not constrScale(p):
        return False
    return True
    

def getMaxCost():
    totalCost = 0
    for nodeId in range(numNodes):
        totalCost += nodes[nodeId]['cost']
    return totalCost

def solutionObjective(c,a):
    
    maxCost = maxTotalCost
    maxAvailability = numNodes
    
    minCost = 0
    minAvailability = 1
    
    normalizedCost = float(c-minCost) / float(maxCost-minCost)
    normalizedAvailability = float(a-minAvailability) / float(maxAvailability-minAvailability)


    return normalizedCost/2.0 + (1.0-normalizedAvailability)/2.0



def initilizePopulation(rnd):
    
    population = list()
    
    while len(population) < populationSize:
        newSol = competidor.randomSolution(rnd,i,numNodes,numPods)
        competidor.addInitialSolution(population,newSol,checkConstrains(newSol))
        
    return population

#CONFIGURATION


t = time.time()


numPods = 4
numNodes = 10
numGenerations = 200
populationSize = 20

mutationProb = 0.2

nodeTemplate = list()
nodeTemplate_ = {}
nodeTemplate_['cpu']=2000
nodeTemplate_['mem']=8192
nodeTemplate_['cost']=100
nodeTemplate.append(nodeTemplate_)
nodeTemplate_ = {}
nodeTemplate_['cpu']=4000
nodeTemplate_['mem']=4096
nodeTemplate_['cost']=250
nodeTemplate.append(nodeTemplate_)


rnd = random.Random()
rnd.seed(23)



#SYSTEM STRUCTURES
nodes = list()
for i in range(numNodes):
    nodes.append(copy.copy(nodeTemplate[rnd.randint(0,len(nodeTemplate)-1)]))
    
maxTotalCost = getMaxCost()

pods = list()
for i in range(numPods):
    pod_ = {}
    pod_['cpu']=rnd.randint(2,5)*100
    pod_['mem']=rnd.randint(1,4)*256
    pods.append(pod_)
    
    
#GA SETUP



population = initilizePopulation(rnd)

cost =list()
calculateCost(population,cost)
availability = list()
calculateAvailability(population,availability)
objective = list()

for pid in range(len(population)):
    obj_ = solutionObjective(cost[pid],availability[pid])
    objective.append(obj_)


bestValue = list()

for currentGeneration in range(numGenerations):
    
   # print "Generation number "+str(currentGeneration)
    offspring = list()
    offsCost = list()
    offsAvailability = list()
    offsObjective = list()
    while len(offspring)<populationSize:
        f1= competidor.getFather(rnd,population,objective)
        f2= competidor.getFather(rnd,population,objective)
        c1, c2 = competidor.crossover(rnd,f1,f2)
        if rnd.random()<mutationProb:
            competidor.mutate(rnd,c1)
        if rnd.random()<mutationProb:
            competidor.mutate(rnd,c2)
        
        childStructure1 = {}
        childStructure1['child']=c1
        childStructure1['constraints']=checkConstrains(c1)
        cost_=solutionCost(c1)
        childStructure1['cost']=cost_
        availability_=solutionAvailability(c1)
        childStructure1['availability']=availability_
        childStructure1['objective']=solutionObjective(cost_,availability_)
        
        childStructure2 = {}
        childStructure2['child']=c2
        childStructure2['constraints']=checkConstrains(c2)
        cost_=solutionCost(c2)
        childStructure2['cost']=cost_
        availability_=solutionAvailability(c2)
        childStructure2['availability']=availability_
        childStructure2['objective']=solutionObjective(cost_,availability_)
        
         
        
        competidor.addChild(offspring,childStructure1,offsCost,offsAvailability,offsObjective)
        competidor.addChild(offspring,childStructure2,offsCost,offsAvailability,offsObjective)
        
    population,cost,availability,objective = competidor.mergePopulations(population,offspring,cost,availability,objective,offsCost,offsAvailability,offsObjective)
    
    print(objective)
    bestValue.append(min(objective))
    
tFinal = time.time() - t

import pickle
f = open('reinier.pckl', 'wb')
pickle.dump(bestValue,f)
f.close()
        
        
