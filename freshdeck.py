import random

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {1,2,3,4,5}
    deck = []
    for k in suits:
        for m in ranks:
            deck+=[{'rank':m,'suit':k}]
    deck+=deck+deck #60개의 카드를 담아요
    deck+=[{'rank':1,'suit':'joker1'}]+[{'rank':1,'suit':'joker2'}]  #조커1,2카드를 추가해요
    random.shuffle(deck) #deck를 섞어요
    return deck[:31],deck[31:]
