import socket
import pickle

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))
    msg = pickle.loads(client.recv(1024))
    data = msg
    client.send(pickle.dumps('init'))
    while True:
        msg = pickle.loads(client.recv(1024))
        if msg == "q":
            break

        client.send(pickle.dumps(data))
        data = msg
        print(msg)
except Exception as e:
    print(f'error: {e}')
finally:
    client.close()
