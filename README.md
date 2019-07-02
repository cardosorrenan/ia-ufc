
  #### Q01. Encontre  o  máximo  da  função f(x,y)  = |xsen(yπ/4)  + ysen(xπ/4)|  por  meio  do algoritmo hill-climbing.  As  variáveis x  e y  pertencem  ao  intervalo  entre  0  e  20. Os vizinhos de determinado estado (x, y) são (x± 0,01, y± 0,01). Por exemplo, os vizinhos do estado (1, 1) são (1,01, 1,01), (0,99, 0,99), (0,99, 1,01) e (1,01, 0,99).
  #### Resultado
  > . / codes / hillClimbing.py
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/codes/img/q01.png" width="450">
  </p>
---
  #### Q02. Construa um programa baseado em lógica fuzzy (inferência de Mamdani) que receba três valores: pressão no pedal, velocidade da roda e velocidade do carro e que devolva a pressão no freio. Siga as regras disponibilizadas nos slides sobre Lógica Fuzzy.
  > . / codes / fuzzy.py
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/codes/img/q02.png" width="450">
  </p>
---
  #### Q03. Usando o conjunto de dados do aerogerador (variável de entrada: velocidade do vento – m/s, variável de saída: potência gerada – kWatts), determine os modelos de regressão polinomial  (graus  2,  3,  4  e  5)  com  parâmetros  estimados  pelo  método  dos  mínimos quadrados. Avalie a qualidade de cada modelo pela métrica R2 e R2aj (equações 48 e 49, slides sobre Regressão Múltipla).
  > . / codes / regressaoPolinomial.py
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/codes/img/q03.png" width="450">
  </p>
---
  #### Q04. Determine um modelo de regressão usando rede neural Extreme Learning Machine (ELM) para o conjunto de dados do aerogerador (variável de entrada: velocidade do vento, variável de saída: potência gerada). Avalie a qualidade do modelo pela métrica R2 para diferentes quantidades de neurônios ocultos.
  > Em revisão
---
  #### Q05. Classifique o conjunto de dados disponível no arquivo iris_log.dat usando: Perceptron, MLP, e ELM. Utilize as estratégias de validação: hold-out (70% treino, 30% teste), 10-fold e leave-one-out. A base iris_log.dat, as quatro primeiras colunas representam os atributos dos vetores de  características  e  as  três últimas representam a classe da amostra ([1 0 0], [0 1 0] e [0 0 1]).
  > Em revisão
---
  #### Q06. Usando o conjunto de dados 2-D disponível no arquivo twomoons.dat. Plote o gráfico de dispersão (scatterplot) usando cores diferentes para diferenciar entre os dados de uma classe e da outra. Considere que na primeira coluna  constam  as  medidas da  variável x1 e na segunda coluna as medidas da variável x2. O rótulo da classe de cada vetor de  medidas (x1, x2) é dado na terceira  coluna. Trace a superfície de decisão obtida com o uso de todas as amostras como treinamento. Obs.: implementar a rede neural ELM.
  > . / codes / elmTwoMoons.py
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/codes/img/q06.png" width="450">
  </p>
---
  #### Q07. Usando o conjunto de dados disponível no arquivo iris_log.dat. Particionar o conjunto de dados aleatoriamente em 80% dos dados para treino e 20% para teste. Repita cada experimento (treino  +  teste) 50 vezes e calcule a taxa média de acertos, e os valores mínimo e máximo. Implementar  a  rede  neural RBF.
 > Em revisão
---
  #### Q08.  Crie  um  algoritmo  genético  para  achar  o  máximo da  função f(x,y)  = |xsen(yπ/4)  + ysen(xπ/4)|. Cada indivíduo da população é um vetor binário de 20 bits, em que os 10 primeiros  representam x  e  os  restantes  representam y.  As  variáveis x  e y  pertencem  ao intervalo entre 0 e 20. O crossover a ser usado é de 1 ponto. 
  > . / codes / genAlg.py
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/codes/img/q08.png" width="450">
  </p>
