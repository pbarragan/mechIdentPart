from matplotlib import pyplot
from math import cos,sin,pi

l = 0.05
w = 0.038


As=[]
Os=[]
ps=[]
vs=[]
As.append([0,0])
Os.append([0,0])
ps.append([0.0511874,-0.295601,0.19,1.74226,0.11])
vs.append([1.66641,0.060721])

for i,(a,o,p,v) in enumerate(zip(As,Os,ps,vs)):

    backCenter=[p[0]+(p[2]+p[4])*cos(p[3]),p[1]+(p[2]+p[4])*sin(p[3])]

    frontCenter=[backCenter[0]+l*cos(p[3]+pi),backCenter[1]+l*sin(p[3]+pi)]
  
    backLeft=[backCenter[0]+(w/2)*cos(p[3]+pi/2),\
              backCenter[1]+(w/2)*sin(p[3]+pi/2)]
    
    backRight=[backCenter[0]-(w/2)*cos(p[3]+pi/2),\
               backCenter[1]-(w/2)*sin(p[3]+pi/2)]

    frontLeft=[backLeft[0]+l*cos(p[3]+pi),backLeft[1]+l*sin(p[3]+pi)]

    frontRight=[backRight[0]+l*cos(p[3]+pi),backRight[1]+l*sin(p[3]+pi)]

    # draw latch
    pts = [backLeft,backRight]
    x,y = zip(*pts)
    pyplot.plot(x,y,'-or')

    pts = [backLeft,frontLeft]
    x,y = zip(*pts)
    pyplot.plot(x,y,'-or')

    pts = [backRight,frontRight]
    x,y = zip(*pts)
    pyplot.plot(x,y,'-or')


    xH = p[0]+(p[2]+v[1])*cos(v[0])
    yH = p[1]+(p[2]+v[1])*sin(v[0])
    pyplot.plot(xH,yH,'sk')

    xS = p[0]+(p[2])*cos(v[0])
    yS = p[1]+(p[2])*sin(v[0])
    
    pts = [[p[0],p[1]],[xS,yS]]
    x,y = zip(*pts)
    pyplot.plot(x,y,'-og')

    pts = [[xS,yS],[xH,yH]]
    x,y = zip(*pts)
    pyplot.plot(x,y,'-ob')
    pyplot.annotate(i,(xH,yH),size='x-large',color='b')


    if(i>0):
        # show action
        x = ps[i-1][0]+(ps[i-1][2]+vs[i-1][1])*cos(vs[i-1][0])+a[0]
        y = ps[i-1][1]+(ps[i-1][2]+vs[i-1][1])*sin(vs[i-1][0])+a[1]
        pyplot.plot(x,y,'xg',markersize=50)
        pyplot.annotate(i,(x,y),size='x-large',color='g')
        
        # show obs
        pyplot.plot(o[0],o[1],'ok',markersize=10)
        pyplot.annotate(i,(o[0],o[1]),size='x-large',color='k')
        
pyplot.axis('equal')
pyplot.show()
