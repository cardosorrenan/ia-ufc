import matplotlib.pyplot as plt

class PressaoPedal():
    def __init__(self,x):
        self.baixa = round(-x/50 + 1,3)
        if x > 50: self.media = round(-x/20 + 7/2,3)
        else: self.media = round(x/20 - 3/2,3)
        self.alta = round(x/50 - 1,3) 

    def normaliza(self):
        if self.baixa < 0: self.baixa = 0
        if self.media < 0: self.media = 0
        if self.alta < 0: self.alta = 0


class VelocidadeCarro():
    def __init__(self,x):
        self.baixa = round(-x/60 + 1,3)
        if x > 50: self.media = round(-x/30 + 8/3,3)
        else: self.media = round(x/30 - 2/3,3)
        self.alta = round(x/60 - 2/3,3)     

    def normaliza(self):
        if self.baixa < 0: self.baixa = 0
        if self.media < 0: self.media = 0
        if self.alta < 0: self.alta = 0


class VelocidadeRoda():
    def __init__(self,x):
        self.baixa = round(-x/60 + 1,3)
        if x > 50: self.media = round(-x/30 + 8/3,3)
        else: self.media = round(x/30 - 2/3,3)
        self.alta = round(x/60 - 2/3,3)
    
    def normaliza(self):
        if self.baixa < 0: self.baixa = 0
        if self.media < 0: self.media = 0
        if self.alta < 0: self.alta = 0


def pertinencia_func_pressao(pressao_final,x):
        if x >= 0 and x <= pressao_final*100:
            return x/100
        elif x <= 100:
            return pressao_final 

def pertinencia_func_liberacao(libere_final,x):
        if x >= 0 and x <= 100-libere_final*100:
            return libere_final
        elif x <= 100:
            return 1-((x)/100)

def main():
    while True: 
        p_p = int(input('Valor da pressão no pedal: '))
        v_r = int(input('Valor da velocidade da roda: '))
        v_c = int(input('Valor da velocidade do carro: '))
        if all((i>=0 and i<=100) for i in [p_p, v_c, v_r]):
            break

    pressao_pedal = PressaoPedal(p_p)
    pressao_pedal.normaliza()
    velocidade_carro = VelocidadeCarro(v_c)
    velocidade_carro.normaliza()
    velocidade_roda = VelocidadeRoda(v_r)
    velocidade_roda.normaliza()
    
    pressao_freio = []
    pressao_freio.append(pressao_pedal.media)
    pressao_freio.append(min(pressao_pedal.alta, velocidade_carro.alta, velocidade_roda.alta))
    pressao_final = sum(pressao_freio)

    libere_freio = []
    libere_freio.append(min(pressao_pedal.alta, velocidade_carro.alta, velocidade_roda.baixa))
    libere_freio.append(pressao_pedal.baixa)
    libere_final = sum(libere_freio)

    print('\n\n  Pressão Pedal: {}\n    Baixa - {} / Média - {} / Alta - {}'.format(p_p, pressao_pedal.baixa, pressao_pedal.media, pressao_pedal.alta))
    print('  Velocidade Carro: {}\n    Baixa - {} / Média - {} / Alta - {}'.format(v_c, velocidade_carro.baixa, velocidade_carro.media, velocidade_carro.alta))
    print('  Velocidade Roda: {}\n    Baixa - {} / Média - {} / Alta - {}'.format(v_r, velocidade_roda.baixa, velocidade_roda.media, velocidade_roda.alta))
    print('\n  Pressão no freio: {}'.format(pressao_freio))
    print('    Aperte o freio: {}'.format(pressao_final))
    print('  Liberação do freio: {}'.format(libere_freio))
    print('    Libere o freio: {}'.format(libere_final))

    y_pressao_freio,y_libere_freio,y_final = [],[],[]
    x = range(0,101) 
    for it in x:
        aux1 = pertinencia_func_pressao(pressao_final,it)
        aux2 = pertinencia_func_liberacao(libere_final,it)
        y_pressao_freio.append(aux1)
        y_libere_freio.append(aux2)
        if aux1 > aux2:
            y_final.append(aux1)
        else:
            y_final.append(aux2)
    grau = 0
    for it in x: grau = grau + it * y_final[it]
    grau = round(grau/sum(y_final)+0.01,3)
    print('\n  Grau em que o freio é aplicado: {}'.format(grau))

    plt.figure(1)
    plt.subplot(221)
    plt.axis([0, 100, 0, 1])
    plt.plot(x,y_pressao_freio)
    plt.subplot(222)
    plt.axis([0, 100, 0, 1])
    plt.plot(x,y_libere_freio)
    plt.subplot(223)
    plt.axis([0, 100, 0, 1])
    plt.plot(x,y_final)
    plt.show()
    
if __name__ == '__main__':
    main()
