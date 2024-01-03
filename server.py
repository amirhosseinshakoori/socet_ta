import socket
import threading


def client_handler(client_socket):
    while True:
        
        encoded_data = client_socket.recv(1024)
        if not encoded_data:
            break

        
        decoded_data = encoded_data.decode('ascii')

        
        client_socket.send(decoded_data.encode('ascii'))

    client_socket.close()

def start_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen(5)
    print(f"[*] Listening on {address}:{port}")





if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 12345
 