import random
import numpy  as np
cards = ["Diamonds","Spades","Hearts","Clubs"]
ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def pick_a_card():
    card1 = random.choice(cards)
    rank1 = random.choice(ranks)
    return  (card1,rank1)
def change_point(s):
    if s=="Jack" or s=="Queen" or s=="King":
        return 10
    elif s=="Ace":
        return 11
    else:
        return s
print("You have been dealt")
check = 'y'
hand1=pick_a_card()
hand = [hand1]
point = [change_point(hand[0][1])]
checkbj = False
while (check=='y' and len(point)<5):
    if len(point)==1:
        while  True:
            hand2 = pick_a_card()
            if hand2!=hand1:
                hand.append(hand2)
                point.append(change_point(hand2[1]))
                print("You just got two cards",hand1[1], "of", hand1[0],"and ",hand2[1],"of",hand2[0])
                break
        if  np.add.reduce(point)>=21:
            checkbj = True
            print("Blackjack!",hand)
            break
        check=input("\nDo you want to pick ? y/n\n")
        continue
    else:
        while  True:
            tmp = pick_a_card()
            flag = False
            for i in hand:
                if tmp==i:
                    flag = True
                    continue
            if not flag:
                hand.append(tmp)
                point.append(change_point(tmp[1]))
                print("You just got a",tmp[1],"of",tmp[0])
                if len(point)<=4:
                    check = input("Do you want to pick ? y/n \n")
                break

if  not checkbj:
    sum = 0
    point.sort()
    length = len(point)
    if length==5:
        for i in point:
            if i==11:
                sum+=1
            else:
                sum+=i
        if sum<=21:
            print("Five link!")
    else:
        for i in point:
            if sum<=10 and i==11:
                sum+=11
            elif sum==11 and i==11:
                sum+=10
            elif sum > 11 and i == 11:
                sum+=1
            else:
                sum+=i
    print("Your point: ", sum,'\n')
    print("Your cards", hand)
    