from pessoa import *

if __name__=="__main__":
    #Lista vazia
    cadastro = []
    
    def cadastrar():
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
    
    def mostrar():
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

    cadastrar()
    atualizar()
                