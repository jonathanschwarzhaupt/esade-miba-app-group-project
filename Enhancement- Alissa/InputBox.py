import pygame

#Class for all input boxes in the shapes menu
class InputBox():
    def __init__(self, x, y, w, h, text=''):
        """Initialize an InputBox object."""
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('red')
        self.color_active = pygame.Color('white')
        self.text = text
        self.font = pygame.font.SysFont('monospace', 20,0)
        self.txt_surface = self.font.render(text, True, self.color_active)
        self.active = False
        self.done = False
    
    def handle_event(self, event):
        """Handle a pygame event."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.done = True
                    """"Deleting the text""""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, self.color)
