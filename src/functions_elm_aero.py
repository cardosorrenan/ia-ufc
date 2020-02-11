import numpy as np
import csv
import math
import matplotlib.pyplot as plt


def open_csv_aero(url):
    reader = csv.reader(open(url), delimiter='\t')
    dataset = np.array([0, 0])
    rows_dataset = 1
    for line in reader:
        row = np.array([float(line[0]), float(line[1])])
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
    return base[:, 0].reshape(rows, 1), base[:, 1].reshape(rows, 1)


def gen_random(n, m):
    return np.random.normal(0, 1, (n, m)) 
        

def prepare_input(base_i):
    bias_hl = np.ones((len(base_i), 1))
    return np.hstack((base_i, bias_hl))


def train_elm(neurons, train_i, train_o):
    input_hl = prepare_input(train_i)
    weight_hl = gen_random(neurons, np.size(train_i, 1) + 1) # Hidden layer weights: (Nº neuronios * (Nº columns inputs + 1 'bias'))
    sum_hl = weight_hl @ input_hl.T
    activation_hl = 1/(1 + np.exp(-sum_hl)).T
    input_ol = prepare_input(activation_hl)
    weight_ol = train_o.T @ input_ol
    weight_ol = weight_ol.dot(np.linalg.inv(input_ol.T @ input_ol))
    training_final = weight_ol @ input_ol.T
    return training_final.T, weight_hl, weight_ol


def test_elm(test_i, weight_hl, weight_ol):
    input_hl = prepare_input(test_i)
    sum_hl = weight_hl @ input_hl.T
    activation_hl = 1/(1 + np.exp(-sum_hl)).T
    input_ol = prepare_input(activation_hl)
    testing_final = weight_ol @ input_ol.T
    return testing_final.T


def quality_output(test_o, estimated_output):
    sq_e, s_yy = 0, 0
    for i in range(0, len(test_o)):
        sq_e = sq_e + (test_o[i] - estimated_output[i])**2
        s_yy = s_yy + (test_o[i] - np.mean(test_o))**2
    r2 = float(1 - (sq_e/s_yy))
    k = 2 # Nº's inputs
    p = k + 1
    r2_aj_q = sq_e / (len(test_o) - p)
    r2_aj_d = s_yy / (len(estimated_output) - 1)
    r2_aj = float(1 - (r2_aj_q/ r2_aj_d))
    return r2, r2_aj


def plot_results(n, base_i, base_o, title, color):
    plt.figure(n)
    plt.title(title)
    for i in range(0, len(base_i)):  
        plt.scatter(x=base_i[i], y=base_o[i], color=f'{color}', s=10, alpha=0.4)
