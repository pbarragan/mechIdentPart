# this is for the 12/15/2015 experiments

import readData
import heapq
import math
import numpy as np

import statsFiles4
import json
import os

import auxUtils

exeDir = os.path.abspath(os.path.dirname(__file__))
print exeDir
dirName = '/home/barragan/data12112014new/data/2014_12_23/'
fileNames = []
errors = [[[],[],[]],[[],[],[]],[[],[],[]]]
misClass = [[0,0,0],[0,0,0],[0,0,0]]

numET = 3 # 1, 10, 20
relevantMT = [0,2,3]
numMT = len(relevantMT)
numT = 30

# goes experiment type (0-3), model type (0-3), trial number (0-9)
if(False):
    files = statsFiles4.files
    files = files[270:540]
    fileNames = [[[],[],[]],[[],[],[]],[[],[],[]]]


    for i in range(numET):
        for j in range(numMT):
            fileNames[i][j] = files[numMT*numT*i+numT*j:numMT*numT*i+numT*j+numT]


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
                for l in relevantMT:
                    maxProbs.append(max(logProbs[-1][l]))
                    maxProbInds.append(logProbs[-1][l].index(maxProbs[-1]))

                maxModelInd = maxProbs.index(max(maxProbs))
                maxProbInd = maxProbInds[maxModelInd]
                maxState = states[-1][relevantMT[maxModelInd]][maxProbInd]

                print realStates[-1]
                print maxState
                rStatesSave.append(realStates[-1])
                mStatesSave.append(maxState)
                errors[i][j].append(auxUtils.stateDist2(realStates[-1],maxState))

    f = open(exeDir+'/rmStates5.txt','w')
    json.dump({'rStatesSave':rStatesSave,'mStatesSave':mStatesSave},f)
    f.close()
else:
    f = open(exeDir+'/rmStates5.txt','r')
    sSave = json.load(f)
    rStatesSave = sSave['rStatesSave']
    mStatesSave = sSave['mStatesSave']
    f.close()

    print len(rStatesSave)
    print len(mStatesSave)

    for i in range(numET):
        for j in range(numMT):
            for k in range(numT):
                sInd = numMT*numT*i+numT*j+k
                e=auxUtils.stateDist2(rStatesSave[sInd],
                                      mStatesSave[sInd])
                if e<1000:
                    errors[i][j].append(e)
                else:
                    misClass[i][j]+=1
                    print "This is a huge ERROR!"
                #print rStatesSave[sInd]
                #print mStatesSave[sInd]
                #print auxUtils.stateDist2(rStatesSave[sInd],
                #                          mStatesSave[sInd])

print errors


typeAndModelError = [[],[],[]]
typeError = []
modelError = []

typeAndModelErrorSD = [[],[],[]]
typeErrorSD = []
modelErrorSD = []

# mean
for i,typeEs in enumerate(errors):
    for modelEs in typeEs:
        typeAndModelError[i].append(np.mean(modelEs))
        typeAndModelErrorSD[i].append(np.std(modelEs))

hold = [[],[],[]]

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


models = ["Free","Rev","Pris"]
types = ["1 Repeat","10 Repeat","20 Repeat"]

print
auxUtils.printTable(models,types,typeAndModelError,typeAndModelErrorSD)
print
auxUtils.printFlatTable(types,typeError,typeErrorSD)
print
auxUtils.printFlatTable(models,modelError,modelErrorSD)

        
print
auxUtils.printTableNoSD(models,types,misClass)

