import pygame
from text import Textcreator

# root setup:
root_w = 1920
root_h = 800

root = pygame.display.set_mode((root_w, root_h))
name = ""
nameText = Textcreator("name: ", 100, [0, 0], root, "white")
# loop setup:
run = True
typing = True
while run:
    root.fill("black")
    nameText.createText()
    nameText.text = f'name: {name}'
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and typing:
            if event.key == 8 or event.key == 127:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                typing = False
                print(f'your name is {name}')
            else:
                name += event.unicode
