 * <center> Find the topmost function f(x,y) = |xsen(yπ/4) + ysen(xπ/4)| through the hill-climbing algorithm. The variables x and y belong to the interval between 0 and 20. The neightbor of (x, y) are (x± 0,01, y± 0,01), for example: the frontier of state (1, 1) are (1,01, 1,01), (0,99, 0,99), (0,99, 1,01) e (1,01, 0,99).</center>
 
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/src/img/q01.png" width="600">
  </p>
  
   > . / src / hillClimbing.py
  
---
  
  * <center> Build a algorithm based in fuzzy logic that receive three values: pedal pressure, wheel speed and car speed and returns the brake pressure.</center>
 
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/src/img/q02.png" width="600">
  </p>
  
  > . / src / fuzzy.py
  
---
  
  * <center> Using a set data of wind turbine (input: speed wind - m/s, output: generated power - kW), determine the models of polynomial regression (degrees 2, 3, 4 and 5) with estimates parameters for the least square method. Measure the quality of each model by R^2 and adjusted R^2 metric.</center>
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/src/img/q03.png" width="550">
  </p>
  
  > . / src / regressaoPolinomial.py
  
---

  * <center> Determine the model of regression using neural network Extreme Learning Machine (ELM) for set data of wind turbine. Measure the quality of each model by R^2 metric for different quantities of hidden neurons.</center>

  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/src/img/q04.png" width="550">
  </p>

  > . / src / elmAero.py
  
---

  * <center> Using the twomoons.dat dataset, plot the dispersion graph (scatterplot) with different colors for different classes. Consider that in the first column there are the measures of variable x1 and in the second column the measures of variable x2. The label of class of each vector measures (x1, x2) is given on third column. Trace the decision surface obtained using all samples as training. Use the ELM neural network.</center>
   
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/src/img/q05.png" width="550">
  </p>
  
  > . / src / fuzzy.py

---

  * <center> Create a genetic algorithm for find the max of function f(x,y) = |xsen(yπ/4) + ysen(xπ/4)|. Each population individual is a binary vector of 20 bits, the first 10 represents 'x' coordenate and the remains the 'y' coordenate. The variables x, y belong to [0, 20] interval. The crossover to be used is 1 point.</center> 
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/src/img/q06.png" width="750">
  </p>
  
  > . / codes / fuzzy.py
  
