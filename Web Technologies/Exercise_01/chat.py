import socket
import threading

def IP_addr():
    pass

def port():
    pass

def client_id_dictionary():
    pass #returns cid

def get_messages():
    pass #returns msg

def braodcast(msg,cid):
    #takes the message in the parameter
    pass #sends the message to all clients

def handle_clients(conn, cid):
    #welcome msg
    #saves the client conn in the dictionary using cid
    #creates an information msg about the new client and broadcast to all clients
    #read msg from the client and broadcast the message
    pass

def accept_client_connection():
    #accept sock.accept() and print it to serverlog
    #send greeting msg and ask for cid
    #if cid is not empty, print log msg
    #start handle_clients(conn) in a thread
    pass

class Thread: #accepts many parameter
    #new_thread = threading.Thread(target=fn, args=arg_tuple)

    pass



