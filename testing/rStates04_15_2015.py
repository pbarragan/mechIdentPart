import numpy as np

def inTOm(inch):
    return 0.0254*inch

trueMeas=[[3.5,12.125,3.25],
          [3.5,12.125,5.125],
          [4.75,9.75,5.125],
          [4.75,9.75,3.25],
          [5.5,5.5,3.25],
          [5.5,5.5,5.125],
          [5.0,0.375,5.125],
          [5.0,0.375,3.25],
          [22.75,16.0,3.25],
          [22.75,16.0,5.125],
          [9.5,55.2],
          [42.6,37.6],
          [56.6,1.0],
          [37.8,-40.3],
          [7.5,-55.1],
          [-9.5,-27.6],
          [19.3,-19.5],
          [27.8,10.8],
          [13.9,26.9],
          [-3.5,29.0],
          [3.7,33.2],
          [13.8,48.6],
          [-2.5,24.3],
          [27.4,42.8],
          [8.5,8.5],
          [45.1,37.4],
          [36.0,17.3],
          [30.1,4.0],
          [29.3,-6.5],
          [-12,-48]]

# free
trueStates = [[0,[],[0.0,0.0]] for x in range(10)]

for tM in trueMeas[0:10]:
    # latch
    # this was in inches for some reason
    opp = inTOm(tM[1]-tM[0])
    h = inTOm(17.5)
    radius = 0.19
    d = inTOm(tM[2])
    offset = radius+d
    thRobot = np.arcsin(opp/h)
    #print thRobot
    thLatch = np.pi/2 + thRobot
    ps = [-offset*np.cos(thLatch),-offset*np.sin(thLatch),radius,thLatch,d]
    vs = [thLatch,d]
    trueStates.append([4,ps,vs])

for tM in trueMeas[10:20]:
    # rev
    # this was in cm
    radius = np.sqrt((0.01*tM[0])**2+(0.01*tM[1])**2)
    th = np.arctan2(tM[1],tM[0])-np.pi
    th = (th+np.pi)%(2*np.pi)-np.pi # wrap to -pi to pi
    ps = [radius*np.cos(th+np.pi),radius*np.sin(th+np.pi),radius]
    vs = [th]
    trueStates.append([2,ps,vs])

for tM in trueMeas[20:30]:
    # pris
    # this was in cm
    h = 0.365
    opp = 0.01*(tM[1]-tM[0])
    th = np.arcsin(opp/h)-np.pi
    th = (th+np.pi)%(2*np.pi)-np.pi # wrap to -pi to pi
    offset = 0.40
    ps = [-offset*np.cos(th),-offset*np.sin(th),th]
    vs = [offset]
    trueStates.append([3,ps,vs])

# fixed
trueStates.extend([[1,[0.0,0.0],[]] for x in range(10)])

