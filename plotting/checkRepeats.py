import readData
import statsFilesNR
from matplotlib import pyplot
import numpy as np

dirName1 = '/home/barragan/data12112014new/data/2014_12_30/'
dirName2 = '/home/barragan/data12112014new/data/2014_12_31/'
switchNum = 811
fileInds = [0,200,400,600,800]
fileInds = [x+150 for x in fileInds]
step = 1

for fI in fileInds:
    if fI < switchNum:
        dName = dirName1
    else:
        dName = dirName2

    f = statsFilesNR.files[fI]

    fbProbs, numSteps, model, statesInRbt, states, logProbs_O,\
             logProbs, poses, actions, obs, \
             actionType, actionSelectionType, numMechanismTypes,\
             numParticles, numRepeats, neff_fract, \
             modelNums, realStates, BIAS, FTSD, FOSD, RTSD, ROSD \
             = readData.get_data(dName+f)

    diffS = []
    diffSvars = []
    for mSs in states[step]:
        diffS.append([]) # for the model
        diffSvars.append([])
        for s in mSs:
            sMP = s[:2]
            if not sMP in diffS[-1]:
                diffS[-1].append(sMP)
                diffSvars[-1].append([s[2]])
            else:
                diffSvars[-1][diffS[-1].index(sMP)].append(s[2])
            #else:
                #if sMP[0] == 3:
                #    print [str.format('{0:.15f}',x) for x in diffS[-1][diffS[-1].index(sMP)][1]]
                #    print [str.format('{0:.15f}',x) for x in sMP[1]]
        #if diffS[-1][0][0]==3:
        #    raise Exception

    print fI,len(diffS)
    for dS in diffS:
        print len(dS)
    #print diffS
    print len(diffSvars),len(diffSvars[3]),len(diffSvars[3][0])

    numBins = 20
    print "mean:",np.mean(np.array(diffSvars[2][0]))
    print "std:",np.std(np.array(diffSvars[2][0]))
    if len(diffSvars[2][0])>numBins:
        pyplot.hist(np.array(diffSvars[2][0]),numBins)
        pyplot.show()
