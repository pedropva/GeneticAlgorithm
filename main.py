import numpy as np
import matplotlib.pyplot as plt
import string as string
import copy
from quickmaths import quickmaths

MAX_GEN = 1000
TAM_POP = 100
TAM_CROM = 64
TX_CROSS = 0.9
TX_MUT = 0.001

def GeraPop():
    return np.random.randint(0,2, size=(TAM_POP, TAM_CROM))

def desenrolaCromossomo(cromossomo):
    listBin=str(cromossomo).strip()
    mid = len(listBin)/2
    x1 = listBin[:mid]
    x2 = listBin[mid:]
    x1 = x1[1:].strip().replace(" ", "")
    x2 = x2[:-1].strip().replace(" ", "")
    numero1 = x1.replace("\n", "").replace(",", "")
    numero2 = x2.replace("\n", "").replace(",", "")
    return [numero1,numero2]

def BinParaInt(cromossomo):
    fator = 65.536/(2**32-1)
    binarios = desenrolaCromossomo(cromossomo)
    #print binarios
    inteiros = [int(binarios[0],2)*fator - 32.768,int(binarios[1],2)*fator - 32.768]#retorna vetor com os dois inteiros
    #print inteiros
    return inteiros
    

def Aptidao(cromossomo):
    x = BinParaInt(cromossomo)    
    return 1/(1+quickmaths.f(x))
    
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
    #print pop
    print "--------------------------------------------------------------------------------------------------"
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
    print "Media da geracao atual:" + str(medias[-1])
    print "Melhor da geracao atual:" + str(melhores[-1])
    
aptidoes = CalculaAptidoes(pop)

index_solucao = aptidoes.index(max(aptidoes))
print "Resposta final: " + str(BinParaInt(pop[index_solucao]))
print "Binarios: " + str(desenrolaCromossomo(pop[index_solucao]))
print "Aptidao: " + str(Aptidao(pop[index_solucao]))  

#Plotando o grafico
plt.figure(1)
plt.subplot(211)    
plt.ylabel('Melhores aptidoes')
plt.plot([x for x in range(1, MAX_GEN+1)], [melhores[i] for i in range(len(melhores))], 'r.')
plt.axis([0, MAX_GEN+1, 0, max(melhores)])

plt.subplot(212)
plt.xlabel('Geracao')
plt.ylabel('Medias de aptidoes')
plt.plot([x for x in range(1, MAX_GEN+1)], [medias[i] for i in range(len(medias))], 'b.')
plt.axis([0, MAX_GEN+1, 0, max(medias)])

plt.show()

#print "teste: "+ str(BinParaInt([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))