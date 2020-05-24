import socket
import threading
import pickle
from time import sleep
import detectOs
import sys

global repeat
connections = []
total_connections = 0
list_of_users=[]
dic_users={}



class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
        self.HEADERSIZE=10
        self.connected=False




    def __str__(self):
        return str(self.id) + " " + str(self.address)


    def run(self):
        global list_of_users
        while self.signal:
            try:
                data = self.socket.recv(50)

            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            if len(data)>0:
                    global one
                    if(self.connected==False):
                        d=detectOs.detectPlatform(self.connected)
                        self.connected=True
                    else:
                        d=detectOs.detectPlatform(self.connected)

                    sleep(0.5)
                    msg=pickle.dumps(d,protocol=2)
                    self.socket.sendall(msg)


            if(len(data))==0:
                self.disconnet()
                break
            user=data.decode('utf-8')
            if(len(data)>0 and user.startswith("User")):

                    user=user.split(" ")
                    dic_users[user[2]]=user[1]
                    list_of_users=list(dic_users.keys())
            else:
                self.disconnet()

    def disconnet(self):
        print("Client " + str(self.address) + " has disconnected")
        self.signal = False
        connections.remove(self)
def getUserPreferences(user):
    return int(dic_users[user])

# Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1

def getListOfUsers():
    global list_of_users
    return list_of_users

def main():
    host = '192.168.1.7'
    print(host)
    port = int(sys.argv[1])
    print(sys.argv[1])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    newConnectionsThread = threading.Thread(target=newConnections, args=(sock,))
    newConnectionsThread.start()


# if __name__ == '__main__':
#     main()