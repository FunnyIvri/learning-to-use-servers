import socket
import random
import ast

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))  # ip: 127.0.0.01 port: 9999
# start listen
server.listen()
client, addr = server.accept()
start = True
general_responses = [
    "I understand.",
    "That's interesting.",
    "Tell me more.",
    "I see.",
    "Interesting point.",
    "Please continue.",
    "That makes sense.",
    "I get your point.",
    "That's a good perspective.",
    "Thanks for sharing."
]
general_greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Good day!",
    "Hey!",
    "Nice to meet you!",
    "Howdy!",
    "Salutations!",
    "Hey, what's up?",
    "Welcome!"
]
tell_me_more_responses = [
    "I'm interested in hearing more.",
    "Could you elaborate further?",
    "I'm all ears, please continue.",
    "I'd like to know more details.",
    "Feel free to provide more information.",
    "Tell me all about it.",
    "I'm curious, please share more.",
    "I'm listening, please go on.",
    "I'd appreciate more context.",
    "Please expand on that."
]
while start:
    msg = ast.literal_eval(client.recv(1024).decode('utf-8'))
    if msg[1] == 'q':
        start = False
        client.send('q'.encode('utf-8'))
    elif msg[0] == 'name':
        client.send(
            f'help bot: {random.choice(general_greetings)} {msg[1].capitalize()} what seems to be the problem?'.encode('utf-8'))
    elif msg[0] == 'conv':
        if random.randint(0,1) == 0:
            client.send(f'{msg[1]}, {random.choice(tell_me_more_responses)}'.encode('utf-8'))
        else:
            client.send(f'{msg[1]}, {random.choice(general_responses)}'.encode('utf-8'))
    else:
        client.send(f'help bot: welcome {msg[0]}!'.encode('utf-8'))
# close socket
client.close()
server.close()
