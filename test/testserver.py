import socket
import pickle
from _thread import *

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()
    move = {"up1": 20,'side1':20}


    def clientHandler(clientSocket: socket, clientAddress: tuple):
        global move
        print(f'new client[{clientAddress}]')
        try:
            while True:
                client.send(pickle.dumps(move))
                msg = pickle.loads(clientSocket.recv(1024))
                move = msg
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
