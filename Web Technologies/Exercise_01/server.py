import socket
import threading


host = '127.0.0.1'            # local host
port = 50007                  # solid port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))    # bind host address and port together
server.listen()        # configure how many client the server can listen simultaneously

clients = []
nicknames = []

# Three methods will be defined: broadcast, handle, receive(combines all method)


def broadcast(message):
    for client in clients:
        client.send(f'>>>{message}')


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()  # accepts new connections
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii ')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server is listening...')
receive()





'''      

def server_program():

   # socket.AF_INET, socket.SOCK_STREAM 


print('Connction from: ' + str(addr))
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
print(('from connected user: ' + str(data)))
data = input(' ->')
conn.send(data.encode())

conn.close()'''



''' host = 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connetcted by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    conn.sendall(data)

'''
