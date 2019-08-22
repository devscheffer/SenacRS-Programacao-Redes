#Author: Gerson Scheffer e Eduardo Pereira
#Turn: Noite

import subprocess
import socket
import datetime
import os
import time

currentDT = datetime.datetime.now()
with open("ListPing.csv", "a+") as file2: #cria um arquivo para colocar os dados
    file2.write("URL , IP , Status, Date , Time\n") #cabecalho do arquivo

while True:
    with open("sites.txt", "r") as file1: #abre o arquivo sites.txt
        fl1 = file1.read().splitlines() #le linha por linha do arquivo
        for i in fl1:
            url = str(i)
            out = subprocess.run(['ping', url], capture_output = True)
            ip  = socket.gethostbyname(url)
            response = os.system('ping -n 1 ' + url)
            if response == 0:
                pingStatus = "Ativo"
            else:
                pingStatus = "Inativo"
            print(out.stdout.decode())
            print("{}, {}, {} , {} , {} ".format(url, ip,pingStatus,currentDT.strftime("%Y/%m/%d"),currentDT.strftime("%H:%M:%S")))
            with open("ListPing.csv", "a+") as f2:
                f2.write("{}, {}, {} , {} , {} \n".format(url, ip,pingStatus,currentDT.strftime("%Y/%m/%d"),currentDT.strftime("%H:%M:%S")))

    time.sleep(5) #delay de 5s para o proximo while
