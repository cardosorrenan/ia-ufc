import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 


class noh:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.valor = np.abs( self.x * np.sin( self.y * np.pi / 4 ) + self.y * np.sin( self.x * np.pi / 4 ) )


def main():  
    max_locais,trajetoria = [],[]

    while True: 
        busca = int(input('Quantidade de buscas aleatórias: '))
        if not busca<=0:
            break

    print('Máximos Locais')    
    for it in range(1,busca+1):
        x_inicio = round(np.random.uniform(-20,20),2)  
        y_inicio = round(np.random.uniform(-20,20),2)
        noh_atual = noh(x_inicio, y_inicio)

        while True:
            trajetoria.append([it,round(noh_atual.x,2),round(noh_atual.y,2),round(noh_atual.valor,6)])
            vizinhos = [noh(noh_atual.x-0.01,noh_atual.y),
                        noh(noh_atual.x+0.01,noh_atual.y), 
                        noh(noh_atual.x,noh_atual.y+0.01),
                        noh(noh_atual.x,noh_atual.y-0.01)]
            valores = [x.valor for x in vizinhos]
            valor_max = max(valores)
            if not any((ax <= -20 or ax >= 20) for ax in [noh_atual.x, noh_atual.y]):
                if noh_atual.valor <= valor_max:
                    for vizinho in vizinhos:
                        if vizinho.valor == valor_max:
                            noh_atual = vizinho
                else: 
                    cont = 0
                    for traj in trajetoria:
                        if traj[0] == it:
                            cont += 1
                    max_locais.append([it,noh_atual.x, noh_atual.y, noh_atual.valor])
                    print(" Busca nº{}: X:{} Y:{} Z:{} / Passos:{}".format(it,round(noh_atual.x,2),round(noh_atual.y,2),round(noh_atual.valor,6),cont))       
                    break
            else: 
                print(" Busca nº{}: A busca encontrou o limite estabelecido (-20 < x,y < 20)".format(it))       
                break

    print('\nMáximo Global')
    max_global = max(max_locais[it][3] for it in range(0,len(max_locais)))
    
    indice_max_global = []
    for loc in max_locais:
        if round(loc[3],6) == round(max_global,6):
            print(" Busca nº{}: X:{} Y:{} Z:{}".format(loc[0],round(loc[1],2),round(loc[2],2),round(loc[3],6))) 
            indice_max_global.append(loc[0])

    def f(x, y):
        return np.abs( x * np.sin( y * np.pi / 4 ) + y * np.sin( x * np.pi / 4 ) )
    
    ax = plt.axes(projection='3d')
    x = np.linspace(-20,20,50)
    y = np.linspace(-20,20,50)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.contour3D(X, Y, Z, 100, cmap='binary', alpha=0.8)
    for ind in indice_max_global:
        for traj in trajetoria:
            if traj[0] == ind:
                ax.scatter(traj[1],traj[2],traj[3], c='red',marker='*', s=10)
    plt.show()


if __name__ == '__main__':
    main()
