import socket
import threading

nickname = input('Choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50007))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print('An error occured!')
            client.close()
            break

def write():
    while True:
        message = (f'{nickname}: {input(">>")}')
        client.send(message.encode('ascii'))



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()










'''
def client_programm():
    host = '127.0.0.1'
    port = 50007

    client_socket = socket.socket()
    client_socket.connect((host,port))

    message = input(' -> ')

    with socket.socket() as s:
        while message.lower().strip() != 'shut down':
            s.send(message.encode())
            data = s.recv(1024).decode()

            print('recieved from server: ' + data)

            message = input(' -> ')

        s.close()

if __name__ == '__main__':
    client_programm()





HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello Rafid')
    data = s.recv(1024)
print('Recieved', repr(data))
'''