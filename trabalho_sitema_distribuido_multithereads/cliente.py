import socket
HOST = '127.0.0.1'
PORT = 3001
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST,PORT))
except:
    print("não foi possivel fazer a conexão")
while True:
    dado = client.recv(1024)
    print("mensagem vinda do servidor: ", dado.decode())
    sair_cliente = input()
    if sair_cliente == 'sair':
          client.sendall(str.encode("desconectado"))
          client.close()
          break
    client.sendall(str.encode("Pode me prestar um servico?"))
    
