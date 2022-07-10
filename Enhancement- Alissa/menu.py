from configparser import MAX_INTERPOLATION_DEPTH
import pygame
from pygame.rect import Rect

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class InputBox():
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('red')
        self.color_active = pygame.Color('white')
        self.text = text
        self.font = pygame.font.SysFont('monospace', 20,0)
        self.txt_surface = self.font.render(text, True, self.color_active)
        self.active = False
        self.done = False
    
    def handle_event(self, event):
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
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, self.color)
        
    def update(self):
        width = max(180, self.txt_surface.get_width()+10)
        self.rect.width = width
        
    def draw(self,screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.shapesx, self.shapesy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Explanations", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Shapes",20, self.shapesx, self.shapesy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.shapesx + self.offset, self.shapesy)
                self.state = 'Shapes'
            elif self.state == "Shapes":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.shapesx + self.offset, self.shapesy)
                self.state = 'Shapes'
            elif self.state == 'Shapes':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == "Shapes":
                self.game.curr_menu = self.game.shapes
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

class ShapesMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Square'
        self.squarex, self.squarey = self.mid_w, self.mid_h + 10
        self.rectanglex, self.rectangley = self.mid_w, self.mid_h + 30
        self.trianglex, self.triangley, = self.mid_w, self.mid_h + 50
        self.circlex, self.circley = self.mid_w, self.mid_h+70
        self.cursor_rect.midtop = (self.squarex + self.offset, self.squarey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose your shape', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Square', 15, self.squarex,self.squarey)
            self.game.draw_text('Rectangle', 15, self.rectanglex,self.rectangley)
            self.game.draw_text('Triangle', 15, self.trianglex,self.triangley)
            self.game.draw_text('Circle', 15, self.circlex,self.circley)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        self.move_cursor()
        if self.game.DOWN_KEY:
            if self.state == 'Square':
                self.cursor_rect.midtop = (self.rectanglex + self.offset, self.rectangley)
                self.state = 'Rectangle'
            elif self.state == 'Rectangle':
                self.cursor_rect.midtop = (self.trianglex + self.offset, self.triangley)
                self.state = 'Triangle'
            elif self.state == 'Triangle':
                self.cursor_rect.midtop = (self.circlex + self.offset, self.circley)
                self.state = 'Circle'
            elif self.state == "Circle":
                self.cursor_rect.midtop = (self.squarex + self.offset, self.squarey)
                self.state = "Square"

        elif self.game.UP_KEY:
            if self.state == 'Square':
                self.cursor_rect.midtop = (self.circlex + self.offset, self.circley)
                self.state = 'Circle'
            elif self.state == 'Circle':
                self.cursor_rect.midtop = (self.trianglex + self.offset, self.triangley)
                self.state = 'Triangle'
            elif self.state == 'Triangle':
                self.cursor_rect.midtop = (self.rectanglex + self.offset, self.rectangley)
                self.state = 'Rectangle'
            elif self.state == "Rectangle":
                self.cursor_rect.midtop = (self.squarex + self.offset, self.squarey)
                self.state = "Square"
  
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Square':
                self.state = 'Rectangle'
                self.cursor_rect.midtop = (self.rectanglex + self.offset, self.rectangley)
            elif self.state == 'Rectangle':
                self.state = 'Triangle'
                self.cursor_rect.midtop = (self.trianglex + self.offset, self.triangley)
            elif self.state == 'Triangle':
                self.state = 'Circle'
                self.cursor_rect.midtop = (self.circlex + self.offset, self.circley)
            elif self.state == "Circle":
                self.state = "Square"
                self.cursor_rect.midtop = (self.squarex + self.offset, self.squarey)
        elif self.game.START_KEY:
            if self.state == 'Square':
                self.game.curr_menu = self.game.square
            elif self.state == 'Rectangle':
                self.game.curr_menu = self.game.rectangle
            elif self.state == 'Triangle':
                self.game.curr_menu = self.game.triangle
            elif self.state == "Circle":
                self.game.curr_menu = self.game.circle
            self.run_display = False


class Square(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Side'
        self.sidex, self.sidey = self.mid_w  , self.mid_h +10 
        self.calcx, self.calcy = self.mid_w , self.mid_h +50
        self.cursor_rect.midtop = (self.sidex + self.offset, self.sidey)
        
    def __init__(self, x, y, w, h, text=''):
        InputBox.__init__(x, y, w, h, text='')


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.shapes_menu
                self.run_display = False
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Input the values', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text('Side', 15, self.sidex-40, self.sidey )
            self.game.draw_text('Calculate',15, self.calcx, self.calcy)
            self.draw_cursor()
            self.blit_screen()


    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.shapes_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Side':
                self.state = 'Calculate'
                self.cursor_rect.midtop = (self.calcx + self.offset, self.calcy)
            elif self.state == 'Calculate':
                self.state = 'Side'
                self.cursor_rect.midtop = (self.sidex + self.offset, self.sidey)

    

class Rectangle(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Calculate'
        self.widthx, self.widthy = self.mid_w -80 , self.mid_h +10 
        self.heightx, self.heighty = self.mid_w -80, self.mid_h +50
        self.calcx, self.calcy = self.mid_w+50, self.mid_h +80
        self.cursor_rect.midtop = (self.widthx + self.offset, self.widthy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.shapes_menu
                self.run_display = False
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Input the values', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text('Width', 15, self.widthx, self.widthy )
            self.game.draw_text('Height', 15, self.heightx, self.heighty)
            self.game.draw_text('Press enter to calculate',15, self.calcx, self.calcy)
            self.draw_cursor()
            self.blit_screen()   


    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.shapes_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Width':
                self.state = 'Height'
                self.cursor_rect.midtop = (self.heightx + self.offset, self.heighty)
            elif self.state == 'Height':
                self.state = 'Width'
                self.cursor_rect.midtop = (self.widthx + self.offset, self.widthy)
                self.run_display = False
        elif self.game.START_KEY:           
            if self.state == 'Width':
                self.game.curr_menu = self.game.rectangle_width
            elif self.state == 'Height':
                self.game.curr_menu = self.game.rectangle_height
            self.run_display = False

class Triangle(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Calculate'
        self.basex, self.basey = self.mid_w -80 , self.mid_h +10 
        self.heightx, self.heighty = self.mid_w -80, self.mid_h +50
        self.calcx, self.calcy = self.mid_w+50, self.mid_h +80
        self.cursor_rect.midtop = (self.basex + self.offset, self.basey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.shapes_menu
                self.run_display = False
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Input the values', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text('Base', 15, self.basex, self.basey )
            self.game.draw_text('Height', 15, self.heightx, self.heighty)
            self.game.draw_text('Press enter to calculate',15, self.calcx, self.calcy)
            self.draw_cursor()
            self.blit_screen()   

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.shapes_menu
            self.run_display = False

class Circle(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Calculate'
        self.radiusx, self.radiusy = self.mid_w -80 , self.mid_h +10 
        self.calcx, self.calcy = self.mid_w+50, self.mid_h +50
        self.cursor_rect.midtop = (self.radiusx + self.offset, self.radiusy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.shapes_menu
                self.run_display = False
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Input the values', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text('Radius', 15, self.radiusx, self.radiusy )
            self.game.draw_text('Press enter to calculate',15, self.calcx, self.calcy)
            self.draw_cursor()
            self.blit_screen()   
            


    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.shapes_menu
            self.run_display = False



