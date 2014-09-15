import numpy
import math
import os

#statesInRbt[step][model][x or y]
#logProbs[step][model]
#poses[x or y][step]
#fbProbs[step][model]
#actions[x or y][step]
#obs[x or y][step]

def skip_lines(f,lines):
    for i in range(lines):
        f.readline()

def get_data(fileName):

    statesInRbt = []
    states = []
    logProbs = []
    fbProbs = []
    f = open(fileName,'r')
    #read the initial stuff you need
    f.readline()
    actionType = int(f.readline())
    f.readline()
    actionSelectionType = int(f.readline())
    f.readline()
    model = int(f.readline())
    skip_lines(f,5)
    numMechanismTypes = int(f.readline())
    f.readline()
    numParticles = int(f.readline())

    # iterate through the mechanisms
    modelNums = []
    numStatesList = []
    
    logProbs.append([])
    statesInRbt.append([])
    states.append([]) # adding a step (-1)
    for i in range(numMechanismTypes):        
        f.readline()
        modelNums.append(int(f.readline()))
        f.readline()
        numStatesList.append(int(f.readline()))

        # this is where we skip the state representation
        skip_lines(f,1)
        # state representation
        states[-1].append([]) # adding a model
        for j in range(numStatesList[-1]):
            # model
            skip_lines(f,1)
            mNum = int(f.readline())

            # params
            skip_lines(f,1)
            holdLine1 = f.readline()
            valList1 = holdLine1.split(',')
            valList1.pop() # remove the last empty string
            numList1 = [float(x) for x in valList1]

            # vars
            skip_lines(f,1)
            holdLine2 = f.readline()
            valList2 = holdLine2.split(',')
            valList2.pop() # remove the last empty string
            numList2 = [float(x) for x in valList2]
            states[-1][-1].append([mNum,numList1,numList2]) # adding a state

            
        # skip last one
        skip_lines(f,1)
        
        #skip_lines(f,numStatesList[-1]*6+2)

        
        # here's where we need to get the cartesian version of the states
        statesInRbt[-1].append([[],[]])
        for j in range(numStatesList[-1]):
            holdLine = f.readline()
            valList = holdLine.split(',')
            numList = []
            numList.append(int(valList[0]))
            numList.append(float(valList[1]))
            numList.append(float(valList[2]))
            statesInRbt[-1][-1][0].append(numList[1])
            statesInRbt[-1][-1][1].append(numList[2])

        # get the log probs
        f.readline()
        logProbs[-1].append([])
        for j in range(numStatesList[-1]):
            logProbs[-1][-1].append(float(f.readline()))

    # Get filter bank probs
    fbProbs.append([])
    skip_lines(f,1)
    for i in range(numMechanismTypes):
        fbProbs[-1].append(float(f.readline()))

    skip_lines(f,2+numMechanismTypes)  
    numActions = int(f.readline())
    skip_lines(f,numActions+2)

    # get the initial pose in rbt:
    poses = [[],[]]
    holdPose = f.readline()
    stringList = holdPose.split(',')
    # get rid of the empty string at the end because of the last ,
    stringList.pop()
    
    poseList = []
    poseList.append(float(stringList[0]))
    poseList.append(float(stringList[1]))
    poses[0].append(poseList[0])
    poses[1].append(poseList[1])
    
    skip_lines(f,1)
    numSteps = int(f.readline())
    #this has to happen until you get to the end of the file
    logProbs_O = []
    actions = [[],[]]
    obs = [[],[]]
    for i in range(numSteps):
        skip_lines(f,3)

        # get action. hellz yeah.
        holdAction = f.readline()
        actionString = holdAction.split(',')
        # get rid of the empty string at the end because of the last ,
        actionString.pop() 
        actionList = []
        actionList.append(float(actionString[0]))
        actionList.append(float(actionString[1]))
        actions[0].append(actionList[0])
        actions[1].append(actionList[1])

        skip_lines(f,1)
        
        # get current pose
        holdP = f.readline()
        stringL = holdP.split(',')
        # get rid of the empty string at the end because of the last ,
        stringL.pop() 
        poseL = []
        poseL.append(float(stringL[0]))
        poseL.append(float(stringL[1]))
        poses[0].append(poseL[0])
        poses[1].append(poseL[1])

        skip_lines(f,1)
        
        # get obs
        holdO = f.readline()
        stringLO = holdO.split(',')
        # get rid of the empty string at the end because of the last ,
        stringLO.pop() 
        obsL = []
        obsL.append(float(stringLO[0]))
        obsL.append(float(stringLO[1]))
        obs[0].append(obsL[0])
        obs[1].append(obsL[1])



        logProbs.append([])
        logProbs_O.append([])
        statesInRbt.append([])
        states.append([]) # adding a step
        for j in range(numMechanismTypes):      
            skip_lines(f,3)
            
            # this is where we skip the state representation
            #skip_lines(f,numStatesList[j]*6)

            # this is where we skip the state representation
            #skip_lines(f,1)
            # state representation
            states[-1].append([]) # adding a model
            for b in range(numStatesList[-1]):
                # model
                skip_lines(f,1)
                mNum = int(f.readline())
                
                # params
                skip_lines(f,1)
                holdLine1 = f.readline()
                valList1 = holdLine1.split(',')
                valList1.pop() # remove the last empty string
                numList1 = [float(x) for x in valList1]
                
                # vars
                skip_lines(f,1)
                holdLine2 = f.readline()
                valList2 = holdLine2.split(',')
                valList2.pop() # remove the last empty string
                numList2 = [float(x) for x in valList2]

                states[-1][-1].append([mNum,numList1,numList2]) # adding a state
                
            # skip last one
            skip_lines(f,1)
        
            # here's where we need to get the cartesian version of the states
            statesInRbt[-1].append([[],[]])
            for k in range(numStatesList[j]):
                holdLine = f.readline()
                valList = holdLine.split(',')
                numList = []
                numList.append(int(valList[0]))
                numList.append(float(valList[1]))
                numList.append(float(valList[2]))
                statesInRbt[-1][-1][0].append(numList[1])
                statesInRbt[-1][-1][1].append(numList[2])

            # O
            skip_lines(f,1)
            logProbs_O[-1].append([])
            for k in range(numStatesList[j]):
                logProbs_O[-1][-1].append(float(f.readline()))

            # get the log probs
            f.readline()
            logProbs[-1].append([])
            for k in range(numStatesList[j]):
                logProbs[-1][-1].append(float(f.readline()))



        # Get filter bank probs
        fbProbs.append([])
        skip_lines(f,1)
        for j in range(numMechanismTypes):
            fbProbs[-1].append(float(f.readline()))

        skip_lines(f,2+numMechanismTypes+8*numMechanismTypes)  

    f.close()


    return fbProbs, numSteps, model, statesInRbt, states, logProbs_O, logProbs, poses, actions, obs, actionType, actionSelectionType, numMechanismTypes, numParticles, modelNums