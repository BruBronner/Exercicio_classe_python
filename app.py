class Carro:
    
    def __init__(self,Carro):
        self._carro = Carro
        self._motor = None
        self._fabricante = None
        
    #property da classe Carro
    @property
    def carro(self):
        return self._carro
    
    @property
    def motor(self):
        return self._motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    #setter da classe carro
    @carro.setter
    def carro(self, valor):
        self._carro = valor
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
#classe do motor do carro
class MotorDoCarro:
    def __init__(self,motor):
        self._motor = motor
#property da classe Motor Do Carro
    @property
    def motor(self):
        return self._motor
#setter da classe Motor Do Carro
    @motor.setter
    def motor(self, motor):
        self._motor = motor

class Fabricante:
    
    def __init__(self, fabricante):
        self._fabricante = fabricante
 #property da classe Fabricante       
    @property
    def fabricante(self):
        return self._fabricante
#setter da Classe Fabricante 
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


#variaveis
porsche = Carro('Porsche')
motorizacao = MotorDoCarro('4.0')
porsche.motor = motorizacao
fabric = Fabricante('Alemã')
porsche.fabricante = fabric

print(f'você possui uma : {porsche.carro}, com o motor de litragem {porsche.motor.motor} de uma fabricante {porsche.fabricante.fabricante}')
    