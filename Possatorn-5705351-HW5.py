def tupl(Alist):
    Tpl=()
    for element in Alist:
        Tpl=Tpl+(element,)
    return(Tpl)
def inpCheck(txt,x,inptxt,status):
    if x in [0,1,2,3,4,5,6,7]:
        if (txt in ['res','q','h','exrec']):
            return(txt)
        if (x==2):
            if (txt in ['A','a','Audit','audit']):
                txt='A'
            else:
                txt='N'
        elif (x==3):
            try:
                fltxt=float(txt)
                if (fltxt<=0):
                    print('Credit must be more than 0.')
                    txt=inpCheck(input(inptxt),x,inptxt,status)
            except ValueError:
                print('Credit must be anumber.')
                txt=inpCheck(input(inptxt),x,inptxt,status)
        else:
            if (x==4):
                if (status!='A'):
                    gradedict={'A':'4.00','B+':'3.50','B':'3.00','C+':'2.50','C':'2.00','D+':'1.50','D':'1.00','F':'0','W':'W','a':'4.00','b+':'3.50','b':'3.00','c+':'2.50','c':'2.00','d+':'1.50','d':'1.00','f':'0','w':'W'}
                    gradeset={4:'4.00',3.5:'3.50',3:'3.00',2.5:'2.50',2:'2.00',1.5:'1.50',1:'1.00',0:'0'}
                    try:
                        fltxt=float(txt)
                        if (fltxt not in gradeset):
                            print('Grade \''+txt+'\' is not in standard grade system.')
                            txt=inpCheck(input(inptxt),x,inptxt,status)
                        else:
                            txt=gradeset[fltxt]
                    except ValueError:
                        if (txt not in gradedict):
                            print('Grade \''+txt+'\' is not in standard grade system.')
                            txt=inpCheck(input(inptxt),x,inptxt,status)
                        else:
                            txt=gradedict[txt]
                else:
                    gradeset={'S':'S','U':'U','s':'S','u':'U'}
                    if (txt not in gradeset):
                        print('Grade for \'Audit\' subject can only be\n S = Sastisfactory\n U = Unsastisfactory')
                        txt=inpCheck(input(inptxt),x,inptxt,status)
                    else:
                        txt=gradeset[txt]
        return(txt)
    else:
        while True:
            print('\'x\' is not in [0,1,2,3,4,5,6,7]')
            x=input('Please change x : ')
            if (x in ['0','1','2','3','4','5','6','7']):
                x=int(x)
                break
        txt=inpCheck(txt,x,inptxt,status)
        return(txt)
def qinput(txt,x,inptxt,status):
    if (txt=='q'):
        quit()
    elif (txt=='h'):
        if (x==0):
            print('\n --- Help message opened. --- \n\nPlease input a subject code here, for ex. SCMAxxx .')
            print('Or you can make the follwing inputs. -->  q = to quit program')
            print('                                        res = to restart program')
        elif (x==1):
            print('\n --- Help message opened. --- \n\nPlease input a subject\'s name here, for ex. Computer Programing in Python .')
            print('Or you can make the follwing inputs. -->  q = to quit program')
            print('                                        res = to restart program')
        elif (x==3):
            print('\n --- Help message opened. --- \n\nPlease input a number of credit(s) of the subject, for ex. 3 .')
            print('Or you can make the follwing inputs. -->  q = to quit program')
            print('                                        res = to restart program')
        elif (x==4):
            print('\n --- Help message opened. --- \n\nPlease input a grade of the subject, for ex.  4 , 3.5 , 3 ,...')
            print('                                     or in text as   A ,B+ ,B ,C+ ...')
            print('                                     or the followings :  W = Withdrawn')
            print('                                                          I = ...')
            print('Or you can make the follwing inputs. -->  q = to quit program')
            print('                                        res = to restart program')
        elif (x==7):
            print('\n --- Help message opened. --- ')
            print('\nPlease make only the follwing inputs. -->  y = yes   |   q = to quit program')
            print('                                           n = no    |   res = to restart program')
            print('If you make other inputs than these,\nthe program will keep asking you again and again. ^^')
        else:
            print('\n --- Help message opened. --- \n\n(Help is not available yet.)')
            print('\n')
        txt=qinput(inpCheck(input(inptxt),x,inptxt,status),x,inptxt,status)
        return(txt)
    else:
        return(txt)
def print_table(rec,printline,Head,nrow,ncol):
    longest=[];Headwid=[]
    for title in Head:
        Headwid.append(len(title)+4)
    for c in range(0,ncol):
        maxlen=len(rec[0][c])
        for r in range(1,nrow):
            if len(rec[r][c])>maxlen:
                maxlen=len(rec[r][c])
        longest.append(maxlen+4)
    for i in range(0,len(longest)):
        if (Headwid[i]>longest[i]):
            longest[i]=Headwid[i]
    if (printline==True):
        wid=0
        for maxlen in longest:
            wid=wid+maxlen
        lin='-'*wid
    for r in range(0,3):
        if (r==1):
            for c in range(0,ncol):
                if (c!=1):
                    nsp1=(longest[c]-len(Head[c]))//2
                    space1=' '*nsp1
                    nsp2=(longest[c]-len(Head[c]))-(longest[c]-len(Head[c]))//2
                    space2=' '*nsp2
                if (c==1):
                    inden=' '*(longest[c]-(len(Head[c])+2))
                    print('  '+Head[c]+inden,end='')
                else:
                    print(space1+Head[c]+space2,end='')
            print()
        else:
            if (printline==True):
                print(lin)
    for r in range(0,nrow):
        for c in range(0,ncol):
            if (c>1):
                nsp1=(longest[c]-len(rec[r][c]))//2
                space1=' '*nsp1
                nsp2=(longest[c]-len(rec[r][c]))-(longest[c]-len(rec[r][c]))//2
                space2=' '*nsp2
            if (c==0):
                inden=' '*(longest[c]-(len(rec[r][c])+2))
                print('  '+rec[r][c]+inden,end='')
            elif (c==1):
                inden=' '*(longest[c]-(len(rec[r][c])+2))
                print('  '+rec[r][c]+inden,end='')
            else:
                print(space1+rec[r][c]+space2,end='')
        print()
    if (printline==True):        
        print(lin)
def recordSubject(rec,strt):
    rec=rec;i=strt;j=1;ans='y'
    editopt=['1','2','3','4','5','r','e'];espace=['1','2','3','4','5'];editmsg='1, 2, 3, 4, 5, r, or  e'
    question=['Subject code : ','Subject\'s name : ','Register status : ','Credit : ','Grade : ']
    while (ans=='y'):
        while True:
            if (i==1):
                print('\nRecord '+str(i)+' information.',end='')
                if (j==1):
                    print('  (Input  h  for help at any point.)')
                else:
                    print()
            else:
                print('\nRecord '+str(i)+' information.')
            subject=[]
            n=0;
            while (n < len(question)):
                cont=True
                if (n==3):
                    if (subject[2]=='A'):
                        ans='-'
                    else:
                        ans=qinput(inpCheck(input(question[n]),n,question[n],''),n,question[n],'')
                elif (n==4):
                        ans=qinput(inpCheck(input(question[n]),n,question[n],subject[2]),n,question[n],subject[2])
                else:
                    ans=qinput(inpCheck(input(question[n]),n,question[n],''),n,question[n],'')
                if ((ans)=='exrec'):
                        if (i>1):
                            return(rec)
                        else:
                            print('Nothing is record yet. Cannot exit.')
                            cont=False
                if (ans=='res'):
                    return(ans)
                else:
                    if (ans!=''):
                        if (ans[0]=='='):
                            newans=''
                            for l in range(1,len(ans)):
                                newans=newans+ans[l]
                            ans=newans
                    if (cont!=False):
                        subject.append(ans)
                        n=n+1
            print('\nRecord '+str(i)+' is')
            print()
            Heading=('Code:','Subject Name:','Reg. status:','Credit:','Grade:')
            print_table([subject],False,Heading,1,len(subject))
            print('\nIf you made any wrong typing. Please input  w.\nOtherwise, just press \'Enter\'.')
            ans=qinput(input('< w  or \'Enter\' > : '),5,'\n< w  or \'Enter\' > : ','')
            if (ans=='exrec'):
                rec.append(subject)
                return(rec)
            if (ans=='res'):
                return(ans)
            if (ans=='w'):
                while True:
                    ans3='';ans4=''
                    print('\nPlease select which of Record '+str(i)+' to be edit.')
                    editdef='\n 1 = Subject code |  2 = Subject\'s name |  3 = Register status\n 4 = Credit       |  5 = Grade\n r = re-enter Record '+str(i)+'     e = exit this editor'
                    print(editdef)
                    ans=qinput(input('\n< '+editmsg+' > : '),6,'\n< '+editmsg+' > : ','')
                    if (ans=='exrec'):
                        rec.append(subject)
                        return(rec)
                    if (ans=='res'):
                        return(ans)
                    if (ans in editopt):
                        if (ans in espace):
                            print()
                            Update=True
                            if (int(ans)-1==2):
                                oldstat=subject[2]
                                if (subject[int(ans)-1]=='A'):
                                    ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],''),int(ans)-1,question[int(ans)-1],'')
                                    if (ans2=='N'):
                                        ans3=qinput(inpCheck(input(question[3]),3,question[3],''),3,question[3],'')
                                        ans4=qinput(inpCheck(input(question[4]),4,question[4],ans2),4,question[4],ans2)
                                else:
                                    ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],''),int(ans)-1,question[int(ans)-1],'')
                                    if (ans2=='A'):
                                        ans3='-'
                                        ans4=qinput(inpCheck(input(question[4]),4,question[4],ans2),4,question[4],ans2)
                            elif (int(ans)-1==3):
                                if (subject[2]=='A'):
                                    ans2=subject[3]
                                    print('\nCredit cannot be edit because the register status is \'Audit\'.')
                                    Update=False
                                else:
                                    ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],''),int(ans)-1,question[int(ans)-1],'')
                            else:
                                ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],subject[2]),int(ans)-1,question[int(ans)-1],subject[2])
                            if (ans2=='exrec' or ans3=='exrec' or ans4=='exrec'):
                                rec.append(subject)
                                return(rec)
                            if (ans2=='res' or ans3=='res' or ans4=='res'):
                                return('res')
                            else:
                                if (ans2!='' and ans2[0]=='='):
                                    newans=''
                                    for l in range(1,len(ans2)):
                                        newans=newans+ans2[l]
                                    ans2=newans
                            subject[int(ans)-1]=ans2
                            if (int(ans)-1==2):
                                if (ans2!=oldstat):
                                    subject[3]=ans3;subject[4]=ans4
                            if (Update==True):
                                print('\nRecord '+str(i)+' was edited.')
                                print()
                                Heading=('Code:','Subject Name:','Reg. status:','Credit:','Grade:')
                                print_table([subject],False,Heading,1,len(subject))
                                print()
                            while True:
                                ans=qinput(input('\nFinish editing Record '+str(i)+' ?? (y/n) : '),7,'\nFinish editing Record '+str(i)+' ?? (y/n) : ','')
                                if (ans=='res'):
                                    return(ans)
                                if (ans in ['y','n','exrec']):
                                    break
                                else:
                                    print('Input is invalid!')
                            if (ans=='y' or ans=='exrec'):
                                break
                        else:
                            break
                    else:
                        print('\nInput is invalid!')
                if (ans=='y' or ans=='e' or ans=='exrec'):
                    rec.append(subject)
                    if (ans=='exrec'):
                        return(rec)
                    break
                else:
                    j=j+1
            else:
                rec.append(subject)
                break
        while True:
            ans=qinput(input('\nDo you want to input more record? (y/n) : '),7,'\nDo you want to input more record? (y/n) : ','')
            if (ans in ['y','n','exrec']):
                if (ans=='y'):
                    i=i+1
                    break
                else:
                    break
            else:
                if (ans=='res'):
                    return(ans)
                else:    
                    print('Input is invalid!')
    return(rec)
def GPAcal(rec,statindx,creditindx,gradeindx):
    GPA1=0;GPA2=0
    for subject in record:
        if (subject[statindx]!='A' or subject[statindx]!='a' or subject[statindx]!='Audit' or subject[statindx]!='audit'):
            try:
                GPA1=GPA1+(float(subject[creditindx])*float(subject[gradeindx]))
                GPA2=GPA2+float(subject[creditindx])
            except ValueError:
                GPA1=GPA1
                GPA2=GPA2
    try:
        result=GPA1/GPA2
    except ZeroDivisionError:
        return('N/A')
    return('%.2f'%result)
def editrec(rec):
    if (len(rec)>1):
        while True:
            code=input('\nPlease enter the code of subject to be edit : ')
            if (code in [subj[0] for subj in rec]):
                for t in range(0,len(rec)):
                    if (code==rec[t][0]):
                        i=t
                        break
                break
            else:
                print('\''+code+'\' is not found.')
    else:
        code=rec[0][0];i=0
    editopt=['1','2','3','4','5','e'];espace=['1','2','3','4','5'];editmsg='1, 2, 3, 4, 5, or  e'
    editdef='\n 1 = Subject code |  2 = Subject\'s name |  3 = Register status\n 4 = Credit       |  5 = Grade\n e = exit this editor'
    question=['Subject code : ','Subject\'s name : ','Register status : ','Credit : ','Grade : ']    
    while True:
        ans3='';ans4=''
        print('\nPlease select which of '+code+' to be edit.')
        print(editdef)
        ans=qinput(input('\n< '+editmsg+' > : '),6,'\n< '+editmsg+' > : ','')
        if (ans=='exrec'):
            return(rec)
        if (ans=='res'):
            return(ans)
        if (ans in editopt):
            if (ans in espace):
                print()
                Update=True
                if (int(ans)-1==2):
                    oldstat=rec[i][2]
                    if (rec[i][int(ans)-1]=='A'):
                        ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],''),int(ans)-1,question[int(ans)-1],'')
                        if (ans2=='N'):
                            ans3=qinput(inpCheck(input(question[3]),3,question[3],''),3,question[3],'')
                            ans4=qinput(inpCheck(input(question[4]),4,question[4],ans2),4,question[4],ans2)
                    else:
                        ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],''),int(ans)-1,question[int(ans)-1],'')
                        if (ans2=='A'):
                            ans3='-'
                            ans4=qinput(inpCheck(input(question[4]),4,question[4],ans2),4,question[4],ans2)
                elif (int(ans)-1==3):
                    if (rec[i][2]=='A'):
                        ans2=rec[i][3]
                        print('\nCredit cannot be edit because the register status is \'Audit\'.')
                        Update=False
                    else:
                        ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],''),int(ans)-1,question[int(ans)-1],'')
                else:
                    ans2=qinput(inpCheck(input(question[int(ans)-1]),int(ans)-1,question[int(ans)-1],rec[i][2]),int(ans)-1,question[int(ans)-1],rec[i][2])
                if (ans2=='exrec' or ans3=='exrec' or ans4=='exrec'):
                    return(rec)
                if (ans2=='res' or ans3=='res' or ans4=='res'):
                    return('res')
                else:
                    if (ans2!='' and ans2[0]=='='):
                        newans=''
                        for l in range(1,len(ans2)):
                            newans=newans+ans2[l]
                        ans2=newans
                rec[i][int(ans)-1]=ans2
                if (int(ans)-1==2):
                    if (ans2!=oldstat):
                        rec[i][3]=ans3;rec[i][4]=ans4
                if (Update==True):
                    print('\n'+code+' was edited.')
                    print()
                    Heading=('Code:','Subject Name:','Reg. status:','Credit:','Grade:')
                    print_table([rec[i]],False,Heading,1,len(rec[i]))
                while True:
                    ans=qinput(input('\nFinish editing '+code+' ?? (y/n) : '),7,'\nFinish editing Record '+str(i)+' ?? (y/n) : ','')
                    if (ans=='res'):
                        return(ans)
                    if (ans in ['y','n','exrec']):
                        break
                    else:
                        print('Input is invalid!')
                if (ans=='y' or ans=='exrec'):
                    break
            else:
                break
        else:
            print('\nInput is invalid!')
    return(rec)
record='';inp=''
while True:
    if (record=='res' or inp=='res'):
        print('\n---------------------------------\n\n The program has been restarted. \n\n---------------------------------')
    print('\n  ++++  Welcome to Python Grade Report & GPA calaulator.  ++++  ')
    print('\n       This program will let you input the subject records,\n         then print a grade report and calculate the GPA.')
    print('\n\nPlease follow the on-screen instruction.')
    while True:
        print('\nPlease select input option.\ni = import from data file    m = create record manually')
        inp=input('< i / m > : ')
        if (inp in ['i','m']):    
            if (inp=='m'):
                record=recordSubject([],1)
                break
            else:
                inp=input('Please input file name : ')
                with open(inp,'r') as fil:
                    fil.seek(0,0)
                    subject=fil.readline()[:-1].split('\t')
                    record=[]
                    while subject!=['']:
                        record.append(subject)
                        subject=fil.readline()[:-1].split('\t')
                break
        else:
            if (inp=='q'):
                quit()
            elif (inp=='res'):
                record='res'
                break
            else:
                print('Input is invalid!')
    if (record!='res'):
        while True:
            print()
            print('Your Grade Report is:')
            record.sort()
            Heading=('Code','Subject Name','Reg. status','Credit','Grade')
            print_table(record,True,Heading,len(record),len(record[0]))
            GPA=GPAcal(record,2,3,4)
            print('  GPA = %-4s'%GPA+'\n  ===========')
            print('\nTo edit this report. Please input  e.\nOtherwise, just press \'Enter\'.')
            inp=qinput(input('< e  or \'Enter\' > : '),5,'\n< e  or \'Enter\' > : ','')
            if (inp!='e'):
                break
            else:
                while True:
                    record=editrec(record)
                    if (record!='res'):
                        while True:
                            if len(record)>1:
                                inp=qinput(input('\nAre there other subject to be edit? (y/n) : '),7,'\nAre there other subject to be edit? (y/n) : ','')
                            else:
                                inp='n'
                            if (inp in ['y','n','res']):
                                break
                            else:
                                print('Input is invalid!')
                        if (inp=='n' or inp=='res'):
                            break
                    else:
                        break
            if (record=='res' or inp=='res'):
                break
        if (record!='res' and inp!='res'):
            inp=input('\nThe program has finish running.\nPress \'Enter\' to exit. ')
            if (inp!='res'):
                for n in range(0,len(record)):
                    subject=tupl(record[n])
                    record[n]=subject
                del inp,Heading,subject,n
                break