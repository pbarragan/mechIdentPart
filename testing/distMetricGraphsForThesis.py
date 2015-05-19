import transExternal
import readData
import json
import os
import numpy as np
import copy
import rStates04_15_2015

from matplotlib import pyplot
import matplotlib.colors as colors
import matplotlib.cm as cmx

from matplotlib.legend_handler import HandlerPatch
import matplotlib.patches as mpatches

def make_legend_ellipse(legend, orig_handle,
                        xdescent, ydescent,
                        width, height, fontsize):
    p = mpatches.Ellipse(xy=(0.5*width-0.5*xdescent, 0.5*height-0.5*ydescent),
                         width = width+xdescent, height=(height+ydescent))

    return p

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


#color stuff
jet = cm = pyplot.get_cmap('cool') # cool 
cNorm  = colors.Normalize(vmin=0, vmax=(len(indexList)-1))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

# plot actions
pose = [0.0,0.0]
s=[0,[],[0.0,0.0]]
poses = [pose]

# change offsets
offsets = [[0.0,0.0] for x in range(len(indexList))]
osd = 0.002
offsets[0][1] = -osd
offsets[2][0] = osd*np.sqrt(2)/2
offsets[2][1] = osd*np.sqrt(2)/2
offsets[3][0] = -osd*np.sqrt(2)/2
offsets[3][1] = -osd*np.sqrt(2)/2
offsets[5][0] = osd
offsets[6][0] = -osd
offsets[8][0] = osd*np.sqrt(2)/2
offsets[8][1] = -osd*np.sqrt(2)/2
offsets[9][0] = -osd*np.sqrt(2)/2
offsets[9][1] = osd*np.sqrt(2)/2
offsets[11][1] = -osd
offsets[12][1] = osd
offsets[14][0] = -osd*np.sqrt(2)/2
offsets[14][1] = -osd*np.sqrt(2)/2
offsets[15][0] = osd*np.sqrt(2)/2
offsets[15][1] = osd*np.sqrt(2)/2
offsets[17][0] = -osd
offsets[18][0] = osd
offsets[20][0] = -osd*np.sqrt(2)/2
offsets[20][1] = osd*np.sqrt(2)/2
offsets[21][0] = osd*np.sqrt(2)/2
offsets[21][1] = -osd*np.sqrt(2)/2
offsets[23][1] = osd

for i,a in enumerate(actionList):
    #o,s = transExternal.simulate(s,a)
    colorVal = scalarMap.to_rgba(i)
    pyplot.arrow(pose[0]+offsets[i][0],pose[1]+offsets[i][1],a[0],a[1],\
                 fc=colorVal,ec=colorVal,length_includes_head=True, \
                 width=0.0001,head_width=0.004,head_length=0.008)
    #pyplot.annotate(i,(pose[0]+a[0]*1.1,pose[1]+a[1]*1.1),\
    #                size='x-large',color='g')

    pose[0]+=a[0]
    pose[1]+=a[1]
    poses.append(list(pose))

#pyplot.annotate('0,22',(poses[1][0],poses[1][1]),size='x-large',color='k')
#pyplot.annotate('1,3',(poses[2][0],poses[2][1]),size='x-large',color='k')
#pyplot.annotate('2',(poses[3][0],poses[3][1]),size='x-large',color='k')
#pyplot.annotate('4,6',(poses[5][0],poses[5][1]),size='x-large',color='k')
#pyplot.annotate('5,',(poses[6][0],poses[6][1]),size='x-large',color='k')

pyplot.xlim([-0.15,.15])
pyplot.ylim([-0.15,.15])
pyplot.gca().set_aspect('equal')
pyplot.xlabel('x [m]')
pyplot.ylabel('y [m]')

#pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/actionSequence.pdf",bbox_inches='tight')
pyplot.show()

sSize = 40
##########################
#sReal = [2,[0.4420,0.3439,0.56],[-2.480]]
thReal = -2.080
rReal = 0.56
sReal = [2,[rReal*np.cos(thReal+np.pi),rReal*np.sin(thReal+np.pi),rReal],\
         [thReal]]

thEst = -1.9 #-1.95 big error, -1.9 small error
rEst = 0.39 # 0.3770 or 0.3771
#thEst = -2.080+np.pi
#rEst = 0.56
sEst = [2,[rEst*np.cos(thEst+np.pi),rEst*np.sin(thEst+np.pi),rEst],[thEst]]

c1=pyplot.Circle((sReal[1][0],sReal[1][1]),sReal[1][2],color='g',fill=False,label='True')
pyplot.gca().add_artist(c1)

c2=pyplot.Circle((sEst[1][0],sEst[1][1]),sEst[1][2],color='r',fill=False,label='Estimate')
pyplot.gca().add_artist(c2)

pyplot.legend(handles=[c1,c2],handler_map={pyplot.Circle:HandlerPatch(patch_func=make_legend_ellipse),})

dists = []
oRprev = [0.0,0.0]
oEprev = [0.0,0.0]
showStart = 0
showEnd = 24
plotDebug = False
for i,a in enumerate(actionList):
    colorVal = scalarMap.to_rgba(i)
    oR,sReal = transExternal.simulate(sReal,a)
    oE,sEst = transExternal.simulate(sEst,a)

    # 5 to 9
    if i in range(showStart,showEnd):
        pyplot.scatter(oR[0],oR[1],c=colorVal,edgecolor=colorVal,s=sSize)
        pyplot.scatter(oE[0],oE[1],c=colorVal,edgecolor=colorVal,s=sSize)
        pyplot.plot([oR[0],oE[0]],[oR[1],oE[1]],'b--')

        if plotDebug:
            pyplot.arrow(oRprev[0],oRprev[1],a[0],a[1],\
                         fc=colorVal,ec=colorVal,length_includes_head=True, \
                         width=0.0001,head_width=0.004,head_length=0.008)

            pyplot.arrow(oEprev[0],oEprev[1],a[0],a[1],\
                         fc=colorVal,ec=colorVal,length_includes_head=True, \
                         width=0.0001,head_width=0.004,head_length=0.008)

            pyplot.annotate(i,(oR[0],oR[1]),size='x-large',color='c')
            pyplot.annotate(i,(oE[0],oE[1]),size='x-large',color='c')

    if plotDebug:
        if i in range(showEnd-2,showEnd-1):
            pyplot.plot([oR[0],sReal[1][0]],[oR[1],sReal[1][1]],'k--')
            pyplot.plot([oE[0],sEst[1][0]],[oE[1],sEst[1][1]],'k--')

    oRprev = list(oR)
    oEprev = list(oE)
    dists.append(distOs(oR,oE))

print dists
print "Circle Circle Distance",np.mean(dists)

#pyplot.xlim([-0.30,.25])
#pyplot.ylim([-0.10,.40])
pyplot.xlim([-0.26,.20])
pyplot.ylim([-0.10,.26])
pyplot.gca().set_aspect('equal')
pyplot.xlabel('x [m]')
pyplot.ylabel('y [m]')

pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/bigErrorFINAL.pdf",bbox_inches='tight')
pyplot.show()
##########################

##########################
#sReal = [2,[0.4420,0.3439,0.56],[-2.480]]
thReal = -2.080
rReal = 0.56
sReal = [2,[rReal*np.cos(thReal+np.pi),rReal*np.sin(thReal+np.pi),rReal],\
         [thReal]]


thEst = -2.080+np.pi/2
offset = 0.4
sEst = [3,[offset*np.cos(thEst),offset*np.sin(thEst),thEst],[-offset]]

c1 = pyplot.Circle((sReal[1][0],sReal[1][1]),sReal[1][2],color='g',fill=False,\
                   label='True')
pyplot.gca().add_artist(c1)

c2, = pyplot.plot([sEst[1][0],sEst[1][0]-0.8*np.cos(sEst[1][2])],\
                 [sEst[1][1],sEst[1][1]-0.8*np.sin(sEst[1][2])],color='r',\
                 label='Estimate')


pyplot.legend(handles=[c1,c2],handler_map={pyplot.Circle:HandlerPatch(patch_func=make_legend_ellipse),})

dists = []
oRprev = [0.0,0.0]
oEprev = [0.0,0.0]
for i,a in enumerate(actionList):
    colorVal = scalarMap.to_rgba(i)
    oR,sReal = transExternal.simulate(sReal,a)
    oE,sEst = transExternal.simulate(sEst,a)

    if i in range(showStart,showEnd):

        pyplot.scatter(oR[0],oR[1],c=colorVal,edgecolor=colorVal,s=sSize)
        pyplot.scatter(oE[0],oE[1],c=colorVal,edgecolor=colorVal,s=sSize)
        pyplot.plot([oR[0],oE[0]],[oR[1],oE[1]],'b--')

        if plotDebug:
            pyplot.arrow(oRprev[0],oRprev[1],a[0],a[1],\
                         fc=colorVal,ec=colorVal,length_includes_head=True, \
                         width=0.0001,head_width=0.004,head_length=0.008)

            pyplot.arrow(oEprev[0],oEprev[1],a[0],a[1],\
                         fc=colorVal,ec=colorVal,length_includes_head=True, \
                         width=0.0001,head_width=0.004,head_length=0.008)

            pyplot.annotate(i,(oR[0],oR[1]),size='x-large',color='c')
            pyplot.annotate(i,(oE[0],oE[1]),size='x-large',color='c')

    if plotDebug:
        if i in range(showEnd-2,showEnd-1):
            pyplot.plot([oR[0],sReal[1][0]],[oR[1],sReal[1][1]],'k--')
            # pyplot.plot([oE[0],sEst[1][0]],[oE[1],sEst[1][1]],'k--')

    oRprev = list(oR)
    oEprev = list(oE)
    dists.append(distOs(oR,oE))
    #pyplot.annotate(i,(oR[0],oR[1]),size='x-large',color='m')

print dists
print "Line Circle Distance",np.mean(dists)

pyplot.xlim([-0.26,.20])
pyplot.ylim([-0.10,.26])
pyplot.gca().set_aspect('equal')
pyplot.xlabel('x [m]')
pyplot.ylabel('y [m]')

pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/smallErrorFINAL.pdf",bbox_inches='tight')
pyplot.show()
##########################

raise Exception

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
    else:
        if (r[0] == 0) or (r[0] == 1):
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
                             
            

