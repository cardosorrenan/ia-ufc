import numpy as np
import csv
import math
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
   
        
def split_dataset(base, rows, method):
    if method == 'holdout':  # 2/3 Training - 1/3 Validation
        np.random.shuffle(base)
        holdout = math.floor(rows/3)
        train = base[holdout:]
        test = base[:holdout]
    return train, test


def extract_io(base, rows): 
    return base[:, 0:2].reshape(rows, 2), base[:, 2].reshape(rows, 1)


def gen_random(n, m):
    return np.random.normal(0, 1, (n, m)) 
        

def prepare_input(base_i):
    bias_hl = np.ones((len(base_i), 1))
    return np.hstack((base_i, bias_hl))


def degree(x):  return 1 if x > 0 else -1


def train_elm(neurons, train_i, train_o):
    input_hl = prepare_input(train_i)
    weight_hl = gen_random(neurons, np.size(train_i, 1) + 1) # Hidden layer weights: (Nº neuronios * (Nº columns inputs + 1 'bias'))
    sum_hl = weight_hl @ input_hl.T
    activation_hl = 1/(1 + np.exp(-sum_hl)).T
    input_ol = prepare_input(activation_hl)
    weight_ol = train_o.T @ input_ol
    weight_ol = weight_ol.dot(np.linalg.inv(input_ol.T @ input_ol))
    training_final = weight_ol @ input_ol.T
    training_final = [i for i in training_final[0]]
    return list(map(degree, training_final)), weight_hl, weight_ol


def test_elm(test_i, weight_hl, weight_ol):
    input_hl = prepare_input(test_i)
    sum_hl = weight_hl @ input_hl.T
    activation_hl = 1/(1 + np.exp(-sum_hl)).T
    input_ol = prepare_input(activation_hl)
    testing_final = weight_ol @ input_ol.T
    testing_final = [i for i in testing_final[0]]
    return list(map(degree, testing_final))


def quality_output(test_o, estimated_output):
    acc, sq_e, s_yy = 0, 0, 0
    for i in range(0, len(test_o)):
        sq_e = sq_e + (test_o[i] - estimated_output[i])**2
        s_yy = s_yy + (test_o[i] - np.mean(test_o))**2
        if test_o[i] == estimated_output[i]:  acc += 1 
    r2 = float(1 - (sq_e/s_yy))
    k = 2 # Nº's inputs
    p = k + 1
    r2_aj_q = sq_e / (len(test_o) - p)
    r2_aj_d = s_yy / (len(estimated_output) - 1)
    r2_aj = float(1 - (r2_aj_q/ r2_aj_d))
    return 100*acc/len(test_o), r2, r2_aj


def plot_results(n, base_i, base_o, title):
    plt.figure(n)
    plt.title(title)
    for i in range(0, len(base_i)):  
        color = 'blue' if base_o[i] == 1 else 'red'
        plt.scatter(x=base_i[i][0], y=base_i[i][1], color=f'{color}', s=10, alpha=0.4)