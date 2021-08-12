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
font3 = pygame.font.Font('Fonts/Walkway_Oblique_Black.ttf', 20)

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
    print("in the function : " + (s))
    ss = "".join(reversed(s))
    print("in the function : " + (ss))
    return ss


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
pos_y = 60

for i in range(27):
    if i != 0 and i % 3 == 0:
        pos_x = 400
        pos_y += 80
    num_img = font1.render(str(i + 1), True, (255, 100, 100))
    new_num = Numbers(num_img, pos_x, pos_y)
    number_group.add(new_num)
    pos_x += 200


class CardGame:
    """Overall class to manage Card Display."""

    step = 0
    counter = 0
    first_page_done = False
    number_chosen = 0

    first_column = 0
    second_column = 0
    third_column = 0

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
            # self.screen.fill(white, pygame.Rect(200, 0, 1200, 1200))

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
                        self.screen.fill((0, 0, 0), (50, 400, 250, 50))
                        txt = font2.render("You Chose " + str(pos + 1), True, (255, 200, 110))
                        self.screen.blit(txt, (50, 400))
                        pygame.display.flip()
                        break
                    pos += 1
            elif event.type == pygame.KEYDOWN:

                if event.type == pygame.QUIT:
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
                        number_chosen = self.number_chosen
                        r, c = Index_Card_Image(Cards_27[number_chosen])

                        self.CardSet.cards[r * 13 + c].rect.x += 125
                        self.screen.fill(self.settings.bg_color)

                        self.CardSet.cards[r * 13 + c].screen.blit(self.CardSet.cards[r * 13 + c].image,
                                                                   self.CardSet.cards[r * 13 + c].rect)
                        xx = self.CardSet.cards[r*13 + c].rect.x
                        yy = self.CardSet.cards[r*13 + c].rect.y
                        nm = font3.render(str(self.number_chosen + 1),True, (255,20,40))
                        self.screen.blit(nm, (xx+40, yy-20))
                        self._update_screen()
                        pygame.display.flip()

    def collect_cards(self):

        space = 0

        if self.step > 0:



        #FIRST COLUMN DETECTION
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

        #SECOND COLUMN DETECTION
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

        #THIRD COLUMN DETECTION
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

                time.sleep(0.4)
                self.screen.fill(self.settings.bg_color, pygame.Rect(x, 20, 100, del_y))
                del_y += 50
                if i == 7:
                    del_y += 400
                r, c = Index_Card_Image(Cards_27[i])
                self.CardSet.cards[r * 13 + c].blitmehere(10, space)
                space += 25
                pygame.display.flip()

                # TO_DO: add a part to remove the selected column
            time.sleep(0.4)


            pygame.display.flip()

            if self.first_column == 2:
                x = x_first
            elif self.second_column == 2:
                x = x_second
            else:
                 x = x_third
            del_y = 50
            for i in range(9, 18):

                time.sleep(0.4)
                self.screen.fill(self.settings.bg_color, pygame.Rect(x, 20, 100, del_y))
                del_y += 50
                if i == 16:
                    del_y += 300
                r, c = Index_Card_Image(Cards_27[i])
                self.CardSet.cards[r * 13 + c].blitmehere(40, space)
                space += 25
                pygame.display.flip()

            time.sleep(0.4)


            pygame.display.flip()

            del_y = 50
            if self.first_column == 3:
                x = x_first
            elif self.second_column == 3:
                x = x_second
            else:
                x = x_third
            for i in range(18, 27):
                time.sleep(0.4)
                self.screen.fill(self.settings.bg_color, pygame.Rect(x, 20, 100, del_y))
                del_y += 50
                if i == 25:
                    del_y += 300
                r, c = Index_Card_Image(Cards_27[i])
                self.CardSet.cards[r * 13 + c].blitmehere(10, space)
                space += 25
                pygame.display.flip()

            time.sleep(0.4)


            col1.clear()
            col2.clear()
            col3.clear()

            for i in range(9):
                col1.append(column1[i])
                col2.append(column2[i])
                col3.append(column3[i])

            time.sleep(0.2)

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
                self.CardSet.cards[r * 13 + c].blitme(var, 1)
                pygame.display.flip()
                time.sleep(0.5)

                # Column 2 Cards
                y += 25
                self.screen.fill((0, 0, 0), pygame.Rect(0, 0, 200, y))
                pygame.display.flip()
                r, c = Index_Card_Image(column2[var])
                self.CardSet.cards[r * 13 + c].blitme(var, 2)
                pygame.display.flip()
                time.sleep(0.5)

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
                self.CardSet.cards[r * 13 + c].blitme(var, 3)
                pygame.display.flip()
                time.sleep(0.5)

        if self.step >= 4:
            print(1)

            x = 250
            y = 25

            for var in range(9):
                # Column 1 Cards

                r, c = Index_Card_Image(column1[var])
                ok = True


                if (3 * var) == self.number_chosen:
                    ok = False
                if ok:
                    self.CardSet.cards[r * 13 + c].blitme(var, 1)
                    num = font3.render(str(var * 3 + 1), True, (0, 0, 0))
                    self.screen.blit(num, (x, y))

                # Column 2 Cards
                r, c = Index_Card_Image(column2[var])
                ok = True

                x += 300
                if (3 * var + 1) == self.number_chosen:
                    ok = False
                if ok:
                    self.CardSet.cards[r * 13 + c].blitme(var, 2)
                    num = font3.render(str(var * 3 + 2), True, (0, 0, 0))
                    self.screen.blit(num, (x, y))

                # Column 3 Cards
                r, c = Index_Card_Image(column3[var])
                ok = True

                x += 300
                if (3 * var + 2) == self.number_chosen:
                    ok = False
                if ok:
                    self.CardSet.cards[r * 13 + c].blitme(var, 3)
                    num = font3.render(str(var * 3 + 3), True, (0, 0, 0))
                    self.screen.blit(num, (x, y))
                pygame.display.flip()
                x = 250
                y += 50


CardDisplay = CardGame()
initialize_deck()
CardDisplay.run_game()
