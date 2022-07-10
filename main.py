import pygame
import button
import InputBox
import music
import classes
import Display
import music

pygame.init()

#load music
music.play_music('music.mp3')

#create game window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ESADE - Geometric Game")
pygame.display.set_icon(pygame.image.load("images/logo_icon.png"))

#game variables
game_paused = False
menu_state = "main"


#define fonts
head_font = pygame.font.SysFont("arialblack", 20, italic=False)

#define colours
TEXT_COL = (0, 0, 0)

#load button images
start_img = pygame.image.load("images/button_start.png").convert_alpha()
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
logo_img = pygame.image.load('images/logo2.jpg').convert_alpha()

sphere_img = pygame.image.load('images/sphere_img.png').convert_alpha()
cone_img = pygame.image.load('images/cone_img.png').convert_alpha()
hexagon_img = pygame.image.load('images/hexagon_img.png').convert_alpha()
pentagon_img = pygame.image.load('images/pentagon_img.png').convert_alpha()
square_img = pygame.image.load('images/square_img.png').convert_alpha()
triangle_img = pygame.image.load('images/triangle_img.png').convert_alpha()
rectangle_img = pygame.image.load('images/rectangle_img.png').convert_alpha()

#create button instances
start_button = button.Button(370, 500, start_img, 1)
resume_button = button.Button(350, 200, resume_img, 1)
options_button = button.Button(350, 350, options_img, 1)
quit_button = button.Button(350, 500, quit_img, 1)
video_button = button.Button(300, 150, video_img, 1)
audio_button = button.Button(300, 300, audio_img, 1)
keys_button = button.Button(300, 450, keys_img, 1)
back_button = button.Button(300, 600, back_img, 1)

sphere_button = button.Button(200, 350, sphere_img, 1)
cone_button = button.Button(425, 350, cone_img, 1)
pentagon_button = button.Button(200, 450, pentagon_img, 1)
square_button = button.Button(425, 450, square_img, 1)
triangle_button = button.Button(650, 450, triangle_img, 1)
rectangle_button = button.Button(650, 350, rectangle_img, 1)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
menu_state = 'init'

while run:

  screen.fill((255, 255, 255))

  #initial menu
  if menu_state == 'init':
    screen.blit(logo_img, (100, 100))
    if start_button.draw(screen):
      menu_state = "game"

  #game loop
  if menu_state == "game":
    screen.fill((255, 255, 255))
    draw_text("Select the geometric shape of the figure", head_font, TEXT_COL, 250, 200)
    if sphere_button.draw(screen):
      Display.Display.sphere_event()
      print("Rectangle function")
    if cone_button.draw(screen):
      Display.Display.cone_event()
      print("Cone function")
    if rectangle_button.draw(screen):
      Display.Display.rectangle_event()
      print("Rectangle function")
    if pentagon_button.draw(screen):
      Display.Display.pentagon_event()
      print("Hexagon function")
    if square_button.draw(screen):
      Display.Display.square_event()
      print("Square function")
    if triangle_button.draw(screen):
      Display.Display.triangle_event()
      print("Triangle function")

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  #else:
    

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        menu_state = "main"
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
