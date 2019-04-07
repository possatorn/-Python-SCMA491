import numpy as np
import matplotlib.pyplot as plt
def regfit(x,y,deg):
    X=np.matrix([[xi**j for j in range(0,deg+1)] for xi in x])
    Y=np.matrix([[yi] for yi in y])
    return([coeff[0] for coeff in np.linalg.solve((X.T)*X,(X.T)*Y).tolist()])
def regval(x,a):
    return([sum([a[i]*(xi**i) for i in range(0,len(a))]) for xi in x])
def smoothcurve(minval,maxval,n):
    return([minval+(((maxval-minval)/(n-1))*i) for i in range(0,n)])
x=[1,2,4,8,8,10];y=[1.5,2.4,4.5,10,15.2,17.5]
fig, axs=plt.subplots(1,2)
ax=axs[0]
ax.plot(x,regval(x,regfit(x,y,1)),label='Regression Line')
ax.scatter(x,y,color='r',s=50,marker='o',label='Data')
ax.legend(loc='upper left')
ax.set_title('Linear Model')
ax.axis([0,11,0,20])
ax1=axs[1]
ax1.plot(x,regval(x,regfit(x,y,2)),label='Regression Line')
ax1.scatter(x,y,color='r',s=50,marker='o',label='Data')
ax1.axis([0,11,0,20])
ax1.legend(loc='upper left')
ax1.set_title('Quadratic Model')

print(smoothcurve(1,2,4))