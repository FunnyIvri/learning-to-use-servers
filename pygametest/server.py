import socket
import pickle
from _thread import *

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()
    data = {
        "squareScore": 0,
        "circleScore": 0,
        "circleStartingY": 0,
        "circleStartingX": 0,
        "squareStartingY": 0,
        "squareStartingX": 0,
        "speedY": 0,
        "speedX": 0
    }


    def clientHandler(clientSocket: socket, clientAddress):
        try:
            print(f'new client[{clientAddress}]')
            global data
            while True:
                print(clientAddress[1])
                client.send(pickle.dumps(data))

                data = msg
                msg = pickle.loads(clientSocket.recv(1024))
                if msg == "init":
                    client.send(pickle.dumps(data))
                    continue
                if msg == "q":
                    client.send(pickle.dumps("q"))
                    print(f'client[{clientAddress}] has left!')
                    break

        except Exception as error:
            print(f'error while handling client!\n{error}')
        finally:
            clientSocket.close()


    while True:
        client, addr = server.accept()
        start_new_thread(clientHandler, (client, addr))
except Exception as error:
    print(f'error!\n {error}')
finally:
    server.close()
