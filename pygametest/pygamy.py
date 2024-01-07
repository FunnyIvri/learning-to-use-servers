import math
import random
import pygame
from text import Textcreator

clock = pygame.time.Clock()
targetFps = 60
root = pygame.display.set_mode((900, 600))
root_x = root.get_width()
root_y = root.get_height()
data = {
    "squareScore": 0,
    "circleScore": 0,
    "circleStartingY": root_y // 2,
    "circleStartingX": 100,
    "squareStartingY": root_y // 2,
    "squareStartingX": root_x - 100,
    "speedY": 5,
    "speedX": 5
}
winGoal = 7
run = True
fpsText = Textcreator("fps: 0", 30, [10, 10], root)
circleText = Textcreator(str(data["circleScore"]), 100, [100, 100], root, [255, 0, 0])
squareText = Textcreator(str(data["squareScore"]), 100, [root_x - 100, 100], root, [0, 0, 255])


def win(circleWin, root_x, root_y):
    root_x = root_x

    root_y = root_y

    root = pygame.display.set_mode((root_x, root_y))
    winText = Textcreator("VICTORY FOR UNKNOWN", 100, [root_x // 2, root_y // 2], root)
    # loop setup:
    run = True
    if circleWin:
        winText.text = "CIRCLE VICTORY!"
        winText.color = (255, 0, 0)
    else:
        winText.text = "SQUARE VICTORY"
        winText.color = (0, 0, 255)
    while run:
        root.fill("black")
        winText.createText()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def movment(keys):
    if keys[pygame.K_UP] and square.rect.y > 0:
        square.rect.y += -data["speedY"]
    if keys[pygame.K_DOWN] and square.rect.y < 600 - 20:
        square.rect.y += data["speedY"]
    if keys[pygame.K_LEFT] and square.rect.x > 0:
        square.rect.x += -data["speedX"]
    if keys[pygame.K_RIGHT] and square.rect.x < 900 - 20:
        square.rect.x += data["speedX"]

    if keys[pygame.K_w] and circle.rect.y > 20:
        circle.rect.y += -data["speedY"]
    if keys[pygame.K_a] and circle.rect.x > 20:
        circle.rect.x += -data["speedX"]
    if keys[pygame.K_s] and circle.rect.y < 600 - 20:
        circle.rect.y += data["speedY"]
    if keys[pygame.K_d] and circle.rect.x < 900 - 20:
        circle.rect.x += data["speedY"]


class Shield:
    def __init__(self, root, color, pos, radius, width, leftHalf):
        self.root = root
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.leftHalf = leftHalf
        self.rect = pygame.draw.circle(self.root, self.color, self.pos, self.radius, self.width)

    def show(self):
        pygame.draw.ellipse(self.root, self.color, self.rect, self.width)

    def randomizePos(self):
        if self.leftHalf:
            self.rect.x = random.randint(0, root_x // 2)
            self.rect.y = random.randint(0, root_y)
        else:
            self.rect.x = random.randint(root_x // 2, root_x)
            self.rect.y = random.randint(0, root_y)


class Player:
    def __init__(self, root, speedY, speedX, startPos, color, size, leftHalf, shieldRadius, shieldWidth):
        self.root = root
        self.speedY = speedY
        self.speedX = speedX
        self.startPos = startPos
        self.color = color
        self.size = size
        self.hasShield = False
        self.leftHalf = leftHalf
        self.shieldRadius = shieldRadius
        self.shieldWidth = shieldWidth
        self.rect = pygame.draw.rect(self.root, self.color, (startPos[0], startPos[1], size, size))
        self.shield = Shield(self.root, self.color, (400, 400), 25, 5, self.leftHalf)

    def returnToStart(self):
        self.rect.x = self.startPos[0]
        self.rect.y = self.startPos[1]

    def showAsCircle(self):
        pygame.draw.ellipse(self.root, self.color, self.rect)

    def showAsSquare(self):
        pygame.draw.rect(self.root, self.color, self.rect)


square = Player(root, 5, 5, [data["squareStartingX"], data["squareStartingY"]], "blue", 20, True, 25, 5)
circle = Player(root, 5, 5, [data["circleStartingX"], data["circleStartingY"]], "red", 20, False, 25, 5)
square.shield.randomizePos()
circle.shield.randomizePos()
data.update({
    "square": square,
    "circle": circle
})
while run:
    root.fill("black")

    fpsText.createText()
    circleText.createText()
    squareText.createText()
    circleText.text = str(data["circleScore"])
    squareText.text = str(data["squareScore"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    # movement
    movment(keys)
    # collision control
    if (square.rect.colliderect(circle) and root_x // 2 < square.rect.x) or (
            square.rect.colliderect(circle.shield) and 0 < square.rect.x and circle.hasShield):
        if circle.hasShield:
            circle.hasShield = False
            circle.shield.randomizePos()
            square.returnToStart()
        circle.returnToStart()
    elif (circle.rect.colliderect(square) and 0 < circle.rect.x) or (
            circle.rect.colliderect(square.shield) and 0 < circle.rect.x and square.hasShield):
        if square.hasShield:
            square.hasShield = False
            square.shield.randomizePos()
            circle.returnToStart()
        else:
            square.returnToStart()
    if 0 >= square.rect.x:
        data["squareScore"] += 1
        square.returnToStart()
        circle.returnToStart()
    elif root_x - 20 <= circle.rect.x:
        data["circleScore"] += 1
        square.returnToStart()
        circle.returnToStart()
    if data["circleScore"] >= winGoal:
        win(True, root_x, root_y)
    elif data["squareScore"] >= winGoal:
        win(False, root_x, root_y)
    if square.shield.rect.colliderect(square.rect) and not square.hasShield:
        square.hasShield = True
    elif square.hasShield:
        square.shield.rect.center = square.rect.center
    if circle.shield.rect.colliderect(circle.rect) and not circle.hasShield:
        circle.hasShield = True
    elif circle.hasShield:
        circle.shield.rect.center = circle.rect.center
    square.shield.show()
    circle.shield.show()
    square.showAsSquare()
    circle.showAsCircle()
    pygame.display.update()
    clock.tick(targetFps)
    fpsText.text = f'fps: {math.ceil(clock.get_fps())}'

pygame.quit()
