from bibliotecas import *
from variaveis import *
import sqlite3

#area do administrador, todas as funções dele estão aqui


           
#função para cadastrar alunos
def cad_aluno():
    tela()
    
    i = True
    
    while i == True:
        
        
        while i == True:
            #esse bloco se repete no hora de cadastrar
            print("nome completo do aluno")
            nome = input()
            
            tela()
            
            if not nome:
                
                print("Nome em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
                
            else:
                tela()
                break

        while i == True:

            print("digite o login do aluno")
            login = input()
            tela()

            if not login:
                
                print("Login em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()        
            
            else:
                break
                        
        while i == True:

            print("digite o e-mail do aluno")
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

            print("digite a data de nascimento do aluno")
            nasc = input()
            tela()
            if not nasc:

                print("Data em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()

            else:
                tela()
                break

        while i == True:
            # com 'getpass' a senha não fica visivel na tela na hora de digitar
            senha = getpass.getpass("digite a senha do aluno\n")
           
            #bloco condicional
            if not senha:
                tela()
                print("Senha em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
            elif (len(senha) < 6):
                tela()
                print("a senha digitada é muito curta!\ndigite pelo menos 6 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()

            elif (len(senha) > 20):
                tela()
                print("a senha digitada é muito grande!\ndigite no maximo 20 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()
 
            senha1 = getpass.getpass("digite a senha novamente\n")
            tela()
            
            if not senha1:
                
                tela()
                print("Senha em branco!")
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
                
            
                
            

        tela()
        # nessa parte é feita a conexão com o banco sqlite e adicionado os valores as chaves do banco
        conexão = sqlite3.connect("database.db")
        cursor = conexão.cursor()

        cursor.execute('''
                insert into aluno (nome, login, senha, email, nascimento)
                    values(?, ?, ?, ?, ?)
                    ''', (nome, login, senha, email, nasc))

        
        conexão.commit()
        cursor.close()
        conexão.close()
        
        tela()

        while i == True:

            menu = input("cadastro efetuado com sucesso!\ndeseja cadastrar outro aluno? (s/n)")
            tela()

            if menu == ("s"):
                break
            elif menu == ("n"):
                i = False
            else:
                opcaoinvalida()

#função para visualizar os alunos por codigo
def vis_aluno_codigo():


    while i == True:

        conexão = sqlite3.connect("database.db")
        cursor = conexão.cursor()

        codaluno = input("digite o codigo do aluno: ")
        tela()

        cursor.execute(''' select * from aluno where codaluno = ?''',(codaluno, ))
        res = cursor.fetchall()

        cursor.close()
        conexão.close()


        if res:
            for x in res:
                print("codigo do aluno: %s\nNome: %s\nLogin: %s\nSenha: %s\nE-mail: %s\nData de nascimento: %s" %(x))
                print("*" * 50)
        else:
            print("não foram encontrados registros com esse codigo")
            input("aperte qualquer tecla para voltar")
            tela()


        menu = input("deseja vizualisar outro aluno?(s/n)")
        tela()

        if menu == ("s"):
            continue
        elif menu == ("n"):
            break
        else:
            opcaoinvalida()


        break
#função para visualizar todos os alunos
def vis_aluno():
    tela()


    conexão = sqlite3.connect("database.db")
    cursor = conexão.cursor()

    cursor.execute("select * from aluno")
    res = cursor.fetchall()

    for x in res:
        print("codigo do aluno: %s\nNome: %s\nLogin: %s\nSenha: %s\nE-mail: %s\nData de nascimento: %s" %(x))
        print("*" * 50)
        
    print("\n")
    input("aperte qualquer tecla para voltar")
    tela()

    cursor.close()
    conexão.close()
    
#função para adicionar aluno em uma turma
def inc_aluno():

    conexão = sqlite3.connect("database.db")
    cursor = conexão.cursor()

    cursor.execute("select * from aluno")
    aluno = cursor.fetchall()


    cursor.execute("select * from turma")
    turma = cursor.fetchall()

    cursor.close()
    conexão.close()
    
    if not turma and not aluno:
        print("não há turmas nem alunos cadastrados")
        print("primeiro cadastre ambos para depois incluir um aluno em uma turma\n")
        input("aperte qualquer tecla para voltar")
        tela()

    elif not aluno:
        print("não há alunos cadastrados")
        print("primeiro cadastre um aluno para depois inclui-lo em uma turma\n")
        input("aperte qualquer tecla para voltar")
        tela()

    elif not turma:
        print("não há turmas cadastradas")
        print("primeiro cadastre uma turma para depois incluir um aluno nela\n")
        input("aperte qualquer tecla para voltar")
        tela()  
        
    else:

        while i == True:

            while i == True:

                print("quais desses alunos você deseja adicionar em uma turma?")
                print("\n")

                for x in aluno:
                    print("codigo do aluno: %s\nNome: %s\nLogin: %s\nSenha: %s\nE-mail: %s\nData de nascimento: %s" % (x))
                    print("*" * 50)


                codaluno = input("\ndigite o codigo do aluno: ")
                tela()

                if not codaluno:
                    print("codigo em branco!, por favor digite novamente ")
                    input("aperte qualquer tecla para continuar")
                    tela()
                else:
                    break


            conexão = sqlite3.connect("database.db")
            cursor = conexão.cursor()

            cursor.execute('''select * from aluno where codaluno = ?''',(codaluno))

            res = cursor.fetchone()

            if res == None:
                opcaoinvalida()
                tela()

            else:
                break

        while i == True:
            input("proxima parte !!!!!!!!!!!!terminar URGENTE!!!!!!!!!!!!!!!!!!!!!")




            cursor.close()
            conexão.close()


#função para cadastrar professores
def cad_prof():

    tela()

    i = True

    while i == True:

        while i == True:
            
            print("nome completo do professor")
            nome = input()
            tela()
            if not nome:
                
                print("Nome em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
            else:
                tela()
                break

        while i == True:

            print("digite o E-mail do professor")
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
            
                
            print("digite o login do professor")
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
            
            senha = getpass.getpass("digite a senha do professor\n")
        
            
            if not senha:
                tela()
                print("Senha em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
                
            elif (len (senha) < 6):
                tela()
                print("a senha digitada é muito curta!\ndigite pelo menos 6 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()

            elif (len(senha) > 20):
                tela()
                print("a senha digitada é muito grande!\ndigite no maximo 20 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()

            senha1 = getpass.getpass("digite a senha novamente\n")
        
            
            if not senha1:
                tela()
                print("Senha em branco!")
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
            insert into professor (nome, login, email, senha)
                values (?, ?, ?, ?)
                ''', (nome, login, email, senha))

        conexão.commit()
        cursor.close()
        conexão.close()
        
    
        
        tela()


        while i == True:

            menu = input("cadastro efetuado com sucesso!\ndeseja cadastrar outro professor? (s/n)")
            tela()

            if menu == ("s"):
                break
            elif menu == ("n"):
                i = False
            else:
                opcaoinvalida()



#função para visualizar todos os professores
def vis_prof():
    
    tela()
    conexão = sqlite3.connect("database.db")
    cursor = conexão.cursor()

    cursor.execute("select * from professor")
    res = cursor.fetchall()

    for x in res:
        print("codigo do professor: %s\nNome: %s\nLogin: %s\nSenha: %s\nE-mail: %s" %(x))
        print("*" * 50)

    print("\n")
    input("aperte qualquer tecla para voltar")
    tela()

    cursor.close()
    conexão.close()

#função para cadastrar administradores
def cad_admin():
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
                print("Senha em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
                
            elif (len (senha) < 6):
                tela()
                print("a senha digitada é muito curta!\ndigite pelo menos 6 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()

            elif (len(senha) > 20):
                tela()
                print("a senha digitada é muito grande!\ndigite no maximo 20 digitos!\n")
                input("aperte qualquer tecla para continuar!")
                tela()

            senha1 = getpass.getpass("digite a senha novamente\n")
            

            if not senha1:
                
                tela()
                print("Senha em branco!")
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


        while i == True:

            menu = input("cadastro efetuado com sucesso!\ndeseja cadastrar outro administrador? (s/n)")
            tela()

            if menu == ("s"):
                break
            elif menu == ("n"):
                i = False
            else:
                opcaoinvalida()
                
#função para visualizar todos os administradores             
def vis_admin():
    
    tela()

    conexão = sqlite3.connect("database.db")
    cursor = conexão.cursor()

    cursor.execute("select * from administrador")
    res = cursor.fetchall()

    for x in res:
        print("codigo do administrador: %s\nNome: %s\nLogin: %s\nSenha: %s\nE-mail: %s" %(x))
        print("*" * 50)
        
    

    print("\n")
    input("aperte qualquer tecla para voltar")
    tela()

    cursor.close()
    conexão.close()
    
#função para cadastrar turmas
def cad_turma():

    i = True

    while i == True:
        
        while i == True:
            
            print("digite o nome da turma")
            nome_turma = input()
            tela()
            if not nome_turma:
                
                print("nome em branco!")
                print("digite novamente")
                print("aperte qualquer tecla para continuar")
                input()
                tela()
                
            else:
                tela()
                break

        conexão = sqlite3.connect("database.db")
        cursor = conexão.cursor()
    
        cursor.execute('''
            insert into turma (nometurma)
                values (?)
                ''', (nome_turma,))

        conexão.commit()
        cursor.close()
        conexão.close()

        print("turma cadastrada com sucesso!")

        while i == True:

            menu = input("deseja cadastrar outra turma? (s/n)")
            tela()

            while i == True:

                if menu == ("s"):
                    break

                elif menu == ("n"):
                    i = False

                else:
                    opcaoinvalida()
                    break
            break
            
            tela()
    
#função para visualizar as turmas

def vis_turma():
    
    tela()
    
    conexão = sqlite3.connect("database.db")
    cursor = conexão.cursor()

    cursor.execute("select * from turma")
    res = cursor.fetchall()

    for x in res:
        print("codigo da turma: %s\nnome da turma: %s" %(x))
        print("*" * 50)
        
    

    print("\n")
    input("aperte qualquer tecla para voltar")
    tela()

    cursor.close()
    conexão.close()


#função onde o professor ira visualizar o boletim do aluno
def verboletim():

    input("em andamento!!")
    
