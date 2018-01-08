import numpy as np
import matplotlib.pyplot as plt

MAX_GEN = 500
TAM_POP = 100
TAM_CROM = 64
TX_CROSS = 0.9
TX_MUT = 0.001

def GeraPop():
    return np.random.randint(0,2, size=(TAM_POP, TAM_CROM))

def BinParaInt(numeroBin):
    x1, x2 = string[:len(numeroBin)/2], string[len(numeroBin)/2:]
    #int(''.join(str(x) for x in x1,2)
    return [int(''.join(str(x) for x in x1,2)),int(''.join(str(x) for x in x2,2))]#retorna vetor com os dois inteiros

def Aptidao(cromossomo):
    x = BinParaInt(cromossomo)
    return 1/(1+f(x))


def CalculaAptidoes(pop):
    return [Aptidao(x) for x in pop]

def SelecaoRoleta(aptidoes):
    percentuais = np.array(aptidoes)/float(sum(aptidoes))
    vet = [percentuais[0]]
    for p in percentuais[1:]:
        vet.append(vet[-1]+p)
    r = np.random.random()
    for i in range(len(vet)):
        if r <= vet[i]:
            return i
            
def Cruzamento(pai,mae):
    corte = np.random.randint(TAM_CROM)
    return (list(pai[:corte])+list(mae[corte:]),list(mae[:corte])+list(pai[corte:]))

def Mutacao(cromossomo):
    r = np.random.randint(TAM_CROM)
    cromossomo[r] = (cromossomo[r]+1)%2
    return cromossomo

pop = GeraPop()

medias = []
melhores = []

for g in range(MAX_GEN):
    
    aptidoes = CalculaAptidoes(pop)
    nova_pop = []
    for c in range(TAM_POP/2):
        pai = pop[SelecaoRoleta(aptidoes)]
        mae = pop[SelecaoRoleta(aptidoes)]
        r = np.random.random()
        if r <= TX_CROSS:
            filho,filha = Cruzamento(pai,mae)
        else:
            filho,filha = pai,mae

        r = np.random.random()
        if r <= TX_MUT:
            filho = Mutacao(filho)
        r = np.random.random()
        if r <= TX_MUT:
            filha = Mutacao(filha)
            
        nova_pop.append(filho)
        nova_pop.append(filha)
    
    pop = nova_pop
    medias.append(np.mean(aptidoes))
    melhores.append(np.max(aptidoes))
    print medias[-1]
    
aptidoes = CalculaAptidoes(pop)

index_solucao = aptidoes.index(max(aptidoes))

print "Resposta final: " + str(BinParaInt(pop[index_solucao])[0]) + "e" + str(BinParaInt(pop[index_solucao])[1])
