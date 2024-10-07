import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Сервер запущен на {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Подключено к {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Получено от клиента: {data.decode()}")
                response = f"Сервер получил: {data.decode()}"
                conn.sendall(response.encode())

if __name__ == "__main__":
    start_server()