import pydealer
import pygame


# Deck of 52 Cards
decka = pydealer.Deck()
deckb = pydealer.Deck()


# get the cards in two different stacks

def Index_Card_Image(value, suit):

    column = -1
    row = -1
    print(value)
    print(suit)
    if suit == "Spades":
        row = 0
    elif suit == "Diamonds":
        row = 1
    elif suit == "Hearts":
        row = 2
    elif suit == "Clubs":
        row = 3
    else:
        row = -1

    if value == "Ace":
        column = 0
    elif value == "Jack":
        column = 10
    elif value == "Queen":
        column = 11
    elif value == "King":
        column = 12
    else:
        column = int(value) - 1

    return row, column

l_cards = decka.get_list([0, 4, 8, 12, 16])
r_cards = deckb.get_list([1, 5, 9, 13, 17])

s = str(r_cards[0])
x = s.split(" ")

r, c = Index_Card_Image(x[0], "Spades")
print(r)
print(c)

s = str(l_cards[0])
x = s.split(" ")

r, c = Index_Card_Image(x[0], x[2])
print(r)
print(c)

