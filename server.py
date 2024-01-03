import socket
import threading




def start_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen(5)
    print(f"[*] Listening on {address}:{port}")


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 12345
 