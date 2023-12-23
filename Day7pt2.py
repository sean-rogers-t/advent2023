


tempHands=[]
bids=[]
with open("day7input.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    tempHands.append(line.strip().split(" ")[0])
    bids.append(line.strip().split(" ")[1])

CardToNum = {"A":14, "K":13, "Q":12, "J":1, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}


hands=[]
for hand in tempHands:
    
    preHand = list(hand)
    postHand=list(map(lambda x: CardToNum[x], preHand))
    
    hands.append(postHand)
def HandType(hand):
    cardCounts={}
    for card in hand:
        if card not in cardCounts:
            cardCounts[card]=1
        else:
            cardCounts[card]+=1
    cardCountsNoJokers = {card:cardCounts[card] for card in cardCounts if card!=1}
    counts=sorted(cardCountsNoJokers.values(), reverse=True)
    alljokers = True if (1 in cardCounts and cardCounts[1]==5) else False
    if not alljokers:
        counts[0]+=cardCounts[1] if (1 in cardCounts and cardCounts[1]!=5) else 0
    else:
        counts=[5]
    
    if counts[0]==5:
        handtype=0
    
    elif counts[0]==4:
        handtype=1
    elif counts[0]==3 and counts[1]==2:
        handtype=2
    elif counts[0]==3:
        handtype=3
    elif counts[0]==2 and counts[1]==2:
        handtype=4
    elif counts[0]==2:
        handtype=5
    else:
        handtype=6
    return handtype

handTypes=[]
handsAndTypes=[]
for i,hand in enumerate(hands):
    #handTypes.append(HandType(hand))
    handsAndTypes.append((i,HandType(hand)))


handsAndTypes.sort(key=lambda x: x[1])
rank=len(hands)
j=0
finalRanks=[]
def RankSameType(sameType):
    x=5
    sameRankHands = [(y,hands[y[0]]) for y in sameType]
    sameRankHands.sort(key=lambda x: x[1],reverse=True)
    return [sameRankHand[0] for sameRankHand in sameRankHands]
while j < len(handsAndTypes):
    print(handsAndTypes[j])
    n=0
    sameType=[]
    while j+n<len(handsAndTypes) and handsAndTypes[j+n][1]==handsAndTypes[j][1]:
        sameType.append(handsAndTypes[j+n])
        n+=1
    X=RankSameType(sameType)
    for i in range(n):
        finalRanks.append((X[i][0],rank))
        rank-=1
    j+=n

answer=0
for hand in finalRanks:
    rank=hand[1]
    bid=int(bids[hand[0]])
    answer+= rank*bid

print(answer)

#249291507
    
# we now have hands and handTypes. Need to rank them by hand type and break ties




    
