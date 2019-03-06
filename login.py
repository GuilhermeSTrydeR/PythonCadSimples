from bibliotecas import *
from adm import *

# essa é a função de cadastro de primeiro login
def login():
    print("bem vindo ao assitente de primeiro acesso!")
    print("nesse assistente iremos configurar o perfil 'administrador',")
    print("que é responsavel por gerenciar o programa.")
    print("\n")
    input("aperte qualquer tecla para continuar")
    tela()

    tela()

    i = True

    while i == True:

        while i == True:
            
            print("nome completo do administrador")
            nome = input()
            tela()
            if not nome:
                
                print("nome em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
            else:
                tela()
                break

        while i == True:

            print("digite o E-mail do administrador")
            email = input()
            tela()
            if not email:

                print("E-mail em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()

            else:
                tela()
                break
                    

        while i == True:
            
                
            print("digite o login do administrador")
            login = input()
            tela()
            if not login:
                
                print("login em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
                
            else:
                tela()
                break
                        
        while i == True:
            
            senha = getpass.getpass("digite a senha do administrador\n")
            
            if not senha:
                tela()
                print("login em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
                
            elif (len (senha) < 5):
                tela()
                print("a senha digitada é muito curta!\ndigite pelo menos 5 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()

            elif (len(senha) > 20):
                tela()
                print("a senha digitada é muito grande!\ndigite no maximo 20 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()

    
            senha1 = getpass.getpass("digite a senha do administrador\n")
            tela()
            
            if not senha1:
                tela()
                print("login em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
                
            elif (senha != senha1):
                tela()
                print("as senhas digitadas são diferentes, digite novamente")
                input("aperte qualquer tecla para continuar!")
                tela()
                

            else:
                tela()
                break

        conexão = sqlite3.connect("database.db")
        cursor = conexão.cursor()

        

    
        cursor.execute('''
            insert into administrador (nome, login, senha, email)
                values(?, ?, ?, ?)
                ''', (nome, login, senha, email))

        conexão.commit()
        cursor.close()
        conexão.close()

        tela()

        print("perfil administrador criado com sucesso!")
        print("\n")
        input("aperte qualquer tecla para entrar no programa")
        tela()
        break
        
