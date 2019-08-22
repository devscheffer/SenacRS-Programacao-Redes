import socket
import re


def ping():
  row = ""
  while True:
    row = (socketClient.recv(1024).decode())
    if re.search("FIM", row):
      with open("ListPing.txt", "a+") as f2:
        f2.write(row)
      break
    else:
      with open("ListPing.txt", "a+") as f2:
        f2.write(row)
  socketClient.send("Obrigado".encode())

# Configurações de conexão do servidor
# Previamente definidos, conhecidos
serverHost = "localhost"
serverPort = 50007

# Criamos o socket e o conectamos ao servidor
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketClient.connect((serverHost, serverPort))

while True:
  datarec = socketClient.recv(1024).decode()
  print(datarec)
  if re.search("incorreto", datarec):
    continue
  if re.search("Efetuado", datarec):
    socketClient.send("0".encode())
    continue
  datasend = input("Enviar:")
  socketClient.send(datasend.encode())
  if re.search("URL", datarec):
    with open("ListPing.txt", "a+") as file2:  # cria um arquivo para colocar os dados
      file2.write("""       | {:<24} | {:^24} | {:^24} | \n""".format(
          "URL",
          "IP",
          "Status"
      )
      )
    ping()
    continue
  


# Fechamos a conexão
socketClient.close()
