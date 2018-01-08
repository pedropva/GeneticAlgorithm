from math import pi, exp, sqrt, cos
class quickmaths():

    #Função Completa
    @staticmethod
    def f(x):#Funcao f(x) completa
        return -20*quickmaths.e1(x)-quickmaths.e2(x)+20+exp(1)

    @staticmethod
    def e1(x):#Exponencial 1
        return exp(-0.2*sqrt((1/2)*quickmaths.s1(x)))

    @staticmethod
    def e2(x):#Exponencial 2
        return exp((1/2)*quickmaths.s2(x))

    #Função Sigma c(x)
    @staticmethod
    def s1(x):#Somatorio 1
        soma = 0
        for i in range(2):
            soma += x[i]**2
        return soma

    @staticmethod
    def s2(x):#Somatorio 2
        soma = 0
        for i in range(2):
            soma += cos(2*pi*x[i])
        return soma
