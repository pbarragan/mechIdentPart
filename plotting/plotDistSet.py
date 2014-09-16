from matplotlib import pyplot
from matplotlib import colors
import numpy
import math
import os

import readData

# for the debugging
import heapq
import mpldatacursor

import numpy as np
import scipy.linalg
from random import randint
import numpy.matlib

def biNormalLog(x,mu):
    r = x-mu
    m = r.shape[0]
    S = 0.0016*np.matlib.identity(m)
    beta = 1/(((2.0*math.pi)**(m/2.0))*(math.sqrt(scipy.linalg.det(S))))
    # print x
    # print mu
    # print r
    # print -0.5*r.transpose()*scipy.linalg.inv(S)*r
    p = math.log(beta*math.exp(-0.5*r.transpose()*scipy.linalg.inv(S)*r))
    return p

def dist(x,y):
    return math.sqrt(sum([(a-b)**2 for a,b in zip(x,y)]))

def stateDist(s1,s2):
    if s1[0]!=s2[0]:
        return 100000000
    else:
        dist = 0
        for p1,p2 in zip(s1[1],s2[1]):
            dist += (p1-p2)**2
        for v1,v2 in zip(s1[2],s2[2]):
            dist += (v1-v2)**2
        return math.sqrt(dist)

def findCloseStates(sRef,stateList,thresh):
    closeStateList = []
    for s in stateList:
        if (stateDist(sRef,s)<thresh):
            closeStateList.append(s)

    return closeStateList

# if you want to plot all models
def plotAll(step,plotType,plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses=None,actions=None,obs=None):
    i = step # so you don't have to go through and change things
    
    # make list of symbols
    symList = ["o","s","*","D","^","v"]
    
    # model names list
    modelNames = ["Free","Fixed","Rev","Pris","L1","L2"]
    
    mSize = 10
    sSize = 50

    pyplot.hold(True)

    for j in range(len(statesInRbt[i+1])):
        if plotLog:
            cProbsS = logProbs[i][j]
            cProbsE = logProbs[i+1][j]
        else:
            cProbsS =[math.exp(x) for x in logProbs[i][j]]
            cProbsE =[math.exp(x) for x in logProbs[i+1][j]]

        pyplot.scatter(statesInRbt[i][j][0],statesInRbt[i][j][1],c=cProbsS,\
                       s=sSize,marker=symList[j],norm=colorNorm,edgecolors='g')
        pyplot.scatter(statesInRbt[i+1][j][0],statesInRbt[i+1][j][1],c=cProbsE,\
                       s=sSize*2,marker=symList[j],norm=colorNorm,\
                       edgecolors='r')
    
    # create the list for the legend
    legendList=[]
    for k in range(len(fbProbs[i+1])): 
        legendList.append(modelNames[modelNums[k]]+" - "\
                          +str("%.3G" % (fbProbs[i+1][k])))
    
    pyplot.legend(legendList,bbox_to_anchor=(0., -.425, 1., .5),\
                  loc=3, ncol=2, mode="expand", borderaxespad=0.)
    pyplot.colorbar()
    print 'step: '+str(i)
    if actions != None:
        pyplot.plot(poses[0][i],poses[1][i],c='g',marker=r"$ {} $".format("S"),\
                    markersize=mSize*1.5,mec='none')
        print 'start: '+str(poses[0][i])+','+str(poses[1][i])
    if obs != None:
        pyplot.plot(poses[0][i+1],poses[1][i+1],c='r',\
                    marker=r"$ {} $".format("E"),\
                    markersize=mSize*1.5,mec='none')
        print 'end: '+str(poses[0][i+1])+','+str(poses[1][i+1])

    if actions != None:
        pyplot.plot(actions[0][i]+poses[0][i],actions[1][i]+poses[1][i],\
                    c='b',marker=r"$ {} $".format("A"),\
                    markersize=mSize*1.5,mec='none')
        print 'action: '+str(actions[0][i])+','+str(actions[1][i])
        print 'result: '+str(actions[0][i]+poses[0][i])+','+str(actions[1][i]+poses[1][i])


    if obs != None:
        pyplot.plot(obs[0][i],obs[1][i],c='y',marker=r"$ {} $".format("O"),\
                    markersize=mSize*1.5,mec='none')
        print 'obs: '+str(obs[0][i])+','+str(obs[1][i])

    pyplot.title('Step '+str(i)+' - '+plotType)
    outFile = setPath+'step'+str(i)+plotType+'.png'
    pyplot.savefig(outFile,bbox_inches='tight')
    
    if plotSet:
        pyplot.show()
        
    pyplot.hold(False)
    pyplot.clf()

# if you don't want to plot all models
def plotSome(whichModels,step,plotType,plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses=None,actions=None,obs=None):
    i = step # so you don't have to go through and change things
    
    # make list of symbols
    symList = ["o","s","*","D","^","v"]
    
    # model names list
    modelNames = ["Free","Fixed","Rev","Pris","L1","L2"]
    
    mSize = 10
    sSize = 50

    pyplot.hold(True)

    for j in whichModels:
        if plotLog:
            cProbsS = logProbs[i][j]
            cProbsE = logProbs[i+1][j]
        else:
            cProbsS =[math.exp(x) for x in logProbs[i][j]]
            cProbsE =[math.exp(x) for x in logProbs[i+1][j]]

        pyplot.scatter(statesInRbt[i][j][0],statesInRbt[i][j][1],c=cProbsS,\
                       s=sSize,marker=symList[j],norm=colorNorm,edgecolors='g')
        pyplot.scatter(statesInRbt[i+1][j][0],statesInRbt[i+1][j][1],c=cProbsE,\
                       s=sSize*2,marker=symList[j],norm=colorNorm,\
                       edgecolors='r')
    
    # create the list for the legend
    legendList=[]
    for k in range(len(fbProbs[i+1])): 
        legendList.append(modelNames[modelNums[k]]+" - "\
                          +str("%.3G" % (fbProbs[i+1][k])))
    
    pyplot.legend(legendList,bbox_to_anchor=(0., -.425, 1., .5),\
                  loc=3, ncol=2, mode="expand", borderaxespad=0.)
    pyplot.colorbar()
    print 'step: '+str(i)
    if actions != None:
        pyplot.plot(poses[0][i],poses[1][i],c='g',marker=r"$ {} $".format("S"),\
                    markersize=mSize*1.5,mec='none')
        print 'start: '+str(poses[0][i])+','+str(poses[1][i])
    if obs != None:
        pyplot.plot(poses[0][i+1],poses[1][i+1],c='r',\
                    marker=r"$ {} $".format("E"),\
                    markersize=mSize*1.5,mec='none')
        print 'end: '+str(poses[0][i+1])+','+str(poses[1][i+1])

    if actions != None:
        pyplot.plot(actions[0][i]+poses[0][i],actions[1][i]+poses[1][i],\
                    c='b',marker=r"$ {} $".format("A"),\
                    markersize=mSize*1.5,mec='none')
        print 'action: '+str(actions[0][i])+','+str(actions[1][i])
        print 'result: '+str(actions[0][i]+poses[0][i])+','+str(actions[1][i]+poses[1][i])


    if obs != None:
        pyplot.plot(obs[0][i],obs[1][i],c='y',marker=r"$ {} $".format("O"),\
                    markersize=mSize*1.5,mec='none')
        print 'obs: '+str(obs[0][i])+','+str(obs[1][i])

    pyplot.title('Step '+str(i)+' - '+plotType)
    outFile = setPath+'step'+str(i)+plotType+'.png'
    pyplot.savefig(outFile,bbox_inches='tight')
    
    if plotSet:
        pyplot.show()
        
    pyplot.hold(False)
    pyplot.clf()


# the beef


# set paths
exeDir = os.path.abspath(os.path.dirname(__file__))

#fileName = '/../data/2014_09_11/data0Thu_Sep_11_18_51_54_2014.txt'
#fileName2 = '/../data/2014_09_11/data0Thu_Sep_11_21_34_32_2014.txt'
#fileName3 = '/../data/2014_09_11/data0Thu_Sep_11_22_36_11_2014.txt'
#fileName4 = '/../data/2014_09_11/data0Thu_Sep_11_22_39_00_2014.txt'
#fileName5 = '/../data/2014_09_11/data0Thu_Sep_11_23_02_59_2014.txt'

#fileName = '/../data/2014_09_15/data0Mon_Sep_15_10_44_40_2014.txt'
#fileName = '/../data/2014_09_15/data1Mon_Sep_15_10_45_21_2014.txt'
#fileName = '/../data/2014_09_15/data2Mon_Sep_15_10_45_54_2014.txt'
#fileName = '/../data/2014_09_15/data2Mon_Sep_15_10_46_24_2014.txt'

#fileName = '/../data/2014_09_15/data2Mon_Sep_15_12_05_08_2014.txt'

# you can use this one to verify things are working
#fileName = '/../data/2014_09_15/data2Mon_Sep_15_14_56_54_2014.txt' 
#fileName = '/../data/2014_09_16/data2Tue_Sep_16_00_00_13_2014.txt'

# this has two models to verify with
#fileName = '/../data/2014_09_16/data2Tue_Sep_16_00_02_46_2014.txt'

# this verifies model 3
fileName = '/../data/2014_09_16/data3Tue_Sep_16_10_28_09_2014.txt'

folderName = fileName[fileName.rfind('/')+1:fileName.find('.txt')]
setPath = exeDir+'/dataPlots/'+folderName+'/'


if not os.path.exists(setPath):
    os.mkdir(setPath)

# parameters
plotLog = True
plotSet = False

# get data
fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses, \
         actions, obs, actionType, actionSelectionType, \
         numMechanismTypes, numParticles, modelNums\
         = readData.get_data(exeDir+fileName)

######################### VERIFICATION CODE ###################################
print logProbs_O
print
print logProbs
print
print obs
print statesInRbt
print len(obs[0])
print len(statesInRbt)

ls = []
for k in range(len(modelNums)):
    ls.extend(logProbs[0][k])
    
for i in range(numSteps):
    o = [obs[0][i],obs[1][i]]
    sList = []
    for k in range(len(modelNums)):
        sList.extend(zip(statesInRbt[i+1][k][0],statesInRbt[i+1][k][1]))
    print i
    print o
    print sList
    print logProbs_O[i]
    lOs = [biNormalLog(np.mat(o).transpose(),\
                       np.mat(s).transpose()) for s in sList]
    print lOs
    print 'full distribution'
    print logProbs[i+1]
    ls = [math.exp(l+lO) for l,lO in zip(ls,lOs)]
    sumLs = sum(ls)
    ls = [math.log(x/sumLs) for x in ls]
    print ls
    
######################### END VERIFICATION CODE ################################

############################### DEBUGGING CODE #################################

'''
print max(logProbs[-1][0])
lastObs = [obs[0][-1],obs[1][-1]]
print lastObs
print
maxes = heapq.nlargest(3,logProbs[-1][0])
maxInds = [logProbs[-1][0].index(x) for x in maxes]
maxesPrev = [logProbs[-2][0][x] for x in maxInds]
maxStates = [states[-1][0][x] for x in maxInds]
maxStatesInRbt = [[statesInRbt[-1][0][0][x],statesInRbt[-1][0][1][x]]\
                  for x in maxInds]
print 'maxes'
for m,mp,mS,mSR in zip(maxes,maxesPrev,maxStates,maxStatesInRbt):
    print mS,m,mp
    print mSR
    print dist(mSR,lastObs)
print   
#print states[-1][0][logProbs[-1][0].index(max(logProbs[-1][0]))]

sRef = [2, [-0.391603, -0.388312, 0.531023], [0.839963]]
closeStates = findCloseStates(sRef,states[-1][0],.15)
closeStateInds = [states[-1][0].index(x) for x in closeStates]
closeStateProbs = [logProbs[-1][0][x] for x in closeStateInds]
closeStateProbsPrev = [logProbs[-2][0][x] for x in closeStateInds]
closeStatesInRbt = [[statesInRbt[-1][0][0][x],statesInRbt[-1][0][1][x]]\
                    for x in closeStateInds]
print 'close states'
print 'ref',sRef
for s,p,pp,sR in zip(closeStates,closeStateProbs,\
                     closeStateProbsPrev,closeStatesInRbt):
    print s,p,pp
    print sR
    print dist(sR,lastObs)
print len(closeStates)
'''
############################# END DEBUGGING CODE ###############################


raise Exception

if plotLog:
    colorNorm = colors.Normalize(-100,0)
else:
    colorNorm = colors.Normalize(0,1) # YOU NEED THIS SO STUFF DOESN'T EXPLODDDEEE
# without colorNorm, you can't do repeated plotting and get a useful
# color answer becasue it normalize colors by default

# plot stuff
for i in range(numSteps):
    plotSome([2],i,'F',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
    #plotAll(i,'F',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)

