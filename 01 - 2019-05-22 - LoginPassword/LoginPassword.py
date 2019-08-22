#Author: Gerson Scheffer

#Import
import os

#Variable
trial = 3

#Function

def LoginPassword():
    """Define se o login e a senha estao corretos para que o usuario possa acessar os dados.
     \nUsuario tem apenas um numero [trial] de tentativas.
    """
    
    global trial

    if trial > 0:
        print("##### Seja Bem vindo ######")
        login    = input("Login   : ")
        password = input("Password: ")
        if login == "aaa" and password == "123":
            return inf()
        else:
            trial -= 1
            print("Senha incorreta (Faltam: {} tentativas)".format(trial))
            return LoginPassword()
    else:
        print("Programa bloqueado")


def PathNow():
    """Caminho do diretorio atual.
    """
    pathnow = os.getcwd()
    print("Path do diretorio atual:\n{}".format(pathnow))
    
def CountFiles():
    """Quantidade de arquivos do diretorio.
    """ 
    listFiles = os.listdir()
    count = len(listFiles)
    print("Numero de arquivos: {}".format(count))
    
def ListFiles():
    """ A lista de arquivos contidos neste diretorio.
    """
    pathnow = os.listdir()
    count = 0
    for i in pathnow:
        count += 1
        print("{} - {}".format(count,i))
        
def Disk():
    """ Unidade de disco atual
    """
    pathnow = str(os.getcwd())
    pathnow = pathnow.split("\\")
    print("Unidade de disco atual:\n {}".format(pathnow[0]))

def UserMachine():
    """ Nome de usuario da máquina
    """
    pathnow = str(os.getcwd())
    pathnow = pathnow.split("\\")
    print("Nome de usuario da máquina:\n {}".format(pathnow[2]))

def DirectoryNow():
    """ Nome do diretório Atual
    """
    pathnow = str(os.getcwd())
    pathnow = pathnow.split("\\")
    print("Diretorio atual:\n {}".format(pathnow[-1]))
    
def inf():
    PathNow()
    CountFiles()
    ListFiles()
    Disk()
    UserMachine()
    DirectoryNow()
    
#Main

LoginPassword()