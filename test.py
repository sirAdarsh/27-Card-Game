import pydealer
from pydealer.const import BOTTOM
import sys
import pygame
from settings import Settings
from CardSet import CardSet
import time

white = (255, 255, 255)

# Deck of 52 Cards
deck = pydealer.Deck()
# get the cards in two different stacks
l_cards = deck.get_list([0, 4, 8, 12, 16])
r_cards = deck.get_list([0, 3, 6, 9, 12])
rr_cards = r_cards[::-1]

# r_cards = r_cards[::-1]


# Flag Variables for graphics events
Arrange_cards_flag = False


def initialize_deck():
    print("List of all 10 Cards are:")
    print(l_cards)
    print(r_cards)


# Arrange Cards row-wise


def Index_Card_Image(value, suit):
    column = -1
    row = -1

    if suit == "Clubs":
        row = 0
    elif suit == "Diamonds":
        row = 1
    elif suit == "Hearts":
        row = 2
    elif suit == "Spades":
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


def rotate(l, y):
    y = y % len(l)
    return l[y:] + l[:y]


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
        pygame.display.set_caption("Mera Bharath Mahan Trick")
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

                # When pressed Enter, the card display starts
                elif event.key == pygame.K_KP_ENTER:
                    if self.step == 0:
                        print("HERE ------ ")
                        print(l_cards)
                        self._update_screen(l_cards)
                        self.step += 1
                elif event.key == pygame.K_RCTRL:
                    if self.step == 1:
                        self._update_screen(r_cards)
                        self.step += 1

                elif event.key == pygame.K_LEFT:
                    if self.step == 2:
                        n_cards = rotate(l_cards, 1)
                        self._update_screen(n_cards)

                elif event.key == pygame.K_RIGHT:
                    if self.step == 2:
                        n_cards = rotate(rr_cards, 1)
                        self._update_screen(n_cards)

    def _update_screen(self, n_cards):
        self.screen.fill(self.settings.bg_color)
        if self.step == 0:
            for var in range(5):
                # left cards
                x = str(l_cards[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitme(1, var)
                pygame.display.flip()
                time.sleep(0.1)

            for var in range(5):
                # right cards
                x = str(r_cards[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitme(6, 1 + var)
                pygame.display.flip()
                time.sleep(0.1)

        if self.step == 1:
            for var in range(5):
                # left cards
                x = str(l_cards[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitmehere(400, var * 80)
                pygame.display.flip()
                time.sleep(0.1)

            for var in range(5):
                # right cards
                x = str(rr_cards[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitmehere(650, var * 80)
                pygame.display.flip()
                time.sleep(0.1)

        if self.step == 2:
            # left rotation
            for var in range(5):
                x = str(n_cards[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitmehere(400, var * 80)
                pygame.display.flip()
                time.sleep(0.1)

        if self.step == 3:
            for var in range(5):
                # right cards
                x = str(n_cards[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitmehere(650, var * 80)
                pygame.display.flip()
                time.sleep(0.1)


CardDisplay = CardGame()
initialize_deck()
CardDisplay.run_game()