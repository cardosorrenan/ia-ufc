import matplotlib.pyplot as plt
import numpy as np

############################
from assistElmAero import *
###########################

neurons = 4
base, rows = open_csv('datasets/aero.dat')
train, test = split_dataset(base, rows, "holdout")
base_input = extract_inputs(base)
base_output = extract_outputs(base)
train_input = extract_inputs(train)
train_output = extract_outputs(train)
test_input = extract_inputs(test)
test_output = extract_outputs(test)
weights_hl, weights_ol = train_elm(neurons, train_input, train_output) # hl: Hidden Layer, ol: Output Layer
estimated_output = test_elm(test_input, weights_hl, weights_ol)

r2, r2_aj = quality_output(test_output, estimated_output)
print('Nº of neurons: ' + str(neurons) + '\nR2: ' + str(round(r2, 5)) + '\nR2 Ajustado: ' + str(round(r2_aj, 5)))

plt.scatter(x=base_input, y=base_output, color='blue', s=10, alpha=0.4)
plt.scatter(x=test_input, y=estimated_output, color='red', s=10, alpha=0.4)
plt.title('Nº of neurons: ' + str(neurons) + '\nR2: ' + str(round(r2, 5)) + '\nR2 Ajustado: ' + str(round(r2_aj, 5)))


