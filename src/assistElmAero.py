import numpy as np
import csv
import math


def open_csv(url):
    reader = csv.reader(open(url), delimiter='\t')
    dataset = np.array([0, 0])
    rows_dataset = 1
    for line in reader:
        row = np.array([float(line[0]), float(line[1])])
        dataset = np.vstack((dataset, row))
        rows_dataset += 1
    return dataset, rows_dataset


def split_dataset(base, rows, validation):
    if validation == 'holdout': 
        # 2/3 Training
        # 1/3 Validation
        np.random.shuffle(base)
        holdout = math.floor(rows/3)
        train = base[holdout:]
        test = base[:holdout]
    return train, test


def extract_inputs(base): 
    return base[:, 0].reshape(1, np.size(base, 0))


def extract_outputs(base): 
    return base[:, 1].reshape(1, np.size(base, 0))


def gen_random(n, m):
    return np.random.normal(0, 1, (n, m)) 
        

def prepare_input_hl(inputs):
    bias_hl = np.ones_like(inputs)
    inputs = np.vstack((bias_hl, inputs))
    return inputs
    

def prepare_input_ol(inputs):
    bias_ol = np.ones((1, np.size(inputs, 1)))
    inputs = np.vstack((bias_ol, inputs))
    return inputs
    

def train_elm(neurons, train_input, train_output): 
    input_hl = prepare_input_hl(train_input) # hl: Hidden Layer
    weights_hl = gen_random(neurons, 1 + 1) # Hidden layer weights: (Nº neuronios * (Nº columns inputs + 1 'bias'))
    sum_hl = weights_hl @ input_hl
    activation_hl = 1/(1 + np.exp(-sum_hl))
    input_ol = prepare_input_ol(activation_hl) # ol: Output Layer
    weights_ol = train_output @ input_ol.T
    weights_ol = weights_ol.dot(np.linalg.inv(input_ol @ input_ol.T))
    return weights_hl, weights_ol


def test_elm(train_input, weight_hl, weight_ol):
    input_hl = prepare_input_hl(train_input)
    sum_hl = weight_hl @ input_hl
    activation_hl = 1/(1 + np.exp(-sum_hl))
    input_ol = prepare_input_ol(activation_hl)
    estimated_output = weight_ol @ input_ol
    return estimated_output


def quality_output(test_output, estimated_output):
    test_output = test_output[0]
    estimated_output = estimated_output[0] 
    len_test = len(test_output)
    len_estimated = len(estimated_output)
    y_media = np.mean(test_output)
    sq_e, s_yy = 0, 0
    for i in range(0, len_test):
        sq_e = sq_e + (test_output[i] - estimated_output[i])**2
        s_yy = s_yy + (test_output[i] - y_media)**2
    r2 = 1 - sq_e/s_yy
    
    k = 1 # Nº's inputs
    p = k + 1
    r2_aj_quocient = sq_e / (len_test - p)
    r2_aj_denominator = s_yy / (len_estimated - 1)
    r2_aj = r2_aj_quocient / r2_aj_denominator
    r2_aj = 1 - r2_aj
    return r2, r2_aj