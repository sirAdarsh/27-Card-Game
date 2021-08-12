import pydealer
import sys
import pygame
import time
from settings import Settings
from CardSet import CardSet

pygame.init()
# Font for text
font1 = pygame.font.Font('Fonts/Walkway_SemiBold.ttf', 32)
font2 = pygame.font.Font('Fonts/Sansation-Bold.ttf', 40)
font3 = pygame.font.Font('Fonts/Walkway_Oblique_Black.ttf', 20)

# Deck of 52 Cards
deck = pydealer.Deck()
deck.shuffle()
Cards_52 = deck.deal(52)


def number_on_card(c):
    return c + 1


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
    step = 0

    side_x = 0
    side_y = 0

    draws = [(300, 20), (500, 20), (700, 20), (900, 20), (1100, 20), (300, 340), (500, 340), (700, 340), (900, 340),
             (1100, 340), (200, 620), (
                 400, 620), (600, 620), (800, 620), (1000, 620)]

    total_stacks_made = 0

    stacks_of_cards = []

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("52 Card Trick")
        self.CardSet = CardSet(self)

    def run_game(self):

        while True:
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    self.step += 1
                    self.update_screen()

    def card_transition(self, Card, init_x, init_y):
        r, c = Index_Card_Image(Card)
        self.CardSet.cards[r * 13 + c].blitmehere(init_x+120, init_y)
        pygame.display.flip()
        time.sleep(0.5)
        self.screen.fill(self.settings.bg_color, (init_x+120, init_y, 100, 300))
        pygame.display.flip()

    def update_screen(self):
        if self.step == 1:
            # display 52 cards on top left
            x = 20
            y = 10
            index = 0
            self.screen.fill(self.settings.bg_color)
            time.sleep(0.5)
            pygame.display.flip()

            for i in range(52):
                r, c = Index_Card_Image(Cards_52[i])
                self.CardSet.cards[r * 13 + c].blitmehere(x, y)
                pygame.display.flip()
                y += 12
                time.sleep(0.01)

        if self.step == 2:
            # Now distribute the 52 cards into stacks

            cards_taken = 0
            stacks = 0

            self.side_x = 20
            self.side_y = 10
            cards_printed = 0

            remaining_cards_after_dist = []

            for i in range(0, 52):
                # current card
                r, c = Index_Card_Image(Cards_52[i])
                num_on_card = number_on_card(c)

                print(i)

                to_break = False

                if cards_taken == 0:

                    temp_stack = []

                    print(i)
                    time.sleep(0.4)
                    x, y = self.draws[stacks]

                    minimum_y = y

                    print(x)
                    for j in range(num_on_card, 14):

                        cards_remaining = 52 - cards_printed

                        print(x, y)

                        if i > 51:
                            to_break = True
                            txt = font3.render('Insufficient Cards for the stack', True, (255, 0, 0))
                            self.screen.blit(txt, (400, 700))
                            pygame.display.flip()
                            time.sleep(0.4)
                            # display this set of cards on the left, unflipped

                            self.screen.fill(self.settings.bg_color, (x, minimum_y, 200, 500))
                            pygame.display.flip()
                            print("HERE?")
                            time.sleep(0.4)
                            # display on left
                            self.side_x = 20

                            self.side_y = 10

                            Cards_52.empty()

                            for card in temp_stack:
                                Cards_52.insert(card)
                                r, c = Index_Card_Image(card)
                                self.CardSet.cards[r * 13 + c].blitmehere(self.side_x, self.side_y)
                                self.side_y += 12
                                time.sleep(0.3)
                                pygame.display.flip()
                            time.sleep(0.4)
                            self.screen.fill(self.settings.bg_color, (400, 700, 300, 50))
                            pygame.display.flip()
                            print(len(Cards_52))
                            break

                        self.screen.fill(self.settings.bg_color, (self.side_x, self.side_y, 100, 12))
                        if i == 51:
                            self.screen.fill(self.settings.bg_color, (self.side_x, self.side_y, 100, 200))
                            self.card_transition(Cards_52[i], self.side_x, self.side_y)
                            self.side_x = 20

                            self.side_y = 10
                        else:
                            self.card_transition(Cards_52[i], self.side_x, self.side_y)

                        r, c = Index_Card_Image(Cards_52[i])
                        self.CardSet.cards[r * 13 + c].blitmehere(x, y)
                        pygame.display.flip()
                        temp_stack.append(Cards_52[i])

                        pygame.display.flip()
                        cards_printed += 1

                        if j == num_on_card:
                            time.sleep(0.5)

                        time.sleep(0.05)

                        self.side_y += 12

                        i += 1
                        y += 12
                        time.sleep(0.3)
                        cards_taken += 1

                        if j == 13:
                            # Reverse the stack and show flipped
                            tmp_x = x
                            tmp_y = y
                            temp_stack.reverse()
                            x, y = self.draws[stacks]
                            self.screen.fill(self.settings.bg_color, (x, y, 100, 300))
                            pygame.display.flip()
                            time.sleep(0.2)
                            for k in temp_stack:
                                r, c = Index_Card_Image(k)
                                # displaying it back-side
                                self.CardSet.cards[4 * 13 + 2].blitmehere(tmp_x, tmp_y)
                                pygame.display.flip()
                                tmp_y -= 12
                            self.stacks_of_cards.append(temp_stack)

                    stacks += 1
                if to_break:
                    break

                cards_taken -= 1

        if self.step == 3:
            print("asking to select 3 ")
            print(len(self.stacks_of_cards))

            txt = font1.render("Select any 3 card stacks", True, (255, 10, 20))
            self.screen.blit(txt, (450, 700))
            pygame.display.flip()

            x = 200
            y = 750

            selects = []

            while 1:
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
                        elif event.key == pygame.K_F10:
                            selects.append(10)
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

            while 1:
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
            print("are we here?")
            not_selected = [i for i in range(0, len(self.stacks_of_cards))]

            print(not_selected)
            selects.reverse()
            for select in selects:
                # disappear the stack, and display it on the left
                del not_selected[select - 1]

            for not_sel in not_selected:
                print(not_sel)
                x, y = self.draws[not_sel]
                print(x, y)
                self.screen.fill(self.settings.bg_color, (x, y, 100, 312))
                pygame.display.flip()
                time.sleep(1.5)
                for card in self.stacks_of_cards[not_sel]:
                    r, c = Index_Card_Image(card)
                    self.CardSet.cards[r * 13 + c].blitmehere(self.side_x, self.side_y)
                    self.side_y += 12
                    pygame.display.flip()
                    time.sleep(0.1)
                    Cards_52.insert(card)

            time.sleep(1)
            self.screen.fill(self.settings.bg_color, (200, 0, 1200, 1200))
            pygame.display.flip()

            three_stacks = []

            idx = 0

            pos_x_1st_stack = 0
            pos_x_2nd_stack = 0
            pos_x_3rd_stack = 0
            pos_y_1st_stack = 0
            pos_y_2nd_stack = 0
            pos_y_3rd_stack = 0

            for select in selects:
                x, y = self.draws[idx]
                stack_card = []
                for card in self.stacks_of_cards[select - 1]:
                    stack_card.append(card)
                    r, c = Index_Card_Image(card)
                    print("oyw")
                    # self.CardSet.cards[r * 13 + c].blitmehere(x, y)
                    self.CardSet.cards[4 * 13 + 2].blitmehere(x, y)
                    pygame.display.flip()
                    y += 12
                    time.sleep(0.1)
                y -= 12
                if idx == 0:
                    pos_x_1st_stack = x
                    pos_y_1st_stack = y
                elif idx == 1:
                    pos_x_2nd_stack = x
                    pos_y_2nd_stack = y
                else:
                    pos_x_3rd_stack = x
                    pos_y_3rd_stack = y
                print(stack_card[len(stack_card) - 1])
                three_stacks.append(stack_card)
                idx += 1

            # Ask to select 2 card stacks

            txt = font3.render('Choose any two stacks (from 1,2,3) ', True, (255, 0, 0))
            self.screen.blit(txt, (400, 700))
            pygame.display.flip()

            selects.clear()

            print(three_stacks[0
                  ])

            print('len of cards_52', len(Cards_52))
            x = 500
            y = 600
            while 1:
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
                        elif event.key == pygame.K_F10:
                            selects.append(10)
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

            self.screen.fill(self.settings.bg_color, pygame.Rect(400, 600, 400, 400))
            pygame.display.flip()

            side_x = 20
            side_y = 10

            index_card_52 = 0

            hidden_stack = [1, 2, 3]

            for select in selects:

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

                print('  ; ' + str(len(three_stacks[select - 1])))
                if select == 1:
                    hidden_stack.remove(1)
                    # print('  ; '+ len(three_stacks[0]))
                    r, c = Index_Card_Image(three_stacks[0][len(three_stacks[0]) - 1])
                    print("oyw")
                    self.CardSet.cards[r * 13 + c].blitmehere(pos_x_1st_stack, pos_y_1st_stack)
                    # self.CardSet.cards[4 * 13 + 2].blitmehere(x, y)
                    pygame.display.flip()

                    here_x = pos_x_1st_stack
                    here_y = pos_y_1st_stack + 30

                    time.sleep(0.5)

                    number = number_on_card(c)
                    for card_number in range(0, number):
                        self.screen.fill(self.settings.bg_color, pygame.Rect(side_x, side_y, 100, 12))
                        pygame.display.flip()
                        side_y += 12
                        time.sleep(0.1)
                        print('len of cards_52', len(Cards_52))
                        r, c = Index_Card_Image(Cards_52[index_card_52])
                        self.CardSet.cards[r * 13 + c].blitmehere(here_x, here_y)
                        pygame.display.flip()
                        here_y += 12
                        index_card_52 += 1
                        time.sleep(0.1)

                if select == 2:
                    hidden_stack.remove(2)
                    r, c = Index_Card_Image(three_stacks[1][len(three_stacks[1]) - 1])
                    print("oyw")
                    self.CardSet.cards[r * 13 + c].blitmehere(pos_x_2nd_stack, pos_y_2nd_stack)
                    # self.CardSet.cards[4 * 13 + 2].blitmehere(x, y)
                    pygame.display.flip()

                    here_x = pos_x_2nd_stack
                    here_y = pos_y_2nd_stack + 30

                    time.sleep(0.5)

                    number = number_on_card(c)
                    for card_number in range(0, number):
                        self.screen.fill(self.settings.bg_color, pygame.Rect(side_x, side_y, 100, 12))
                        pygame.display.flip()
                        side_y += 12
                        time.sleep(0.1)
                        print('len of cards_52', len(Cards_52))
                        r, c = Index_Card_Image(Cards_52[index_card_52])
                        self.CardSet.cards[r * 13 + c].blitmehere(here_x, here_y)
                        pygame.display.flip()
                        here_y += 12
                        index_card_52 += 1
                        time.sleep(0.1)

                if select == 3:
                    hidden_stack.remove(3)
                    r, c = Index_Card_Image(three_stacks[2][len(three_stacks[2]) - 1])
                    print("oyw")
                    self.CardSet.cards[r * 13 + c].blitmehere(pos_x_3rd_stack, pos_y_3rd_stack)
                    # self.CardSet.cards[4 * 13 + 2].blitmehere(x, y)
                    pygame.display.flip()

                    here_x = pos_x_3rd_stack
                    here_y = pos_y_3rd_stack + 30

                    time.sleep(0.5)

                    number = number_on_card(c)
                    for card_number in range(0, number):
                        self.screen.fill(self.settings.bg_color, pygame.Rect(side_x, side_y, 100, 12))
                        pygame.display.flip()
                        side_y += 12
                        time.sleep(0.1)
                        r, c = Index_Card_Image(Cards_52[index_card_52])
                        self.CardSet.cards[r * 13 + c].blitmehere(here_x, here_y)
                        pygame.display.flip()
                        here_y += 12
                        index_card_52 += 1
                        time.sleep(0.1)

                time.sleep(0.1)

            print(Cards_52[0])

            # Removing 10 cards
            s = 'TENNUMBERS'

            here_x = pos_x_2nd_stack
            here_y = 600

            idx = 0
            str_x = here_x + 10
            str_y = here_y + 150
            for card_number in range(10):

                # ENTER- listener
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

                self.screen.fill(self.settings.bg_color, pygame.Rect(side_x, side_y, 100, 12))
                pygame.display.flip()
                side_y += 12
                time.sleep(0.1)
                r, c = Index_Card_Image(Cards_52[index_card_52])
                self.CardSet.cards[r * 13 + c].blitmehere(here_x, here_y)
                pygame.display.flip()
                here_x += 25
                time.sleep(0.5)
                index_card_52 += 1
                txt = font2.render(s[idx], True, (255, 10, 20))
                self.screen.blit(txt, (str_x, str_y))
                pygame.display.flip()
                str_x += 30
                idx += 1

            here_x = pos_x_3rd_stack + 150
            here_y = 200

            r, c = Index_Card_Image(three_stacks[hidden_stack[0] - 1][len(three_stacks[hidden_stack[0] - 1]) - 1])
            number = number_on_card(c)

            total_card = 0

            for card_number in range(0, number):
                if card_number == number - 1:
                    self.screen.fill(self.settings.bg_color, pygame.Rect(side_x, side_y, 100, 200))
                self.screen.fill(self.settings.bg_color, pygame.Rect(side_x, side_y, 100, 12))
                pygame.display.flip()
                side_y += 12
                time.sleep(0.1)
                r, c = Index_Card_Image(Cards_52[index_card_52])
                self.CardSet.cards[r * 13 + c].blitmehere(here_x, here_y)
                pygame.display.flip()
                here_y += 30
                index_card_52 += 1
                time.sleep(0.5)
                total_card += 1

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

            time.sleep(0.5)
            txt = font2.render("Total Card =  " + str(total_card), True, (255, 10, 20))
            self.screen.blit(txt, (900, 750))
            pygame.display.flip()

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

            # Flipping the last card of the hidden stack!

            r, c = Index_Card_Image(three_stacks[hidden_stack[0] - 1][len(three_stacks[hidden_stack[0] - 1]) - 1])
            print("oyw")
            pos_x = 0
            pos_y = 0
            if hidden_stack[0] == 1:
                pos_x = pos_x_1st_stack
                pos_y = pos_y_1st_stack
            if hidden_stack[0] == 2:
                pos_x = pos_x_2nd_stack
                pos_y = pos_y_2nd_stack
            if hidden_stack[0] == 3:
                pos_x = pos_x_3rd_stack
                pos_y = pos_y_3rd_stack

            self.CardSet.cards[r * 13 + c].blitmehere(pos_x, pos_y)
            pygame.display.flip()


CardDisplay = CardGame()
CardDisplay.run_game()
