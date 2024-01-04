#This code is part of the employment task for Asia Telecommunications company.

import socket
import threading


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


def client_handler(client_socket):
    while True:
        hex_decimal_str = client_socket.recv(4).decode('ascii')  # Assuming 4 characters for the hexadecimal input
        if not hex_decimal_str:
            break

        # استفاده از تابع جدید برای جدا کردن اعداد
        separated_digits = separate_digits(hex_decimal_str)

        # ارسال اعداد جدا شده به کلاینت
        for digit in separated_digits:
            client_socket.send(digit.encode('ascii'))

    client_socket.close()

def start_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen(5)
    print(f"[*] Listening on {address}:{port}")

    while True:
        client_sock, addr = server_socket.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_thread = threading.Thread(target=client_handler, args=(client_sock,))
        client_thread.start()



if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 12345
    start_server(HOST, PORT)




#This code is part of the employment task for Asia Telecommunications company.
 