import pygame
from menu import *

"""This is the main game class. It handles the game loop and the main menu."""
class Game():
    def __init__(self):
        pygame.init()
        """Initialize the game."""
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        """"Creating the main menus"""
        self.main_menu = MainMenu(self)
        self.shapes_menu = ShapesMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.shapes = ShapesMenu(self)
        self.square= Square(self)
        self.rectangle = Rectangle(self)
        self.triangle = Triangle(self)
        self.circle = Circle(self)
        #self.input_box = InputBox(self)
        self.curr_menu = self.main_menu

    """"This is the main function. It runs the game loop and the main menu."""

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            """Drawing the current menu"""
            self.draw_text('Explanations', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.draw_text("You can choose a shape and input",12, self.DISPLAY_W/2, self.DISPLAY_H/2+20)
            self.draw_text("its dimensions to return its area",12, self.DISPLAY_W/2, self.DISPLAY_H/2+30)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()


    """"This is the main function. It runs the game loop and the main menu."""
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    """"Reseting the keys."""
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
