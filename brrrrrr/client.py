import socket
import pickle
import keyboard
import pygame
root_w = 800
root_h = 800
root = pygame.display.set_mode((root_w,root_h))
clock = pygame.time.Clock()
speed = 5
try:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))
    while True:
        msg = pickle.loads(client.recv(1024))
        if keyboard.is_pressed('w'):
            msg['up1'] += -speed
        if keyboard.is_pressed('s'):
            msg['up1'] += speed
        if keyboard.is_pressed('a'):
            msg['side1'] += -speed
        if keyboard.is_pressed('d'):
            msg['side1'] += speed

        root.fill("black")

        if msg['side1'] <= 0:
            msg['side1'] += speed
        if msg['side1'] >= root_w:
            msg['side1'] += -speed
        if msg['up1'] <= 0:
            msg['up1'] += speed
        if msg['up1'] >= root_h:
            msg['up1'] += -speed
        pygame.draw.circle(root, (255, 255, 255), (msg['side1'], msg['up1']), 20)
        client.send(pickle.dumps(msg))
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        if msg == "q":
            break
        else:
            print(msg)
except Exception as e: print(f'error: {e}')
finally:
    client.close()

