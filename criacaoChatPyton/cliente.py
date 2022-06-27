import socket
import threading
IP = "localhost"
PORT = 3011
msg = ""
def receberMensagens():
    while True: 
        try:
            mensagemRecebida = client.recv(2048).decode()
            print(mensagemRecebida)
        except:
            print("Voce desconectou do servidor com sucesso!")
            break 
try: 
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((IP,PORT))         
    nomeUsuario = input("Primeiro digite o seu nome usuário:")
    threading.Thread(target=receberMensagens).start()
    print("Digite suas mensagens:")
    print('Digite "saiu" para desconectar do servidor !')
    while True:
        msg = input()
        msgCompleta = nomeUsuario+": "+msg
        client.send(msgCompleta.encode())
        if(msg.lower() == "saiu"):
            break
except:
    print("Erro ao se conectar ao servidor!")
    print("Tente mais tarde!")

client.close()   
   
   


