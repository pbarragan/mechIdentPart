import transExternal
import readData
import json
import os
import numpy as np
import copy
import rStates04_15_2015

def distOs(o1,o2):
    return np.sqrt((o1[0]-o2[0])**2+(o1[1]-o2[1])**2)

def initialState(sF):
    sI = copy.deepcopy(sF)
    if sF[0] == 2:
        # revolute
        sI[2][0] = np.arctan2(-sI[1][1],-sI[1][0]) # atan2(-yp,-xp)
    elif sF[0] == 3:
        # prismatic
        c = np.cos(sF[1][2])
        s = np.sin(sF[1][2])
        if np.abs(c) >= np.abs(s):
            sI[2][0] = -sF[1][0]/c
        else:
            sI[2][0] = -sF[1][1]/s
    elif sF[0] == 4:
        # latch
        sI[2][0] = sI[1][3]
        sI[2][1] = sI[1][4]

    return sI

#fbProbs, numSteps, model, statesInRbt, states, logProbs_T, logProbs_O, logProbs, poses, actions, obs, actionType, actionSelectionType, numMechanismTypes, numParticles, numRepeats, neff_fract, modelNums, realStates, BIAS, FTSD, FOSD, RTSD, ROSD = readData.getData(fileName)


# create action list
numPts = 8
radius = 0.12
thDel = 2*np.pi/numPts

actions = [[radius*np.cos(i*thDel),radius*np.sin(i*thDel)]\
           for i in range(numPts)]

indexList = [0,6,3,7,4,2,6,4,1,5,2,0,4,2,7,3,0,6,2,0,5,1,6,4]
actionList = [actions[x] for x in indexList]

# set up to read file
exeDir = os.path.abspath(os.path.dirname(__file__))
outFile = exeDir+'/../plotting/rmStates04_15_2015.txt'

# set up needed variables
relevantMT = [0,1,2,3,4]
numMT = len(relevantMT)
numT = 10 # number of trials per setting

# set up holding lists
errors = [[] for y in range(numMT)]
misClass = [0]*numMT
misClassMT = [[0]*numMT for y in range(numMT)]

# get info from file
f = open(outFile,'r')
sSave = json.load(f)
rStatesSave = sSave['rStatesSave']
mStatesSave = sSave['mStatesSave']
f.close()

# copy over the empty rStatesSave from the file
rStatesSave = rStates04_15_2015.trueStates

print len(rStatesSave)
print len(mStatesSave)

# iterate over states
for r,m in zip(rStatesSave,mStatesSave):
    if r[0] != m[0]:
        # misclassified
        misClass[r[0]] += 1
        misClassMT[r[0]][m[0]] += 1
    else: # this is the line that needs to change if you want to include misclassifications
        if ((r[0] == 0) and (m[0] == 0)) or ((r[0] == 1) and (m[0] == 1)):
            errors[r[0]].append(0)
        else:
            # get initial states
            rI = initialState(r)
            mI = initialState(m)

            dists = []
            for a in actionList:
                oR,rI = transExternal.simulate(rI,a)
                oM,mI = transExternal.simulate(mI,a)
                dists.append(distOs(oR,oM))

            errors[r[0]].append(np.mean(dists))
            
print "Errors:"
print errors
print "Misclassifcations:"
print misClass
print "Misclassifications per Model:"
print misClassMT
print "Avgerage Error per Model:"
print [np.mean(es) for es in errors]
print "Standard Deviation per Model:"
print [np.std(es) for es in errors]
                             
            

