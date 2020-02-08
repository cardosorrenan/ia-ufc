from assist_elm_aero import *


neurons = 5
base, rows = open_csv_aero('datasets/aero.dat')
train, test = split_dataset(base, rows, "holdout")
base_i, base_o = extract_io(base, rows)
train_i, train_o = extract_io(train, len(train))
test_i, test_o = extract_io(test, len(test))
training_final, weights_hl, weights_ol = train_elm(neurons, train_i, train_o) # hl: Hidden Layer, ol: Output Layer
testing_final = test_elm(test_i, weights_hl, weights_ol)

# Show results...
plot_results(1, base_i, base_o, 'Dataset', 'red')

r2, r2_aj = quality_output(train_o, training_final)
title1 = 'Neurons: {} / R2: {} / R2 Aj: {}\n'.format(neurons, round(r2, 3), round(r2_aj, 3))
title2 = 'Dataset 66% / Training'
plot_results(2, train_i, training_final, title1+title2, 'green')

r2, r2_aj = quality_output(test_o, testing_final)
title1 = 'Neurons: {} / R2: {} / R2 Aj: {}\n'.format(neurons, round(r2, 3), round(r2_aj, 3))
title2 = 'Dataset 33% / Testing'
plot_results(3, test_i, testing_final, title1+title2, 'blue')

plot_results(4, base_i, base_o, '', 'red')
plot_results(4, train_i, training_final, '', 'green')
plot_results(4, test_i, testing_final, '', 'blue')
plt.show()
