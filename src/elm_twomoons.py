from functions_elm_twomoons import *

        
neurons = 10
base, rows = open_csv_twomoons('../datasets/twomoons.dat')
base_i, base_o = extract_io(base, rows) # i: input, o: output
classification_final = classifier_elm(neurons, base_i, base_o)
acc = calc_acc(base_o, classification_final)

# Show results...
plot_results(1, base_i, classification_final, "Neurons: {} - Classifier accuracy: {:.2f}%".format(neurons, acc))
plt.savefig('plot_output/elm_twomoons1.png')



