from pessoa import *
import os, time

if __name__=="__main__":
    #Lista vazia
    cadastro = []
    
    def cadastrar():
        limpar()
        #Interação armazena a resposta
        res = int(input("Deseja cadastrar uma pessoa?\n1 - SIM\n0 - NÃO\n"))
        #Se a resposta for igual a 1 peça os dados
        while(res==1):
            #Interação e armazenamento dos dados
            nome = str(input("\nDigite seu nome: "))
            cpf = str(input("Digite seu cpf: "))
            dt_nasc = str(input("Digite a sua data de nascimento: "))
            endereco = str(input("Digite o seu endereço: "))
            #Lista cadastro guarda um objeto pessoa com os atributos
            cadastro.append(pessoa(nome,cpf,dt_nasc,endereco))
            #Alerta de cadastro
            print("\nCadastrado com sucesso!")
            #Nova pergunta
            res = int(input("Deseja cadastrar uma pessoa?\n1 - SIM\n0 - NÃO\n"))
            mostrar()
        interface()

    #Mostrar dados
    def mostrar():
        limpar()
        #Formatação dos dados exibidos
        y = 0
        print("{:<4}{:<10}{:<14}{:<15}{:<15}".format("Nº","Nome","CPF","Nascimento","Endereço"))
        #Para cada objeto guardado no cadastro
        for x in cadastro:
            y= y+1
            #Format com o metodo getter
            print("{:<4}{:<10}{:<14}{:<15}{:<15}".format(
                    y,
                    x.get_nome(),
                    x.get_cpf(),
                    x.get_dt_nasc(),
                    x.get_endereco()))
        x = int(input("\nDigite 1 - Retornar: "))
        if(x==1):interface()
        else:
            print("\nOperação invalida!")
            limpar()
            mostrar()

    #Atualizar cadastro
    def atualizar():
        res = int(input("Deseja atualizar um dado?\n1 - SIM\n0 - NÃO\n"))
        while(res==1):
            x = int(input("Digite a linha que deseja atualizar:"))
            x -= 1
            y = int(input("Escolha o dado que deseja atualizar:\n1 - NOME\n2 -  CPF\n3 - NASCIMENTO\n4 - ENDEREÇO\n"))
            if(y<=4 and y>0):
                if(y==1):
                    z = str(input("Digite o nome atual: "))
                    cadastro[x].set_nome(z)
                elif(y==2):
                    z = str(input("Digite o cpf atual: "))
                    cadastro[x].set_cpf(z)
                elif(y==3):
                    z = str(input("Digite a data de nascimento atual: "))
                    cadastro[x].set_dt_nasc(z)
                elif(y==4):
                    z = str(input("Digite o endereço atual: "))
                    cadastro[x].set_endereco(z)
            else:
                    print("Opção incorreta")
            
            res = int(input("Deseja atualizar um dado?\n1 = SIM\n0 - NÃO\n"))
            mostrar()
        interface()
        
    #Limpar tela do prompt
    def limpar(): os.system('cls')

    #Remover um cadastro
    def remover():
        limpar()
        res = int(input("Deseja remover um dado?\n1 - SIM\n0 - NÃO\n"))
        while(res ==1):
            x = int(input("Digite a linha que deseja remover: "))
            x-=1
            res = int(input(f"Certeza que deseja remover os dados de {cadastro[x].get_nome()}?\n1 - SIM\n0 - NÃO\n"))
            if(res==1):
                cadastro.pop(x)
                print("Cadastro removido com sucesso!\n")
            remover()
        interface()
        mostrar()

#Tela inicial com as opções
def interface():
    limpar()
    print("=====CADASTRO DE CLIENTES=====")
    res = int(input("Digite quais opções deseja:\n1 - CADASTRAR CLIENTE\n2 - ATUALIZAR CADASTRO\n3 - REMOVER CLIENTE\n4 - MOSTRAR TABELA\n5 - SAIR\n"))
    if(res ==1):cadastrar()
    if(res ==2):atualizar()
    if(res ==3):remover()
    if(res ==4):mostrar()
    if(res ==5):exit()
    if(res>5 or res<1):
        print("Operação invalida\n")
        time.sleep(2)
        interface()

interface()