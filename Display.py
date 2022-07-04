import pygame
import classes
import InputBox
import button



# Parameters
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#define fonts
head_font = pygame.font.SysFont("arialblack", 20, italic=False)

#define colours
TEXT_COL = (0, 0, 0)

# Resources
calculate_img = pygame.image.load('images/calculate_button.jpeg').convert_alpha()
calculate_img = pygame.image.load('images/calculate_button.jpeg').convert_alpha()
sphere_big = pygame.image.load('images/sphere_big.png').convert_alpha()
retry_img = pygame.image.load('images/retry_img.png').convert_alpha()

calculate_button = button.Button(80, 620, calculate_img, 0.5)
retry_button = button.Button(100, 660, calculate_img, 0.5)


# Draw text function
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

class Display():
    '''
    This functions display the interface and background calculations for each geometric figure.
    '''
    def sphere_event():
        clock = pygame.time.Clock()
        input_box1 = InputBox.InputBox(100, 550, 140, 32)
        input_boxes = [input_box1]
        done = False
        result = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            screen.fill((255, 255, 255))
            for box in input_boxes:
                box.draw(screen)
            screen.blit(sphere_big, (300, 150))
            draw_text("Radius:", head_font, TEXT_COL, 100, 520)

            if calculate_button.draw(screen):
                result = True
                #print(InputBox.input1[-1])
                #print(classes.Circle.area(InputBox.input1[-1]))
                
            if result == True:
                draw_text("The area equals to: {}".format(round(classes.Circle.area(InputBox.input1[-1]))), head_font, TEXT_COL, 500, 670)
                draw_text(classes.Circle.formula(), head_font, TEXT_COL, 120, 70)
            
            pygame.display.flip()
            clock.tick(30)
        
        
    def square_event():
        clock = pygame.time.Clock()
        input_box1 = InputBox.InputBox(100, 450, 140, 32)
        input_box2 = InputBox.InputBox(100, 550, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            screen.fill((255, 255, 255))
            for box in input_boxes:
                box.draw(screen)
            screen.blit(sphere_big, (300, 100))
            draw_text("Diameter:", head_font, TEXT_COL, 100, 420)
            draw_text("Radius:", head_font, TEXT_COL, 100, 520)

            if calculate_button.draw(screen):
                print(InputBox.input1[-1])
                #classes.Circle.area(InputBox.input1[-1])
                classes.Circle.area()

            pygame.display.flip()
            clock.tick(30)



# Get last input of print in terminal
#for line in sys.stdin:
#    tmp = line.strip()
#   print(tmp) 
