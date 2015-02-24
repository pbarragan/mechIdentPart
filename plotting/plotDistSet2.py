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
################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


# set paths
exeDir = os.path.abspath(os.path.dirname(__file__))

# real robot
#fileName = '/../data/2014_12_02/'
#fileName += 'data2Tue_Dec__2_09_48_21_2014.txt'
#fileName += 'data2Tue_Dec__2_12_45_00_2014.txt'
# nominal rev model
#fileName += 'data2Tue_Dec__2_13_16_08_2014.txt' # compare these two

# this was a faked experiment
#fileName = '/../data/2014_12_04/'
# using nominal rev model actions and obs
#fileName += 'data2Thu_Dec__4_13_35_47_2014.txt' # compare these two

# real robot
#fileName = '/../data/2014_12_05/'

# nominal x-axis aligned pris model
#fileName += 'data3Fri_Dec__5_09_42_02_2014.txt'

# nominal pris model at ~0.588 or ~-2.554 [rad]
# random
#fileName += 'data3Fri_Dec__5_10_02_28_2014.txt' # success
#fileName += 'data3Fri_Dec__5_10_47_56_2014.txt' # failure
#fileName += 'data3Fri_Dec__5_10_52_26_2014.txt' # failure
#fileName += 'data3Fri_Dec__5_10_55_39_2014.txt' # success

# going back to it
#fileName += 'data3Fri_Dec__5_11_52_56_2014.txt' # success
#fileName += 'data3Fri_Dec__5_11_56_00_2014.txt' # failure
#fileName += 'data3Fri_Dec__5_12_11_32_2014.txt' # success

# relax before reading observation
#fileName += 'data3Fri_Dec__5_12_28_29_2014.txt' # success
#fileName += 'data3Fri_Dec__5_12_30_47_2014.txt' # 

# back to normal
# entropy
#fileName += 'data3Fri_Dec__5_10_59_36_2014.txt' # ? right model, bad param
#fileName += 'data3Fri_Dec__5_11_06_56_2014.txt' # ? right model eventually, bad param

#after adjusting the drawer
#fileName += 'data3Fri_Dec__5_11_38_45_2014.txt' # success
#fileName += 'data3Fri_Dec__5_11_45_14_2014.txt' # success

# debug after systematic error
#fileName = '/../data/2014_12_11/data2Thu_Dec_11_10_57_22_2014.txt'

# 12/18/14 - checking about the revolute model
#fileName = '/home/barragan/data12112014new/data/2014_12_15/data2Mon_Dec_15_21_06_59_2014.txt'

# 12/23/14
#fileName = '/home/barragan/data12112014new/data/2014_12_23/data0Tue_Dec_23_22_57_42_2014.txt'

#fileName = '/home/barragan/data12112014new//data/2014_12_24/data0Wed_Dec_24_11_55_39_2014.txt'

#fileName = '/home/barragan/data12112014new//data/2014_12_24/data0Wed_Dec_24_12_23_46_2014.txt'

#fileName = '/home/barragan/data12112014new//data/2014_12_26/data0Fri_Dec_26_15_33_42_2014.txt'

# 12/26/14
#fileName = '/home/barragan/data12112014new/data/2014_12_26/data0Fri_Dec_26_19_15_52_2014.txt'

#dataDir = '/home/barragan/data12112014new/data/2014_12_27fifty/'
#fileName = 'data0Sat_Dec_27_12_12_08_2014.txt'
#fileName = 'data0Sat_Dec_27_12_36_53_2014.txt'
#fileName = 'data2Sat_Dec_27_12_26_27_2014.txt'
#fileName = 'data2Sat_Dec_27_13_10_47_2014.txt'
#fileName = 'data3Sat_Dec_27_12_31_20_2014.txt'

#dataDir = '/home/barragan/data12112014new/data/2014_12_27eighty/'
#fileName = 'data2Sat_Dec_27_01_55_05_2014.txt'

#fileName = dataDir+fileName

#fileName = '/home/barragan/data12112014new//data/2015_01_16/data2Fri_Jan_16_17_29_21_2015.txt' # failure
fileName = '/home/barragan/data12112014new//data/2015_01_16/data2Fri_Jan_16_17_48_57_2015.txt' # scripted huge success
fileName = '/home/barragan/data12112014new//data/2015_01_16/data2Fri_Jan_16_17_53_23_2015.txt' # scripted huge success
fileName = '/home/barragan/data12112014new//data/2015_01_16/data2Fri_Jan_16_17_59_22_2015.txt' # random failure

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_09_52_42_2015.txt' # not perfect script failure

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_10_03_40_2015.txt' # not perfect script success with smaller rev dynamics

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_10_10_33_2015.txt' # not perfect script succes with smaller rev dynamics and large actions

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_10_16_42_2015.txt' # random success with smaller rev dynamics and large actions

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_10_31_58_2015.txt' # random success (very weird actual failure) with Small D and large A

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_10_43_14_2015.txt' # random failure (looked really good though) with Small D and large A

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_10_50_36_2015.txt' # same as last one

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_10_58_57_2015.txt' # random failure but close between rev and pris with resampling

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_02_55_2015.txt' # same as last time

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_06_19_2015.txt' # same as last time

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_21_40_2015.txt' # almost tied but bad

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_31_10_2015.txt' # almost tied but bad

#fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_36_49_2015.txt' # same as last time with lower forward stiffness (got it right)

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_43_51_2015.txt' # same as last time with even lower forward stiffness (got it right)

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_51_00_2015.txt' # same with lower resampling. not as good.

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_53_20_2015.txt' # same with lower resampling. failed. but better rev guess.

fileName = '/home/barragan/data12112014new//data/2015_01_19/data2Mon_Jan_19_11_55_49_2015.txt' # also just a failure with a bad rev guess.

# a new day
fileName = '/home/barragan/data12112014new//data/2015_01_20/data2Tue_Jan_20_09_49_10_2015.txt' # repeat of yesterday

fileName = '/home/barragan/data12112014new//data/2015_01_20/data2Tue_Jan_20_10_00_15_2015.txt' # with sampling much closer to the right answer for Rev

fileName = '/home/barragan/data12112014new//data/2015_01_20/data2Tue_Jan_20_10_10_56_2015.txt' # got the right answer i think because so many particles near it

fileName = '/home/barragan/data12112014new//data/2015_01_20/data2Tue_Jan_20_10_18_41_2015.txt' # got the right answer I think because so many particles near it

fileName = '/home/barragan/data12112014new//data/2015_01_20/data0Tue_Jan_20_10_25_25_2015.txt' # switched to make sure Free model was going to still work. It did.

fileName = '/home/barragan/data12112014new//data/2015_01_20/data3Tue_Jan_20_10_38_26_2015.txt' # Pris model fail (to fixed) because no usable action used

fileName = '/home/barragan/data12112014new//data/2015_01_20/data3Tue_Jan_20_10_41_18_2015.txt' # same as last one

fileName = '/home/barragan/data12112014new//data/2015_01_20/data3Tue_Jan_20_10_45_22_2015.txt' # Pris worked after turning up the forward gain

fileName = '/home/barragan/data12112014new//data/2015_01_20/data3Tue_Jan_20_11_03_13_2015.txt' # same as last one

# a new day

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_09_46_37_2015.txt' # failure I think because the particles aren't in the right place

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_09_51_44_2015.txt' # failure weird arm freak out at the end. stupid kinematics.

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_09_54_38_2015.txt' # failure but it should have worked. too sensitive.

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_09_58_28_2015.txt' # also a failure. I'm changing the gain back.

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_10_02_51_2015.txt' # success with a lower gain

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_10_05_10_2015.txt' # also success with a lower gain

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_10_08_13_2015.txt' # failure higher gain but bigger swing in translator

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_10_13_13_2015.txt' # higher gain but kp = 500 in translator too

# these are faked

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_16_33_29_2015.txt' # rev worked after changing transitions back to old way

#fileName = '/home/barragan/data12112014new//data/2015_01_21/data2Wed_Jan_21_16_43_21_2015.txt' # pris still works after the previous change

# a new day 1/22

#fileName = '/home/barragan/data12112014new//data/2015_01_22/data2Thu_Jan_22_10_31_41_2015.txt' # failed rev with old school rev transitions

#fileName = '/home/barragan/data12112014new//data/2015_01_22/data2Thu_Jan_22_11_07_47_2015.txt' # failed rev with old school rev transitions and sampling only one r but lots of thetas





# Rev with Kx = 400 Ky = 100, switched translator to the "appropriate" sim
s = [2,[0.49555,0.2608,0.56],[-2.657]]
s = [3,[0.1864,-0.3539,-1.086],[-.40]]
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_12_59_06_2015.txt' # failure
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_01_18_2015.txt' # failure
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_04_13_2015.txt' # failure
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_06_30_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_08_53_2015.txt' # mega fail


# pris with Kx = 400 Ky = 100
#s = [3,[0.3327,0.222,0.588424174],[-0.40]]
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_21_21_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_24_05_2015.txt' # sucess
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_27_23_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_30_52_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_35_50_2015.txt' # success


# Back to robot experiments Free and Fixed with Kx = 400 and Ky = 100
# Free
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data0Tue_Feb__3_11_59_41_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data0Tue_Feb__3_12_02_01_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data0Tue_Feb__3_12_04_27_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data0Tue_Feb__3_12_06_42_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data0Tue_Feb__3_12_09_11_2015.txt' # success

# Fixed
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data1Tue_Feb__3_12_14_12_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data1Tue_Feb__3_12_16_27_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data1Tue_Feb__3_12_18_35_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_02_03/data1Tue_Feb__3_12_21_02_2015.txt' # success
fileName = '/home/barragan/data12112014new//data/2015_02_03/data1Tue_Feb__3_12_23_46_2015.txt' # success


#check
fileName = '/home/barragan/data12112014new//data/2015_02_04/data3Wed_Feb__4_00_22_51_2015.txt' # doesn't work

# rev
fileName = '/home/barragan/data12112014new//data/2015_02_04/data2Wed_Feb__4_20_39_36_2015.txt' # failure with angle 0.84781697379 - close
fileName = '/home/barragan/data12112014new//data/2015_02_04/data2Wed_Feb__4_20_43_05_2015.txt' # same as above

# 2/20/15
# latch
fileName = '/home/barragan/data12112014new//data/2015_02_20/data3Fri_Feb_20_10_44_51_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_02_20/data3Fri_Feb_20_10_47_49_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_02_20/data3Fri_Feb_20_10_50_07_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_02_20/data3Fri_Feb_20_10_52_34_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_02_20/data3Fri_Feb_20_10_54_43_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_02_20/data3Fri_Feb_20_10_57_10_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_02_20/data3Fri_Feb_20_10_59_36_2015.txt'

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
fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses, actions, obs, actionType, actionSelectionType, numMechanismTypes, numParticles, numRepeats, neff_fract, modelNums, realStates, BIAS, FTSD, FOSD, RTSD, ROSD = readData.get_data(fileName)

print "YO"
print numParticles
print numRepeats
print neff_fract
print BIAS,FTSD,FOSD,RTSD,ROSD

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
    plotLines = False
    plotArrows = False
    resampling = False

    whichModels = [2,3]

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

    #sRef = [0, [], [1,1]] # for free
    #sRef = [3, [0.0,-0.4,1.57],[0.4]] # for pris
    #sRef = [3, [-0.396, 0.396, -0.785], [0.56]] # for pris
    #sRef = [3, [-0.56, 0.0, 0.0], [0.56]] # for pris
    #sRef = [2, [0.396, 0.396, 0.56], [-2.35619]] # for rev
    sRef = [2, [0.3731,0.4176,0.56], [-2.3]] # for rev real
    #sRef = [2, [0.405179,0.361999,0.543335], [-2.3448]] # for rev real
    #sRef = [2, [-0.396,-0.396,0.56],[0.7854]] # for rev
    #sRef = [2, [0.46, 0.32, 0.56], [-2.514]] # for rev, nominal from 12/2/14
    #sClosest =
    # find the closest states to sref
    # this probably shouldn't have which step and only look at step 0
    srefMI = modelNums.index(sRef[0])
    closeStates = findCloseStates(sRef,states[0][srefMI],.000325) #.03 for rev, .003 for pris
    
    closeStateInds = [states[0][srefMI].index(x) for x in closeStates]
    closeStateProbs = [logProbs[whichStep][srefMI][x] for x in closeStateInds]
    closeStateProbsPrev = [logProbs[whichStep-1][srefMI][x] \
                           for x in closeStateInds]

    closeStateProbsList = []
    closeStatesInRbtList = []
    maxStatesInRbtList = [[] for x in maxInds]
    maxProbsList = [[] for x in maxInds]


    #  here's where to do it

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

    for msL in maxStatesInRbtList:
        #maxDists.append([dist([obs[0][i],obs[1][i]],x) \
        #                 for x in maxStatesInRbtList[i+1]])
        print "here"
        print msL

    print 'here we go:'
    print 'probs'
    print closeStateProbsList
    print 'in rbt'
    print closeStatesInRbtList
    print 'dists'
    print closeStateDists
    print 'actions'
    print actions
    print
    print
    print
    for i,(x,y) in enumerate(zip(actions[0],actions[1])):
        print "std::vector<double> actions"+str(i)+";"
        print "actions"+str(i)+".push_back("+str(x)+");"
        print "actions"+str(i)+".push_back("+str(y)+");"
        print "fakeActions.push_back(actions"+str(i)+");"
    print
    print
    print
    print 'obs'
    print obs
    print
    print
    print
    for i,(x,y) in enumerate(zip(obs[0],obs[1])):
        print "std::vector<double> obs"+str(i)+";"
        print "obs"+str(i)+".push_back("+str(x)+");"
        print "obs"+str(i)+".push_back("+str(y)+");"
        print "fakeObs.push_back(obs"+str(i)+");"
    print
    print
    print
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

            for f,(x,y) in enumerate(zip(plotableClose[i][0],\
                                     plotableClose[i][1])):
                if f!=0:
                    pyplot.annotate(f-1,(x,y),color='magenta',size='large')
            #if s[0]==0:
                #pyplot.scatter(s[2][0],s[2][1],c='r',s=sSize)
            #if s[0]==1:
                #pyplot.scatter(s[1][0],s[1][1],'sr')
            if s[0]==2:
                cir = pyplot.Circle((s[1][0],s[1][1]),s[1][2],\
                                    color=col,fill=False,ls='dashed')
                pyplot.gcf().gca().add_artist(cir)
            if s[0]==3:
                x1 = s[1][0]+math.cos(s[1][2])
                x2 = s[1][0]-math.cos(s[1][2])
                y1 = s[1][1]+math.sin(s[1][2])
                y2 = s[1][1]-math.sin(s[1][2])
                pyplot.plot([x1,x2],[y1,y2],'--',color=col)

        cListUsed = []

        # plotableMax[model type][which max 1,2,3][x or y]
        for k,mIs in enumerate(maxInds):
            cListUsed.append([])
            colorListIT = itertools.cycle(colorListNIT)
            for i in range(len(mIs)):
                col = colorListIT.next()
                cListUsed[-1].append(col)
                pyplot.scatter(plotableMax[k][i][0],plotableMax[k][i][1],\
                               marker='*',c=col,s=sSize,edgecolor='None')

                for f,(x,y) in enumerate(zip(plotableMax[k][i][0],\
                                             plotableMax[k][i][1])):
                    if f!=0:
                        pyplot.annotate(f-1,(x,y),color='magenta',size='large')
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
                    pyplot.plot([x1,x2],[y1,y2],color=col)

        if sRef[0]==2:
            cir = pyplot.Circle((sRef[1][0],sRef[1][1]),sRef[1][2],\
                                color='g',fill=False,ls='dashdot')
            pyplot.gcf().gca().add_artist(cir)

            cirFit = pyplot.Circle((xc,yc),R,\
                                color='k',fill=False,ls='dashdot')
            pyplot.gcf().gca().add_artist(cirFit)

        # add workspace
        pyplot.gcf().gca().add_patch(pylab.Rectangle((-.15,-.15),\
                                                     .3,.3,facecolor='none'))
        # add arrows
        if plotArrows:
            for i in range(len(obs[0])-1):
                pyplot.arrow(obs[0][i],obs[1][i], \
                             obs[0][i+1]-obs[0][i],obs[1][i+1]-obs[1][i], \
                             fc='k',ec='k',length_includes_head=True, \
                             width=0.0001,head_width=0.004)
            
        # add observations
        pyplot.scatter(obs[0],obs[1],c='k',s=sSize)
        for i, txt in enumerate(range(len(obs[0]))):
            pyplot.annotate(txt,(obs[0][i],obs[1][i]),\
                            color='magenta',size='large')

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

