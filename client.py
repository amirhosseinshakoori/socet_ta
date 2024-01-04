#This code is part of the employment task for Asia Telecommunications company.

import socket

def separate_digits(number_str):
    
    separated_digits = []
    
    
    while len(number_str) > 0:
        # گرفتن دو یا سه رقم
        if number_str.startswith('1'):
            separated_digits.insert(0, number_str[:3])
            number_str = number_str[3:]
        else:
            separated_digits.insert(0, number_str[:2])
            number_str = number_str[2:]

    return separated_digits


def start_client(server_address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, port))

    try:
        while True:
            hex_decimal_input = input("Enter a hexadecimal number to send: ")
            if not hex_decimal_input:
                break
            
            hex_decimal_input =separate_digits(hex_decimal_input)
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