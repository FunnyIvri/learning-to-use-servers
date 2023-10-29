import ast
import socket
import pygame
# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))  # ip: 127.0.0.01 port: 9999
# start listen
server.listen()
client, addr = server.accept()
root_w = 800
root_h = 800
root = pygame.display.set_mode((root_w, root_h))
circle = pygame.Rect(((root_w//2, root_w//2), (root_h//2, root_h//2)))
start = True
while start:
    msg = ast.literal_eval(client.recv(1024).decode('utf-8'))
    root.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    if msg[0] == 'q':
        start = False
        client.send('q'.encode('utf-8'))
    else:
        circle.x += msg[0]
        circle.y += msg[1]
        client.send('done'.encode('utf-8'))
    pygame.draw.ellipse(root, 'white', circle)
    pygame.display.update()
# close socket
client.close()
server.close()
pygame.quit()