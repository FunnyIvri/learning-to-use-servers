import socket

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
start = True
client.send(str([0,0]).encode('utf-8'))

while start:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'q':
        start = False
    else:
        print(msg)
        direction = input('direction to move circle (left,right,up,down)?\nyou: ')
        match direction:
            case 'q':
                moveAmount = ['q']
            case 'left':
                moveAmount = [-100, 0]
            case 'right':
                moveAmount = [100, 0]
            case 'up':
                moveAmount = [0, -100]
            case 'down':
                moveAmount = [0, 100]
            case _:
                moveAmount = [0, 0]
        client.send(str(moveAmount).encode('utf-8'))


# close socket
client.close()

