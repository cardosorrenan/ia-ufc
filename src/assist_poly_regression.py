import csv
import matplotlib.pyplot as plt
import numpy as np


def open_csv_aero(url):
    reader = csv.reader(open(url), delimiter='\t')
    x, y = np.array([]), np.array([])
    for line in reader:
        x = np.append(x, float(line[0]))
        y = np.append(y, float(line[1]))
    return x, y


def get_degree():
    while True:
        n_degree = int(input('Choose degree [2, 5]: '))
        if n_degree >= 2 and n_degree <= 5:
            break
        print("type a [1, 5] interval...")
    print('OK')
    return n_degree


def regression(degree, x, y):
    y_final = 0
    matrix_ones = np.ones((len(x), 1))
    x_big = np.column_stack([matrix_ones, x])
    
    for i in range(1, degree):
        x_big = np.column_stack([x_big, x**(i+1)]) 
             
    beta = np.linalg.inv(np.matrix.transpose(x_big) @ x_big) @ np.matrix.transpose(x_big) @ y
    
    for i in range(0, degree + 1):  
        y_final = y_final + (beta[i] * (x**i))
        
    return y_final


def output_quality(test_o, estimated_output):
    sq_e, s_yy = 0, 0
    for i in range(0, len(test_o)):
        sq_e = sq_e + (test_o[i] - estimated_output[i])**2
        s_yy = s_yy + (test_o[i] - np.mean(test_o))**2
    r2 = float(1 - (sq_e/s_yy))
    k = 2
    p = k + 1
    r2_aj_q = sq_e / (len(test_o) - p)
    r2_aj_d = s_yy / (len(estimated_output) - 1)
    r2_aj = float(1 - (r2_aj_q/ r2_aj_d))
    return r2, r2_aj