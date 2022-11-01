import os
import numpy
import math
import random
import numpy as np

card=numpy.zeros((4,13),dtype=int)
human_state=0

Player_win=0
Computer_win=0
Dealer_win=0


CardName='♥♦♣♠X'
CardTypes=["2","3","4","5","6","7","8","9","10","A","J","K","Q","X"]
deck=np.arange(52)
np.random.shuffle(deck)
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

def clearConsole():
    print('\033[H\033[J', end='')

def card_gen():
    draw=deck[card_gen.count]
    card_name=int(draw/13)
    card_type=draw % 13
    card_gen.count+=1
    return [card_type,card_name]
card_gen.count=0
class Dealer:
    dealer_card_type=[]
    dealer_card_value=[]
    value=0
    dealer_hidden_card=[]
    dealer_state=0;
        
    def deal(self):
        temp=card_gen()
        self.dealer_card_type.append(temp[0])
        self.dealer_card_value.append(temp[1])
        self.value+=values[CardTypes[temp[0]]]
        card[temp[1]][temp[0]]=1
        temp=card_gen()
        self.dealer_hidden_card.append(temp[0])
        self.dealer_hidden_card.append(temp[1])
        self.dealer_card_type.append(13)
        self.dealer_card_value.append(4)
        
    def hit_upto_17(self):
        self.dealer_state=1;
        card[self.dealer_hidden_card[1]][self.dealer_hidden_card[0]]=1
        self.dealer_card_type[1]=self.dealer_hidden_card[0]
        self.dealer_card_value[1]=(self.dealer_hidden_card[1])
        self.value+=values[CardTypes[self.dealer_hidden_card[0]]]
        if(self.dealer_hidden_card[0]==9):
            if(self.value>21):
                self.value-=10
        while(self.value<17):
            temp=card_gen()
            self.dealer_card_type.append(temp[0])
            self.dealer_card_value.append(temp[1])
            self.value+=values[CardTypes[temp[0]]]
            card[temp[1]][temp[0]]=1
            if(CardTypes[temp[0]]=="A"):
                if(self.value>21):
                    self.value-=10
        return
    def new_start(self):
        self.value=0
        self.dealer_state=0
        self.dealer_card_type.clear()
        self.dealer_card_value.clear()
        self.dealer_hidden_card.clear()
        
        
        
class Player:
    player_card_type=[]
    player_card_value=[]
    value=0
    
    def deal(self):
        temp=card_gen()
        card[temp[1]][temp[0]]=1
        self.player_card_type.append(temp[0])
        self.player_card_value.append(temp[1])
        self.value+=values[CardTypes[temp[0]]]
        if(CardTypes[temp[0]]=="A"):
            if(self.value>21):
                self.value-=10
    def new_start(self):
        self.value=0
        self.player_card_type.clear()
        self.player_card_value.clear()




class Computer:
    computer_card_type=[]
    computer_card_value=[]
    value=0
    count_a=0
    def deal(self):
        temp=card_gen() 
        self.computer_card_type.append(temp[0])
        self.computer_card_value.append(temp[1])
        self.value+=values[CardTypes[temp[0]]]
        card[temp[1]][temp[0]]=1
        if(CardTypes[temp[0]]=="A"):
            if(self.value>21):
                self.value-=10

        
    def new_start(self):
        self.value=0
        self.computer_card_type.clear()
        self.computer_card_value.clear()
        self.count_a=0
    
    def check(self):
        # print(self.value)
        need=21-self.value
        if(self.computer_card_type.count(9)>0 and self.count_a==0 and self.value<=16):
            need+=10
            count=1
        more=0
        less=0
        total_card=0
        card_A=0
        for i in range(4):
            for j in range(13):
                if(card[i][j]!=1):
                    total_card+=1
                    if(CardTypes[j]=="A"):
                        card_A=+1
                    if(values[CardTypes[j]]<=need):
                        less+=1
                    else:
                        more+=1
        # print(more,less,total_card,need)
        prob_higher=float(more/total_card * 1.0)
        prob_lower=float(less/total_card * 1.0)
        risk=float(card_A/total_card * 1.0)
        return [prob_higher,prob_lower,risk]
    
    def AI(self):
        factor=self.check()
        prob_higher=factor[0]
        prob_lower=factor[1]
        risk=factor[2]
        # print(prob_higher,prob_lower,risk)
        if(prob_lower+ (2*risk)>=prob_higher or prob_higher-prob_lower<.001):
            temp=card_gen()
            card[temp[1]][temp[0]]=1
            self.computer_card_type.append(temp[0])
            self.computer_card_value.append(temp[1])
            self.value+=values[CardTypes[temp[0]]]
            if(CardTypes[temp[0]]=="A"):
                if(self.value>21):
                    self.value-=10
            return 0
        if(human_state):
            if(prob_lower+2*risk>=prob_higher or prob_higher-prob_lower<.001 ):
                temp=card_gen()
                card[temp[1]][temp[0]]=1
                self.computer_card_type.append(temp[0])
                self.computer_card_value.happend(temp[1])
                self.value+=values[CardTypes[temp[0]]]
                if(CardTypes[temp[0]]=="A"):
                    if(self.value>21):
                        self.value-=10
                return 0
            else:
                print("AI Stand")
                return 1
                
                
                
def Game_screan(player, ai, dealer):
    global Player_win
    global Computer_win
    global Dealer_win
    if(player==21):
        Player_win+=1
    elif((dealer<player and player<=21) or (dealer>21 and player<=21)):
        Player_win+=1
    if(ai==21):
        Computer_win+=1
    elif((dealer<ai and ai<=21) or (dealer>21 and ai<=21)):
        Computer_win+=1
    if((dealer>player or player>21) and (dealer>ai or ai>21) and dealer<=21):
        Dealer_win+=1         

    print("player win  Computer win  dealer win")
    print("     ",Player_win, "          " ,Computer_win,"     ",Dealer_win)
                
    
def display():
    print("Press 'H/h' for hit")
    print("Press 'S/s' for stand")
def card_print(card_name, card_type):
    for i in range(len(card_name)):
        print('┌───────┐', end=" ")
    print()
    for i in range(len(card_name)):
        print(f'| {CardTypes[card_type[i]]:<2}    |',end=" ")
    print()
    for i in range(len(card_name)):
        print('|       |',end=" ")
    print()
    for i in range(len(card_name)):
        print(f'|   {CardName[card_name[i]]}   |',end=" ")
    print()
    for i in range(len(card_name)):
        print('|       |',end=" ")
    print()
    for i in range(len(card_name)):
        print(f'|    {CardTypes[card_type[i]]:>2} |',end=" ")
    print()
    for i in range(len(card_name)):
        print('└───────┘',end=" ")
    print() 


def card_display(dealer, player, computer):
    print("Dealer Card and current value ",dealer.value)
    card_print(dealer.dealer_card_value,dealer.dealer_card_type)
    print("Player Card and current value ",player.value)
    card_print(player.player_card_value,player.player_card_type)
    print("Computer Card and current value ",computer.value)
    card_print(computer.computer_card_value,computer.computer_card_type)
    

#main game start From Here
       
for i in range(5):
    print("\nRound ",i+1,"\n")
    dealer=Dealer()
    dealer.new_start()
    player=Player()
    player.new_start()
    computer=Computer()
    computer.new_start()
    player.deal()
    computer.deal()
    player.deal()
    computer.deal()
    dealer.deal()
    card_display(dealer, player, computer)
    user_input=""
    while(1):
        if(player.value<=21):
            if(player.value==21):
                user_input="s"
                human_state=1
                while(not computer.AI()):
                    # clearConsole()
                    card_display(dealer, player, computer)
                dealer.hit_upto_17()
                # clearConsole()
                card_display(dealer, player, computer)
                Game_screan(player.value, computer.value, dealer.value)
                break
                
            else:
                if(user_input==""):
                    display()
                    user_input=input()
                    print(user_input)
                if(user_input=="H" or user_input=="h"):
                    player.deal()
                    computer.AI()
                    # clearConsole()
                    card_display(dealer, player, computer)
                    user_input=""
                    continue;
                elif(user_input=="s" or user_input=="S"):
                    human_state=1
                    while(not computer.AI()):
                        # clearConsole()
                        card_display(dealer, player, computer)
                    dealer.hit_upto_17()
                    # clearConsole()
                    card_display(dealer, player, computer)
                    Game_screan(player.value, computer.value, dealer.value)
                    break
        else:
            human_state=1
            if(computer.value==21):
                dealer.hit_upto_17()
                # clearConsole()
                card_display(dealer, player, computer)
                Game_screan(player.value, computer.value, dealer.value)
                break
                
            else:
                while(not computer.AI()):
                    # clearConsole()
                    card_display(dealer, player, computer)
                dealer.hit_upto_17()
                # clearConsole()
                card_display(dealer, player, computer)
                Game_screan(player.value, computer.value, dealer.value)
                break
                
                    