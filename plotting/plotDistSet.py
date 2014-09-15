from matplotlib import pyplot
from matplotlib import colors
import numpy
import math
import os

import readData

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

fileName = '/../data/2014_09_11/data0Thu_Sep_11_18_51_54_2014.txt'
fileName2 = '/../data/2014_09_11/data0Thu_Sep_11_21_34_32_2014.txt'
fileName3 = '/../data/2014_09_11/data0Thu_Sep_11_22_36_11_2014.txt'
fileName4 = '/../data/2014_09_11/data0Thu_Sep_11_22_39_00_2014.txt'
fileName5 = '/../data/2014_09_11/data0Thu_Sep_11_23_02_59_2014.txt'

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
         = readData.get_data(exeDir+fileName5)

if plotLog:
    colorNorm = colors.Normalize(-100,0)
else:
    colorNorm = colors.Normalize(0,1) # YOU NEED THIS SO STUFF DOESN'T EXPLODDDEEE
# without colorNorm, you can't do repeated plotting and get a useful
# color answer becasue it normalize colors by default

# plot stuff
for i in range(numSteps):
    plotSome([1],i,'F',plotSet,plotLog,colorNorm,setPath,statesInRbt,states,logProbs,fbProbs,poses,actions,obs)
