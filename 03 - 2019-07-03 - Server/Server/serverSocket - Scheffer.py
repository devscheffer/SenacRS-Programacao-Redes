import subprocess
import socket
import datetime
import os
import time

#Function
menuT = (
        """
    O que voce deseja?
    [1] Informações do Diretório atual do Cliente
    [2] Ping
    [3] Sair

    Digite uma opcao:
    """
    )

trial = 5
def LoginPassword(login, password):
    """Define se o login e a senha estao corretos para que o usuario possa acessar os dados.
     \nUsuario tem apenas um numero [trial] de tentativas.
    """
    global trial
    if trial > 0:
        if login == "aaa" and password == "123":
            return "OK"
        else:
            trial -= 1
            return "NOK"
    else:
        print("Programa bloqueado")


listText = []
def ping(url, ip):
    with open("ListPing.txt", "a+") as file2:  # cria um arquivo para colocar os dados
        file2.write("""| {:<24} | {:^24} | {:^24} | \n""".format(
            "URL",
            "IP",
            "Status"
            )
        )

    out = subprocess.run(['ping', url], capture_output=True)
    ip = socket.gethostbyname(url)
    response = os.system('ping -n 1 ' + url)
    if response == 0:
        pingStatus = "Ativo"
    else:
        pingStatus = "Inativo"
    pingT = out.stdout.decode()
    with open("ListPing.txt", "a+") as f2:
        f2.write("""| {:<24} | {:^24} | {:^24} |  \n""".format(
            url, 
            ip, 
            pingStatus
            )
        )
        listText.append("row 0: | {:<24} | {:^24} | {:^24} | \n".format(
            url, ip, pingStatus))
        c = 1
        for i in pingT.splitlines():
            f2.write("{} \n".format(i))
            listText.append("row {}: {}\n".format(c, i))
            c += 1
    return listText

def PathNow():
    """Caminho do diretorio atual.
    """
    pathnow = os.getcwd()
    print("Path do diretorio atual:\n{}".format(pathnow))
    return "Path do diretorio atual:\n{}".format(pathnow)

#Nome do host
hostServidor = "localhost"
#Porta
portaServidor = 50007

#Criando um Servidor ....
#Objeto Servidor Criado
sockObjServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET -> Protocolo Endereco IP
#SOCK_STREAM -> Protocolo TCP/IP
#SOCK_DGRAM -> Protocolo UDP

#Vinculando Servidor a uma porta ...
sockObjServer.bind((hostServidor, portaServidor))
#Na escuta...
sockObjServer.listen(1)
while(True):
    print("Servidor Escutando...")
    connection, id = sockObjServer.accept()
    print('Server conectado por', id)

    while(True):
        connection.send("Login: ".encode())
        dataLogin = connection.recv(1024).decode()
        if not dataLogin:
            break
        connection.send("Password: ".encode())
        dataPassword = connection.recv(1024).decode()
        if not dataPassword:
            break
        if LoginPassword(dataLogin, dataPassword) == "OK":
            connection.send("Login Efetuado".encode())
            break
        else:
            connection.send("Login ou Password incorreto (Faltam: {} tentativas)".format(trial).encode())

    while(True): 
        dataOp = connection.recv(1024).decode()
        if not dataOp:
            break
        if dataOp == "0":
            connection.send(menuT.encode())
        if dataOp == "1":
            diretorio = PathNow()
            connection.send("""
                {}

                {}
                """.format(diretorio,menuT).encode())
        if dataOp == "2":
            connection.send("URL: ".encode())
            url = connection.recv(1024).decode()
            print(url)
            ip = socket.gethostbyname(url)
            ping(url, ip)
            print(listText)
            print("tamanho {}".format(len(listText)))
            for i in listText:
                print("{}".format(i))
                connection.send(i.encode())

            connection.send("""
                {}\n""".format("FIM").encode())
            print(connection.recv(1024).decode())
            connection.send(menuT.encode())
            listText = []
        if dataOp == "3":
            connection.send("Log out".encode())
            break

#encerrando conexao
connection.close()



