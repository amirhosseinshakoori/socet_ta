import socket



def start_client(server_address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, port))

    try:
        while True:
            
            string_to_send = input("Enter ASCII characters to send: ")

            
            client_socket.send(string_to_send.encode('ascii'))

           
            received_data = client_socket.recv(1024)
            print(f"Received: {received_data.decode('ascii')}")

    except KeyboardInterrupt:
        print("\nClient interrupted by user.")

    finally:
        client_socket.close()



if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 12345
    start_client(HOST, PORT)