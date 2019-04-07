nmat=2;dimmin=2;dimmax=6
def inpChecker(inpt,txt1,txt2,inmin,inmax,failed):
    f=0
    while True:
        if (f!=0):
            inpt=input(txt1)
        try:
            floatinp=float(inpt)
            if (floatinp==int(floatinp)):
                if (floatinp<inmin):
                    if (floatinp<0):
                        print(str(inpt)+' is negative. Please try again.')
                        f=f+1
                    else:
                        print(str(inpt)+' is less than '+str(inmin)+'. Please try again.')
                        f=f+1
                elif (floatinp>inmax) :
                    print(str(inpt)+' is more than '+str(inmax)+'. Please try again.')
                    f=f+1
                else:
                    return(int(inpt))
                    break
            else:
                print(txt2+' must be an integer. Please try again')
                f=f+1
        except ValueError:
            print('\''+inpt+'\' is not a number. Please try again.')
            f=f+1
        if (f==failed-1):
            print('\n** Warning: Next time, if you keep making invalid input,\n   the program will be shut down.')
        if (f==failed):
            print('\nYou made too many invalid input.\nThe program is terminated!')
            end=input('\nPress \'Enter\' to exit.')
            quit(end)
def diminput(x,dim0,dim1):
    asked=0
    while (asked<x):
        n=inpChecker(input('\nrows = '),'\nrows = ','Number of rows',dim0,dim1,11)
        m=inpChecker(input('\ncolumns = '),'\ncolumns = ','Number of columns',dim0,dim1,11)
        asked=asked+1
        print('\nYour matrices size is \''+str(n)+'x'+str(m)+'\'')
        if (asked<x):   
            print('\nIf you entered a wrong size, please input  w.')
            print('Otherwise, just press \'Enter\' to continue.')
            if (asked==(x-1)): 
                print('\n** Warning: This will be last time which you can make mistake.\n   Next time you must enter it correctly!!')
            inp=input('\nPress \'Enter\' or input  w : ')
        if inp not in ['w']:
            break
    return([n,m])
def matprint(mat):
    ncol=[]
    for c in range(0,len(mat[0])):
        maxlen=len(mat[0][c])
        for r in range(1,len(mat)):
            if len(mat[r][c])>maxlen:
                maxlen=len(mat[r][c])
        ncol.append(maxlen+4)
    for r in range(0,len(mat)):
        for c in range(0,len(mat[0])):
            space1='';space2=''
            for s in range(0,(ncol[c]-len(mat[r][c]))//2):
                space1=space1+' '
            for s in range(0,(ncol[c]-len(mat[r][c]))-(ncol[c]-len(mat[r][c]))//2):
                space2=space2+' '
            print(space1+str(mat[r][c])+space2,end='')
        print('')
def matName(num):
    eng=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if (num<=26):
        return(eng[num-1])
    else:
        return('Mat'+str(num))
def createMat(nm,rw,cl):
    i=1;MatSet=[];
    while (i<nm+1):
        print('\nNow you are creating Matrix  \''+matName(i)+'\',\nPlease input the following elements.')
        print('')
        Mat=[]
        for n in range(1,rw+1):
            row=[]
            for m in range(1,cl+1):
                inp=input(matName(i)+'('+str(n)+','+str(m)+') = ')
                row.append(inp)
            Mat.append(row)
            print('')    
        print('\nYou created the matrix\n\n'+matName(i)+' =')
        matprint(Mat)
        print('\nIf you made any wrong typing, please input  w.\nOtherwise, just press \'Enter\' to continue.')
        inp=input('\nPress \'Enter\' or input  w : ')
        if inp not in ['w']:
            MatSet.append(Mat)
            i=i+1
        else:
            print('\nTo re-create whole matrix, please input  r.\nOtherwise, to edit only some of elements just press \'Enter\'.')
            inp=input('\nPress \'Enter\' or input  r : ')
            if inp not in ['r']:
                while True:
                    print('\nPlease input index of element to be adjusted.')
                    print('**(row must be in [1 to '+str(rw)+'],\n   column must be in [1 to '+str(cl)+'])')
                    rwind=inpChecker(input('\nrow = '),'\nrow = ','Row index',1,rw,11)
                    clind=inpChecker(input('\ncolumn = '),'\ncolumn = ','Column index',1,cl,11)
                    inp=input('\n'+matName(i)+'('+str(rwind)+','+str(clind)+') = ')
                    Mat[rwind-1][clind-1]='\''+str(inp)+'\''
                    print('\nYou edited the matrix\n\n'+matName(i)+' =')
                    matprint(Mat)
                    Mat[rwind-1][clind-1]=inp
                    print('\nTo edit more elements, please input  m.\nOtherwise, just press \'Enter\' to continue.')
                    inp=input('\nPress \'Enter\' or input  m : ')
                    if inp not in ['m']:
                        MatSet.append(Mat)
                        i=i+1
                        break  
    return(MatSet)
def mul(a,b):
    try:
        result=float(a)*float(b)
        if (result==round(result)):
            result=str(int(result))
        else:
            result=str(result)
    except ValueError:
        result='('+a+')'+'('+b+')'
    return(result)
def plus(a,b):
    try:
        result=float(a)+float(b)
        if (result==round(result)):
            result=str(int(result))
        else:
            result=str(result)
    except ValueError:
        result='('+a+'+'+b+')'
    return(result)
print('Welcome to Possatorn\'s matrix calculation program.')
print('\nThis program will generate '+str(nmat)+' equal-size matrices:  ',end='')
for a in range(0,nmat):
    if (a==nmat-2):
        last=' and '
    elif (a==nmat-1):
        last=''
    else:
        last=', '
    print(matName(a+1)+last,end='')
print(',\nand will carry out some basic matrix operations.')
print('\nNow,please specify your matrices size.')
print('**(row must be in ['+str(dimmin)+' to '+str(dimmax)+'],\n   column must be in ['+str(dimmin)+' to '+str(dimmax)+'])')
dim=diminput(4,dimmin,dimmax)
Matrix=createMat(nmat,dim[0],dim[1])
Ax3=[]
for i in range(0,dim[0]):
    row=[]
    for j in range(0,dim[1]):
        row.append(mul('3',Matrix[0][i][j]))
    Ax3.append(row)
print('\n3A =')
matprint(Ax3)
Atr=[]
for j in range(0,dim[1]):
    row=[]
    for i in range(0,dim[0]):
        row.append(Matrix[0][i][j])
    Atr.append(row)
print('\nA\' =')
matprint(Atr)
Ap2B=[]
for i in range(0,dim[0]):
    row=[]
    for j in range(0,dim[1]):
        row.append(plus(Matrix[0][i][j],mul('2',Matrix[1][i][j])))
    Ap2B.append(row)
print('\nA+2B =')
matprint(Ap2B)
ABtran=[]
print('\nAxB\' =')
for i in range(0,dim[0]):
    row=[]
    for j in range(0,dim[0]):
        prod=[]
        for k in range(0,dim[1]):
            prod.append(mul(Matrix[0][i][k],Matrix[1][j][k]))
        summ=prod[0]
        for l in range(1,len(prod)):
            summ=plus(summ,prod[l])
        row.append(summ)
    ABtran.append(row)
matprint(ABtran)

