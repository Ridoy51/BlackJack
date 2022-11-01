# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 04:15:37 2022

@author: RIDOY
"""

import os
import numpy
import math
import random
import numpy as np

Card_count=np.zeros((4,13),dtype=int)
maximum = np.ones(13,dtype=int)
maximum = maximum*4

User_point = 0
AI_point =0
Dealer_point=0


User =[]
AI =[]
Dealer =[]


point = [0,0,0]


CardName='♥♦♣♠X'
Card = ['Hurt','Diamond','Club','Spade','X']
CardType=["2","3","4","5","6","7","8","9","10","A","J","K","Q","X"]

deck=np.arange(52)
deck_index=0
np.random.shuffle(deck)
print(deck)

values= {
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "A": 11,
  "J": 10,
  "K": 10,
  "Q": 10,
}

def show(cardtype,cardname):
    print(CardType[cardtype],CardName[cardname])

def User_Turn(k):
    print("----------------User Turn-----------------")
    point=0
    ace=0
    while(1):
        a=input("Enter H to hit or S to stand")
        if(a=='H'):
            p = deck[k]
            k+=1
            b = p%13
            point += values[CardType[b]]
            show(b,p//13)
            User.append(CardType[b])
            Card_count[p//13][b]=1
            maximum[b]-=1
            print(point)
            if(CardType[b]=='A'):
                ace+=1
        else:
            break
        if(point>21 and ace>0):
            a=input("You are out of boundary and have ACE.Press Y to make ACE=1 from ACE=11")
            if(a=='Y'):
                point-=10
                ace-=1
        if(point>21):
            point=0
            print("User Brust")
            break
           
    return [k,point]

k = User_Turn(deck_index)
User_point = k[1]
deck_index = k[0]
point[0]=k[1]
print(User)
    
    


def probability(need):
    sum=0.0
    low=0.0
    up=0.0
    risk=0.0
    for i in range(13):
        if(i+2 <= need and i!=9):
            low+=maximum[i]
        elif(i+2 > need and i!=9):
            up+=maximum[i]
        sum+=maximum[i]
    risk=maximum[9]
    return [low/sum,up/sum,risk/sum]
    
  

probability(10)
def AI_Turn(k):
    print("----------------AI Turn-----------------")
    point=0
    ace=0
    while(1):
        need = 21-point
        z = probability(need)
        if(z[0]+2*z[2] >= z[1]):
             print("AI Hit")
             p = deck[k]
             k+=1
             b = p%13
             point += values[CardType[b]]
             show(b,p//13)
             AI.append(CardType[b])
             Card_count[p//13][b]=1
             maximum[b]-=1
             print("point = ",point)
             if(CardType[b]=='A'):
                 ace+=1
        else:
            print("AI Stand")
            break
    return [k,point]
        
k = AI_Turn(deck_index)
AI_point = k[1]
deck_index = k[0]
point[1]=k[1]
print(point)


def Dealer_Turn(k):
    point=0
    print("----------------Dealer Turn-----------------")
    while(1):
        print("Dealer Hit")
        p = deck[k]
        k+=1
        b = p%13
        point += values[CardType[b]]
        show(b,p//13)
        Dealer.append(CardType[b])
        Card_count[p//13][b]=1
        maximum[b]-=1
        print(point)
        if(point>=17 and point<=21):
            print("Dealer Stand")
            return [k,point]
        if(point>21):
            print("Dealer Burst")
            return [k,0]


k = Dealer_Turn(deck_index)
deck_index=k[0]
Dealer_point=k[1]
print(Dealer_point)

print(Dealer)


print(User_point,AI_point,Dealer_point)
User=0
AI=0
Dealer = 0

if(User_point==21):
    User=1
elif(AI_point==21):
    AI=1    
if (User==1):
    print("User Win")
elif (AI==1):
    print("AI Win")
else:
    if(Dealer_point<User_point):
        User = 2
    if(Dealer_point<AI_point):
        AI=2
    if(AI!=2 and User!=2):
        print("Dealer Wins")
    elif(AI==2 and User==2):
        print("MAtch Drawn")
    elif(AI==2):
        print("AI Wins")
    elif(User==2):
        print("User Wins")
        



















