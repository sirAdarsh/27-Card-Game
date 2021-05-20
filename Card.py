"""Module to represent a card."""

class Card:

    def __init__(self, card_game):
        """Initialize attributes to represent a card."""
        self.image = None
        self.name = ''
        self.color = ''

        self.screen = card_game.screen

        # Show each card at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)
