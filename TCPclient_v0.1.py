# -*- coding: utf-8 -*-
import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_input = input("Entre com o endereço IP do servidor ou pressione ENTER ")
if user_input != '':
    HOST = user_input
user_input = input("Entre agora com a porta de conexão com o servidor ou pressione ENTER para porta padrão ")
if user_input != '':
    PORT = int(user_input)
servidor = (HOST, PORT)
tcp.connect(servidor)
print("Para sair use CTRL+X\n")
msg = input("Mensagem à enviar: ")
while msg != '\x18':    # Enquanto o usuário não usar a tecla "ESC"
    tcp.send(str.encode(msg))
    msg = input("Mensagem à enviar: ")
tcp.close()