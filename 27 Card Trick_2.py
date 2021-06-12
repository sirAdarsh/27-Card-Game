import pydealer
from pydealer.const import BOTTOM
import sys
import pygame
from settings import Settings
from CardSet import CardSet
import time

white = (255, 255, 255)

pygame.init()
# Font for text
font1 = pygame.font.Font('Fonts/Walkway_SemiBold.ttf', 32)
font2 = pygame.font.Font('Fonts/Sansation-Bold.ttf', 40)
font3 = pygame.font.Font('Fonts/Walkway_Oblique_Black.ttf', 45)

# Deck of 52 Cards
deck = pydealer.Deck()
deck.shuffle()
Cards_27 = deck.deal(27)

# Lists for 3 Coloumns of cards
column1 = []
column2 = []
column3 = []

col1 = []
col2 = []
col3 = []

# Flag Variables for graphics events
Arrange_cards_flag = False


def initialize_deck():
    print("List of all 27 Cards:")
    print(Cards_27)


# Arrange Cards Column-wise

def arrange_cards_columnwise(var, operation_number, series):
    if var == 0:
        for i in range(9):
            column1.append(Cards_27[i * 3])
            col1.append(Cards_27[i * 3])
            column2.append(Cards_27[i * 3 + 1])
            col2.append(Cards_27[i * 3 + 1])
            column3.append(Cards_27[i * 3 + 2])
            col3.append(Cards_27[i * 3 + 2])

    if var == 1:
        # Put the Column 1 in middle
        Cards_27.empty()
        # print("Empty Deck:")
        print(Cards_27)

        for i in range(9):
            Cards_27.add(column2[i])
        for i in range(9):
            Cards_27.add(column1[i])
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

    if var == 2:
        # Put the Column 2 in middle
        Cards_27.empty()
        # print("Empty Deck:")
        print(Cards_27)

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

    if var == 3:
        # Put the Column 3 in middle
        Cards_27.empty()
        # print("Empty Deck:")
        print(Cards_27)

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


class CardGame:
    """Overall class to manage Card Display."""

    flag_to_flip = False

    ans_r = 0
    ans_c = 0

    step = 0
    counter = 0
    first_page_done = False
    number_chosen = 0

    first_column = 0
    second_column = 0
    third_column = 0

    stacks = []  # nine stacks

    map_cards = []
    x = 250
    y = 25
    map_cards.append([x, y])
    x += 400
    map_cards.append([x, y])
    x += 400
    map_cards.append([x, y])
    x = 250
    y += 250
    map_cards.append([x, y])
    x += 400
    map_cards.append([x, y])
    x += 400
    map_cards.append([x, y])
    x = 250
    y += 250
    map_cards.append([x, y])
    x += 400
    map_cards.append([x, y])
    x += 400
    map_cards.append([x, y])

    chosen_number_ternary = ''

    coord_x = 50
    coord_y = 25

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
        r = 4
        c = 2
        self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
        pygame.display.flip()
        print(self.map_cards)
        while True:
            # self.screen.fill(white, pygame.Rect(200, 0, 1200, 1200))

            pygame.display.update()
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
                        self.screen.fill((0, 0, 0), (50, 400, 250, 50))

                        arrange_cards_columnwise(0, self.step, self.chosen_number_ternary)
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_LEFT:
                    if self.step >= 1:
                        arrange_cards_columnwise(1, self.step, self.chosen_number_ternary)
                        self.collect_cards()

                        # add another event listener
                        here = True
                        while here:
                            txt = font1.render("Press any key to distribute the cards ", True, (255, 10, 20))
                            pygame.display.flip()
                            self.screen.blit(txt, (450, 600))
                            for event1 in pygame.event.get():
                                if event1.type == pygame.KEYDOWN:
                                    here = False
                                    break
                                if event1.type == pygame.QUIT:
                                    sys.exit()

                        # self.screen.fill(white)
                        pygame.display.flip()
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_RIGHT:
                    if self.step >= 1:
                        arrange_cards_columnwise(3, self.step, self.chosen_number_ternary)
                        self.collect_cards()

                        # add another event listener
                        here = True
                        while here:
                            txt = font1.render("Press any key to distribute the cards ", True, (255, 10, 20))
                            pygame.display.flip()
                            self.screen.blit(txt, (450, 600))
                            for event1 in pygame.event.get():
                                if event1.type == pygame.KEYDOWN:
                                    here = False
                                    break
                                if event1.type == pygame.QUIT:
                                    sys.exit()

                        # self.screen.fill(white)
                        pygame.display.flip()
                        self._update_screen()
                        self.step += 1

                elif event.key == pygame.K_DOWN:
                    arrange_cards_columnwise(2, self.step, self.chosen_number_ternary)
                    self.collect_cards()

                    # add another event listener
                    here = True
                    while here:
                        txt = font1.render("Press any key to distribute the cards ", True, (255, 10, 20))
                        pygame.display.flip()
                        self.screen.blit(txt, (450, 600))
                        for event1 in pygame.event.get():
                            if event1.type == pygame.KEYDOWN:
                                here = False
                                break
                            if event1.type == pygame.QUIT:
                                sys.exit()

                    pygame.display.flip()
                    self._update_screen()
                    self.step += 1


                elif event.key == pygame.K_UP:
                    if self.step == 4:
                        # self.collect_cards()

                        r, c = Index_Card_Image(Cards_27[13])

                        self.ans_r = r
                        self.ans_c = c

                        self._update_screen()
                        self.step += 1

                    if self.step > 4:
                        self._update_screen()

                elif event.key == pygame.K_SPACE:
                    self.screen.fill(self.settings.bg_color)
                    txt = font3.render("The final 3 cards :::= ", True, (255, 0, 0))
                    self.screen.blit(txt, (400, 400))
                    pygame.display.flip()
                    time.sleep(2)
                    self.handle_last_stack(self.stacks[0])


    def handle_last_stack(self, stack):

        print(stack)
        self.screen.fill(self.settings.bg_color)
        # The required card is at the position 2
        r, c = Index_Card_Image(stack[0])
        if self.flag_to_flip:
            r = 4
            c = 2
            self.CardSet.cards[r * 13 + c].blitmehere(200, 100)
        else:
            self.CardSet.cards[r * 13 + c].blitmehere(200, 100)
        pygame.display.flip()

        r, c = Index_Card_Image((stack[1]))
        if self.flag_to_flip:
            r = 4
            c = 2
            self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
        else:
            self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
        pygame.display.flip()

        r, c = Index_Card_Image((stack[2]))
        if self.flag_to_flip:
            r = 4
            c = 2
            self.CardSet.cards[r * 13 + c].blitmehere(600, 100)
        else:
            self.CardSet.cards[r * 13 + c].blitmehere(600, 100)
        pygame.display.flip()

        # ASK TO SELECT 1 card from (1,2,3)

        selects = []

        x = 200
        y = 750

        txt = font1.render("Select any 1 card ", True, (255, 10, 20))
        pygame.display.flip()
        self.screen.blit(txt, (450, 600))

        while (True):
            to_break = False

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        sys.exit()

                    if event.key == pygame.K_1:
                        selects.append(1)
                        txt = font3.render(str(1), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_2:
                        selects.append(2)
                        txt = font3.render(str(2), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_3:
                        selects.append(3)
                        txt = font3.render(str(3), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_4:
                        selects.append(4)
                        txt = font3.render(str(4), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_5:
                        selects.append(5)
                        txt = font3.render(str(5), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_6:
                        selects.append(6)
                        txt = font3.render(str(6), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_7:
                        selects.append(7)
                        txt = font3.render(str(7), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_8:
                        selects.append(8)
                        txt = font3.render(str(8), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    elif event.key == pygame.K_9:
                        selects.append(9)
                        txt = font3.render(str(9), True, (255, 0, 0))
                        self.screen.blit(txt, (x, y))
                        pygame.display.flip()
                    print(len(selects))
                    x += 100
                if len(selects) == 1:
                    to_break = True
                    break

            if to_break:
                break

        while True:
            to_break = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.QUIT:
                        sys.exit()
                    if event.key == pygame.K_KP_ENTER:
                        to_break = True
                        break
            if to_break:
                break

                # we have made 5 selections now, ALSO CARD IS IN STACK - 5

        if selects[0] == 2:
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            r, c = Index_Card_Image(stack[1])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
                pygame.display.flip()
                while True:
                    to_break = False
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                to_break = True
                                break
                    if to_break:
                        break
                txt = font1.render("Your Final card is : ", True, (255, 10, 20))
                pygame.display.flip()
                self.screen.blit(txt, (500, 50))

                r, c = Index_Card_Image(stack[1])
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            pygame.display.flip()


        elif selects[0] == 1:
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

            r, c = Index_Card_Image(stack[1])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            pygame.display.flip()
            r, c = Index_Card_Image(stack[2])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(600, 100)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(600, 100)
            pygame.display.flip()
            #ask to choose one again

            selects.clear()

            txt = font1.render("Select any 1 card  ", True, (255, 10, 20))
            pygame.display.flip()
            self.screen.blit(txt, (450, 600))

            while (True):
                to_break = False

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.QUIT:
                            sys.exit()

                        if event.key == pygame.K_1:
                            selects.append(1)
                            txt = font3.render(str(1), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_2:
                            selects.append(2)
                            txt = font3.render(str(2), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_3:
                            selects.append(3)
                            txt = font3.render(str(3), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_4:
                            selects.append(4)
                            txt = font3.render(str(4), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_5:
                            selects.append(5)
                            txt = font3.render(str(5), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_6:
                            selects.append(6)
                            txt = font3.render(str(6), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_7:
                            selects.append(7)
                            txt = font3.render(str(7), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_8:
                            selects.append(8)
                            txt = font3.render(str(8), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_9:
                            selects.append(9)
                            txt = font3.render(str(9), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        print(len(selects))
                        x += 100
                    if len(selects) == 1:
                        to_break = True
                        break

                if to_break:
                    break

            while True:
                to_break = False
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.QUIT:
                            sys.exit()
                        if event.key == pygame.K_KP_ENTER:
                            to_break = True
                            break
                if to_break:
                    break

                    # we have made 5 selections now, ALSO CARD IS IN STACK - 5


            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            r, c = Index_Card_Image(stack[1])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
                pygame.display.flip()
                while True:
                    to_break = False
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                to_break = True
                                break
                    if to_break:
                        break
                txt = font1.render("Your Final card is : ", True, (255, 10, 20))
                pygame.display.flip()
                self.screen.blit(txt, (500, 50))

                r, c = Index_Card_Image(stack[1])
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            pygame.display.flip()

        else:
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            r, c = Index_Card_Image(stack[1])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            pygame.display.flip()
            r, c = Index_Card_Image(stack[0])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(600, 100)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(600, 100)
            pygame.display.flip()
            # ask to choose one again

            selects.clear()

            txt = font1.render("Select any 1 card ", True, (255, 10, 20))
            pygame.display.flip()
            self.screen.blit(txt, (450, 600))

            while (True):
                to_break = False

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.QUIT:
                            sys.exit()

                        if event.key == pygame.K_1:
                            selects.append(1)
                            txt = font3.render(str(1), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_2:
                            selects.append(2)
                            txt = font3.render(str(2), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_3:
                            selects.append(3)
                            txt = font3.render(str(3), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_4:
                            selects.append(4)
                            txt = font3.render(str(4), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_5:
                            selects.append(5)
                            txt = font3.render(str(5), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_6:
                            selects.append(6)
                            txt = font3.render(str(6), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_7:
                            selects.append(7)
                            txt = font3.render(str(7), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_8:
                            selects.append(8)
                            txt = font3.render(str(8), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_9:
                            selects.append(9)
                            txt = font3.render(str(9), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        print(len(selects))
                        x += 100
                    if len(selects) == 1:
                        to_break = True
                        break

                if to_break:
                    break

            while True:
                to_break = False
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.QUIT:
                            sys.exit()
                        if event.key == pygame.K_KP_ENTER:
                            to_break = True
                            break
                if to_break:
                    break

                    # we have made 5 selections now, ALSO CARD IS IN STACK - 5

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            r, c = Index_Card_Image(stack[1])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
                pygame.display.flip()
                while True:
                    to_break = False
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                to_break = True
                                break
                    if to_break:
                        break
                txt = font1.render("Your Final card is : ", True, (255, 10, 20))
                pygame.display.flip()
                self.screen.blit(txt, (500, 50))
                r, c = Index_Card_Image(stack[1])
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(400, 100)
            pygame.display.flip()

    def collect_cards(self):

        space = 0

        if self.step > 0:

            # FIRST COLUMN DETECTION
            r_last, c_last = Index_Card_Image(Cards_27[8])
            r_temp, c_temp = Index_Card_Image(col1[8])
            # If first 9 cards is from column1
            if r_temp == r_last and c_temp == c_last:
                self.first_column = 1
            r_temp, c_temp = Index_Card_Image(col2[8])
            # If first 9 cards is from column 2
            if r_temp == r_last and c_temp == c_last:
                self.first_column = 2
            r_temp, c_temp = Index_Card_Image(col3[8])
            # If first 9 cards is from column 3
            if r_temp == r_last and c_temp == c_last:
                self.first_column = 3

            # SECOND COLUMN DETECTION
            r_last, c_last = Index_Card_Image(Cards_27[17])
            r_temp, c_temp = Index_Card_Image(col1[8])
            # If first 9 cards is from column 1
            if r_temp == r_last and c_temp == c_last:
                self.second_column = 1
            r_temp, c_temp = Index_Card_Image(col2[8])
            # If first 9 cards is from column 2
            if r_temp == r_last and c_temp == c_last:
                self.second_column = 2
            r_temp, c_temp = Index_Card_Image(col3[8])
            # If first 9 cards is from column 3
            if r_temp == r_last and c_temp == c_last:
                self.second_column = 3

            # THIRD COLUMN DETECTION
            r_last, c_last = Index_Card_Image(Cards_27[26])
            r_temp, c_temp = Index_Card_Image(col1[8])
            # If first 9 cards is from column 1
            if r_temp == r_last and c_temp == c_last:
                self.third_column = 1

            r_temp, c_temp = Index_Card_Image(col2[8])

            # If first 9 cards is from column 2
            if r_temp == r_last and c_temp == c_last:
                self.third_column = 2

            r_temp, c_temp = Index_Card_Image(col3[8])

            # If first 9 cards is from column 3
            if r_temp == r_last and c_temp == c_last:
                self.third_column = 3

            x_first = 300
            x_second = 600
            x_third = 900
            del_y = 50

            if self.first_column == 1:
                x = x_first
            elif self.second_column == 1:
                x = x_second
            else:
                x = x_third
            for i in range(9):

                time.sleep(0.01)
                self.screen.fill(self.settings.bg_color, pygame.Rect(x, 20, 100, del_y))
                del_y += 50
                if i == 7:
                    del_y += 400
                r, c = Index_Card_Image(Cards_27[i])
                self.CardSet.cards[r * 13 + c].blitmehere(10, space)
                space += 25
                pygame.display.flip()

                # TO_DO: add a part to remove the selected column
            time.sleep(0.01)

            pygame.display.flip()

            if self.first_column == 2:
                x = x_first
            elif self.second_column == 2:
                x = x_second
            else:
                x = x_third
            del_y = 50
            for i in range(9, 18):

                time.sleep(0.01)
                self.screen.fill(self.settings.bg_color, pygame.Rect(x, 20, 100, del_y))
                del_y += 50
                if i == 16:
                    del_y += 300
                r, c = Index_Card_Image(Cards_27[i])
                self.CardSet.cards[r * 13 + c].blitmehere(40, space)
                space += 25
                pygame.display.flip()

            time.sleep(0.01)

            pygame.display.flip()

            del_y = 50
            if self.first_column == 3:
                x = x_first
            elif self.second_column == 3:
                x = x_second
            else:
                x = x_third
            for i in range(18, 27):
                time.sleep(0.01)
                self.screen.fill(self.settings.bg_color, pygame.Rect(x, 20, 100, del_y))
                del_y += 50
                if i == 25:
                    del_y += 300
                r, c = Index_Card_Image(Cards_27[i])
                self.CardSet.cards[r * 13 + c].blitmehere(10, space)
                space += 25
                pygame.display.flip()

            time.sleep(0.01)

            col1.clear()
            col2.clear()
            col3.clear()

            for i in range(9):
                col1.append(column1[i])
                col2.append(column2[i])
                col3.append(column3[i])

            time.sleep(0.01)

    def draw_cards(self, t_stacks):

        x = 250
        y = 25
        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 800))
        pygame.display.flip()

        for i in range(len(t_stacks)):

            r, c = Index_Card_Image(t_stacks[i][0])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(x, y)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(x, y)
            pygame.display.flip()
            y += 25

            r, c = Index_Card_Image(t_stacks[i][1])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(x, y)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(x, y)
            pygame.display.flip()
            y += 25

            r, c = Index_Card_Image(t_stacks[i][2])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(x, y)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(x, y)
            pygame.display.flip()
            y += 25

            x += 400
            y -= 75

            if x >= 1100:
                x = 250
                y += 250

    def print_stack_on_left(self, stack):

        for i in range(len(stack)):
            r, c = Index_Card_Image(stack[i])
            if self.flag_to_flip:
                r = 4
                c = 2
                self.CardSet.cards[r * 13 + c].blitmehere(self.coord_x, self.coord_y)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(self.coord_x, self.coord_y)
            self.coord_y += 25
            pygame.display.flip()

    def _update_screen(self):
        # Display cards
        if self.step < 4:

            self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 800))
            pygame.display.flip()
            y = 0

            for var in range(9):
                # Column 1 Cards
                y += 25
                self.screen.fill((0, 0, 0), pygame.Rect(0, 0, 200, y))

                pygame.display.flip()
                r, c = Index_Card_Image(column1[var])
                if self.flag_to_flip:
                    r = 4
                    c = 2
                    self.CardSet.cards[r * 13 + c].blitme(var, 1)
                else:
                    self.CardSet.cards[r * 13 + c].blitme(var, 1)
                pygame.display.flip()
                time.sleep(0.01)

                # Column 2 Cards
                y += 25
                self.screen.fill((0, 0, 0), pygame.Rect(0, 0, 200, y))
                pygame.display.flip()
                r, c = Index_Card_Image(column2[var])
                if self.flag_to_flip:
                    r = 4
                    c = 2
                    self.CardSet.cards[r * 13 + c].blitme(var, 2)
                else:
                    self.CardSet.cards[r * 13 + c].blitme(var, 2)
                pygame.display.flip()
                time.sleep(0.01)

                if var == 2:
                    self.screen.fill((0, 0, 0), pygame.Rect(0, 0, 40, y + 180))
                    pygame.display.flip()

                if var == 5:
                    self.screen.fill((0, 0, 0), pygame.Rect(107, 0, 50, y + 180))
                    pygame.display.flip()
                # Column 3 Cards
                y += 25
                if var == 8:
                    self.screen.fill((0, 0, 0), pygame.Rect(0, 0, 200, 1200))
                    pygame.display.flip()
                self.screen.fill((0, 0, 0), pygame.Rect(0, 0, 200, y))
                pygame.display.flip()
                r, c = Index_Card_Image(column3[var])
                if self.flag_to_flip:
                    r = 4
                    c = 2
                    self.CardSet.cards[r * 13 + c].blitme(var, 3)
                else:
                    self.CardSet.cards[r * 13 + c].blitme(var, 3)
                pygame.display.flip()
                time.sleep(0.01)

        if self.step == 4:
            print('YE WALA')
            done = False
            self.screen.fill(self.settings.bg_color)
            self.flag_to_flip = True
            for i in range(9):
                stack = [col1[i], col2[i], col3[i]]
                self.stacks.append(stack)

            # print(self.stacks[1][0])

        if self.step > 4:

            time.sleep(2)
            self.draw_cards(self.stacks)

            time.sleep(2)
            # First selection of 5 stacks

            selects = []

            pygame.display.flip()
            x = 200
            y = 750

            # SELECT 5 CARD STACKS
            txt = font1.render("Select any 5 card ", True, (255, 10, 20))
            self.screen.blit(txt, (700, 750))
            pygame.display.flip()

            while True:
                to_break = False

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.QUIT:
                            sys.exit()

                        if event.key == pygame.K_1:
                            selects.append(1)
                            txt = font3.render(str(1), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_2:
                            selects.append(2)
                            txt = font3.render(str(2), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_3:
                            selects.append(3)
                            txt = font3.render(str(3), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_4:
                            selects.append(4)
                            txt = font3.render(str(4), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_5:
                            selects.append(5)
                            txt = font3.render(str(5), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_6:
                            selects.append(6)
                            txt = font3.render(str(6), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_7:
                            selects.append(7)
                            txt = font3.render(str(7), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_8:
                            selects.append(8)
                            txt = font3.render(str(8), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        elif event.key == pygame.K_9:
                            selects.append(9)
                            txt = font3.render(str(9), True, (255, 0, 0))
                            self.screen.blit(txt, (x, y))
                            pygame.display.flip()
                        print(len(selects))
                        x += 100
                    if len(selects) == 5:
                        to_break = True
                        break

                if to_break:
                    break

            while True:
                to_break = False
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.QUIT:
                            sys.exit()
                        if event.key == pygame.K_KP_ENTER:
                            to_break = True
                            break
                if to_break:
                    break

            # we have made 5 selections now, ALSO CARD IS IN STACK - 5

            stack_selected = False

            for i in range(len(selects)):
                if selects[i] == 5:
                    stack_selected = True

            if stack_selected:
                # means now these 5 card stacks should be displayed
                # display the selected stacks only

                # THE LUCKY STACK IS IN POSITION STACK - 1 NOW!!

                # ERASE the unselected stacks

                new_stack = []
                print(selects)
                new_stack.append(self.stacks[4])
                nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(len(selects)):
                    nums.remove(selects[i])
                    if selects[i] != 5:
                        new_stack.append(self.stacks[selects[i] - 1])

                time.sleep(2)
                for i in range(len(nums)):
                    print(self.map_cards[nums[i] - 1][0])
                    print(self.map_cards[nums[i] - 1][1])
                    pygame.display.flip()
                    self.screen.fill(self.settings.bg_color,
                                     pygame.Rect(self.map_cards[nums[i] - 1][0], self.map_cards[nums[i] - 1][1], 100,
                                                 220))
                    pygame.display.flip()
                    if len(self.stacks) < nums[i]:
                        continue
                    time.sleep(1)
                    self.print_stack_on_left(self.stacks[nums[i] - 1])

                time.sleep(2)

                self.stacks.clear()
                for i in range(len(new_stack)):
                    self.stacks.append(new_stack[i])

                self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                pygame.display.flip()
                self.draw_cards(new_stack)

                # Again, select 3 card stacks3
                # SELECT 3 CARD STACKS
                selects.clear()
                x = 200
                y = 750
                txt = font1.render("Select any 3 card ", True, (255, 10, 20))
                self.screen.blit(txt, (700, 750))
                pygame.display.flip()
                while (True):
                    to_break = False

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.type == pygame.QUIT:
                                sys.exit()

                            if event.key == pygame.K_1:
                                selects.append(1)
                                txt = font3.render(str(1), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_2:
                                selects.append(2)
                                txt = font3.render(str(2), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_3:
                                selects.append(3)
                                txt = font3.render(str(3), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_4:
                                selects.append(4)
                                txt = font3.render(str(4), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_5:
                                selects.append(5)
                                txt = font3.render(str(5), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_6:
                                selects.append(6)
                                txt = font3.render(str(6), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_7:
                                selects.append(7)
                                txt = font3.render(str(7), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_8:
                                selects.append(8)
                                txt = font3.render(str(8), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_9:
                                selects.append(9)
                                txt = font3.render(str(9), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            print(len(selects))
                            x += 100
                        if len(selects) == 3:
                            to_break = True
                            break

                    if to_break:
                        break

                while True:
                    to_break = False
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.QUIT:
                                sys.exit()
                            if event.key == pygame.K_KP_ENTER:
                                to_break = True
                                break
                    if to_break:
                        break

                        # we have made 5 selections now, ALSO CARD IS IN STACK - 5

                stack_selected = False

                for i in range(len(selects)):
                    if selects[i] == 1:
                        stack_selected = True

                # 3 CARD STACKS
                if stack_selected:
                    # means now these 3 card stacks should be displayed
                    #                     # display the selected stacks only

                    # THE LUCKY STACK IS IN POSITION STACK - 1 NOW!!

                    new_stack = []
                    new_stack.append(self.stacks[1 - 1])
                    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for i in range(len(selects)):
                        nums.remove(selects[i])
                        if selects[i] != 1:
                            new_stack.append(self.stacks[selects[i] - 1])

                    for i in range(len(nums)):
                        print(self.map_cards[nums[i] - 1][0])
                        print(self.map_cards[nums[i] - 1][1])
                        pygame.display.flip()
                        self.screen.fill(self.settings.bg_color,
                                         pygame.Rect(self.map_cards[nums[i] - 1][0], self.map_cards[nums[i] - 1][1],
                                                     100, 220))
                        pygame.display.flip()
                        time.sleep(1)
                        if len(self.stacks) < nums[i]:
                            continue
                        self.print_stack_on_left(self.stacks[nums[i] - 1])
                        time.sleep(2)

                    time.sleep(2)

                    self.stacks.clear()
                    for i in range(len(new_stack)):
                        self.stacks.append(new_stack[i])

                    self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                    self.draw_cards(new_stack)

                    # Again ask to select 2 card stacks
                    # SELECT 2 CARD STACKS

                    selects.clear()
                    x = 200
                    y = 750
                    txt = font1.render("Select any 2 card ", True, (255, 10, 20))
                    self.screen.blit(txt, (700, 750))
                    pygame.display.flip()
                    while (True):
                        to_break = False

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.type == pygame.QUIT:
                                    sys.exit()

                                if event.key == pygame.K_1:
                                    selects.append(1)
                                    txt = font3.render(str(1), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_2:
                                    selects.append(2)
                                    txt = font3.render(str(2), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_3:
                                    selects.append(3)
                                    txt = font3.render(str(3), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_4:
                                    selects.append(4)
                                    txt = font3.render(str(4), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_5:
                                    selects.append(5)
                                    txt = font3.render(str(5), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_6:
                                    selects.append(6)
                                    txt = font3.render(str(6), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_7:
                                    selects.append(7)
                                    txt = font3.render(str(7), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_8:
                                    selects.append(8)
                                    txt = font3.render(str(8), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_9:
                                    selects.append(9)
                                    txt = font3.render(str(9), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                print(len(selects))
                                x += 100
                            if len(selects) == 2:
                                to_break = True
                                break

                        if to_break:
                            break

                    while True:
                        to_break = False
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.QUIT:
                                    sys.exit()
                                if event.key == pygame.K_KP_ENTER:
                                    to_break = True
                                    break
                        if to_break:
                            break

                            # we have made 5 selections now, ALSO CARD IS IN STACK - 5

                    stack_selected = False

                    for i in range(len(selects)):
                        if selects[i] == 1:
                            stack_selected = True

                    # 2 CARDS STACKS REMAINING
                    if stack_selected:
                        # means now these 2 card stacks should be displayed
                        # display the selected stacks only

                        new_stack = []
                        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        new_stack.append(self.stacks[1 - 1])
                        for i in range(len(selects)):
                            nums.remove(selects[i])
                            if selects[i] != 1:
                                new_stack.append(self.stacks[selects[i] - 1])

                        for i in range(len(nums)):
                            print(self.map_cards[nums[i] - 1][0])
                            print(self.map_cards[nums[i] - 1][1])
                            pygame.display.flip()
                            self.screen.fill(self.settings.bg_color,
                                             pygame.Rect(self.map_cards[nums[i] - 1][0], self.map_cards[nums[i] - 1][1],
                                                         100, 220))
                            pygame.display.flip()
                            if len(self.stacks) < nums[i]:
                                continue
                            time.sleep(1)
                            self.print_stack_on_left(self.stacks[nums[i] - 1])

                        time.sleep(2)

                        self.stacks.clear()
                        for i in range(len(new_stack)):
                            self.stacks.append(new_stack[i])

                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        pygame.display.flip()
                        self.draw_cards(new_stack)

                        # Again ask to select 1 card stacks
                        # SELECT 1 CARD STACKS

                        selects.clear()
                        x = 200
                        y = 750
                        txt = font1.render("Select any 1 card ", True, (255, 10, 20))
                        self.screen.blit(txt, (700, 750))
                        pygame.display.flip()
                        while True:
                            to_break = False

                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.type == pygame.QUIT:
                                        sys.exit()

                                    if event.key == pygame.K_1:
                                        selects.append(1)
                                        txt = font3.render(str(1), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_2:
                                        selects.append(2)
                                        txt = font3.render(str(2), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_3:
                                        selects.append(3)
                                        txt = font3.render(str(3), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_4:
                                        selects.append(4)
                                        txt = font3.render(str(4), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_5:
                                        selects.append(5)
                                        txt = font3.render(str(5), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_6:
                                        selects.append(6)
                                        txt = font3.render(str(6), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_7:
                                        selects.append(7)
                                        txt = font3.render(str(7), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_8:
                                        selects.append(8)
                                        txt = font3.render(str(8), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    elif event.key == pygame.K_9:
                                        selects.append(9)
                                        txt = font3.render(str(9), True, (255, 0, 0))
                                        self.screen.blit(txt, (x, y))
                                        pygame.display.flip()
                                    print(len(selects))
                                    x += 100
                                if len(selects) == 1:
                                    to_break = True
                                    break

                            if to_break:
                                break

                        while True:
                            to_break = False
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.QUIT:
                                        sys.exit()
                                    if event.key == pygame.K_KP_ENTER:
                                        to_break = True
                                        break
                            if to_break:
                                break

                                # we have made 5 selections now, ALSO CARD IS IN STACK - 5

                        stack_selected = False

                        for i in range(len(selects)):
                            if selects[i] == 1:
                                stack_selected = True

                        # 2 CARDS REMAINING
                        if stack_selected:

                            new_stack = []
                            # THIS IS THE FINAL STACK, DISPLY IT!
                            new_stack.append(self.stacks[1 - 1])
                            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            for i in range(len(selects)):
                                nums.remove(selects[i])
                                if selects[i] != 1:
                                    new_stack.append(self.stacks[selects[i] - 1])

                            for i in range(len(nums)):
                                print(self.map_cards[nums[i] - 1][0])
                                print(self.map_cards[nums[i] - 1][1])
                                pygame.display.flip()
                                self.screen.fill(self.settings.bg_color,
                                                 pygame.Rect(self.map_cards[nums[i] - 1][0],
                                                             self.map_cards[nums[i] - 1][1],
                                                             100, 220))
                                pygame.display.flip()
                                if len(self.stacks) < nums[i]:
                                    continue
                                time.sleep(1)
                                self.print_stack_on_left(self.stacks[nums[i] - 1])

                            time.sleep(2)
                            print("line 1364")
                            self.stacks.clear()
                            for i in range(len(new_stack)):
                                self.stacks.append(new_stack[i])

                            self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                            pygame.display.flip()
                            self.draw_cards(new_stack)
                            time.sleep(2)

                        else:

                            self.print_stack_on_left(self.stacks[selects[0] - 1])
                            time.sleep(1)

                            # THIS IS THE FINAL STACK, DISPLY IT!
                            print("CHECK ")
                            # Display the other card deck
                            print("size - " + str(len(self.stacks)))
                            for i in range(len(selects)):
                                self.print_stack_on_left(self.stacks[selects[i] - 1])
                                self.stacks.pop(selects[i] - 1)
                            print("size - " + str(len(self.stacks)))
                            self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                            pygame.display.flip()
                            self.draw_cards(self.stacks)
                            time.sleep(2)

                    else:
                        print("remaining 1")
                        print(len(self.stacks))
                        # Display remaining 1 cards
                        # Pop out the selected card stacks
                        j = 0
                        for i in range(len(selects)):
                            print(selects[i] - 1)
                            self.print_stack_on_left(self.stacks[selects[i] - 1 - j])
                            self.stacks.pop(selects[i] - 1 - j)
                            j += 1
                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        pygame.display.flip()
                        self.draw_cards(self.stacks)
                        time.sleep(2)
                        # NOW WE HAVE JUST ONE CARD REMAINING, WHICH IS THE REQUIRED STACK!!

                # If the selected 3 card stacks are not the desired set, DISPLAY remaining 2
                else:

                    for i in range(len(selects)):
                        print(self.map_cards[selects[i] - 1][0])
                        print(self.map_cards[selects[i] - 1][1])
                        pygame.display.flip()
                        self.screen.fill(self.settings.bg_color,
                                         pygame.Rect(self.map_cards[selects[i] - 1][0],
                                                     self.map_cards[selects[i] - 1][1],
                                                     100, 220))
                        pygame.display.flip()
                        time.sleep(1)

                        self.print_stack_on_left(self.stacks[selects[i] - 1])

                    j = 0
                    for i in range(len(selects)):
                        self.stacks.pop(selects[i] - 1 - j)
                        j += 1
                    print("size - " + str(len(self.stacks)))

                    self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                    pygame.display.flip()
                    self.draw_cards(self.stacks)

                    # SO NOW I HAVE 2 CARD STACKS, OKAY! PROCESS IT NOW

                    # Again ask to select 1 card stacks
                    # SELECT 1 CARD STACKS

                    selects.clear()
                    x = 200
                    y = 750

                    txt = font1.render("Select any 1 card ", True, (255, 10, 20))
                    self.screen.blit(txt, (700, 750))
                    pygame.display.flip()
                    while (True):
                        to_break = False

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.type == pygame.QUIT:
                                    sys.exit()

                                if event.key == pygame.K_1:
                                    selects.append(1)
                                    txt = font3.render(str(1), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_2:
                                    selects.append(2)
                                    txt = font3.render(str(2), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_3:
                                    selects.append(3)
                                    txt = font3.render(str(3), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_4:
                                    selects.append(4)
                                    txt = font3.render(str(4), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_5:
                                    selects.append(5)
                                    txt = font3.render(str(5), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_6:
                                    selects.append(6)
                                    txt = font3.render(str(6), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_7:
                                    selects.append(7)
                                    txt = font3.render(str(7), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_8:
                                    selects.append(8)
                                    txt = font3.render(str(8), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_9:
                                    selects.append(9)
                                    txt = font3.render(str(9), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                print(len(selects))
                                x += 100
                            if len(selects) == 1:
                                to_break = True
                                break

                        if to_break:
                            break

                    while True:
                        to_break = False
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.QUIT:
                                    sys.exit()
                                if event.key == pygame.K_KP_ENTER:
                                    to_break = True
                                    break
                        if to_break:
                            break

                            # we have made 5 selections now, ALSO CARD IS IN STACK - 5

                    stack_selected = False

                    for i in range(len(selects)):
                        if selects[i] == 1:
                            stack_selected = True
                    print("YOOOYOYO")
                    # 2 CARDS REMAINING
                    if stack_selected:

                        self.print_stack_on_left(self.stacks[1])

                        print("FIRST")
                        new_stack = []
                        # THIS IS THE FINAL STACK, DISPLY IT!
                        new_stack.append(self.stacks[1 - 1])
                        for i in range(len(selects)):
                            if selects[i] != 1:
                                new_stack.append(self.stacks[selects[i] - 1])
                        print("LINE 1535")
                        self.stacks.clear()
                        for i in range(len(new_stack)):
                            self.stacks.append(new_stack[i])

                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        pygame.display.flip()
                        self.draw_cards(new_stack)
                        time.sleep(2)

                    else:
                        self.print_stack_on_left(self.stacks[selects[0] - 1])
                        # THIS IS THE FINAL STACK, DISPLY IT!
                        # Display the other card deck
                        print("size - " + str(len(self.stacks)))

                        for i in range(len(selects)):
                            del self.stacks[selects[i] - 1]

                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        time.sleep(2)
                        pygame.display.flip()
                        self.draw_cards(self.stacks)
                        time.sleep(2)

            else:

                print("size - " + str(len(self.stacks)))

                for i in range(len(selects)):
                    print(self.map_cards[selects[i] - 1][0])
                    print(self.map_cards[selects[i] - 1][1])
                    pygame.display.flip()
                    self.screen.fill(self.settings.bg_color,
                                     pygame.Rect(self.map_cards[selects[i] - 1][0], self.map_cards[selects[i] - 1][1],
                                                 100, 220))
                    pygame.display.flip()
                    time.sleep(1)
                    self.print_stack_on_left(self.stacks[selects[i] - 1])

                tmp = self.stacks[5 - 1]

                j = 0
                for i in range(len(selects)):
                    self.stacks.pop(selects[i] - 1 - j)
                    j += 1

                tmp_stacks = []
                tmp_stacks.append(tmp)
                for stack in self.stacks:
                    if stack != tmp:
                        tmp_stacks.append(stack)

                self.stacks.clear()

                for stack in tmp_stacks:
                    self.stacks.append(stack)

                self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                pygame.display.flip()
                self.draw_cards(self.stacks)
                time.sleep(2)
                # NOW WE HAVE 4 CARDS REMAINING

                # ASK TO SELECT 3 cards and so on...

                # Again ask to select 2 card stacks
                # SELECT 2 CARD STACKS

                selects.clear()
                x = 200
                y = 750
                txt = font1.render("Select any 2 card ", True, (255, 10, 20))
                self.screen.blit(txt, (700, 750))
                pygame.display.flip()
                while (True):
                    to_break = False

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.type == pygame.QUIT:
                                sys.exit()

                            if event.key == pygame.K_1:
                                selects.append(1)
                                txt = font3.render(str(1), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_2:
                                selects.append(2)
                                txt = font3.render(str(2), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_3:
                                selects.append(3)
                                txt = font3.render(str(3), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_4:
                                selects.append(4)
                                txt = font3.render(str(4), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_5:
                                selects.append(5)
                                txt = font3.render(str(5), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_6:
                                selects.append(6)
                                txt = font3.render(str(6), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_7:
                                selects.append(7)
                                txt = font3.render(str(7), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_8:
                                selects.append(8)
                                txt = font3.render(str(8), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            elif event.key == pygame.K_9:
                                selects.append(9)
                                txt = font3.render(str(9), True, (255, 0, 0))
                                self.screen.blit(txt, (x, y))
                                pygame.display.flip()
                            print(len(selects))
                            x += 100
                        if len(selects) == 2:
                            to_break = True
                            break

                    if to_break:
                        break

                while True:
                    to_break = False
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.QUIT:
                                sys.exit()
                            if event.key == pygame.K_KP_ENTER:
                                to_break = True
                                break
                    if to_break:
                        break

                        # we have made 5 selections now, ALSO CARD IS IN STACK - 5

                stack_selected = False

                for i in range(len(selects)):
                    if selects[i] == 1:
                        stack_selected = True

                # 2 CARDS STACKS REMAINING
                if stack_selected:
                    # means now these 2 card stacks should be displayed
                    # display the selected stacks only

                    new_stack = []
                    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    new_stack.append(self.stacks[1 - 1])

                    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for i in range(len(selects)):
                        nums.remove(selects[i])
                        if selects[i] != 1:
                            new_stack.append(self.stacks[selects[i] - 1])

                    for i in range(len(nums)):
                        print(self.map_cards[nums[i] - 1][0])
                        print(self.map_cards[nums[i] - 1][1])
                        pygame.display.flip()
                        self.screen.fill(self.settings.bg_color,
                                         pygame.Rect(self.map_cards[nums[i] - 1][0],
                                                     self.map_cards[nums[i] - 1][1],
                                                     100, 220))
                        pygame.display.flip()
                        time.sleep(1)
                        if len(self.stacks) < nums[i]:
                            break
                        self.print_stack_on_left(self.stacks[nums[i] - 1])

                    self.stacks.clear()
                    for i in range(len(new_stack)):
                        self.stacks.append(new_stack[i])

                    self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                    pygame.display.flip()
                    self.draw_cards(new_stack)

                    # Again ask to select 1 card stacks
                    # SELECT 1 CARD STACKS

                    selects.clear()
                    x = 200
                    y = 750
                    txt = font1.render("Select any 1 card ", True, (255, 10, 20))
                    self.screen.blit(txt, (700, 750))
                    pygame.display.flip()
                    while (True):
                        to_break = False

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.type == pygame.QUIT:
                                    sys.exit()

                                if event.key == pygame.K_1:
                                    selects.append(1)
                                    txt = font3.render(str(1), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_2:
                                    selects.append(2)
                                    txt = font3.render(str(2), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_3:
                                    selects.append(3)
                                    txt = font3.render(str(3), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_4:
                                    selects.append(4)
                                    txt = font3.render(str(4), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_5:
                                    selects.append(5)
                                    txt = font3.render(str(5), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_6:
                                    selects.append(6)
                                    txt = font3.render(str(6), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_7:
                                    selects.append(7)
                                    txt = font3.render(str(7), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_8:
                                    selects.append(8)
                                    txt = font3.render(str(8), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_9:
                                    selects.append(9)
                                    txt = font3.render(str(9), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                print(len(selects))
                                x += 100
                            if len(selects) == 1:
                                to_break = True
                                break

                        if to_break:
                            break

                    while True:
                        to_break = False
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.QUIT:
                                    sys.exit()
                                if event.key == pygame.K_KP_ENTER:
                                    to_break = True
                                    break
                        if to_break:
                            break

                            # we have made 5 selections now, ALSO CARD IS IN STACK - 5

                    stack_selected = False

                    for i in range(len(selects)):
                        if selects[i] == 1:
                            stack_selected = True

                    # 2 CARDS REMAINING
                    if stack_selected:
                        self.print_stack_on_left(self.stacks[1])
                        new_stack = []
                        # THIS IS THE FINAL STACK, DISPLY IT!
                        new_stack.append(self.stacks[1 - 1])
                        for i in range(len(selects)):
                            if selects[i] != 1:
                                new_stack.append(self.stacks[selects[i] - 1])

                        self.stacks.clear()
                        for i in range(len(new_stack)):
                            self.stacks.append(new_stack[i])

                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        pygame.display.flip()
                        self.draw_cards(new_stack)
                        time.sleep(2)

                    else:

                        for i in range(len(selects)):
                            print(self.map_cards[selects[i] - 1][0])
                            print(self.map_cards[selects[i] - 1][1])
                            pygame.display.flip()
                            self.screen.fill(self.settings.bg_color,
                                             pygame.Rect(self.map_cards[selects[i] - 1][0],
                                                         self.map_cards[selects[i] - 1][1],
                                                         100, 220))
                            pygame.display.flip()
                            time.sleep(1)
                            self.print_stack_on_left(self.stacks[selects[i] - 1])

                            # THIS IS THE FINAL STACK, DISPLY IT!
                            print("CHECK ")
                            # Display the other card deck
                            print("size - " + str(len(self.stacks)))
                            for i in range(len(selects)):
                                self.stacks.pop(selects[i] - 1)
                            print("size - " + str(len(self.stacks)))

                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        pygame.display.flip()
                        self.draw_cards(self.stacks)
                        time.sleep(2)

                else:

                    for i in range(len(selects)):
                        print(self.map_cards[selects[i] - 1][0])
                        print(self.map_cards[selects[i] - 1][1])
                        pygame.display.flip()
                        self.screen.fill(self.settings.bg_color,
                                         pygame.Rect(self.map_cards[selects[i] - 1][0],
                                                     self.map_cards[selects[i] - 1][1],
                                                     100, 220))
                        pygame.display.flip()
                        time.sleep(1)
                        self.print_stack_on_left(self.stacks[selects[i] - 1])

                    time.sleep(2)
                    print(len(self.stacks))
                    # Display remaining 1 cards
                    # Pop out the selected card stacks
                    j = 0

                    for i in range(len(selects)):
                        print(selects[i] - 1)
                        self.stacks.pop(selects[i] - 1 - j)
                        j += 1
                    self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                    pygame.display.flip()
                    self.draw_cards(self.stacks)
                    time.sleep(2)

                    # HERE TWO CARDS ARE GETTING DISPLAYED, ASK TO CHOOSE ONE

                    selects.clear()
                    x = 200
                    y = 750

                    txt = font1.render("Select any 1 card ", True, (255, 10, 20))
                    self.screen.blit(txt, (700, 750))
                    pygame.display.flip()
                    while (True):
                        to_break = False

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.type == pygame.QUIT:
                                    sys.exit()

                                if event.key == pygame.K_1:
                                    selects.append(1)
                                    txt = font3.render(str(1), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_2:
                                    selects.append(2)
                                    txt = font3.render(str(2), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_3:
                                    selects.append(3)
                                    txt = font3.render(str(3), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_4:
                                    selects.append(4)
                                    txt = font3.render(str(4), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_5:
                                    selects.append(5)
                                    txt = font3.render(str(5), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_6:
                                    selects.append(6)
                                    txt = font3.render(str(6), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_7:
                                    selects.append(7)
                                    txt = font3.render(str(7), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_8:
                                    selects.append(8)
                                    txt = font3.render(str(8), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                elif event.key == pygame.K_9:
                                    selects.append(9)
                                    txt = font3.render(str(9), True, (255, 0, 0))
                                    self.screen.blit(txt, (x, y))
                                    pygame.display.flip()
                                print(len(selects))
                                x += 100
                            if len(selects) == 1:
                                to_break = True
                                break

                        if to_break:
                            break

                    while True:
                        to_break = False
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.QUIT:
                                    sys.exit()
                                if event.key == pygame.K_KP_ENTER:
                                    to_break = True
                                    break
                        if to_break:
                            break

                            # we have made 5 selections now, ALSO CARD IS IN STACK - 5

                    stack_selected = False

                    for i in range(len(selects)):
                        if selects[i] == 1:
                            stack_selected = True

                    # 2 CARDS REMAINING
                    if stack_selected:

                        new_stack = []
                        # THIS IS THE FINAL STACK, DISPLY IT!
                        new_stack.append(self.stacks[1 - 1])
                        for i in range(len(selects)):
                            if selects[i] != 1:
                                new_stack.append(self.stacks[selects[i] - 1])
                        print("HOOOOOOOOOOOOOOOOOOOO")

                        self.print_stack_on_left(self.stacks[1])

                        self.stacks.clear()
                        for i in range(len(new_stack)):
                            self.stacks.append(new_stack[i])

                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        pygame.display.flip()
                        self.draw_cards(new_stack)
                        time.sleep(2)

                    else:

                        for i in range(len(selects)):
                            print(self.map_cards[selects[i] - 1][0])
                            print(self.map_cards[selects[i] - 1][1])
                            pygame.display.flip()
                            self.screen.fill(self.settings.bg_color,
                                             pygame.Rect(self.map_cards[selects[i] - 1][0],
                                                         self.map_cards[selects[i] - 1][1],
                                                         100, 220))
                            pygame.display.flip()
                            time.sleep(1)
                            self.print_stack_on_left(self.stacks[selects[i] - 1])

                            # THIS IS THE FINAL STACK, DISPLY IT!
                            print("CHECK ")
                            # Display the other card deck
                            print("size - " + str(len(self.stacks)))
                            for i in range(len(selects)):
                                self.stacks.pop(selects[i] - 1)
                            print("size - " + str(len(self.stacks)))

                        self.screen.fill(self.settings.bg_color, pygame.Rect(200, 0, 1000, 1000))
                        pygame.display.flip()
                        self.draw_cards(self.stacks)
                        time.sleep(2)

                    # NOW WE HAVE JUST ONE CARD REMAINING, WHICH IS THE REQUIRED STACK!!


CardDisplay = CardGame()
initialize_deck()

CardDisplay.run_game()
