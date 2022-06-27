import socket
import threading
msgRecebida = " "
clientesServidor = []
IP = "127.0.0.1"
PORT = 3011
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
servidor.bind((IP,PORT))
servidor.listen(10);
def enviarMensagemTodosClientes(clienteEnviaMensagem):
    for clientes in clientesServidor:
        if(clienteEnviaMensagem != clientes):
            clientes.send(msgRecebida.encode())
def clientesConectados(objetoConexao,dadosCliente):
    global msgRecebida;
    while True:
        try:
            msgRecebida = objetoConexao.recv(2048).decode()
            enviarMensagemTodosClientes(objetoConexao)
            
        except:
            objetoConexao.close()
            clientesServidor.remove(objetoConexao)
            break     

while True:
    (objConexao,dadosCliente)= servidor.accept()
    clientesServidor.append(objConexao)
    threading.Thread(target=clientesConectados, args=(objConexao,dadosCliente), ).start()  
servidor.close()