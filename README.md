  ##### :pencil: This repo contain some codes developed in the computational intelligence course (2019.1) - Universidade Federal do Ceará.
  ##### :v: Enjoy and learn... if you find some error please contact me on renanhc96@gmail.com
  ##### :dart: Prerequisites
  ```
   $ sudo apt-get install virtualenv                         - install a tool to create isolated py environments
   $ git clone https://github.com/cardosorrenan/ia-ufc.git   - clone this repo
   $ cd ia-ufc                                               
   $ virtualenv env                                          - create a virtual environment
   $ source env/bin/activate                                 - turn on env
   $ sudo pip3 install -r requirements.txt                   - install dependencies (numpy and matplotlib)
  
     try it ;)
     
   $ deactivate                                              - turn off env
  ``` 
---
  
 * <center> Find the topmost function f(x,y) = |xsen(yπ/4) + ysen(xπ/4)| through the hill-climbing algorithm. The variables x and y belong to the interval between 0 and 20. The neightbor of (x, y) are (x± 0,01, y± 0,01), for example: the frontier of state (1, 1) are (1,01, 1,01), (0,99, 0,99), (0,99, 1,01) and (1,01, 0,99).</center>
 
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/assets/hill_climbing.png" height="300">
  </p>
  
  * [ . / src / hill_climbing.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/hill_climbing.py)
    * [ . / src / functions_hill_climbing.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/functions_hill_climbing.py)
  
---
  
  * <center> Develop an algorithm based in fuzzy logic that receive three values: pedal pressure, wheel speed, car speed and returns the brake pressure. 
 
    * Especifications: [fuzzy.pdf](https://github.com/cardosorrenan/ia-ufc/blob/master/assets/fuzzy.pdf)
 
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/assets/fuzzy.png" height="200">
  </p>
  
  * [ . / src / fuzzy.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/fuzzy.py)
    * [ . / src / functions_fuzzy.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/functions_fuzzy.py) 
  
---
  
  * <center> Using a set data of wind turbine (input: speed wind - m/s, output: generated power - kW), determine the models of polynomial regression (degrees 2, 3, 4 and 5) with estimates parameters for the least square method. Measure the quality of each model by R^2 and adjusted R^2 metric.</center>
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/assets/poly_regression.png" width="400">
  </p>
  
  * [ . / src / poly_regression.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/poly_regression.py)
    * [ . / src / functions_poly_regression.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/functions_poly_regression.py)
  
---

  * <center> Determine the model of regression using neural network Extreme Learning Machine (ELM) for set data of wind turbine. Measure the quality of model by R^2 metric and adjusted R^2 metric.</center>

  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/assets/elm_aero.png" height="250">
  </p>

  * [ . / src / elm_aero.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/elm_aero.py)
    * [ . / src / functions_elm_aero.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/functions_elm_aero.py)
  
---

  * <center> Using the twomoons.dat dataset, plot the dispersion graph (scatterplot) with different colors for different classes. Consider that in the first column there are the measures of variable x1 and in the second column the measures of variable x2. The label of class of each vector measures (x1, x2) is given on third column. Trace the decision surface obtained using all samples as training. Use the ELM neural network.</center>
   
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/assets/elm_twomoons.png" height="350">
  </p>
  
  * [ . / src / elm_twomoons.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/elm_twomoons.py)
    * [ . / src / functions_elm_twomoons.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/functions_elm_twomoons.py)

---

  * <center> Create a genetic algorithm for find the max of function f(x,y) = |xsen(yπ/4) + ysen(xπ/4)|. Each population individual is a binary vector of 20 bits, the first 10 represents 'x' coordenate and the remains the 'y' coordenate. The variables x, y belong to [0, 20] interval. The crossover to be used is 1 point.</center> 
  
  <p align="center">
    <img src="https://github.com/cardosorrenan/ia-ufc/blob/master/assets/genetic_alg.png" width="750">
  </p>
  
 * [ . / src / genetic-alg / genetic_alg.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/genetic-alg/genetic_alg.py)
   * [ . / src / genetic-alg  / functions_genetic_alg.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/functions_genetic_alg.py)
   * [ . / src / genetic-alg  / individual.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/genetic-alg/individual.py)
   * [ . / src / genetic-alg  / population.py ](https://github.com/cardosorrenan/ia-ufc/blob/master/src/genetic-alg/population.py)
   * [ . / src / genetic-alg  / results /](https://github.com/cardosorrenan/ia-ufc/blob/master/src/genetic-alg/results/)
  
---
  
