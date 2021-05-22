import pydealer
from pydealer.const import BOTTOM
import sys
import pygame
from settings import Settings
from CardSet import CardSet
import time

white = (255, 255, 255)

buuletImg = pygame.image.load('bullets.png')

pygame.init()
# Font for text
font = pygame.font.Font('freesansbold.ttf', 32)

# Deck of 52 Cards
deck = pydealer.Deck()
deck.shuffle()
Cards_27 = deck.deal(27)

# Lists for 3 Coloumns of cards
column1 = []
column2 = []
column3 = []

# Flag Variables for graphics events
Arrange_cards_flag = False


def initialize_deck():
    print("List of all 27 Cards:")
    print(Cards_27)


# Converting to ternary
def ternary(n):
    if n == 0:
        return "000"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    s = ''.join(reversed(nums))
    if len(s) == 0:
        s = "000"
    if len(s) == 1:
        s = "00" + s
    elif len(s) == 2:
        s = "0" + s
    print("in the function : " +(s))
    ss = "".join(reversed(s))
    print("in the function : " + (ss))
    return s


# Arrange Cards Column-wise

def arrange_cards_columnwise(var, operation_number, series):
    if var == 0:
        for i in range(9):
            column1.append(Cards_27[i * 3])
            column2.append(Cards_27[i * 3 + 1])
            column3.append(Cards_27[i * 3 + 2])

    # var = The chosen column
    operation_number -= 1
    print("  operation number - " + str(operation_number))
    if var == 1:
        ##### Put the Column 1 in middle
        Cards_27.empty()
        # print("Empty Deck:")
        print(Cards_27)
        # Put the column 1 on top
        if series[operation_number] == '0':
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column2[i])
            for i in range(9):
                Cards_27.add(column3[i])

        # Put the column 1 in Middle
        if series[operation_number] == '1':
            for i in range(9):
                Cards_27.add(column2[i])
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column3[i])

        # Put the column 1 in Bottom
        if series[operation_number] == '2':
            for i in range(9):
                Cards_27.add(column2[i])
            for i in range(9):
                Cards_27.add(column3[i])
            for i in range(9):
                Cards_27.add(column1[i])

        print("After Rearrangment:")
        print(Cards_27)

        # Empty the Column Lists
        column1.clear()
        column2.clear()
        column3.clear()
        for i in range(9):
            column1.append(Cards_27[i * 3])
            column2.append(Cards_27[i * 3 + 1])
            column3.append(Cards_27[i * 3 + 2])

    if var == 2:
        ##### the Column 2 in middle
        Cards_27.empty()
        # print("Empty Deck:")
        print(Cards_27)
        # Put the column 2 on top
        if series[operation_number] == '0':
            for i in range(9):
                Cards_27.add(column2[i])
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column3[i])

        # Put the column 2 in Middle
        if series[operation_number] == '1':
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column2[i])
            for i in range(9):
                Cards_27.add(column3[i])
        # Put the column 2 in Bottom
        if series[operation_number] == '2':
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column3[i])
            for i in range(9):
                Cards_27.add(column2[i])

        print("After Rearrangment:")
        print(Cards_27)

        # Empty the Column Lists
        column1.clear()
        column2.clear()
        column3.clear()
        for i in range(9):
            column1.append(Cards_27[i * 3])
            column2.append(Cards_27[i * 3 + 1])
            column3.append(Cards_27[i * 3 + 2])

    if var == 3:
        # Put the Column 3 in middle
        Cards_27.empty()
        # print("Empty Deck:")
        print(Cards_27)
        # Put the column 3 on top
        if series[operation_number] == '0':
            for i in range(9):
                Cards_27.add(column3[i])
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column2[i])

        # Put the column 3 in Middle
        if series[operation_number] == '1':
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column3[i])
            for i in range(9):
                Cards_27.add(column2[i])

        # Put the column 1 in Bottom
        if series[operation_number] == '2':
            for i in range(9):
                Cards_27.add(column1[i])
            for i in range(9):
                Cards_27.add(column2[i])
            for i in range(9):
                Cards_27.add(column3[i])

        print("After Rearrangment:")
        print(Cards_27)

        # Empty the Column Lists
        column1.clear()
        column2.clear()
        column3.clear()
        for i in range(9):
            column1.append(Cards_27[i * 3])
            column2.append(Cards_27[i * 3 + 1])
            column3.append(Cards_27[i * 3 + 2])



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
        column = int(value) - 1

    return row, column


class Numbers(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# 27 Numbers as an option to choose
number_group = pygame.sprite.Group()
pos_x = 400
pos_y = 20
for i in range(27):
    if i != 0 and i % 3 == 0:
        pos_x = 400
        pos_y += 80
    num_img = font.render(str(i + 1), True, (255, 100, 100))
    new_num = Numbers(num_img, pos_x, pos_y)
    number_group.add(new_num)
    pos_x += 200


class CardGame:
    """Overall class to manage Card Display."""

    step = 0
    counter = 0
    first_page_done = False
    number_chosen = 0

    chosen_number_ternary = ''

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
        # self.screen.fill(self.settings.bg_color)

        while True:
            self.screen.fill(white)

            if not self.first_page_done:
                number_group.draw(self.screen)
                pygame.display.update()

            self._check_events()

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                pos = 0
                for num in number_group:

                    if num.rect.collidepoint(x, y):
                        print("THE NUMBER CHOSEN IS ----  " + str(pos))
                        self.first_page_done = True
                        self.number_chosen = pos
                        self.chosen_number_ternary = ternary(self.number_chosen)
                        print("TERNARY -------- "+self.chosen_number_ternary)
                        print(" INT TERNATY ------------  " + str(self.chosen_number_ternary) + "        " +
                              self.chosen_number_ternary[2])
                        break
                    pos += 1
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    sys.exit()

                # When pressed Enter, the card display starts
                elif event.key == pygame.K_KP_ENTER:
                    if self.step == 0:
                        arrange_cards_columnwise(0, self.step, self.chosen_number_ternary)
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_LEFT:
                    if self.step >= 1:
                        arrange_cards_columnwise(1, self.step, self.chosen_number_ternary)
                        self.screen.fill(white)
                        pygame.display.flip()
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_RIGHT:
                    if self.step >= 1:
                        arrange_cards_columnwise(3, self.step, self.chosen_number_ternary)
                        self.screen.fill(white)
                        pygame.display.flip()
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_DOWN:
                    if self.step >= 1:
                        arrange_cards_columnwise(2, self.step, self.chosen_number_ternary)
                        self.screen.fill(white)
                        pygame.display.flip()
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_UP:
                    if self.step == 4:
                        number_chosen = self.number_chosen
                        r, c = Index_Card_Image(Cards_27[number_chosen])



                        self.CardSet.cards[r * 13 + c].rect.x += 70
                        self.screen.fill(self.settings.bg_color)


                        self.CardSet.cards[r * 13 + c].screen.blit(self.CardSet.cards[r * 13 + c].image,
                                                                   self.CardSet.cards[r * 13 + c].rect)
                        self._update_screen()
                        pygame.display.flip()

    def _update_screen(self):
        # Display cards
        if self.step < 4:

            self.screen.fill(self.settings.bg_color)

            for var in range(9):
                # Column 1 Cards
                r, c = Index_Card_Image(column1[var])
                self.CardSet.cards[r * 13 + c].blitme(var, 1)
                pygame.display.flip()
                time.sleep(0.01)

                # Column 2 Cards
                r, c = Index_Card_Image(column2[var])
                self.CardSet.cards[r * 13 + c].blitme(var, 2)
                pygame.display.flip()
                time.sleep(0.01)

                # Column 3 Cards
                r, c = Index_Card_Image(column3[var])
                self.CardSet.cards[r * 13 + c].blitme(var, 3)
                pygame.display.flip()
                time.sleep(0.01)

        if self.step >= 4:
            print(1)
            for var in range(9):
                # Column 1 Cards

                r, c = Index_Card_Image(column1[var])
                ok = True
                if (3 * var ) == self.number_chosen:
                    ok = False
                if ok:
                    self.CardSet.cards[r * 13 + c].blitme(var, 1)

                # Column 2 Cards
                r, c = Index_Card_Image(column2[var])
                ok = True
                if (3 * var + 1) == self.number_chosen:
                    ok = False
                if ok:
                    self.CardSet.cards[r * 13 + c].blitme(var, 2)

                # Column 3 Cards
                r, c = Index_Card_Image(column3[var])
                ok = True
                if (3 * var + 2) == self.number_chosen:
                    ok = False
                if ok:
                    self.CardSet.cards[r * 13 + c].blitme(var, 3)
                pygame.display.flip()


CardDisplay = CardGame()
initialize_deck()
CardDisplay.run_game()
