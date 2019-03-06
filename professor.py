from bibliotecas import *
from variaveis import *
import sqlite3


def cad_ava():

    tela()

    i = True
    
    while i == True:

        while i == True:
            
            print("qual disciplina se refere essa avaliação?")
            disc = input()
            tela()            
            if not disc:
                print("nome em branco, por favor digite novamente!")
                input()
                tela()
                    
            else:
                tela()
                break
                
        while i == True:
            
            print("qual a descrição da avaliação?")
            desc = input()
            tela()
            if not desc:

                print("descrição em branco, por favor digite novamente!")
                input()
                tela()
            else:
                tela()
                break

        while i == True:

            print("qual o valor dessa avalição?")
            valor = input()
            tela()
            if not valor:
                print("valor em branco, por favor digite novamente!")
                input()
                tela()
            else:
                tela()
                break
            
        while i == True:

            print("qual a data dessa avaliação?")
            data = input()
            tela()

            if not data:
                print("data em branco, por favor digite novamente!")
                input()
                tela()
            else:
                tela()
                break

        tela()
        # nessa parte é feita a conexão com o banco sqlite e adicionado os valores às chaves do banco
        conexão = sqlite3.connect("database.db")
        cursor = conexão.cursor()

        cursor.execute('''
                insert into avaliacao (disciplina, descricao, valor, data)
                    values(?, ?, ?, ?)
                    ''', (disc, desc, valor, data))

        
        conexão.commit()
        cursor.close()
        conexão.close()
        
        tela()

        tela()
        while i == True:
            
            menu = input("deseja cadastrar outra avaliação? (s/n) ")
            tela()
            
            if menu == ("s"):
                break
            elif menu == ("n"):
                i = False
            else:
                opcaoinvalida()
            
# função para visualizar avaliações
def vis_ava():

    conexão = sqlite3.connect("database.db")
    cursor = conexão.cursor()

    cursor.execute(" select * from avaliacao")
    res = cursor.fetchall()

    if not res:
        
        print("não há avaliação casdastrada!")
        print("\n")
        input("aperte qualquer tecla para voltar")
        tela()
        
    else:
        
        for x in res:
            print("disciplina: %s\ndescrição: %s\nvalor: %s\ndata: %s" %(x))
            print("*" * 50)
            
        input("aperte qualquer tecla para voltar")
        tela()
    
    cursor.close()
    conexão.close()
    
# função para lançar todas as notas de uma vez
def lancarnota():


    conexão = sqlite3.connect("database.db")
    cursor = conexão.cursor()

    cursor.execute(" select * from aluno")
    res = cursor.fetchall()    


    if not res:
        print("não há alunos casdastrados!")
        print("primeiro cadastre um aluno para depois lançar sua nota")
        print("\n")
        input("aperte qualquer tecla para voltar")
        tela()
        
    else:
        
        for x in res:
            print("codigo do aluno: %s\nNome: %s\nLogin: %s\nSenha: %s\nE-mail: %s\nData de nascimento: %s" %(x))
            print("*" * 50)

            n1 = input("digite a N1: ")
            n2 = input("digite a N2: ")
            n3 = input("digite a N3: ")
     
            tela()

            cursor.execute('''
                insert into notaxaluno (n1, n2, n3)
                    values (?, ?, ?)
                         ''', (n1, n2, n3,))

            
            conexão.commit()
            
            print("notas lançadas com sucesso!")
            input("aperte qualquer tecla para continuar")
            tela()
            
        
        cursor.close()
        conexão.close()
        
        print("todos as notas ja foram lançadas")
        input("aperte qualquer tecla para voltar")
        tela()

        
            

