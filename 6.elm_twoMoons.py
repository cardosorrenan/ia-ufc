import numpy as np
import csv
import matplotlib.pyplot as plt

# Extração dos dados
with open('twomoons.dat') as f:
	reader = csv.reader(f, delimiter='\t')
	cont = 0
	#  Extrai linha e concatena ao array base
	for line in reader:
		row = np.array([float(line[0][0:15]), float(line[0][16:30]), float(line[0][31:45])])
		if cont == 0:
			base = row
		else:
			base = np.vstack((base, row))
		cont+=1

neuronios_ocultos = 20
saidas = base[:,2].reshape(1,1001)
entradas = base[:,0:2].T
pesos_camadaOculta = np.random.normal(0, 1, (neuronios_ocultos, 3))

# Prepara o vetor para a camada oculta: entrada + bias
bias_camadaOculta =  np.ones((1,np.size(entradas,1)))
entradas_teste = np.vstack((bias_camadaOculta, entradas))

# Realiza a soma e ativação de todos as (entradas * pesos) em cada neurônio
somaSinapse_camadaOculta = pesos_camadaOculta @ entradas_teste 
ativacao_camadaOculta =  1/(1 + np.exp(-somaSinapse_camadaOculta))

# Prepara o vetor para a camada de saida: resultado final em cada neuronio + bias
bias_camadaSaida =  np.ones((1,np.size(ativacao_camadaOculta,1)))
ativacao_camadaOculta = np.vstack((bias_camadaSaida, ativacao_camadaOculta))

# Calcula os pesos para a camada de saída
pesos_camadaSaida_pt1 = saidas @ ativacao_camadaOculta.T
pesos_camadaSaida_pt2 = np.linalg.inv(ativacao_camadaOculta @ ativacao_camadaOculta.T)
pesos_camadaSaida = pesos_camadaSaida_pt1.dot(pesos_camadaSaida_pt2)

# Resultado Final; Arrendonda o valor mais próximo: 0 ou 1
saidas_test = pesos_camadaSaida @ ativacao_camadaOculta
saidas_test = saidas_test.round(0)

# Plotagem e validação
cont = 0
for i in range(0,1001):
    if saidas_test[0,i] == saidas[0,i]:
        cont += 1
    if saidas_test[0,i] == 1:
        plt.scatter(x=entradas[0, i], y=entradas[1, i], color='red', s=10, alpha=0.4)
    elif saidas_test[0,i] == -1:
        plt.scatter(x=entradas[0, i], y=entradas[1, i], color='blue', s=10, alpha=0.4)
        
acuracia = (cont / 1001) * 100
plt.title(str(round(acuracia,2)) + "%")
plt.show()
