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


import pytrans

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

def leastsq_line(x,y):
    xA = np.array(x)
    yA = np.array(y)
    A = np.vstack([xA, np.ones(len(xA))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    # wikipedia: b=-1, a=m, c=c 
    dists = np.abs(m*xA-yA+c)/np.sqrt(m**2+1)
    residu = np.sum(dists**2)
    return m, c, residu

###########

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

fileName = '/home/barragan/data12112014new//data/2015_01_22/data2Thu_Jan_22_11_07_47_2015.txt' # failed rev with old school rev transitions and sampling only one r but lots of thetas

# these are faked

fileName = '/home/barragan/data12112014new//data/2015_01_22/data2Thu_Jan_22_13_42_10_2015.txt' # the above rerun with resampling before instead of after

fileName = '/home/barragan/data12112014new//data/2015_01_22/data2Thu_Jan_22_17_11_35_2015.txt' # after fixing the resampling


# use these for robot observations
# Kx = 500 Ky = 30

# Rev [0.4572,0.3175,0.56]
s = [2,[0.4572,0.3175,0.56],[-2.5346]]
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_09_27_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_13_00_2015.txt'
fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_14_56_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_17_01_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_18_59_2015.txt'

# Rev [0.56, 0.0, 0.56]
# these experiments were causing errors because the robot gripper was running into the door. use with caution
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_25_26_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_27_24_2015.txt'
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_30_45_2015.txt'

# Rev ~ [0.0, 0.56, 0.56]
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_39_19_2015.txt' # weird arm things
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_42_27_2015.txt' # weird arm things
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_45_11_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_47_03_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data2Fri_Jan_23_17_49_33_2015.txt' # manually attempted to fix it when it swung way out of the workspace. didn't do it fast enough the second time so it failed totally.

# Pris ~ [14in in x, 3 in in y, neg theta]
#s = [3,[-0.391,0.084,2.930],[-0.40]]
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data3Fri_Jan_23_17_56_06_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data3Fri_Jan_23_17_58_03_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data3Fri_Jan_23_18_00_18_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data3Fri_Jan_23_18_02_29_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data3Fri_Jan_23_18_04_31_2015.txt' # success

# Free
#s = [0,[],[0.0,0.0]]
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data0Fri_Jan_23_18_06_58_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data0Fri_Jan_23_18_08_51_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data0Fri_Jan_23_18_10_40_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data0Fri_Jan_23_18_12_31_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_23/data0Fri_Jan_23_18_14_21_2015.txt' # success

# Rev with Kx = Ky = 500
s = [2,[0.49555,0.2608,0.56],[-2.657]]
#s = [3,[0.2346,-0.32396,2.1976],[0.40]]
fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_11_46_56_2015.txt' # failure
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_12_05_06_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_12_08_01_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_12_16_18_2015.txt' # succes or failure?
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_12_19_13_2015.txt' # failure

# Rev with Kx = 400 Ky = 100, switched translator to the "appropriate" sim
s = [2,[0.49555,0.2608,0.56],[-2.657]]
#s = [3,[0.1864,-0.3539,-1.086],[-.40]]
fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_12_59_06_2015.txt' # failure
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_01_18_2015.txt' # failure
fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_04_13_2015.txt' # failure
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_06_30_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data2Wed_Jan_28_13_08_53_2015.txt' # mega fail

# pris with Kx = 400 Ky = 100
#s = [3,[0.3327,0.222,0.588424174],[-0.40]]
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_21_21_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_24_05_2015.txt' # sucess
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_27_23_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_30_52_2015.txt' # success
#fileName = '/home/barragan/data12112014new//data/2015_01_28/data3Wed_Jan_28_13_35_50_2015.txt' # success


# get data
fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses, actions, obs, actionType, actionSelectionType, numMechanismTypes, numParticles, numRepeats, neff_fract, modelNums, realStates, BIAS, FTSD, FOSD, RTSD, ROSD = readData.get_data(fileName)

whichStep = -1

whichSteps = range(len(states))
sNew = list(s)

obsFakeList = [[],[]]
for whichStep in whichSteps:

    pyplot.subplot(3,4,whichStep+1)
    if s[0] == 2:
        revThs = [x[2][0] for x in states[whichStep][2]]
        ws=[math.exp(x) for x in logProbs[whichStep][2]]
        n, b, p = pyplot.hist(revThs,100,weights=ws)
        th = math.atan2(obs[0][whichStep-1]-s[1][0],obs[1][whichStep-1]-s[1][1])
        print whichStep-1,":",th
        pyplot.plot([th,th],[0,max(n)],c='r')

        maxW = max(ws)
        maxWI = ws.index(maxW)
        print 'Step:',whichStep
        print 'Prob:',maxW
        print 'Log Prob:',logProbs[whichStep][2][maxWI]
        print 'Th:',revThs[maxWI]
        print 'State:',states[whichStep][2][maxWI]
        pyplot.plot([revThs[maxWI],revThs[maxWI]],[0,max(n)],c='g')

        
    elif s[0] == 3:
        prisThs = [x[1][2] for x in states[whichStep][3]]
        ws=[math.exp(x) for x in logProbs[whichStep][3]]
        pyplot.hist(prisThs,100,weights=ws)

    

    #print 'Index 1000:'
    #print states[whichStep][2][1000]
        
pyplot.show()


