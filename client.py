import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = input("Введите сообщение для сервера: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Ответ от сервера: {data.decode()}")

if __name__ == "__main__":
    start_client()