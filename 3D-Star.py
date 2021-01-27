"""
@author Francisco Grijalva
@date 11/Enero/2021
Rotate a five pointed star 3D like rotation circles 3D exercise
"""

import numpy as np
import matplotlib.pyplot as plt
#import functions tools3D
import tools3D as Tools

plt.axis([0,150,100,0])
plt.axis()
plt.grid()

#  Ejes X Y
plt.plot([8,130],[8,8],color='k')
plt.text(120,6,'X')

plt.plot([8,8],[8,85],color='k')
plt.text(4,80,'Y')

#   Definir lista de puntos
#Exterior de la estrella
x=[]
y=[]
z=[]

xg=[]
yg=[]
zg=[]

#Exterior de la estrella
xx=[]
yy=[]
zz=[]

xg2=[]
yg2=[]
zg2=[]

#   Llenar la lista de puntos
p1=np.radians(0)
p2=np.radians(360)
dp=np.radians(72)#Distancia entre punto y punto

rad=20

#Set coordenadas de los puntos del circulo
for pi in np.arange(p1,p2+dp,dp):
    xp = np.cos(pi)*rad
    yp = np.sin(pi)*rad
    zp = 0

    x.append(xp)
    y.append(yp)
    z.append(zp)

    xg.append(xp)
    yg.append(yp)
    zg.append(zp)

#       Definir funcion plot circle
def plotcircle(xg,yg,zg):
    """xglast = xg[0]
    yglast = yg[0]
    for i in range( len(x) ):
        plt.plot([xglast,xg[i]], [yglast,yg[i]], color='g')
        xglast = xg[i]
        yglast = yg[i]

        plt.scatter(xc,yc,s=5)#Plot star center
    """

    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='r')
    plt.plot([xg[2],xg[4]],[yg[2],yg[4]],color='r')
    plt.plot([xg[4],xg[1]],[yg[4],yg[1]],color='r')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='r')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='r')
    plt.scatter(xc,yc,s=5,color='g')

#Apply transform a las coordenadas and plot it
def plotCircleX(xc,yc,zc,Rx):#Calcuclar puntos de rot y plot circle
    for i in range(len(x)):
        [xg[i],yg[i],zg[i]] = Tools.rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]] = [xg[i]-xc,yg[i]-yc,zg[i]-zc]

    plotcircle(xg,yg,zg)

def plotCircleY(xc,yc,zc,Ry):#Calcuclar puntos de rot y plot circle
    for i in range(len(x)):
        [xg[i],yg[i],zg[i]] = Tools.rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]] = [xg[i]-xc,yg[i]-yc,zg[i]-zc]

    plotcircle(xg,yg,zg)

def plotCircleZ(xc,yc,zc,Rz):#Calcuclar puntos de rot y plot circle
    for i in range(len(x)):
        [xg[i],yg[i],zg[i]] = Tools.rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]] = [xg[i]-xc,yg[i]-yc,zg[i]-zc]

    plotcircle(xg,yg,zg)

Rx=np.radians(0)
xc=30
yc=50
zc=20
plotCircleX(xc,yc,zc,Rx)
plt.text(22,80,'(a)')
plt.text(20,90,'R=0')

#       Plot star b
Rx=np.radians(45)
xc=60
yc=50
zc=20
plotCircleX(xc,yc,zc,Rx)
plt.text(52,80,'(b)')
plt.text(50,90,'Rx=45')

#       Plot star c
Ry=np.radians(70)
xc=90
yc=50
zc=20
plotCircleY(xc,yc,zc,Ry)
plt.text(82,80,'(c)')
plt.text(80,90,'Ry=70')

#       Plot star d
Rz=np.radians(90)
xc=120
yc=50
zc=20
plotCircleZ(xc,yc,zc,Rz)
plt.text(112,80,'(d)')
plt.text(110,90,'Rz=90')

plt.show()
