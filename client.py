#This code is part of the employment task for Asia Telecommunications company.

import socket


def start_client(server_address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, port))

    try:
        while True:
            hex_decimal_input = input("Enter a hexadecimal number to send: ")
            if not hex_decimal_input:
                break

            # Assuming the input is a valid hexadecimal string
            client_socket.send(hex_decimal_input.encode('ascii'))

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

#This code is part of the employment task for Asia Telecommunications company.