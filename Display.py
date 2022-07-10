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
rectangle_big = pygame.image.load('images/rectangle_big.png').convert_alpha()
square_big = pygame.image.load('images/square_big.png').convert_alpha()
cone_big = pygame.image.load('images/cone_big.png').convert_alpha()
pentagon_big = pygame.image.load('images/pentagon_big.png').convert_alpha()
triangle_big = pygame.image.load('images/triangle_big.png').convert_alpha()
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
                
            if result == True:
                draw_text("The area equals to: {}".format(round(classes.Circle.area(InputBox.input1[-1]))), head_font, TEXT_COL, 500, 670)
                draw_text(classes.Circle.formula(), head_font, TEXT_COL, 100, 50)
            
            pygame.display.flip()
            clock.tick(30)

    def square_event():
        '''
        This functions display the interface and background calculations for each geometric figure.
        '''
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
            screen.blit(square_big, (300, 150))
            draw_text("Side Lenght:", head_font, TEXT_COL, 100, 520)

            if calculate_button.draw(screen):
                result = True
                
            if result == True:
                draw_text("The area equals to: {}".format(round(classes.Square.area(InputBox.input1[-1]))), head_font, TEXT_COL, 500, 670)
                draw_text(classes.Square.formula(), head_font, TEXT_COL, 100, 50)
            
            pygame.display.flip()
            clock.tick(30)
    
    def rectangle_event():
        '''
        This functions display the interface and background calculations for each geometric figure.
        '''
        clock = pygame.time.Clock()
        input_box1 = InputBox.InputBox(100, 450, 140, 32)
        input_box2 = InputBox.InputBox(100, 550, 140, 32)
        input_boxes = [input_box1, input_box2]
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
            screen.blit(rectangle_big, (300, 150))
            draw_text("Length:", head_font, TEXT_COL, 100, 420)
            draw_text("Width:", head_font, TEXT_COL, 100, 520)

            if calculate_button.draw(screen):
                result = True
                
            if result == True:
                draw_text("The area equals to: {}".format(round(classes.Rectangle.area(InputBox.input1[-2], InputBox.input1[-1]))), head_font, TEXT_COL, 500, 670)
                draw_text(classes.Rectangle.formula(), head_font, TEXT_COL, 100, 50)
            
            pygame.display.flip()
            clock.tick(30)        
    
    def cone_event():
        '''
        This functions display the interface and background calculations for each geometric figure.
        '''
        clock = pygame.time.Clock()
        input_box1 = InputBox.InputBox(100, 450, 140, 32)
        input_box2 = InputBox.InputBox(100, 550, 140, 32)
        input_boxes = [input_box1, input_box2]
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
            screen.blit(cone_big, (300, 150))
            draw_text("Radius:", head_font, TEXT_COL, 100, 420)
            draw_text("Height:", head_font, TEXT_COL, 100, 520)

            if calculate_button.draw(screen):
                result = True
                
            if result == True:
                draw_text("The area equals to: {}".format(round(classes.Cone.area(InputBox.input1[-2], InputBox.input1[-1]))), head_font, TEXT_COL, 500, 670)
                draw_text(classes.Cone.formula(), head_font, TEXT_COL, 100, 50)
            
            pygame.display.flip()
            clock.tick(30)

    def triangle_event():
        '''
        This functions display the interface and background calculations for each geometric figure.
        '''
        clock = pygame.time.Clock()
        input_box1 = InputBox.InputBox(100, 450, 140, 32)
        input_box2 = InputBox.InputBox(100, 550, 140, 32)
        input_boxes = [input_box1, input_box2]
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
            screen.blit(triangle_big, (300, 150))
            draw_text("Base:", head_font, TEXT_COL, 100, 420)
            draw_text("Height:", head_font, TEXT_COL, 100, 520)

            if calculate_button.draw(screen):
                result = True
                
            if result == True:
                draw_text("The area equals to: {}".format(round(classes.Triangle.area(InputBox.input1[-2], InputBox.input1[-1]))), head_font, TEXT_COL, 500, 670)
                draw_text(classes.Triangle.formula(), head_font, TEXT_COL, 100, 50)
            
            pygame.display.flip()
            clock.tick(30) 

    def pentagon_event():
        '''
        This functions display the interface and background calculations for each geometric figure.
        '''
        clock = pygame.time.Clock()
        input_box1 = InputBox.InputBox(100, 450, 140, 32)
        input_box2 = InputBox.InputBox(100, 550, 140, 32)
        input_boxes = [input_box1, input_box2]
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
            screen.blit(pentagon_big, (300, 150))
            draw_text("Perimeter:", head_font, TEXT_COL, 100, 420)
            draw_text("Apothem:", head_font, TEXT_COL, 100, 520)

            if calculate_button.draw(screen):
                result = True
                
            if result == True:
                draw_text("The area equals to: {}".format(round(classes.Pentagon.area(InputBox.input1[-2], InputBox.input1[-1]))), head_font, TEXT_COL, 500, 670)
                draw_text(classes.Pentagon.formula(), head_font, TEXT_COL, 100, 50)
            
            pygame.display.flip()
            clock.tick(30)               