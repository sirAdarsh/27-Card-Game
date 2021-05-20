import pydealer
from pydealer.const import BOTTOM
import sys
import pygame
from settings import Settings


#Deck of 52 Cards
deck = pydealer.Deck()
Cards_27 = deck.deal(27)

#Lists for 3 Coloumns of cards
column1 = []
column2 = []
column3 = []

def initialize_deck():
    deck.shuffle()
    print("List of all 27 Cards:")
    print(Cards_27)


#Arrange Cards Column-wise

def arrange_cards_columnwise():
    for i in range(9):
        column1.append(Cards_27[i*3])
        column2.append(Cards_27[i*3+1])
        column3.append(Cards_27[i*3+2])

    print("Column 1:")
    print(column1)
    print("Column 2:")
    print(column2)
    print("Column 3:")
    print(column3)

    #Collect the cards Column-wise
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


class CardGame:
    """Overall class to manage Card Display."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("27 Card Trick")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()   


initialize_deck()
arrange_cards_columnwise()
CardDisplay = CardGame()
CardDisplay.run_game()

