import socket
import ast

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
start = True
client.send('new_trivia'.encode('utf-8'))
score = 0
while start:
    msg = ast.literal_eval(client.recv(1024).decode('utf-8'))
    if msg[0] == 'q':
        start = False
    else:
        answer = input(f'trivia_bot: {msg[0]}\nyou: ')
        if answer == 'q':  client.send('q'.encode('utf-8'))
        elif answer.lower() == msg[1].lower():
            score += 1
            print(f'Correct!\ncurrent score: {score}')
            client.send('new_trivia'.encode('utf-8'))
        else:
            score -= 1
            print(f'incorrect the correct answer was {msg[1]}\ncurrent score: {score}')
            client.send('new_trivia'.encode('utf-8'))
# close socket
client.close()
