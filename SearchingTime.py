import random as rnd
import time as T
import numpy as np
import matplotlib.pyplot as pyplot

def BinarySearch(alist, item):
    if len(alist)==0:
        return()
    else:
        center = len(alist)//2
        if alist[center]==item:
            return()
        else:
            if item<alist[center]:
                return BinarySearch(alist[:center].item)
            else:
                return BinarySearch(alist[center+1:],item)

def SequentialSearch(Alist,item):
    for i in range(0,len(Alist)):
        if(Alist[i]==item):
            return()
        elif(Alist[i]>item):
            return()
        if(i==len(Alist)-1):
            return()
                
def SearchOptionTime(alist,item,option):
    if option=='sequential':
        start=T.time()
        SequentialSearch(alist,item)
        stop=T.time()
    if option=='binary':
        start=T.time()
        BinarySearch(alist, item)
        stop=T.time()
    return(stop-start)

def AverageSearchingTime(alist,method,n):
    AvgTime=0
    for j in range(0,n):
        B=alist.copy()
        AvgTime=AvgTime+(SearchOptionTime(B,B[len(B)-1],method)*(1/n))
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

x=[i*10000 for i in range(1,16)];y1=[];y2=[]
for size in x:
    A=RandomIntList(0,100000,size)
    A.sort()
    y1.append(AverageSearchingTime(A,'sequential',20))
    y2.append(AverageSearchingTime(A,'binary',20))
pyplot.plot([min(x),max(x)],regval([min(x),max(x)],regfit(x,y1,1)),color='r')
pyplot.plot([min(x),max(x)],regval([min(x),max(x)],regfit(x,y2,1)),color='b')
pyplot.scatter(x,y1,color='r',s=50,marker='o',label='Sequential Search')
pyplot.scatter(x,y2,color='b',s=50,marker='s',label='Binary Search')
pyplot.legend(loc='upper left')
pyplot.xlabel('Number of elements in list')
pyplot.ylabel('CPU Time used to search for the last element of list')
pyplot.title('Searching time by different searching methods')


                
            
        

            