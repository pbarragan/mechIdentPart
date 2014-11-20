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
        if s1[0] != 3:
            for p1,p2 in zip(s1[1],s2[1]):
                dist += (p1-p2)**2
            for v1,v2 in zip(s1[2],s2[2]):
                dist += (v1-v2)**2
            return math.sqrt(dist)
        else:
            return math.sqrt((s1[1][2]-s2[1][2])**2)

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
    
    #pyplot.legend(legendList,bbox_to_anchor=(0., -.425, 1., .5),\
    #              loc=3, ncol=2, mode="expand", borderaxespad=0.)
    cbar = pyplot.colorbar()
    cbar.set_label('Log Probability')
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

    print "is this working"
    pyplot.axis('equal')
    #pyplot.xlim([-.20,.20])
    #pyplot.ylim([-.20,.20])
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    
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
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_42_31_2014.txt'
#fileName = '/../data/2014_10_02/data2Thu_Oct__2_00_51_21_2014.txt'

# demo of model 0 for group meeting
#fileName = '/../data/2014_10_10/data0Fri_Oct_10_11_06_45_2014.txt'

# testing distance action selection
#fileName = '/../data/2014_10_16/data3Thu_Oct_16_11_37_43_2014.txt' # wrong mech, right particle
#fileName = '/../data/2014_10_16/data3Thu_Oct_16_11_38_40_2014.txt' # right mech, right particle

# 11/12/14 - real robot tests
#fileName = '/../data/2014_11_12/data3Wed_Nov_12_11_49_27_2014.txt'
#fileName = '/../data/2014_11_12/data3Wed_Nov_12_11_54_10_2014.txt'
#fileName = '/../data/2014_11_12/data3Wed_Nov_12_11_58_59_2014.txt'

# 11/13/14 - real robot tests
#fileName = '/../data/2014_11_13/data2Thu_Nov_13_13_17_56_2014.txt' # chose rev but wrong
#fileName = '/../data/2014_11_13/data2Thu_Nov_13_13_23_38_2014.txt' # chose rev but wrong
#fileName = '/../data/2014_11_13/data2Thu_Nov_13_13_26_21_2014.txt' # chose rev but wrong entropy maybe
#fileName = '/../data/2014_11_13/data2Thu_Nov_13_13_33_44_2014.txt' # chose rev but wrong random with bigger actions
#fileName = '/../data/2014_11_13/data0Thu_Nov_13_13_36_54_2014.txt' # free failed
#fileName = '/../data/2014_11_13/data0Thu_Nov_13_13_39_59_2014.txt' # free failed
#fileName = '/../data/2014_11_13/data1Thu_Nov_13_13_43_30_2014.txt' # fixed wins
#fileName = '/../data/2014_11_13/data3Thu_Nov_13_13_46_27_2014.txt' # good guess for pris but still chose rev

# 11/19/14 - real robot tests
# scripted actions - 6cm, +x,+x,-x,-x,-x,-x or +x,+x,+y,-x,-x,-y,-x,-x,+y
# low stiffness caused weird failures. high stiffness on free helps.
# the last two show how this works for ideal conditions
# without more noise added to transitions. It doesn't work completely because
# huge radii are still allowed

fileName = '/../data/2014_11_19/'

#fileName += 'data0Wed_Nov_19_12_07_40_2014.txt' # 0, short set, low stiffness
#fileName += 'data0Wed_Nov_19_13_10_23_2014.txt' # 0, short set, low stiffness
#fileName += 'data0Wed_Nov_19_13_13_05_2014.txt' # 0, short set, low stiffness
#fileName += 'data0Wed_Nov_19_13_16_26_2014.txt' # 0, short set, low stiffness
#fileName += 'data0Wed_Nov_19_13_21_26_2014.txt' # 0, short set, high stiffness
#fileName += 'data0Wed_Nov_19_13_27_26_2014.txt' # 0, short set, high stiffness
fileName += 'data0Wed_Nov_19_13_42_11_2014.txt' # 0, long set, high stiffness
#fileName += 'data3Wed_Nov_19_13_46_44_2014.txt' # 3, long set, low stiffness


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
    plotLines = True

    whichModels = [0,2,3]

    # to make sure indices match up
    lookAtList = [modelNums.index(x) for x in whichModels]
    
    whichStep = -1 # set to -1 for last step
    print max(logProbs[whichStep][0])
    lastObs = [obs[0][whichStep],obs[1][whichStep]]
    print lastObs

    # find the largest probability particles for the models
    maxes = []
    numMaxes = 3
    for m in lookAtList:
        maxes.append(heapq.nlargest(numMaxes,logProbs[whichStep][m]))

    # find the corresponding indeces
    maxInds = []
    maxesPrev = []
    maxStates = []
    maxStatesInRbt = []
    for i,ms in zip(lookAtList,maxes):
        maxInds.append([logProbs[whichStep][i].index(x) for x in ms])
        maxesPrev.append([logProbs[whichStep-1][i][x] for x in maxInds[-1]])
        maxStates.append([states[whichStep][i][x] for x in maxInds[-1]])
        maxStatesInRbt.append([[statesInRbt[whichStep][i][0][x],\
                                statesInRbt[whichStep][i][1][x]]\
                               for x in maxInds[-1]])
    print 'maxes'
    for m,mp,mS,mSR in zip(maxes,maxesPrev,maxStates,maxStatesInRbt):
        print 'states'
        print mS
        print 'prob'
        print m
        print 'previous step prob'
        print mp
        print 'state in robot'
        print mSR
        #print dist(mSR,lastObs)
    print
    
    #print states[whichStep][0][logProbs[whichStep][0].index(max(logProbs[whichStep][0]))]

    sRef = [0, [], [1,1]] # for free
    #sRef = [3, [-0.396, 0.396, -0.785], [0.56]] # for pris
    #sRef = [2, [0.396, 0.396, 0.56], [-2.35619]] # for rev
    #sClosest =
    # find the closest states to sref
    # this probably shouldn't have which step and only look at step 0
    srefMI = modelNums.index(sRef[0])
    closeStates = findCloseStates(sRef,states[0][srefMI],.003) #.003 for pris
    
    closeStateInds = [states[0][srefMI].index(x) for x in closeStates]
    closeStateProbs = [logProbs[whichStep][srefMI][x] for x in closeStateInds]
    closeStateProbsPrev = [logProbs[whichStep-1][srefMI][x] \
                           for x in closeStateInds]

    closeStateProbsList = []
    closeStatesInRbtList = []
    maxStatesInRbtList = [[] for x in maxInds]
    maxProbsList = [[] for x in maxInds]

    for i in range(numSteps+1):
        closeStateProbsList.append([logProbs[i][srefMI][x] \
                                    for x in closeStateInds])
        closeStatesInRbtList.append([[statesInRbt[i][srefMI][0][x],\
                             statesInRbt[i][srefMI][1][x]]\
                            for x in closeStateInds])

    for k,(m,mIs) in enumerate(zip(lookAtList,maxInds)):
        for i in range(numSteps+1):
            maxStatesInRbtList[k].append([[statesInRbt[i][m][0][x],\
                                        statesInRbt[i][m][1][x]]\
                                       for x in mIs]) #########
            maxProbsList[k].append([logProbs[i][3][x] for x in mIs]) #######


    closeStateDists = []
    maxDists = []

    for i in range(numSteps):
        closeStateDists.append([dist([obs[0][i],obs[1][i]],x) \
                                for x in closeStatesInRbtList[i+1]])
        #maxDists.append([dist([obs[0][i],obs[1][i]],x) \
        #                 for x in maxStatesInRbtList[i+1]])


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

    
    closeStatesInRbt = [[statesInRbt[whichStep][srefMI][0][x],\
                         statesInRbt[whichStep][srefMI][1][x]]\
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
        colorList = itertools.cycle(('r', 'g', 'b', 'c', 'm', 'y')) 
        colorListNIT = ['r', 'g', 'b', 'c', 'm', 'y']
        plotableClose = [[[],[]] for x in range(len(closeStateInds))]
        plotableMax = []
        for mIs in maxInds:
            plotableMax.append([[[],[]] for x in range(len(mIs))])

        print "plotableMax",plotableMax
        
        for i in range(numSteps+1):
            for j in range(len(closeStateInds)):
                plotableClose[j][0].append(closeStatesInRbtList[i][j][0])
                plotableClose[j][1].append(closeStatesInRbtList[i][j][1])
            for k,mIs in enumerate(maxInds):
                for j in range(len(mIs)):
                    plotableMax[k][j][0].append(maxStatesInRbtList[k][i][j][0])
                    plotableMax[k][j][1].append(maxStatesInRbtList[k][i][j][1])


        #closeStatesInRbtList[thisStep][thisOne][x or y]
        for i in range(len(closeStates)):
            s = closeStates[i]
            col = colorList.next()
            pyplot.scatter(plotableClose[i][0],plotableClose[i][1],\
                           marker='v',c=col,s=sSize,edgecolor='None')
            #if s[0]==0:
                #pyplot.scatter(s[2][0],s[2][1],c='r',s=sSize)
            #if s[0]==1:
                #pyplot.scatter(s[1][0],s[1][1],'sr')
            if s[0]==2:
                cir = pyplot.Circle((s[1][0],s[1][1]),s[1][2],\
                                    color=col,fill=False)
                pyplot.gcf().gca().add_artist(cir)
            if s[0]==3:
                x1 = s[1][0]+math.cos(s[1][2])
                x2 = s[1][0]-math.cos(s[1][2])
                y1 = s[1][1]+math.sin(s[1][2])
                y2 = s[1][1]-math.sin(s[1][2])
                pyplot.plot([x1,x2],[y1,y2],'--',color=col)

        cListUsed = []
        for k,mIs in enumerate(maxInds):
            cListUsed.append([])
            colorListIT = itertools.cycle(colorListNIT)
            for i in range(len(mIs)):
                col = colorListIT.next()
                cListUsed[-1].append(col)
                pyplot.scatter(plotableMax[k][i][0],plotableMax[k][i][1],\
                               marker='*',c=col,s=sSize,edgecolor='None')
        for cLs,mSs in zip(cListUsed,maxStates):
            for col,s in zip(cLs,mSs):
                #if s[0]==0:
                    #pyplot.scatter(s[2][0],s[2][1],c='b',s=sSize)
                #if s[0]==1:
                    #pyplot.scatter(s[1][0],s[1][1],'sb')
                if s[0]==2:
                    cir = pyplot.Circle((s[1][0],s[1][1]),s[1][2],\
                                        color=col,fill=False)
                    pyplot.gcf().gca().add_artist(cir)
                if s[0]==3:
                    x1 = s[1][0]+math.cos(s[1][2])
                    x2 = s[1][0]-math.cos(s[1][2])
                    y1 = s[1][1]+math.sin(s[1][2])
                    y2 = s[1][1]-math.sin(s[1][2])
                    pyplot.plot([x1,x2],[y1,y2],'--',color=col)

        #if sRef[0]==2:
            #cir = pyplot.Circle((sRef[1][0],sRef[1][1]),sRef[1][2],\
            #                    color='g',fill=False)
            #pyplot.gcf().gca().add_artist(cir)

            #cirFit = pyplot.Circle((xc,yc),R,\
            #                    color='k',fill=False)
            #pyplot.gcf().gca().add_artist(cirFit)

        # add workspace
        pyplot.gcf().gca().add_patch(pylab.Rectangle((-.15,-.15),\
                                                     .3,.3,facecolor='none'))
        # add arrows
        for i in range(len(obs[0])-1):
            pyplot.arrow(obs[0][i],obs[1][i], \
                         obs[0][i+1]-obs[0][i],obs[1][i+1]-obs[1][i], \
                         fc='k',ec='k',length_includes_head=True, \
                         width=0.0001,head_width=0.0002)
        # add observations
        pyplot.scatter(obs[0],obs[1],c='k',s=sSize)

        if plotLines:
            # add lines between close states and corresponding observations
            for i in range(len(closeStateInds)):
                for j in range(numSteps):
                    pyplot.plot([plotableClose[i][0][j+1],obs[0][j]],\
                                [plotableClose[i][1][j+1],obs[1][j]],'r--')

            # add lines between max states and corresponding observations
            for k,mIs in enumerate(maxInds):
                for i in range(len(mIs)):
                    for j in range(numSteps):
                        pyplot.plot([plotableMax[k][i][0][j+1],obs[0][j]],\
                                [plotableMax[k][i][1][j+1],obs[1][j]],'b--')
        pyplot.xlim([-.8,.3])
        pyplot.ylim([-.8,.3])
        pyplot.axis('equal')
        pyplot.show()

############################# END DEBUGGING CODE ###############################

if doWhat == 2:

    #print logProbs
    #print len(logProbs)
    #print len(logProbs[0])

    if plotLog:
        colorNorm = colors.Normalize(-6,-4)
    else:
        colorNorm = colors.Normalize(0,1) # YOU NEED THIS SO STUFF DOESN'T EXPLODDDEEE
    # without colorNorm, you can't do repeated plotting and get a useful
    # color answer becasue it normalize colors by default

    # plot stuff
    for i in range(numSteps):
        plotSome([2,3],modelNums,i,'F',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
        #plotAll(i,'F',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
        plotHist(3,modelNums,i,'H',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
        print [sum([math.exp(y) for y in logProbs[i][x]]) for x in range(len(modelNums))]

