"""Module to represent a cards set, and individual pieces."""

from CardSheet import CardSheet


class CardSet:

    def __init__(self, card_game):
        """Initialize attributes to represent the overall cards."""

        self.card_game = card_game
        self.cards = []
        self._load_cards()

    def _load_cards(self):
        pass

    
    def _load_cards(self):
        """Builds the overall set:
        - Loads images from the card sheet.
        - Adds each card to the list self.pieces.
        """
        filename = 'images/cards.png'
        card_cs = CardSheet(filename)

        # Load all cards images.
        card_images = card_cs.load_grid_images(5, 13, x_margin=0,
                x_padding=0, y_margin=0, y_padding=0)

        # Create a new Piece object for every image.
        for image in card_images:
            card = Cards(self.card_game)
            card.image = image
            self.cards.append(card)
        
class Cards:
    def __init__(self, card_game):
        super().__init__()

        self.image = None
        self.name = ''
        self.color = ''

        self.screen = card_game.screen

        # Start each card off at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self, i, j):
        """Draw the card at its current location."""
        self.rect = self.image.get_rect()
        self.rect.y = 20 + 50*i
        self.rect.x = 300 + 300*(j-1)
        self.screen.blit(self.image, self.rect)

    def blitmehere(self, pos_x, pos_y):
        """Draw the card at position (x,y) on the screen"""
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.screen.blit(self.image, self.rect)

    def moveright(self):
        """Move the card to right."""
        self.rect = self.image.get_rect()
        self.rect.x += 1
        self.screen.blit(self.image, self.rect)
