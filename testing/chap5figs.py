from matplotlib import pyplot
import pylab
from matplotlib import colors
import numpy as np
from matplotlib.lines import Line2D

import matplotlib.colors as colors
import matplotlib.cm as cmx

################################################################################
################################################################################
################################################################################
################################################################################



first = False
if first:
    rotOffset = 0 #-np.pi/64

    thReal = -np.pi/2 + rotOffset
    rReal = 0.20
    sReal = [2,[rReal*np.cos(thReal+np.pi),rReal*np.sin(thReal+np.pi),rReal],\
             [thReal]]


    thEst = 0.0 + rotOffset
    offset = 0.4
    sEst = [3,[offset*np.cos(thEst),offset*np.sin(thEst),thEst],[-offset]]

    c1 = pyplot.Circle((sReal[1][0],sReal[1][1]),sReal[1][2],color='b',fill=False,\
                       zorder=1,lw=2)
    pyplot.gca().add_artist(c1)

    c2, = pyplot.plot([sEst[1][0],sEst[1][0]-0.8*np.cos(sEst[1][2])],\
                     [sEst[1][1],sEst[1][1]-0.8*np.sin(sEst[1][2])],color='b',\
                     zorder=1,lw=2)

    pyplot.scatter(0,0,s=150,c='g',edgecolor='k',zorder=2,lw=2,label='Start Point') # start state

    #rev end point
    endTh = -np.pi/4-.22
    pyplot.scatter(sReal[1][2]*np.cos(endTh)+sReal[1][0],\
                   sReal[1][2]*np.sin(endTh)+sReal[1][1],\
                   s=150,c='r',edgecolor='k',zorder=2,lw=2,label='End Point')

    pyplot.scatter(0.1125,0.02,s=150,c='m',edgecolor='k',zorder=2,lw=2,label='Observation') # observation

    aTh = 0.1
    a = [0.12*np.cos(aTh),0.12*np.sin(aTh)]
    pyplot.arrow(0,0,a[0],a[1],\
                 fc='k',ec='k',length_includes_head=True, \
                 width=0.0001,head_width=0.004,head_length=0.008)

    # end pris point
    pyplot.scatter(0.12*np.cos(aTh),0.0,\
                   s=150,c='r',edgecolor='k',zorder=2,lw=2)

    #pyplot.annotate('Prismatic', xy=(0.06, 0.0), xytext=(0.03, -0.015),\
    #            arrowprops=dict(arrowstyle="->",facecolor='black'))

    pyplot.annotate('Prismatic',xy=(0.13,-0.007),fontweight=1000,fontsize=14)
    pyplot.annotate('Revolute',xy=(0.125,0.0725),fontweight=1000,fontsize=14)

    pyplot.xlim([-0.02,0.16])
    pyplot.ylim([-0.02,0.08])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.legend(loc=2,scatterpoints=1)
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/modelQualityGood.pdf",bbox_inches='tight')
    pyplot.show()


################################################################################
################################################################################
################################################################################
################################################################################


second = False
if second:
    rotOffset = 0 #-np.pi/64

    thReal = -np.pi/2 + rotOffset
    rReal = 0.20
    sReal = [2,[rReal*np.cos(thReal+np.pi),rReal*np.sin(thReal+np.pi),rReal],\
             [thReal]]


    thEst = 0.0 + rotOffset
    offset = 0.4
    sEst = [3,[offset*np.cos(thEst),offset*np.sin(thEst),thEst],[-offset]]

    c1 = pyplot.Circle((sReal[1][0],sReal[1][1]),sReal[1][2],color='b',fill=False,\
                       zorder=1,lw=2)
    pyplot.gca().add_artist(c1)

    c2, = pyplot.plot([sEst[1][0],sEst[1][0]-0.8*np.cos(sEst[1][2])],\
                     [sEst[1][1],sEst[1][1]-0.8*np.sin(sEst[1][2])],color='b',\
                     zorder=1,lw=2)

    pyplot.scatter(0,0,s=150,c='g',edgecolor='k',zorder=2,lw=2,label='Start Point') # start state

    #rev end point
    endTh = -np.pi/4
    pyplot.scatter(sReal[1][2]*np.cos(endTh)+sReal[1][0],\
                   sReal[1][2]*np.sin(endTh)+sReal[1][1],\
                   s=150,c='r',edgecolor='k',zorder=2,lw=2,label='End Point')

    pyplot.scatter(0.1125,0.02,s=150,c='m',edgecolor='k',zorder=2,lw=2,label='Observation') # observation

    aTh = 0.1
    a = [0.12*np.cos(aTh),0.12*np.sin(aTh)]
    pyplot.arrow(0,0,a[0],a[1],\
                 fc='k',ec='k',length_includes_head=True, \
                 width=0.0001,head_width=0.004,head_length=0.008)

    # end pris point
    pyplot.scatter(0.11*np.cos(aTh),0.0,\
                   s=150,c='r',edgecolor='k',zorder=2,lw=2)

    #pyplot.annotate('Prismatic', xy=(0.06, 0.0), xytext=(0.03, -0.015),\
    #            arrowprops=dict(arrowstyle="->",facecolor='black'))

    pyplot.annotate('Prismatic',xy=(0.13,-0.007),fontweight=1000,fontsize=14)
    pyplot.annotate('Revolute',xy=(0.125,0.0725),fontweight=1000,fontsize=14)

    pyplot.xlim([-0.02,0.16])
    pyplot.ylim([-0.02,0.08])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.legend(loc=2,scatterpoints=1)
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/modelQualityBad.pdf",bbox_inches='tight')
    pyplot.show()

################################################################################
################################################################################
################################################################################
################################################################################



third = False
if third:
    # show absolute actions

    # workspace
    pyplot.plot([-0.15,0.15],[0.15,0.15],'k--',lw=2)
    pyplot.plot([-0.15,0.15],[-0.15,-0.15],'k--',lw=2)
    pyplot.plot([0.15,0.15],[-0.15,0.15],'k--',lw=2)
    pyplot.plot([-0.15,-0.15],[-0.15,0.15],'k--',lw=2)

    # actions
    pts = [-0.12,0.0,0.12]
    xs = list(pts)
    xs.extend(pts)
    xs.extend(pts)
    print xs
    ys = [pts[0]]*3
    ys.extend([pts[1]]*3)
    ys.extend([pts[2]]*3)
    print ys
    pyplot.scatter(xs,ys,s=150,c='k',edgecolor='r',lw=2,label='End Point')


    pyplot.xlim([-0.20,0.20])
    pyplot.ylim([-0.20,0.20])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.legend(loc='lower center',scatterpoints=1)
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/absActionFigure.pdf",bbox_inches='tight')
    pyplot.show()



################################################################################
################################################################################
################################################################################
################################################################################


fourth = False
if fourth:
    cm = pyplot.get_cmap('jet')
    valMax = 0.3
    cNorm  = colors.Normalize(vmin=0, vmax=valMax)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    # Occam's Razor Figure
    #o = [0.5,0.485] # far
    o = [0.1,0.1] # near
    sString = 'near'
    r = 0.5
    
    # setup your distribution
    x = np.arange(-1,1.01,.01)
    y = np.arange(-1,1.01,.01)
    xx,yy = np.meshgrid(x,y)
    positions = np.vstack([xx.ravel(), yy.ravel()])
    #xy = zip(positions[0],positions[1])
    numPoints = len(positions[0])
    print numPoints
    probs = [1.0/numPoints]*numPoints

    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)
    H,xedges,yedges = np.histogram2d(positions[0],positions[1],\
                                     bins=b,weights=probs)
    print max(H[0])
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()
    
    # plot observation
    c1 = pyplot.Circle((o[0],o[1]),r,color='r',fill=False,\
                       zorder=1,lw=2)
    pyplot.gca().add_artist(c1)

    #pyplot.scatter(o[0],o[1],s=100,c='k',edgecolor='m',zorder=2,lw=4,label='Observation') # observation
    
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel(r'$\theta_1$ [m]')
    pyplot.ylabel(r'$\theta_2$ [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim0"+sString+".pdf",bbox_inches='tight')
    pyplot.show()


    # plot prismatic model
    fig1 = pyplot.figure(facecolor='white')
    ax1 = pyplot.axes(frameon=False)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.get_xaxis().tick_bottom()
    
    colorVal = scalarMap.to_rgba(0.063*2)
    pyplot.plot([-1.0,1.0],[0.0,0.0],lw=2,c=colorVal)

    highR = [-np.sqrt(r**2-o[1]**2)+o[0],np.sqrt(r**2-o[1]**2)+o[0]]
    pyplot.plot(highR,[0.0,0.0],lw=4,c='r')

    xmin, xmax = ax1.get_xaxis().get_view_interval()
    ymin, ymax = ax1.get_yaxis().get_view_interval()
    ax1.add_artist(Line2D((xmin, xmax), (ymin, ymin), color='black', linewidth=2))

    #pyplot.colorbar()
    
    pyplot.xlabel(r'$\theta_3$ [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim1"+sString+".pdf",bbox_inches='tight')
    pyplot.show()

    # plot free in observation space
    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)
    H,xedges,yedges = np.histogram2d(positions[0],positions[1],\
                                     bins=b,weights=probs)
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()
    
    # plot observation
    c1 = pyplot.Circle((o[0],o[1]),r,color='r',fill=False,\
                       zorder=1,lw=2)
    pyplot.gca().add_artist(c1)

    pyplot.scatter(o[0],o[1],s=100,c='m',edgecolor='m',zorder=2,lw=4,label='Observation') # observation
    
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim2"+sString+".pdf",bbox_inches='tight')
    pyplot.show()

    # plot prismatic model in observation space
    colorVal = scalarMap.to_rgba(0.063*2)
    pyplot.plot([-1.0,1.0],[0.0,0.0],lw=2,zorder=1,c=colorVal)


    # plot observation
    c1 = pyplot.Circle((o[0],o[1]),r,color='r',fill=False,\
                       zorder=2,lw=2)
    pyplot.gca().add_artist(c1)

    pyplot.scatter(o[0],o[1],s=100,c='m',edgecolor='m',zorder=2,lw=4,label='Observation') # observation


    #pyplot.colorbar()

    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim3"+sString+".pdf",bbox_inches='tight')
    pyplot.show()



################################################################################
################################################################################
################################################################################
################################################################################


fourth2 = False
plotObs = True
if fourth2:
    cC = 'k' # circle color
    cm = pyplot.get_cmap('jet')
    valMax = 0.3
    cNorm  = colors.Normalize(vmin=0, vmax=valMax)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    # Occam's Razor Figure
    #o = [0.5,0.485] # far
    o = [0.1,0.1] # near
    sString = 'near'
    r = 0.5
    
    # setup your distribution
    x = np.linspace(-1,1,200)
    y = np.linspace(-1,1,200)
    xx,yy = np.meshgrid(x,y)
    positions = np.vstack([xx.ravel(), yy.ravel()])
    #xy = zip(positions[0],positions[1])
    numPoints = len(positions[0])
    print numPoints
    probs = [1.0/numPoints]*numPoints


    #setup prismatic distribution
    probsP = [1.0/numPoints]*numPoints
    xP = np.linspace(-1,1,numPoints)
    yP = np.linspace(0,0,numPoints)

    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)
    H,xedges,yedges = np.histogram2d(positions[0],positions[1],\
                                     bins=b,weights=probs)
    print max(H[0])
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()

    if plotObs:
        # plot observation
        c1 = pyplot.Circle((o[0],o[1]),r,color=cC,fill=False,\
                           zorder=1,lw=2)
        pyplot.gca().add_artist(c1)

    #pyplot.scatter(o[0],o[1],s=100,c='k',edgecolor='m',zorder=2,lw=4,label='Observation') # observation
    
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel(r'$\theta_1$ [m]')
    pyplot.ylabel(r'$\theta_2$ [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim0"+sString+".pdf",bbox_inches='tight')
    pyplot.show()


    # plot prismatic model
    fig1 = pyplot.figure(facecolor='white')
    ax1 = pyplot.axes(frameon=False)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.get_xaxis().tick_bottom()


    # plot thin histogram
    b = [np.arange(-1,1.5,.5),np.linspace(-.01,0.01,2)]
    H,xedges,yedges = np.histogram2d(xP,yP,\
                                     bins=b,weights=probsP)
    print max(H[0])
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()
    
    #colorVal = scalarMap.to_rgba(0.063*2)
    #pyplot.plot([-1.0,1.0],[0.0,0.0],lw=2,c=colorVal)

    if plotObs:
        highR = [-np.sqrt(r**2-o[1]**2)+o[0],np.sqrt(r**2-o[1]**2)+o[0]]
        pyplot.plot(highR,[0.0,0.0],lw=6,c=cC)


    pyplot.xlim([-1,1])
    pyplot.ylim([-.04,.04])
    pyplot.gca().set_aspect('equal')

    xmin, xmax = ax1.get_xaxis().get_view_interval()
    ymin, ymax = ax1.get_yaxis().get_view_interval()
    ax1.add_artist(Line2D((xmin, xmax), (ymin, ymin), color='black', linewidth=2))

    #pyplot.colorbar()
    pyplot.xlabel(r'$\theta_3$ [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim1"+sString+".pdf",bbox_inches='tight')
    pyplot.show()

    # plot free in observation space
    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)
    H,xedges,yedges = np.histogram2d(positions[0],positions[1],\
                                     bins=b,weights=probs)
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()

    if plotObs:
        # plot observation
        c1 = pyplot.Circle((o[0],o[1]),r,color=cC,fill=False,\
                           zorder=1,lw=2)
        pyplot.gca().add_artist(c1)

        pyplot.scatter(o[0],o[1],s=200,c='m',edgecolor='k',zorder=2,lw=2,label='Observation') # observation
    
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim2"+sString+".pdf",bbox_inches='tight')
    pyplot.show()

    # plot prismatic model in observation space

    # plot thin histogram
    b = [np.arange(-1,1.5,.5),np.linspace(-.01,0.01,2)]
    H,xedges,yedges = np.histogram2d(xP,yP,\
                                     bins=b,weights=probsP)
    print max(H[0])
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()
    
    #colorVal = scalarMap.to_rgba(0.063*2)
    #pyplot.plot([-1.0,1.0],[0.0,0.0],lw=2,zorder=1,c=colorVal)

    if plotObs:
        # plot observation
        c1 = pyplot.Circle((o[0],o[1]),r,color=cC,fill=False,\
                           zorder=2,lw=2)
        pyplot.gca().add_artist(c1)
        
        pyplot.scatter(o[0],o[1],s=200,c='m',edgecolor='k',zorder=2,lw=2,label='Observation') # observation


    #pyplot.colorbar()

    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/dim3"+sString+".pdf",bbox_inches='tight')
    pyplot.show()




################################################################################
################################################################################
################################################################################
################################################################################



fifth = True
plotObs = True
if fifth:
    cC = 'k' # circle color
    cm = pyplot.get_cmap('jet')
    valMax = 0.3
    cNorm  = colors.Normalize(vmin=0, vmax=valMax)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    
    # Projection Figure
    o = [0.75,0.75] # far
    #o = [0.1,0.1] # near
    sString = 'far'
    r = 0.5
    
    # setup your distribution
    x = np.linspace(-1,1,200)
    y = np.linspace(-1,1,200)
    xx,yy = np.meshgrid(x,y)
    positions = np.vstack([xx.ravel(), yy.ravel()])
    #xy = zip(positions[0],positions[1])
    numPoints = len(positions[0])
    print numPoints
    probs = [1.0/numPoints]*numPoints

    # plot free model normal
    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)

    H,xedges,yedges = np.histogram2d(positions[0],positions[1],\
                                     bins=b,weights=probs)
    print max(H[0])
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=.3,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()

    if plotObs:
        # plot observation
        c1 = pyplot.Circle((o[0],o[1]),r,color=cC,fill=False,\
                           zorder=1,lw=2)
        pyplot.gca().add_artist(c1)
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel(r'$\theta_1$ [m]')
    pyplot.ylabel(r'$\theta_2$ [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/proj0"+sString+".pdf",bbox_inches='tight')
    pyplot.show()


    # plot free compress model
    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)

    H,xedges,yedges = np.histogram2d(positions[0],positions[1],\
                                     bins=b,weights=probs)
    print max(H[0])
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()

    if plotObs:
        # plot observation
        c1 = pyplot.Circle((2*o[0],2*o[1]),2*r,color=cC,fill=False,\
                           zorder=1,lw=2)
        pyplot.gca().add_artist(c1)
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel(r'$\theta_3$ [m]')
    pyplot.ylabel(r'$\theta_4$ [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/proj1"+sString+".pdf",bbox_inches='tight')
    pyplot.show()



    # plot free in observation space
    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)

    H,xedges,yedges = np.histogram2d(positions[0],positions[1],\
                                     bins=b,weights=probs)
    pyplot.imshow(H.T,interpolation='None',
                  extent=[xedges[0],\
                          xedges[-1],\
                          yedges[0],\
                          yedges[-1]],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()

    if plotObs:
        # plot observation
        c1 = pyplot.Circle((o[0],o[1]),r,color=cC,fill=False,\
                           zorder=1,lw=2)
        pyplot.gca().add_artist(c1)
        
        pyplot.scatter(o[0],o[1],s=200,c='m',edgecolor='k',zorder=2,lw=2,label='Observation') # observation
    
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/proj2"+sString+".pdf",bbox_inches='tight')
    pyplot.show()

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # plot free compress model in observation space
    # plot histogram
    b = 201
    b = np.arange(-1,1.5,.5)
    H,xedges,yedges = np.histogram2d(0.5*positions[0],0.5*positions[1],\
                                     bins=b,weights=probs)
    pyplot.imshow(H.T,interpolation='None',
                  extent=[-1,\
                          1,\
                          -1,\
                          1],\
                  vmin=0,vmax=valMax,origin='lower',cmap=cm,norm=cNorm)
    #pyplot.colorbar()

    if plotObs:
        # plot observation
        c1 = pyplot.Circle((o[0],o[1]),r,color=cC,fill=False,\
                           zorder=1,lw=2)
        pyplot.gca().add_artist(c1)
        
        pyplot.scatter(o[0],o[1],s=200,c='m',edgecolor='k',zorder=2,lw=2,label='Observation') # observation
    
    
    pyplot.xlim([-1.0,1.0])
    pyplot.ylim([-1.0,1.0])
    pyplot.gca().set_aspect('equal')
    pyplot.xlabel('x [m]')
    pyplot.ylabel('y [m]')
    pyplot.savefig("/mit/barragan/Public/LIS/thesisFigures/proj3"+sString+".pdf",bbox_inches='tight')
    pyplot.show()

