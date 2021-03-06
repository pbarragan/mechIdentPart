# this is for the 12/14/2015 experiments

import readData
import heapq
import math
import numpy as np

import statsFiles
import json
import os

import auxUtils

def stateDist(s1,s2):
    if s1[0]!=s2[0]:
        return 100000000
    else:
        if s1[0] != 3:
            dist = 0
            count = 0.0
            for p1,p2 in zip(s1[1],s2[1]):
                dist += (p1-p2)**2
                count += 1.0
            for v1,v2 in zip(s1[2],s2[2]):
                dist += (v1-v2)**2
                count += 1.0
            return math.sqrt(dist/count)
        elif s1[0]==3:
            dist1 = 0
            dist2 = 0
            lengthPs = math.sqrt((s1[1][0]-s2[1][0])**2
                                 + (s1[1][1]-s2[1][1])**2)
            dist1 = (s1[1][0]-s2[1][0])**2 + (s1[1][1]-s2[1][1])**2 \
                    + (s1[1][2]-s2[1][2])**2 + (s1[2][0]-s2[2][0])**2
            dist2 = (s1[1][0]+s2[1][0])**2 + (s1[1][1]+s2[1][1])**2 \
                    + (s1[1][2]-(s2[1][2]+math.pi))**2 \
                    + (s1[2][0]-(lengthPs-s2[2][0]))**2
            dist3 = (s1[1][0]+s2[1][0])**2 + (s1[1][1]+s2[1][1])**2 \
                    + (s1[1][2]-(s2[1][2]+math.pi))**2 \
                    + (s1[2][0]-(lengthPs-s2[2][0]))**2

            dist = min([dist1,dist2,dist3])
            return math.sqrt(dist/4.0)

exeDir = os.path.abspath(os.path.dirname(__file__))
print exeDir
dirName = '/home/barragan/data12112014new/data/2014_12_13/'
fileNames = []
errors = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]

numET = 4
numMT = 4
numT = 10

# goes experiment type (0-3), model type (0-3), trial number (0-9)
if(False):
    files = statsFiles.files

    fileNames = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]


    for i in range(numET):
        for j in range(numMT):
            fileNames[i][j] = files[40*i+10*j:40*i+10*j+numT]


    rStatesSave = []
    mStatesSave = []

    for i,fileLists in enumerate(fileNames):
        for j,fList in enumerate(fileLists):
            dists = []

            for f in fList:
                print i,j
                print f

                fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses, actions, obs, actionType, actionSelectionType, numMechanismTypes, numParticles, modelNums, realStates = readData.get_data(dirName+f)

                # find max state
                maxProbs = []
                maxProbInds = []
                for l in range(numMT):
                    maxProbs.append(max(logProbs[-1][l]))
                    maxProbInds.append(logProbs[-1][l].index(maxProbs[-1]))

                maxModelInd = maxProbs.index(max(maxProbs))
                maxProbInd = maxProbInds[maxModelInd]
                maxState = states[-1][maxModelInd][maxProbInd]

                print realStates[-1]
                print maxState
                rStatesSave.append(realStates[-1])
                mStatesSave.append(maxState)
                errors[i][j].append(stateDist(realStates[-1],maxState))

    f = open(exeDir+'/rmStates.txt','w')
    json.dump({'rStatesSave':rStatesSave,'mStatesSave':mStatesSave},f)
    f.close()
else:
    f = open(exeDir+'/rmStates.txt','r')
    sSave = json.load(f)
    rStatesSave = sSave['rStatesSave']
    mStatesSave = sSave['mStatesSave']
    f.close()

    for i in range(numET):
        for j in range(numMT):
            for k in range(numT):
                sInd = 40*i+10*j+k
                errors[i][j].append(auxUtils.stateDist2(rStatesSave[sInd],
                                                        mStatesSave[sInd]))
    

print errors


typeAndModelError = [[],[],[],[]]
typeError = []
modelError = []

typeAndModelErrorSD = [[],[],[],[]]
typeErrorSD = []
modelErrorSD = []

# mean
for i,typeEs in enumerate(errors):
    for modelEs in typeEs:
        typeAndModelError[i].append(np.mean(modelEs))
        typeAndModelErrorSD[i].append(np.std(modelEs))

hold = [[],[],[],[]]

for es in typeAndModelError:
    typeError.append(np.mean(es))
    typeErrorSD.append(np.std(es))    
    for i,e in enumerate(es):
        hold[i].append(e)

for es in hold:
    modelError.append(np.mean(es))
    modelErrorSD.append(np.std(es))

print
print
print
print "[Type][Model]"
print "RMSE:",typeAndModelError
print "SD:",typeAndModelErrorSD
print "[Type]"
print "RMSE:",typeError
print "SD:",typeErrorSD
print "[Model]"
print "RMSE:",modelError
print "SD:",modelErrorSD


models = ["Free","Fixed","Rev","Pris"]
types = ["Low FTSD","High FTSD","Bias+Low FTSD","Bias+High FTSD"]

print
auxUtils.printTable(models,types,typeAndModelError,typeAndModelErrorSD)
print
auxUtils.printFlatTable(types,typeError,typeErrorSD)
print
auxUtils.printFlatTable(models,modelError,modelErrorSD)
