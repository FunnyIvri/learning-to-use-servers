import socket
import pickle
try:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))
    while True:
        msg = pickle.loads(client.recv(1024))
        client.send(pickle.dumps(msg))
        if msg == "q":
            break
        else:
            print(msg)
except Exception as e: print(f'error: {e}')
finally:
    client.close()

