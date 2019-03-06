# esse arquivo contem algumas fuções basicas para facilitar o programa

#import os: biblioteca na qual eu usei a função 'os.system("cls")'
#           para impar a tela, essa função se encontra em:
#           bibliotecas\tela()\import os
              
#import getpass: biblioteca na qual eu usei a função 'getpass.getpass()'
#                para esconder a senha quando digitada   
#                obs: pode causar erros no interpretador
#                         principalmente no 'pycharm'
#                localizada em bibliotecas\getpass


import os
import getpass


# algumas funções para facilitar na hora de escrever o codigo
def tela():
    os.system("clear")

def opcaoinvalida():
    print("opção invalida!")
    print("Digite Novamente!")
    input("aperte qualquer tecla para continuar")
    tela()

def senhainvalida():
    print("usuario ou senha invalidos!")
    print("digite novamente")
    input("aperte qualquer tecla para continuar")
    tela()


    

   
