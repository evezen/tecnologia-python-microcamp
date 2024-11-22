#Orientação a objetos em Python
#Uma classe é uma instrução que possui requisitos 
# básicos para o desenvolvimento de um objeto.
#Dentro dela existem métodos (funções) e atributos (variaveis).
#Quando é criada necessita de um método construtor e de métodos
#de acesso aos atributos.

class pessoa:
    def __init__(self,nome,cpf,dt_nasc,endereco):
        self.nome = nome
        self.cpf = cpf
        self.dt_nasc = dt_nasc
        self.endereco = endereco
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self,cpf):
        self.cpf = cpf

    def get_dt_nasc(self):
        return self.dt_nasc
    
    def set_dt_nasc(self,dt_nasc):
        self.dt_nasc = dt_nasc

    def get_endereco(self):
        return self.endereco
    
    def set_endereco(self,endereco):
        self.endereco = endereco
        