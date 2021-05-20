import pydealer
from pydealer.const import BOTTOM
import sys
import pygame
from settings import Settings
from CardSet import CardSet
import time

white = (255,255,255)

#Deck of 52 Cards
deck = pydealer.Deck()
deck.shuffle()
Cards_27 = deck.deal(27)


#Lists for 3 Coloumns of cards
column1 = []
column2 = []
column3 = []

#Flag Variables for graphics events
Arrange_cards_flag = False

def initialize_deck():
    print("List of all 27 Cards:")
    print(Cards_27)


#Arrange Cards Column-wise

def arrange_cards_columnwise(var):

    if var == 0: 
        for i in range(9):
            column1.append(Cards_27[i*3])
            column2.append(Cards_27[i*3+1])
            column3.append(Cards_27[i*3+2])

    if var == 1:
        #Put the Column 1 in middle
        Cards_27.empty()
        #print("Empty Deck:")
        print(Cards_27)

        for i in range(9):
            Cards_27.add(column2[i])
        for i in range(9):
            Cards_27.add(column1[i])
        for i in range(9):
            Cards_27.add(column3[i])

        print("After Rearrangment:")
        print(Cards_27)

        #Empty the Column Lists
        column1.clear()
        column2.clear()
        column3.clear()
        for i in range(9):
            column1.append(Cards_27[i*3])
            column2.append(Cards_27[i*3+1])
            column3.append(Cards_27[i*3+2])
    
    if var == 2:
        #Put the Column 2 in middle
        Cards_27.empty()
        #print("Empty Deck:")
        print(Cards_27)

        for i in range(9):
            Cards_27.add(column1[i])
        for i in range(9):
            Cards_27.add(column2[i])
        for i in range(9):
            Cards_27.add(column3[i])

        print("After Rearrangment:")
        print(Cards_27)

        #Empty the Column Lists
        column1.clear()
        column2.clear()
        column3.clear()
        
        for i in range(9):
            column1.append(Cards_27[i*3])
            column2.append(Cards_27[i*3+1])
            column3.append(Cards_27[i*3+2])

    if var == 3:
        #Put the Column 3 in middle
        Cards_27.empty()
        #print("Empty Deck:")
        print(Cards_27)

        for i in range(9):
            Cards_27.add(column1[i])
        for i in range(9):
            Cards_27.add(column3[i])
        for i in range(9):
            Cards_27.add(column2[i])

        print("After Rearrangment:")
        print(Cards_27)

        #Empty the Column Lists
        column1.clear()
        column2.clear()
        column3.clear()
        
        for i in range(9):
            column1.append(Cards_27[i*3])
            column2.append(Cards_27[i*3+1])
            column3.append(Cards_27[i*3+2])

##    if var == 4:
##        #Highlight the Selected Card
##        Cards_27.empty()
##
##        for i in range(9):
##            Cards_27.add(column1[i])
##        for i in range(9):
##            Cards_27.add(column2[i])
##        for i in range(9):
##            Cards_27.add(column3[i])
##
##        print("After Rearrangment:")
##        print(Cards_27)
##
##        #Empty the Column Lists
##        column1.clear()
##        column2.clear()
##        column3.clear()
##        
##        for i in range(9):
##            column1.append(Cards_27[i*3])
##            column2.append(Cards_27[i*3+1])
##            column3.append(Cards_27[i*3+2])


def Index_Card_Image(card):
    value = card.value
    suit = card.suit

    column = -1
    row = -1

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
        column = int(value) -1

        
    return row, column
    

class CardGame:
    """Overall class to manage Card Display."""

    step = 0
    counter = 0
    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("27 Card Trick")
        self.CardSet = CardSet(self)


    def run_game(self):
        """Start the main loop for the game."""
        self.screen.fill(self.settings.bg_color)

        while True:
            self._check_events()
            

    def _check_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                #When pressed Enter, the card display starts
                elif event.key == pygame.K_KP_ENTER:
                    if self.step == 0:
                        arrange_cards_columnwise(0)
                        self._update_screen()
                        self.step += 1
                        
                elif event.key == pygame.K_LEFT:
                    if self.step >= 1:
                        arrange_cards_columnwise(1)
                        self.screen.fill(white)
                        pygame.display.flip()   
                        self._update_screen()
                        self.step += 1
                        
                elif event.key == pygame.K_RIGHT:
                    if self.step >= 1:
                        arrange_cards_columnwise(3)
                        self.screen.fill(white)
                        pygame.display.flip()   
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_DOWN:
                    if self.step >= 1:
                        arrange_cards_columnwise(2)
                        self.screen.fill(white)
                        pygame.display.flip()   
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_UP:
                    if self.step == 4:
                        r, c = Index_Card_Image(Cards_27[13])
                        self.CardSet.cards[r*13 + c].rect.x += 125
                        self.screen.fill(self.settings.bg_color)
                        self._update_screen()
                        self.CardSet.cards[r*13 + c].screen.blit(self.CardSet.cards[r*13 + c].image, self.CardSet.cards[r*13 + c].rect)
                        pygame.display.flip()
##                        while self.counter <= 100:
##                            self.CardSet.cards[r*13 + c].rect.x += 1
##                            self.screen.fill(self.settings.bg_color)
##                            self.CardSet.cards[r*13 + c].screen.blit(self.CardSet.cards[r*13 + c].image, self.CardSet.cards[r*13 + c].rect)
##                            pygame.display.flip()
##                            self.counter += 1
                    

    def _update_screen(self):

        # Display cards
        if self.step < 4:

            self.screen.fill(self.settings.bg_color)
           
            for var in range(9):
                #Column 1 Cards
                r, c = Index_Card_Image(column1[var])
                self.CardSet.cards[r*13 + c].blitme( var, 1)
                pygame.display.flip()
                time.sleep(0.5)

                #Column 2 Cards
                r, c = Index_Card_Image(column2[var])                    
                self.CardSet.cards[r*13 + c].blitme( var, 2)
                pygame.display.flip()
                time.sleep(0.5)

                #Column 3 Cards
                r, c = Index_Card_Image(column3[var])
                self.CardSet.cards[r*13 + c].blitme( var, 3)
                pygame.display.flip()   
                time.sleep(0.5)
                
        if self.step == 4:
            
            for var in range(9):
                #Column 1 Cards
                r, c = Index_Card_Image(column1[var])
                self.CardSet.cards[r*13 + c].blitme( var, 1)
        
                #Column 2 Cards
                r, c = Index_Card_Image(column2[var])
                if var==4:
                    continue
                else:                    
                    self.CardSet.cards[r*13 + c].blitme( var, 2)
                
                #Column 3 Cards
                r, c = Index_Card_Image(column3[var])
                self.CardSet.cards[r*13 + c].blitme( var, 3)



CardDisplay = CardGame()
initialize_deck()
CardDisplay.run_game()

