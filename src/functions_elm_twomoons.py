import numpy as np
import csv
import matplotlib.pyplot as plt


def open_csv_twomoons(url):
    reader = csv.reader(open(url), delimiter='\t')
    dataset = np.array([0, 0, 0])
    rows_dataset = 1
    for line in reader:
        row = np.array([float(line[0][0:15]), float(line[0][16:30]), float(line[0][31:45])])
        dataset = np.vstack((dataset, row))
        rows_dataset += 1
    return dataset[1:], rows_dataset-1
   
        
def extract_io(base, rows): 
    return base[:, 0:2].reshape(rows, 2), base[:, 2].reshape(rows, 1)


def gen_random(n, m):
    return np.random.normal(0, 1, (n, m)) 
        

def prepare_input(base_i):
    bias_hl = np.ones((len(base_i), 1))
    return np.hstack((base_i, bias_hl))


def degree(x):  return 1 if x > 0 else -1


def classifier_elm(neurons, train_i, train_o):
    input_hl = prepare_input(train_i)
    weight_hl = gen_random(neurons, np.size(train_i, 1) + 1) # Hidden layer weights: (Nº neurons * (Nº columns inputs + 1 'bias'))
    sum_hl = weight_hl @ input_hl.T
    activation_hl = 1/(1 + np.exp(-sum_hl)).T
    input_ol = prepare_input(activation_hl)
    weight_ol = train_o.T @ input_ol
    weight_ol = weight_ol.dot(np.linalg.inv(input_ol.T @ input_ol))
    classification_final = weight_ol @ input_ol.T
    classification_final = [i for i in classification_final[0]]
    return list(map(degree, classification_final))


def calc_acc(base_o, training_final):
    acc = 0
    for i in range(0, len(base_o)):
        if base_o[i] == training_final[i]:
            acc += 1
    return 100*acc/len(base_o)
            
            
def plot_results(n, base_i, base_o, title):
    plt.figure(n)
    plt.title(title)
    for i in range(0, len(base_i)):  
        color = 'blue' if base_o[i] == 1 else 'red'
        plt.scatter(x=base_i[i][0], y=base_i[i][1], color=f'{color}', s=10, alpha=0.4)
            
