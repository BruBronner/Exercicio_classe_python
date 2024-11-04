class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def trabalhar(self):
        print(f'o {self.nome}{self.sobrenome} está trabalhando')

class heranca(Pessoa):
    def __init__(self,nome,sobrenome):
        Pessoa.__init__(self, nome,sobrenome)


c1 = heranca('Brunno', 'Bronner')
#print(c1.nome, c1.sobrenome)
print(c1.trabalhar())
print(c1.mro())

    