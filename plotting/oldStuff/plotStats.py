# this is for the 12/14/2015 experiments

import readData
import heapq
import math

import statsFiles

    
def stateDist(s1,s2):
    if s1[0]!=s2[0]:
        return 100000000
    else:
        dist = 0
        if s1[0] != 3:
            for p1,p2 in zip(s1[1],s2[1]):
                dist += (p1-p2)**2
            for v1,v2 in zip(s1[2],s2[2]):
                dist += (v1-v2)**2
            return math.sqrt(dist)
        else:
            return math.sqrt((s1[1][2]-s2[1][2])**2)
        
# no bias error
# filter trans: 0.001
# filter obs: 0.01
# real trans: 0.001
# real obs: 0.001

print len(statsFiles.files)

#dirName = '/home/barragan/data12112014new/data/2014_12_13'
dirName = '/home/barragan/data12112014new//data/2014_12_11/'
fileNames = []
fileNames.append(['data2Thu_Dec_11_13_41_20_2014.txt',\
'data2Thu_Dec_11_13_42_18_2014.txt',\
'data2Thu_Dec_11_13_43_04_2014.txt',\
'data2Thu_Dec_11_13_44_24_2014.txt',\
'data2Thu_Dec_11_13_45_44_2014.txt'])

# no bias error
# filter trans: 0.05
# filter obs: 0.01
# real trans: 0.001
# real obs: 0.001


fileNames.append(['data2Thu_Dec_11_13_50_25_2014.txt',\
'data2Thu_Dec_11_13_50_53_2014.txt',\
'data2Thu_Dec_11_13_51_21_2014.txt',\
'data2Thu_Dec_11_13_52_53_2014.txt',\
'data2Thu_Dec_11_13_53_22_2014.txt'])

# bias error
# filter trans: 0.001
# filter obs: 0.01
# real trans: 0.001
# real obs: 0.001

fileNames.append(['data2Thu_Dec_11_13_54_51_2014.txt',\
'data2Thu_Dec_11_13_55_32_2014.txt',\
'data2Thu_Dec_11_13_56_00_2014.txt',\
'data2Thu_Dec_11_13_56_26_2014.txt',\
'data2Thu_Dec_11_13_56_43_2014.txt'])

# bias error
# filter trans: 0.05
# filter obs: 0.01
# real trans: 0.001
# real obs: 0.001

fileNames.append(['data2Thu_Dec_11_13_57_57_2014.txt',\
'data2Thu_Dec_11_13_58_17_2014.txt',\
'data2Thu_Dec_11_13_58_43_2014.txt',\
'data2Thu_Dec_11_13_59_28_2014.txt',\
'data2Thu_Dec_11_13_59_47_2014.txt'])

typeError = []
for fList in fileNames:
    dists = []

    for f in fList:
        print f
    
        fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses, actions, obs, actionType, actionSelectionType, numMechanismTypes, numParticles, modelNums, realStates = readData.get_data(dirName+f)

        # find max state

        # find the largest probability particles for the models
        # maxes = []
        # numMaxes = 1
        # lookAtList = [2]
        # for m in lookAtList:
        #     maxes.append(heapq.nlargest(numMaxes,logProbs[-1][m]))

        # # find the corresponding indeces
        # whichStep = -1
        # maxInds = []
        # maxesPrev = []
        # maxStates = []
        # maxStatesInRbt = []
        # for i,ms in zip(lookAtList,maxes):
        #     maxInds.append([logProbs[whichStep][i].index(x) for x in ms])
        #     maxesPrev.append([logProbs[whichStep-1][i][x] for x in maxInds[-1]])
        #     maxStates.append([states[whichStep][i][x] for x in maxInds[-1]])
        #     maxStatesInRbt.append([[statesInRbt[whichStep][i][0][x],\
        #                             statesInRbt[whichStep][i][1][x]]\
        #                            for x in maxInds[-1]])

        # maxState = maxStates[0]

        maxState = states[-1][2][logProbs[-1][2].index(max(logProbs[-1][2]))]
        
        print realStates[-1]
        print maxState
        dists.append(stateDist(realStates[-1],maxState))

    typeError.append(math.fsum(dists)/float(len(dists)))

print typeError
        
        


