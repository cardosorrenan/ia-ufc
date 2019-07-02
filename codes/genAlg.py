import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class Individuo:
    def __init__(self, x, y):
        self.x = x * 0.01953125
        self.y = y * 0.01953125
        self.valor = np.abs(self.x * np.sin(self.y * np.pi / 4) + self.y * np.sin(self.x * np.pi / 4))
        self.cromossomo = np.binary_repr(x, 10) + np.binary_repr(y, 10)

    def crossover(self, conjuge):
        tam_vetor = int(len(self.cromossomo)/2)
        ponto_corte = round(np.random.rand() * tam_vetor)

        pai1_x = self.cromossomo[0:tam_vetor]
        pai1_y = self.cromossomo[tam_vetor::]

        pai2_x = conjuge.cromossomo[0:tam_vetor]
        pai2_y = conjuge.cromossomo[tam_vetor::]

        filho1_x = pai1_x[0: ponto_corte] + pai2_x[ponto_corte::]
        filho1_y = pai1_y[0: ponto_corte] + pai2_y[ponto_corte::]

        filho2_x = pai2_x[0: ponto_corte] + pai1_x[ponto_corte::]
        filho2_y = pai2_y[0: ponto_corte] + pai1_y[ponto_corte::]

        filhos = [Individuo(int(filho1_x, 2), int(filho1_y, 2)),
                  Individuo(int(filho2_x, 2), int(filho2_y, 2))]

        '''
        print("\n\nPonto de Corte: {} -----------------------\n".format(ponto_corte))
        print("  Pai 1: x: {}  y: {}  Cromossomo: {}".format(pai1_x, pai1_y, self.cromossomo))
        print("         x: {}  y: {}  z: {:.2f}\n".format(self.x, self.y, self.valor))

        print("  Pai 2: x: {}  y: {}  Cromossomo: {}".format(pai2_x, pai2_y, conjuge.cromossomo))
        print("         x: {}  y: {}  z: {:.2f}\n".format(conjuge.x, conjuge.y, conjuge.valor))

        print("Após o corte...\n")

        print("  Filho 1: x (pai 1): {} +  x (pai 2): {}".format(pai1_x[0: ponto_corte], pai2_x[ponto_corte::]))
        print("           y (pai 1): {} +  y (pai 2): {}".format(pai1_y[0: ponto_corte], pai2_y[ponto_corte::]))
        print("           Cromossomo: {}".format(filhos[0].cromossomo))
        print("           Novo Indivíduo: x: {}  y: {}  z: {:.2f}\n".format(filhos[0].x, filhos[0].y, filhos[0].valor))
        print("  Filho 2: x (pai 2): {} +  x (pai 1): {}".format(pai2_x[0: ponto_corte], pai1_x[ponto_corte::]))
        print("           y (pai 2): {} +  y (pai 1): {}".format(pai2_y[0: ponto_corte], pai1_y[ponto_corte::]))
        print("           Cromossomo: {}".format(filhos[1].cromossomo))
        print("           Novo Indivíduo: x: {}  y: {}  z: {:.2f}\n".format(filhos[1].x, filhos[1].y, filhos[1].valor))
        '''
        return filhos

    def mutacao(self, taxa_mutacao):
        cromossomo_modificado = []  

        for i in range(len(self.cromossomo)):
            if np.random.rand() < taxa_mutacao:                
                if self.cromossomo[i] == '1':
                    cromossomo_modificado += '0'
                else:
                    cromossomo_modificado += '1'
            else:
                cromossomo_modificado += self.cromossomo[i]

        return ''.join(cromossomo_modificado)


class Populacao:
    def __init__(self, tamanho_pop, total_individuos):
        print("\n Geração      X           Y             Z       Cromossomo")
        self.populacao = []
        self.tamanho_pop = tamanho_pop
        self.geracao = 0
        self.soma_valores = 0
        self.geracao = 1

        for i in range(self.tamanho_pop):
            n = np.random.randint(0, len(total_individuos))
            self.populacao.append(total_individuos[n])
            self.soma_valores += total_individuos[n].valor

    def melhor_individuo(self):
        self.populacao = sorted(self.populacao,
                            key = lambda populacao: populacao.valor,
                            reverse = True)
        return self.populacao[0]

    def gira_roleta(self):
        pai = -1
        valor_sorteado = np.random.rand() * self.soma_valores
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].valor
            pai += 1
            i += 1
        return pai

    def nova_populacao(self):
        filhos = []
        nova_geracao = []
        '''
        Exibe a chance de cada indivíduo ser pai em cada rodada

        print("Individuo    Valor      Probabilidade")
        for individuo in self.populacao:
            print("     {}       {:6.3f}     {:.3f}%".format(0, individuo.valor, (individuo.valor/self.soma_valores)*100))
        print("-----------------------------------------")
        print("Total:  {}    {}%".format(self.soma_valores, (self.soma_valores/self.soma_valores)*100))
        '''

        for i in range(0, int(self.tamanho_pop/2)):
            pai1 = self.gira_roleta()
            pai2 = self.gira_roleta()
            filhos = self.populacao[pai1].crossover(self.populacao[pai2])
            filhos[0].mutacao(taxa_mutacao)
            filhos[1].mutacao(taxa_mutacao)
            nova_geracao.append(filhos[0])
            nova_geracao.append(filhos[1])

        self.populacao = list(nova_geracao)
        self.geracao += 1
        return self

    def visualiza_geracao(self):
        print("  {:3d}      {:3f}    {:3f}    {:3f}    {}".format(self.geracao, self.populacao[0].x, self.populacao[0].y, self.populacao[0].valor, self.populacao[0].cromossomo))

if __name__ == '__main__':
    total_individuos = []
    for x in range(0, 1024):
        for y in range(0, 1024):
            total_individuos.append(Individuo(x, y))
        # print("Carregando todos os pontos... {:.2f}%".format((x/1023)*100))

    tam_pop = 100
    taxa_mutacao = 0.05
    numero_geracoes = 30
    melhores_individuos = []
    populacao = Populacao(tam_pop, total_individuos)
    ax = plt.axes(projection='3d')

    for geracoes in range(numero_geracoes):
        melhores_individuos.append(populacao.melhor_individuo())
        populacao.visualiza_geracao()
        populacao = populacao.nova_populacao()

    melhor_individuo = sorted(melhores_individuos,
                              key=lambda pop: pop.valor,
                              reverse=True)[0]

    print(" \nMelhor solução \n      x= {}\n      y= {:3f}\n f(x,y)= {:3f}\n".format(melhor_individuo.x, melhor_individuo.y, melhor_individuo.valor))
    x_plot = np.linspace(0, 20, 100)
    y_plot = np.linspace(0, 20, 100)
    x_grid, y_grid = np.meshgrid(x_plot, y_plot)
    z_grid = np.abs(x_grid * np.sin(y_grid * np.pi / 4) + y_grid * np.sin(x_grid * np.pi / 4))
    ax.contour3D(x_grid, y_grid, z_grid, 100, cmap='binary', alpha=0.8)
    for ind in melhores_individuos:
        ax.scatter(ind.x, ind.y, ind.valor, c='red', marker='*', s=100)
    plt.show()
