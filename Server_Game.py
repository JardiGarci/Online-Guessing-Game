import socket
import threading
import numpy as np

def join_world(list_world):
    new_world = ''
    for letter in list_world:
        new_world += f'{letter} '
    return new_world


class Game():
    def __init__(self): 
        
        data = np.load('C:\\Users\\jygar\\Dropbox\\Maestria\\Programacion\\data.npz')
        self.data = data['datos']
        self.players = {}
        self.n_jugadores = 0

        self.main()


    def new_game(self):
        word = np.random.choice(self.data)
        mix_word = [letter for letter in word]
        np.random.shuffle(mix_word)
        clues = []
        clue = []
        for i in range(len(word)):
            clue.append('_ ')
        n_clues = np.arange(len(word))
        np.random.shuffle(n_clues)
        for n in n_clues[:-1]:
            clue[n] = f'{word[n]} '
            clues.append(join_world(clue))
        return word, clues



    def handle_client(self,client_socket, client_address):
        
        player = f'{client_address[1]}'
        self.players[player] = {}
        self.players[player]['word'] = []
        self.players[player]['clues'] = []
        self.players[player]['intentos'] = []
        self.players[player]['ganes'] = 0
        self.n_jugadores += 1
        n_jugador = self.n_jugadores
        self.players[player]['n'] = n_jugador
        print(f"Jugador {n_jugador} en línea")
    
        while True: 
            word, clues = self.new_game()
            estado = 0   
            n_intento = 0
            intentos = []
            

            self.players[player]['word'].append(word)
            self.players[player]['clues'].append(clues)

            client_socket.send(f"\nAdivina la siguiente palabra: \n {clues[n_intento]}\n".encode())   
            try:
                while True:    
                    try:
                        message = client_socket.recv(1024)
                        n_intento += 1
                        if not message:
                            print(f"Cliente {client_address} desconectado")
                            break

                        if message.decode() == word:
                            client_socket.send('Felicidades has ganado!\n'.encode())
                            client_socket.send('Si deseas volver a jugar presiona "y" \n'.encode())
                            estado = 1
                            break                            
                        else:
                            client_socket.send(f'Intento: {n_intento}, continua intentando.\n'.encode())
                            if n_intento%3 == 0 and n_intento//3 <= (len(clues) -1):
                                client_socket.send(f"Pista \n {clues[n_intento//3]}\n".encode())  
                        
                        intentos.append(message.decode())
                            
                        print(f"El jugador {n_jugador} con la palabra '{word}' probó con: {message.decode()}")
                        # Enviar eco de vuelta al cliente
                        # client_socket.send(f"Eco: {message.decode()}".encode())
                    except:
                        print(f"Se ha cerrado la comunicación con el jugador{n_jugador}")
                        break
                
                self.players[player]['intentos'].append(intentos)
                if estado == 1:
                    message = client_socket.recv(1024) 
                    self.players[player]['ganes'] += 1

                    if message.decode().lower() == 'y':
                        print(f'El jugador {n_jugador} ha ganado y continua jugando')
                        pass
                    else:
                        print(f'El jugador {n_jugador} ha ganado y ha dejado de jugar')
                        break

                for p in self.players:
                    print(f'El jugador : {self.players[p]['n']} ha ganado : {self.players[p]['ganes']} veces.')





            except:
                print(f"Se ha cerrado la comunicación con el jugador{n_jugador}")
                break
        client_socket.close()

    def main(self):
        host = 'localhost'
        port = 65432
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Servidor escuchando en {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()
            print(f"Jugadores activos: {threading.active_count() - 1}")  # -1 porque el hilo principal también se cuenta


if __name__ == "__main__":
    Game()