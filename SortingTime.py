import random as rnd
import time as T
import numpy as np
import matplotlib.pyplot as pyplot

def SortOptionTime(alist,option):
    if option=='insertion':
        start=T.time()
        for index in range(1,len(alist)):
           currentvalue = alist[index]
           position = index
           while position>0 and alist[position-1]>currentvalue:
               alist[position]=alist[position-1]
               position = position-1
           alist[position]=currentvalue
        stop=T.time()
    if option=='bubble':
        start=T.time()
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        stop=T.time()
    if option=='selection':
        start=T.time()
        for fillslot in range(len(alist)-1,0,-1):
            positionOfMax=0
            for location in range(1,fillslot+1):
               if alist[location]>alist[positionOfMax]:
                   positionOfMax = location
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
        stop=T.time()
    return(stop-start)

def AverageSortingTime(alist,method,n):
    AvgTime=0
    for j in range(0,n):
        B=alist.copy()
        AvgTime=AvgTime+(SortOptionTime(B,method)*(1/n))
    return(AvgTime)

def RandomIntList(minInt,maxInt,size):
    output=[]
    for i in range(0,size):
        num=rnd.randint(minInt,maxInt)
        output.append(num)
    return(output)
    
def matrix_mul(mat1,mat2):
    mult=[]
    for i in range(0,len(mat1)):
        row=[]
        for j in range(0,len(mat2[0])):
            summ=0
            for k in range(0,len(mat1[0])):
                summ=summ+mat1[i][k]*mat2[k][j]
            row.append(summ)
        mult.append(row)
    return(mult)

def regfit(x,y,deg):
    X=np.matrix([[xi**j for j in range(0,deg+1)] for xi in x])
    Y=[[yi] for yi in y]
    XtX=np.matrix(matrix_mul(X.T.tolist(),X.tolist()))
    XtY=np.matrix(matrix_mul(X.T.tolist(),Y))
    return([a[0] for a in np.linalg.solve(XtX,XtY).tolist()])
    
def regval(x,a):
    return([sum([a[i]*(xi**i) for i in range(0,len(a))]) for xi in x])
    
def smoothcurve(minval,maxval,n):
    return([minval+(((maxval-minval)/(n-1))*i) for i in range(0,n)])

x=[i*100 for i in range(1,11)];y1=[];y2=[];y3=[]
for size in x:
    A=RandomIntList(0,100000,size)
    y1.append(AverageSortingTime(A,'bubble',20))
    y2.append(AverageSortingTime(A,'insertion',20))
    y3.append(AverageSortingTime(A,'selection',20))
pyplot.plot(smoothcurve(min(x),max(x),(max(x)-min(x))*10),regval(smoothcurve(min(x),max(x),(max(x)-min(x))*10),regfit(x,y1,2)),color='r')
pyplot.plot(smoothcurve(min(x),max(x),(max(x)-min(x))*10),regval(smoothcurve(min(x),max(x),(max(x)-min(x))*10),regfit(x,y2,2)),color='b')
pyplot.plot(smoothcurve(min(x),max(x),(max(x)-min(x))*10),regval(smoothcurve(min(x),max(x),(max(x)-min(x))*10),regfit(x,y3,2)),color='g')
pyplot.scatter(x,y1,color='r',s=50,marker='o',label='Bubble Sort')
pyplot.scatter(x,y2,color='b',s=50,marker='s',label='Insertion Sort')
pyplot.scatter(x,y3,color='g',s=80,marker='^',label='Selection Sort')
pyplot.legend(loc='upper left')
pyplot.axis([0,1100,-0.02,0.2])
pyplot.xticks([i*100 for i in range(0,11)])
pyplot.yticks([i*0.02 for i in range(0,11)])
pyplot.xlabel('Number of elements in list')
pyplot.ylabel('CPU Time used to sort')
pyplot.title('Sorting time by different sorting methods')


                
            
        

            