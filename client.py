import socket



def start_client(server_address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, port)



if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 12345
    start_client(HOST, PORT)