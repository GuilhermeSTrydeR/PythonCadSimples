#from bibliotecas import *, biblioteca que eu criei com algumas funções básicas
#from professor import *, biblioteca que contem todas as funções do professor
#from adm import *, biblioteca que contem todas as funções de administrador
from login import *
from professor import *
from bibliotecas import *
from adm import *
from variaveis import *

#essa parte vai criar caso não exista, as tabelas do banco de dados sqlite

conexão = sqlite3.connect("database.db")
cursor = conexão.cursor()

cursor.execute('''
        create table if not exists aluno(
            codaluno integer PRIMARY KEY AUTOINCREMENT,
            nome text,
            login text,
            senha text,
            email text,
            nascimento text)
            ''')

cursor.execute('''
        create table if not exists professor(
            codprof integer PRIMARY KEY AUTOINCREMENT,
            nome text,
            login text,
            senha text,
            email text)
            ''')

cursor.execute('''
        create table if not exists administrador(
            codadmin integer PRIMARY KEY AUTOINCREMENT,
            nome text,
            login text,
            senha text,
            email text)
            ''')

cursor.execute('''
        create table if not exists turma(
            codturma integer PRIMARY KEY AUTOINCREMENT,
            nometurma text)
            ''')

cursor.execute('''
        create table if not exists turmaxaluno(
            codturma text,
            codaluno text)
            ''')

cursor.execute('''
        create table if not exists avaliacao(
            disciplina text,
            descricao text,
            valor text,
            data text)
            ''')

cursor.execute('''
        create table if not exists notaxaluno(
            codaluno integer PRIMARY KEY AUTOINCREMENT,
            n1 float,
            n2 float,
            n3 float)
            ''')
# essa parte vai ser verificado se existe algum administrador registrado,
# caso não tenha o programa vai entrar em modo 'primeiro login' e
# cadastrar um administrador

cursor.close()
conexão.close()

conexão = sqlite3.connect("database.db")
cursor = conexão.cursor()


cursor.execute("select * from administrador")
res = cursor.fetchone()


if res == None:
    login()

cursor.close()
conexão.close()

# menu principal
print("seja bem vindo!")
input("aperte qualquer tecla para continuar")
tela()

while i == True:
    
    tela()
    print("com qual perfil você está acessando?\n")
    print("1 - aluno")
    print("2 - professor")
    print("3 - administrador")
    print("4 - Sair do Programa")
    menu = input()   

    tela()


# primeira area do programa, area "aluno"

    if menu == ("1"):
        
        while i == True:

            print("Perfil: aluno")
            print("digite suas credenciais")
            print("para retornar ao menu digite 'sair' \n")
            usr = input("digite seu nome de usuario: ")
            if usr == ("sair"):
                break
            pas = getpass.getpass("Digite sua senha: ")
            if pas == ("sair"):
                break

            tela()

            conexão = sqlite3.connect("database.db")
            cursor = conexão.cursor()

            cursor.execute(" select * from aluno where login = '%s'" % usr)
            res = cursor.fetchone()
            
            if res == None:
                senhainvalida()
                continue


            cursor.close()
            conexão.close()
            
            conexão = sqlite3.connect("database.db")
            cursor = conexão.cursor()

            cursor.execute(" select codaluno from notaxaluno where codaluno = '%s'" % res[0])
            cod = cursor.fetchone()

            
            cursor.close()
            conexão.close()

                          


            if (usr == res[2] and pas == res[3]):

                while i == True:

                    print("você esta logado com o perfil: %s \n" % usr)
                    print("bem vindo %s" % res[1])
                    print("gostaria de ver seu boletim? (S/N)")
                    menu = input()
                    tela()
      
                    if menu == ("s"):
                        # nessa parte devera ser exibido o boletim do aluno logado ( essa parte ta travando)
                        conexão = sqlite3.connect("database.db")
                        cursor = conexão.cursor()

                        cursor.execute(" select n1, n2, n3 from notaxaluno where codaluno = '%s'" % cod)
                        res = cursor.fetchone()

                        if cod == None:
                                
                            print("não há registros")
                            input("aperte qualquer tecla para voltar")
                            tela()
                            break


                        cursor.close()
                        conexão.close()

                        
                        media = float(res[0] + res[1] + res[2])
                       

                       
                            
                        print("N1: %s\nN2: %s\nN3: %s" % (res))
                        print("\nTotal: ", media)
                        print("\n")


                        if (media > 60):
                            print("APROVADO")
                            
                        elif (media < 40):
                            print("REPROVADO")
                            
                        elif (media >= 40 < 60):
                            print("RECUPERAÇÃO FINAL")
                                  
                        print("*" * 50)

                        input("aperte qualquer tecla para voltar ao menu!")
                        tela()
                        break

                    elif menu == ("n"):

                        while i == True:

                            cond = input("deseja voltar ao menu principal ou sair? (menu/sair)")
                            tela()

                            if cond == ("sair"):
                                i = False

                            elif cond == ("menu"):
                                break

                            else:
                                opcaoinvalida()

                        break


                    else:
                        opcaoinvalida()
                        continue
                    break


            else:
                senhainvalida()
                continue
            break


          


           
# segunda area do programa, area "professor"     
    elif menu == ("2"):

        while i == True:

            print("Perfil: professor")
            print("digite suas credenciais")
            print("para retornar ao menu digite 'sair' \n")

            usr = input("digite seu nome de usuario: ")
            if usr == ("sair"):
                break

            pas = getpass.getpass("digite sua senha: ")
            if pas == ("sair"):
                break


            tela()

            conexão = sqlite3.connect("database.db")
            cursor = conexão.cursor()

            cursor.execute("select * from professor where login = '%s'" % usr)
            res = cursor.fetchone()

            if res == None:
                senhainvalida()
                continue


            cursor.close()
            conexão.close()

         
            if (usr == res[2] and pas == res[3]):
                
                while i == True:

                    print("você esta logado com o perfil: %s\n" % usr)
                    print("bem vindo %s" % res[1])
                    print("\n")
                    print("1 - Cadastrar Avaliação")
                    print("2 - Lançar Nota")
                    print("3 - Ver Boletim")
                    print("4 - voltar ao menu principal")
                    print("5 - sair do programa")

                    menu = input()
                    tela()

                    if menu == ("1"):
                        cad_ava()

                    elif menu == ("2"):
                        lancarnota()

                    elif menu == ("3"):
                        verboletim()

                    elif menu == ("4"):
                        break

                    elif menu == ("5"):
                        i = False
                            
                    else:
                        opcaoinvalida()
                            
                    
                break
            
            else:
                senhainvalida()
                continue
            break

# terceira area do programa, area "administrador"
    elif menu == ("3"):
        
        while i == True:
            i = True

            print("Perfil: administrador")
            print("digite suas credenciais")
            print("para retornar ao menu digite 'sair' \n")

            usr = input("digite seu nome de usuario: ")
            if usr == ("sair"):
                break
            pas = getpass.getpass("digite sua senha: ")
            if pas == ("sair"):
                break
            
            tela()

            conexão = sqlite3.connect("database.db")
            cursor = conexão.cursor()

            cursor.execute("select * from administrador where login = '%s'" % usr)
            res = cursor.fetchone()

            if res == None:
                senhainvalida()
                continue

            cursor.close()
            conexão.close()

            if (usr == res[2] and pas == res[3]):

                while i == True:

                    print("você esta logado com o perfil:", usr, "\n")
                    print("1 - administradores")
                    print("2 - professores")
                    print("3 - turmas")
                    print("4 - alunos")
                    print("5 - Visualizar Avaliação")
                    print("6 - Visualizar Boletim")
                    print("7 - Visualizar Nota")
                    print("8 - voltar ao menu principal")
                    print("9 - sair do programa")
                    menu = input()
                    tela()

                    if menu == ("1"):

                        while i == True:

                            print("administradores")
                            print("*" * 50)
                            print("1 - Cadastrar administradores")
                            print("2 - Visualizar todos os administradores")
                            print("3 - Sair")
                            menu = input()
                            tela()

                            if menu == ("1"):
                                cad_admin()

                            elif menu == ("2"):
                                vis_admin()



                            elif menu == ("3"):
                                break
                            else:
                                opcaoinvalida()

                    elif menu == ("2"):

                        while i == True:

                            print("professores")
                            print("*" * 50)
                            print("1 - Cadastrar professor")
                            print("2 - Visualizar todos os professores")
                            print("3 - Sair")
                            menu = input()
                            tela()

                            if menu == ("1"):
                                cad_prof()

                            elif menu == ("2"):
                                vis_prof()

                            elif menu == ("3"):
                                break
                            else:
                                opcaoinvalida()

                    elif menu == ("3"):

                        while i == True:

                            print("turmas")
                            print("*" * 50)
                            print("1 - Cadastrar turmas")
                            print("2 - Visualizar todas as turmas")
                            print("3 - Sair")
                            menu = input()
                            tela()

                            if menu == ("1"):
                                cad_turma()

                            elif menu == ("2"):
                                vis_turma()

                            elif menu == ("3"):
                                break

                            else:

                                opcaoinvalida()

                    elif menu == ("4"):

                        while i == True:

                            print("alunos")
                            print("*" * 50)
                            print("1 - Cadastrar alunos")
                            print("2 - Visualizar todos os alunos")
                            print("3 - visualizar aluno por codigo")
                            print("4 - Vincular aluno em turma")
                            print("5 - Sair")
                            menu = input()
                            tela()

                            if menu == ("1"):
                                cad_aluno()

                            elif menu == ("2"):
                                vis_aluno()

                            elif menu == ("3"):
                                vis_aluno_codigo()

                            elif menu == ("4"):
                                inc_aluno()

                            elif menu == ("5"):
                                break
                            else:
                                opcaoinvalida()


                    elif menu == ("5"):
                        vis_ava()




                    elif menu == ("6"):
                        print("visualizar boletim")

                    elif menu == ("7"):
                        print("visualizar notas")

                    elif menu == ("8"):
                        break

                    elif menu == ("9"):
                        i = False

                    else:
                        opcaoinvalida()

                break


            else:
                senhainvalida()
                continue
            break
  
       
                
    
    elif menu == ("4"):
        break
       
    else:
        opcaoinvalida()

