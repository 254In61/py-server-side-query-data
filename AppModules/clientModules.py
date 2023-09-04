import socket
from AppModules.socketParams import *

def create_socket():
    # Create client socket
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((SERVER_HOST, PORT))
    return cs

class ClientChat():
    """
    Class that handles chat.
    Gets input from CreateQuery class for the query to send.
    """
    def __init__(self,query):
        self.query = query
        
    def messaging(self):
        # Method to perform the messaging with server
        
        # Send query to server through socket
        cs = create_socket()
        print("Message sent: ", self.query)
        cs.sendall(self.query.encode("utf-8"))

        # Recieve result from server
        query_result = cs.recv(1024).decode("utf-8")
        print("Message recieved : ", query_result)

        return query_result

def menu():
    print("\nMENU\n1 = Get information\n2 = Put updated information\n3 = Post new information\n4 = Delete existing information\n")


def collect_values():
    country = input("Key in country name : ").capitalize()
    capital = input("Key in capitol name : ").capitalize()
    leader  = input("Key in political leader full names : ").capitalize()
    extras  = input("Any interesting fact about the country? : ").capitalize()
    
    return country + ":"+ capital + ":" + leader + ":" + extras
