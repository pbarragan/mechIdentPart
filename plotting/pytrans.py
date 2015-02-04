import math

def trans(stm1,a):
    s = [stm1[0],list(stm1[1]),list(stm1[2])]
    if s[0] == 0:
        # free
        s[2][0] += a[0]
        s[2][1] += a[1]
    elif s[0] == 1:
        # fixed
        pass
    elif s[0] == 2:
        # revolute
        if False:
            # old way
            x = a[0]+s[1][2]*math.cos(s[2][0])
            y = a[1]+s[1][2]*math.sin(s[2][0])
            s[2][0] = math.atan2(y,x)
        else:
            # new way
            thi = s[2][0]
            numSteps = 360
            dth = 2*math.pi/float(numSteps)
            E = []
            r = s[1][2]
            ax = a[0]
            ay = a[1]
            KxP = 100
            KyP = 400

            for i in range(numSteps):
                th = -math.pi+(i+1)*dth
                E.append(0.5*KxP*(r*((math.cos(thi)-math.cos(th))*ay\
                                     -(math.sin(thi)-math.sin(th))*ax))**2\
                         +0.5*KyP*(r*((math.cos(thi)-math.cos(th))\
                                      *ax+(math.sin(thi)-math.sin(th))*ay)\
                                   +ax*ax+ay*ay)**2)
                
            s[2][0] = -math.pi+(E.index(min(E))+1)*dth;
    elif s[0] == 3:
        # prismatic
        s[2][0] += a[0]*math.cos(s[1][2])+a[1]*math.sin(s[1][2]);

    return s

def transWbias(stm1,a,errorScale):
    s = trans(stm1,a)
    for i in range(len(s[2])):
        if s[0] == 2:
            diff = s[2][i]-stm1[2][i]
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi
            th = errorScale*diff+stm1[2][i]
            s[2][i] = th-math.floor((th+math.pi)/(2*math.pi))*2*math.pi
        else:
            s[2][i] = errorScale*(s[2][i]-stm1[2][i])+stm1[2][i]
    return s

def transWscale(stm1,a,low=0,high=1):
    s = trans(stm1,a)
    if s[0] == 3:
        # unit vector of line
        l_x = math.cos(s[1][2])
        l_y = math.sin(s[1][2])

        # unit vector of action
        a_norm = math.sqrt(a[0]**2+a[1]**2)
        a_x = a[0]/a_norm
        a_y = a[1]/a_norm

        dot = abs(l_x*a_x+l_y*a_y)
        print 'a:',a
        print 'scale:',max([(low+(high-low)*dot),0.0])
        s[2][0]=max([(low+(high-low)*dot),0.0])*(s[2][0]-stm1[2][0])+stm1[2][0]
    elif s[0] == 2:
        # unit vector of tangent line
        l_x = math.cos(stm1[2][0]+math.pi/2)
        l_y = math.sin(stm1[2][0]+math.pi/2)
        
        # unit vector of action
        a_norm = math.sqrt(a[0]**2+a[1]**2)
        a_x = a[0]/a_norm
        a_y = a[1]/a_norm

        dot = abs(l_x*a_x+l_y*a_y)

        scale = max([(low+(high-low)*dot),0.0])

        print 'a:',a
        print 'scale:',scale

        # do the regular thing (you're repeating yourself from above)
        diff = s[2][0]-stm1[2][0]
        if diff > math.pi:
            diff -= 2*math.pi
        elif diff < -math.pi:
            diff += 2*math.pi
        th = scale*diff+stm1[2][0]
        s[2][0] = th-math.floor((th+math.pi)/(2*math.pi))*2*math.pi
            
    return s

def obs(s):
    if s[0] == 0:
        o = list(s[2])
    elif s[0] == 1:
        o = list(s[1])
    elif s[0] == 2:
        o = [s[1][0]+s[1][2]*math.cos(s[2][0]),\
             s[1][1]+s[1][2]*math.sin(s[2][0])]
    elif s[0] == 3:
        o = [s[1][0]+s[2][0]*math.cos(s[1][2]),\
             s[1][1]+s[2][0]*math.sin(s[1][2])]

    return o
