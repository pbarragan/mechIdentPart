import statsFilesNPB
import auxUtils
import kdeUtils
import readData
import numpy as np


dirName = '/home/barragan/data12112014new/data/2014_12_27eighty/'
f = statsFilesNPB.files[775]
print f

r = 0.2

fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses,\
         actions, obs, \
         actionType, actionSelectionType, numMechanismTypes, numParticles,\
         numRepeats, neff_fract, \
         modelNums, realStates, BIAS, FTSD, FOSD, RTSD, ROSD \
         = readData.get_data(dirName+f)

relevantMT = [0,1,2,3]
# find max state
maxProbs = []
maxProbInds = []

kSs = []
kPs = []

for l in relevantMT:
    maxProbs.append(max(logProbs[-1][l]))
    maxProbInds.append(logProbs[-1][l].index(maxProbs[-1]))

    kdS,kdP = kdeUtils.findMaxState(states[-1][l],logProbs[-1][l],r)
    kSs.append(kdS)
    kPs.append(kdP)

maxModelInd = maxProbs.index(max(maxProbs))
maxProbInd = maxProbInds[maxModelInd]
maxState = states[-1][relevantMT[maxModelInd]][maxProbInd]

print 'ref:',maxState,maxProbs[maxModelInd]
for p,s in zip(logProbs[-1][relevantMT[maxModelInd]],
               states[-1][relevantMT[maxModelInd]]):
    if p>=2*maxProbs[maxModelInd]:
        print s,p

#raise Exception

maxModelIndK2 = kPs.index(max(kPs))
maxProbK2 = max(kPs)
maxStateK2 = kSs[maxModelIndK2]

print 'True state:'
print realStates[-1]
print 'Max state:'
print maxState
print 'Max prob:'
print maxProbs[maxModelInd]
print 'Max error:'
print auxUtils.stateDist2(realStates[-1],maxState)
print 'KDE state:'
kdeS,kdeP = kdeUtils.findMaxState(states[-1][relevantMT[maxModelInd]],\
                                  logProbs[-1][relevantMT[maxModelInd]],r)
print kdeS
print 'KDE prob:'
print kdeP
print 'KDE error:'
print auxUtils.stateDist2(realStates[-1],kdeS)
print 'KDE2 state:'
print maxStateK2
print 'KDE2 prob:'
print kPs
print maxProbK2
print 'KDE2 error:'
print auxUtils.stateDist2(realStates[-1],maxStateK2)


k3S,k3P =kdeUtils.findMaxRegionState(states[-1][relevantMT[maxModelInd]],\
                                     logProbs[-1][relevantMT[maxModelInd]],r)
print 'KDE3 state:'
print k3S
print 'KDE3 prob:'
print k3P
print 'KDE3 error:'
print auxUtils.stateDist2(realStates[-1],k3S)
