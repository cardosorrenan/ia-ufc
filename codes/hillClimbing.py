import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 


class Noh:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.valor = np.abs(self.x * np.sin(self.y * np.pi / 4) + self.y * np.sin(self.x * np.pi / 4))


def main():
    max_locais, trajetoria = [], []

    while True:
        busca = int(input('Quantidade de buscas aleatórias: '))
        if not busca <= 0:
            break

    print('Máximos Locais')
    for it in range(1, busca+1):
        x_inicio = round(np.random.uniform(-20, 20), 2)
        y_inicio = round(np.random.uniform(-20, 20), 2)
        noh_atual = Noh(x_inicio, y_inicio)

        while True:
            trajetoria.append([it, round(noh_atual.x, 2), round(noh_atual.y, 2), round(noh_atual.valor, 6)])
            vizinhos = [Noh(noh_atual.x-0.01, noh_atual.y),
                        Noh(noh_atual.x+0.01, noh_atual.y),
                        Noh(noh_atual.x, noh_atual.y+0.01),
                        Noh(noh_atual.x, noh_atual.y-0.01)]
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
                    max_locais.append([it, noh_atual.x, noh_atual.y, noh_atual.valor])
                    print("Busca nº{}: X:{} Y:{} Z:{} / Passos:{}".format(it, round(noh_atual.x, 2), round(noh_atual.y, 2), round(noh_atual.valor, 6), cont))
                    break
            else:
                print("Busca nº{}: A busca encontrou o limite estabelecido (-20 < x,y < 20)".format(it))
                break

    print('\nMáximo Global')
    max_global = max(max_locais[it][3] for it in range(0, len(max_locais)))

    indice_max_global = []
    for loc in max_locais:
        if round(loc[3], 6) == round(max_global, 6):
            print("Busca nº{}: X:{} Y:{} Z:{}".format(loc[0], round(loc[1], 2), round(loc[2], 2), round(loc[3], 6)))
            indice_max_global.append(loc[0])

    def func(x_func, y_func):
        return np.abs(x_func * np.sin(y_func * np.pi / 4) + y_func * np.sin(x_func * np.pi / 4))

    a_x = plt.axes(projection='3d')
    x_plot = np.linspace(-20, 20, 50)
    y_plot = np.linspace(-20, 20, 50)
    x_grid, y_grid = np.meshgrid(x_plot, y_plot)
    z_grid = func(x_grid, y_grid)
    a_x.contour3D(x_grid, y_grid, z_grid, 100, cmap='binary', alpha=0.8)

    for ind in indice_max_global:
        for traj in trajetoria:
            if traj[0] == ind:
                a_x.scatter(traj[1], traj[2], traj[3], c='red', marker='*', s=10)
    plt.show()


if __name__ == '__main__':
    main()
