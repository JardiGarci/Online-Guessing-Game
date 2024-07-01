import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"{message.decode()}\n")
        except:
            print("Conexión cerrada por el servidor\n")
            break

def main():
    host = 'localhost'
    port = 65432
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Conectado al servidor en {host}:{port}")

    # Iniciar hilo para recibir mensajes del servidor
    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    recv_thread.start()

    try:
        while True:
            # message = input("Ingresa un palabra (o 'exit' para salir): \n")
            message = input('\n')
            if message.lower() == 'exit':
                print("Cerrando la conexión...")
                break
            client_socket.send(message.encode())
    finally:
        client_socket.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    main()
