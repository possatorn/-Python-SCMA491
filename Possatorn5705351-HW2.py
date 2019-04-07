# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:38:44 2016

@author: HOME
"""

import random
answer='y'
win=0
lose=0
ngame=1
randspace=[1]*100
for i in range(1,100):
    randspace[i]=i+1
print('\nGuess one integer in range 1 to 100 until you get the correct one.')
print('You have 8 turns to try.\nGood luck!')
while (answer=='y'):
    if (ngame>1):
        if (ngame%10==1):
            order='st'
        elif (ngame%10==2):
            order='nd'
        elif (ngame%10==3):
            order='rd' 
        else:
            order='th' 
        if (ngame%100 in [11,12,13]):
            order='th'
        print('\n',str(ngame)+order,' game :     You have   win =',win,' , lose =',lose,)
    WinningVal=random.randint(1,100)
    turn=0
    for i in range(1,9):
        if (i==8):
            guessvalin=input('\nYour 8th guess is \n(Warning this is your last chance!) : ')
        else :
            if (i==1):
               order='st'
            elif (i==2):
               order='nd'
            elif (i==3):
               order='rd'
            else:
               order='th'
            guessvalin=input('\nYour '+str(i)+order+' guess is : ')
        try:
            guessval=float(guessvalin)
            if (guessval in randspace):
                if (guessval==WinningVal):
                    print('\nThat is the number.\nYou win!')
                    break
                elif (guessval<WinningVal):
                    print('Your number is too small')
                else:
                    print('Your number is too large')
            else:
                if ((guessval>=1)and(guessval<=100)):
                    print('\nInput is invalid.\n',str(guessvalin),' is not an integer!')
                else:
                    print('\nInput is invalid.\n',str(guessvalin),' is not in range 1 to 100!')
        except ValueError:
            print('\nInput is invalid.\n',str(guessvalin),' is not a number!')
        turn=turn+1
    if (turn==8):
        lose=lose+1
        print('\nSorry.You lose!\nThe number is',WinningVal)
    else:
        win=win+1
    ngame=ngame+1
    answer=input('\nTry again? (y/n):')
    while (answer not in ['y','n']):
        print('\nInput is invalid.\nPlease enter only  y  or  n')
        answer=input('\nTry again? (y/n):')
if (ngame-1>1):
    print('\n\nYou played ',ngame-1,' games and   win =',win,' , lose =',lose,)
print('\nThe game is over.')
over=input('\nPress \'Enter\' to exit.')