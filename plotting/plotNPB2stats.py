# this is for the 12/27/2015 experiments
# varied over 10, 100, 1000, 5000, 10000 particles per filter
# bias is at 0.5 instead of 0.8

import readData
import heapq
import math
import numpy as np

import statsFilesNPB2
import json
import os

import auxUtils

from matplotlib import pyplot

exeDir = os.path.abspath(os.path.dirname(__file__))
print exeDir
dirName = '/home/barragan/data12112014new/data/2014_12_27fifty/'

outFile = exeDir+'/rmStatesNPB2.txt'

numET = 5 # 10, 100, 1000, 5000, 10000 particles per filter
relevantMT = [0,1,2,3]
numMT = len(relevantMT)
numT = 50 # number of trials per setting

errors = [[[] for y in range(numMT)] for x in range(numET)]
misClass = [[0]*numMT for x in range(numET)]
misClassMT = [[[0]*numMT for y in range(numMT)] for x in range(numET)]

# goes experiment type (0-3), model type (0-3), trial number (0-9)
if(False):
    files = statsFilesNPB2.files
    fileNames = [[[] for y in range(numMT)] for x in range(numET)]


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

                fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses, actions, obs, \
                         actionType, actionSelectionType, numMechanismTypes, numParticles, numRepeats, neff_fract, \
                         modelNums, realStates, BIAS, FTSD, FOSD, RTSD, ROSD \
                         = readData.get_data(dirName+f)

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

    f = open(outFile,'w')
    json.dump({'rStatesSave':rStatesSave,'mStatesSave':mStatesSave},f)
    f.close()
else:
    f = open(outFile,'r')
    sSave = json.load(f)
    rStatesSave = sSave['rStatesSave']
    mStatesSave = sSave['mStatesSave']
    f.close()

    print len(rStatesSave)
    print len(mStatesSave)

    for i in range(numET):
        for j in range(numMT):
            for k in range(numT):
                print i,j,k
                sInd = numMT*numT*i+numT*j+k
                print "Index:",sInd
                e=auxUtils.stateDist2(rStatesSave[sInd],
                                      mStatesSave[sInd])
                if e<1000:
                    errors[i][j].append(e)
                else:
                    misClass[i][j]+=1
                    misClassMT[i][j][relevantMT.index(mStatesSave[sInd][0])]+=1
                    print "This is a huge ERROR!"
                #print rStatesSave[sInd]
                #print mStatesSave[sInd]
                #print auxUtils.stateDist2(rStatesSave[sInd],
                #                          mStatesSave[sInd])

print errors


typeAndModelError = [[] for x in range(numET)]
typeError = []
modelError = []

typeAndModelErrorSD = [[] for x in range(numET)]
typeErrorSD = []
modelErrorSD = []

# mean
for i,typeEs in enumerate(errors):
    for modelEs in typeEs:
        typeAndModelError[i].append(np.mean(modelEs))
        typeAndModelErrorSD[i].append(np.std(modelEs))

hold = [[] for x in range(numMT)]

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
types = ["10","100","1000","5000","10000"]
typesF = [float(x) for x in types]

print
auxUtils.printTable(models,types,typeAndModelError,typeAndModelErrorSD)
print
auxUtils.printFlatTable(types,typeError,typeErrorSD)
print
auxUtils.printFlatTable(models,modelError,modelErrorSD)
print
#auxUtils.printTableNoSD(models,types,misClass)        
print "Misclassification Error:"
auxUtils.printMisClassTable(models,types,misClass,misClassMT)

if(True):

    pyplot.scatter(typesF,typeError)
    pyplot.errorbar(typesF,typeError,yerr=typeErrorSD)
    pyplot.xlabel('Number of Particles')
    pyplot.ylabel('Error [m]')
    
    pyplot.show()
