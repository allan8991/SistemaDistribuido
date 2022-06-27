import socket
import threading
PORT = 3001
HOST ='127.0.0.1'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)
print(f'escutando na porta :{PORT} e ip:{HOST}')

class Service(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
class Cliente(threading.Thread):
    def __init__(self, end, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        print("Nova conexão detectada: ", end)
    
    def run(self):
        print("Endereço da conexão do cliente: ", end)
        print("ID da Thread de conexão do cliente: ", self.name)
        self.conn.send(str.encode("Seja bem vindo cliente!\nDigite 'sair' para desconectar.\n"))
        mensagem = ''
        while True:
            data = self.conn.recv(1024)
            mensagem = data.decode()
            print(f' O Cliente em {end} da {self.name} Respondeu:\n{mensagem}')
            if mensagem == 'desconectado':
                self.conn.send(str.encode(f'Desconectado!'))
                conn.close()
                break
            else:
                serv = Service()
                self.conn.send(str.encode(f'Serviço prestado pela {serv.name}\n'))   
            
while True:    
    conn, end = server.accept()
    novo_thread = Cliente(end, conn)
    novo_thread.start() 

