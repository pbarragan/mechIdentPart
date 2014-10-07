from matplotlib import pyplot
import pylab
from matplotlib import colors
#from matplotlib impo
import numpy
import math
import os

import readData

import itertools # for marker cycling


# for the debugging
import heapq
import mpldatacursor

import numpy as np
import scipy.linalg
from random import randint
import numpy.matlib

from scipy import optimize
###########
def calc_R(x,y, xc, yc):
    """ calculate the distance of each 2D points from the center (xc, yc) """
    return np.sqrt((x-xc)**2 + (y-yc)**2)
 
def f(c, x, y):
    """ calculate the algebraic distance between the data points and the mean circle centered at c=(xc, yc) """
    Ri = calc_R(x, y, *c)
    return Ri - Ri.mean()
 
def leastsq_circle(x,y):
    # coordinates of the barycenter
    x_m = np.mean(x)
    y_m = np.mean(y)
    center_estimate = x_m, y_m
    center, ier = optimize.leastsq(f, center_estimate, args=(x,y))
    xc, yc = center
    Ri       = calc_R(x, y, *center)
    R        = Ri.mean()
    residu   = np.sum((Ri - R)**2)
    return xc, yc, R, residu
###########

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
def plotSome(whichModels,modelNums,step,plotType,plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses=None,actions=None,obs=None):
    i = step # so you don't have to go through and change things
    
    # make list of symbols
    symList = ["o","s","*","D","^","v"]
    
    # model names list
    modelNames = ["Free","Fixed","Rev","Pris","L1","L2"]
    
    mSize = 10
    sSize = 50

    pyplot.hold(True)

    # to make sure indices match up
    lookAtList = [modelNums.index(x) for x in whichModels]

    for j in lookAtList:
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
    pyplot.axis('equal')
    outFile = setPath+'step'+str(i)+plotType+'.png'
    pyplot.savefig(outFile,bbox_inches='tight')
    
    if plotSet:
        pyplot.show()
        
    pyplot.hold(False)
    pyplot.clf()

# if you want to plot one model as a histogram
def plotHist(whichModel,modelNums,step,plotType,plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses=None,actions=None,obs=None):
    i = step # so you don't have to go through and change things
    
    # make list of symbols
    symList = ["o","s","*","D","^","v"]
    
    # model names list
    modelNames = ["Free","Fixed","Rev","Pris","L1","L2"]
    
    mSize = 10
    sSize = 50

    pyplot.hold(True)

    # to make sure indices match up
    j = modelNums.index(whichModel) # so you don't ahve to go change things
    
    b = 20 # how many bins for histogram
    
    if plotLog:
        cProbsS = logProbs[i][j]
        cProbsE = logProbs[i+1][j]
    else:
        cProbsS =[math.exp(x) for x in logProbs[i][j]]
        cProbsE =[math.exp(x) for x in logProbs[i+1][j]]

    f, axarr = pyplot.subplots(1,2)
    
    axarr[0].hist2d(statesInRbt[i][j][0],statesInRbt[i][j][1],b,\
                  weights=[math.exp(x) for x in cProbsS])
    rTup = axarr[1].hist2d(statesInRbt[i+1][j][0],statesInRbt[i+1][j][1],b,\
                           weights=[math.exp(x) for x in cProbsE])
    pyplot.colorbar(rTup[-1],ax=axarr.ravel().tolist())
    # create the list for the legend
    legendList=[]
    for k in range(len(fbProbs[i+1])): 
        legendList.append(modelNames[modelNums[k]]+" - "\
                          +str("%.3G" % (fbProbs[i+1][k])))
    
    pyplot.legend(legendList,bbox_to_anchor=(0., -.425, 1., .5),\
                  loc=3, ncol=2, mode="expand", borderaxespad=0.)
    #pyplot.colorbar(name,ax=axarr.ravel().tolist())
    
    print 'step: '+str(i)
    if actions != None:
        for a in axarr:
            a.plot(poses[0][i],poses[1][i],c='g',marker=r"$ {} $".format("S"),\
                   markersize=mSize*1.5,mec='none')
        print 'start: '+str(poses[0][i])+','+str(poses[1][i])
    if obs != None:
        for a in axarr:
            a.plot(poses[0][i+1],poses[1][i+1],c='r',\
                   marker=r"$ {} $".format("E"),\
                   markersize=mSize*1.5,mec='none')
        print 'end: '+str(poses[0][i+1])+','+str(poses[1][i+1])

    if actions != None:
        for a in axarr:
            a.plot(actions[0][i]+poses[0][i],actions[1][i]+poses[1][i],\
                   c='b',marker=r"$ {} $".format("A"),\
                   markersize=mSize*1.5,mec='none')
        print 'action: '+str(actions[0][i])+','+str(actions[1][i])
        print 'result: '+str(actions[0][i]+poses[0][i])+','+str(actions[1][i]+poses[1][i])


    if obs != None:
        for a in axarr:
            a.plot(obs[0][i],obs[1][i],c='y',marker=r"$ {} $".format("O"),\
                   markersize=mSize*1.5,mec='none')
        print 'obs: '+str(obs[0][i])+','+str(obs[1][i])

    pyplot.title('Step '+str(i)+' - '+plotType+' - before (left), after(right)')
    #pyplot.xlim([-.4,.4])
    #pyplot.ylim([-.4,.4])
    #for a in axarr:
    #    a.axis('equal')

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
#fileName = '/../data/2014_09_16/data3Tue_Sep_16_10_28_09_2014.txt'

# model 2, 10000 particles, still wrong
#fileName = '/../data/2014_09_16/data2Tue_Sep_16_14_21_25_2014.txt'

# model 2, 3 particles, just to verify, seems right
#fileName = '/../data/2014_09_16/data2Tue_Sep_16_14_49_08_2014.txt'

# model 2, 1000 particles, need to see what's going on
#fileName = '/../data/2014_09_19/data2Fri_Sep_19_11_06_46_2014.txt'

# model 2, 1000 particles, .01*paramSD, correct mu
#fileName = '/../data/2014_09_22/data2Mon_Sep_22_20_14_31_2014.txt'
#fileName = '/../data/2014_09_22/data2Mon_Sep_22_20_14_38_2014.txt'

# model 2, 1000 particles, .1*paramSD, correct mu
#fileName = '/../data/2014_09_22/data2Mon_Sep_22_20_15_23_2014.txt'
#fileName = '/../data/2014_09_22/data2Mon_Sep_22_20_21_16_2014.txt'

# trying to figure out how bad the problem of sampling is
#fileName = '/../data/2014_09_23/data2Tue_Sep_23_18_08_16_2014.txt'

# PARAMVAR 2
#fileName = '/../data/2014_09_23/data2Tue_Sep_23_20_22_35_2014.txt'
#fileName = '/../data/2014_09_23/data2Tue_Sep_23_20_51_51_2014.txt'
#fileName = '/../data/2014_09_23/data2Tue_Sep_23_21_27_13_2014.txt'

# ENTROPY
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_10_37_30_2014.txt'

# prechosen actions
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_15_34_29_2014.txt'
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_15_39_27_2014.txt'
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_15_45_32_2014.txt'
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_16_07_30_2014.txt'
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_16_12_49_2014.txt'
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_16_27_39_2014.txt'
#fileName = '/../data/2014_10_01/data2Wed_Oct__1_16_28_44_2014.txt'
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_16_17_2014.txt'
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_19_58_2014.txt'
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_29_04_2014.txt'
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_30_14_2014.txt'
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_35_59_2014.txt'
fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_42_31_2014.txt'
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_51_21_2014.txt'

folderName = fileName[fileName.rfind('/')+1:fileName.find('.txt')]
setPath = exeDir+'/dataPlots/'+folderName+'/'

doWhat = 1 # 0 - verify, 1 - debug, 2 - plot

if doWhat == 2:
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
if doWhat == 0:
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
if doWhat == 1:
    plotDebug = True
    
    whichStep = -1 # set to -1 for last step
    print max(logProbs[whichStep][0])
    lastObs = [obs[0][whichStep],obs[1][whichStep]]
    print lastObs
    print
    maxes = heapq.nlargest(3,logProbs[whichStep][0])
    maxInds = [logProbs[whichStep][0].index(x) for x in maxes]
    maxesPrev = [logProbs[-2][0][x] for x in maxInds]
    maxStates = [states[whichStep][0][x] for x in maxInds]
    maxStatesInRbt = [[statesInRbt[whichStep][0][0][x],\
                       statesInRbt[whichStep][0][1][x]]\
                      for x in maxInds]
    print 'maxes'
    for m,mp,mS,mSR in zip(maxes,maxesPrev,maxStates,maxStatesInRbt):
        print mS,m,mp
        print mSR
        print dist(mSR,lastObs)
    print   
    #print states[whichStep][0][logProbs[whichStep][0].index(max(logProbs[whichStep][0]))]

    sRef = [2, [-0.396, -0.396, 0.56], [0.7854]]
    #sRef = [2, [0.396, 0.396, 0.56], [-2.35619]]
    #sClosest =
    # this probably shouldn't have which step and only look at step 0
    closeStates = findCloseStates(sRef,states[0][0],.03)
    closeStateInds = [states[0][0].index(x) for x in closeStates]
    closeStateProbs = [logProbs[whichStep][0][x] for x in closeStateInds]
    closeStateProbsPrev = [logProbs[-2][0][x] for x in closeStateInds]

    closeStateProbsList = []
    closeStatesInRbtList = []
    maxStatesInRbtList = []
    maxProbsList = []

    for i in range(numSteps+1):
        closeStateProbsList.append([logProbs[i][0][x] for x in closeStateInds])
        closeStatesInRbtList.append([[statesInRbt[i][0][0][x],\
                             statesInRbt[i][0][1][x]]\
                            for x in closeStateInds])

        maxStatesInRbtList.append([[statesInRbt[i][0][0][x],\
                           statesInRbt[i][0][1][x]]\
                          for x in maxInds])
        maxProbsList.append([logProbs[i][0][x] for x in maxInds])


    closeStateDists = []
    maxDists = []

    for i in range(numSteps):
        closeStateDists.append([dist([obs[0][i],obs[1][i]],x) \
                                for x in closeStatesInRbtList[i+1]])
        maxDists.append([dist([obs[0][i],obs[1][i]],x) \
                         for x in maxStatesInRbtList[i+1]])


    print 'here we go:'
    print 'probs'
    print closeStateProbsList
    print 'in rbt'
    print closeStatesInRbtList
    print 'dists'
    print closeStateDists
    print 'obs'
    print obs
    print 'max dists'
    print maxDists
    print 'maxes in rbt'
    print maxStatesInRbtList
    print 'max probs'
    print maxProbsList

    
    closeStatesInRbt = [[statesInRbt[whichStep][0][0][x],\
                         statesInRbt[whichStep][0][1][x]]\
                        for x in closeStateInds]
    print
    print 'close states'
    print 'ref',sRef
    for s,p,pp,sR in zip(closeStates,closeStateProbs,\
                         closeStateProbsPrev,closeStatesInRbt):
        print s,p,pp
        print sR
        print dist(sR,lastObs)
    print len(closeStates),'close states to s_Ref'

    # do some fitting
    xc, yc, R, residu = leastsq_circle(obs[0],obs[1])

    print xc, yc, R, residu

    
    if plotDebug:
        sSize = 100
        markerList = itertools.cycle(('^', 'v', '.', 'o', '*')) 

        plotableClose = [[[],[]] for x in range(len(closeStateInds))]
        plotableMax = [[[],[]] for x in range(len(maxInds))]
        for i in range(numSteps+1):
            for j in range(len(closeStateInds)):
                plotableClose[j][0].append(closeStatesInRbtList[i][j][0])
                plotableClose[j][1].append(closeStatesInRbtList[i][j][1])
            for j in range(len(maxInds)):
                plotableMax[j][0].append(maxStatesInRbtList[i][j][0])
                plotableMax[j][1].append(maxStatesInRbtList[i][j][1])

        #closeStatesInRbtList[thisStep][thisOne][x or y]
        for i in range(len(closeStateInds)):
            pyplot.scatter(plotableClose[i][0],plotableClose[i][1],\
                           marker=markerList.next(),c='r',s=sSize)
        for s in closeStates:
            if s[0]==2:
                cir = pyplot.Circle((s[1][0],s[1][1]),s[1][2],\
                                    color='r',fill=False)
                pyplot.gcf().gca().add_artist(cir)
        for i in range(len(maxInds)):
            pyplot.scatter(plotableMax[i][0],plotableMax[i][1],\
                           marker=markerList.next(),c='b',s=sSize)
        for s in maxStates:
            if s[0]==2:
                cir = pyplot.Circle((s[1][0],s[1][1]),s[1][2],\
                                    color='b',fill=False)
                pyplot.gcf().gca().add_artist(cir)

        if sRef[0]==2:
            cir = pyplot.Circle((sRef[1][0],sRef[1][1]),sRef[1][2],\
                                color='g',fill=False)
            pyplot.gcf().gca().add_artist(cir)

            cirFit = pyplot.Circle((xc,yc),R,\
                                color='k',fill=False)
            pyplot.gcf().gca().add_artist(cirFit)

        pyplot.gcf().gca().add_patch(pylab.Rectangle((-.15,-.15),.3,.3,facecolor='none'))
        pyplot.scatter(obs[0],obs[1],c='g',s=sSize)
        pyplot.xlim([-.8,.3])
        pyplot.ylim([-.8,.3])
        pyplot.show()

############################# END DEBUGGING CODE ###############################

if doWhat == 2:

    #print logProbs
    #print len(logProbs)
    #print len(logProbs[0])

    if plotLog:
        colorNorm = colors.Normalize(-100,0)
    else:
        colorNorm = colors.Normalize(0,1) # YOU NEED THIS SO STUFF DOESN'T EXPLODDDEEE
    # without colorNorm, you can't do repeated plotting and get a useful
    # color answer becasue it normalize colors by default

    # plot stuff
    for i in range(numSteps):
        plotSome([2],modelNums,i,'F',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
        #plotAll(i,'F',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
        plotHist(2,modelNums,i,'H',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
        print [sum([math.exp(y) for y in logProbs[i][x]]) for x in range(len(modelNums))]

