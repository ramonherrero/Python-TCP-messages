# -*- coding: utf-8 -*-
import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_input = input("Entre com o endereço IP do servidor ou pressione ENTER ")
if user_input != '':
    HOST = user_input
user_input = input("Entre agora com a porta de conexão com o servidor ou pressione ENTER para porta padrão ")
if user_input != '':
    PORT = int(user_input)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print("Conectado à ", cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, " enviou a mensagem ", str(msg, 'utf-8'))
    print("Conexão com o cliente ", cliente, " encerrada!")
    con.close()