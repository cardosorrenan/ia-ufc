import csv
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x, y = np.array([]), np.array([])
    with open('datasets/aerogerador.dat') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            x = np.append(x, float(line[0]))
            y = np.append(y, float(line[1]))

    n_x = x.size
    matrix_ones = np.ones((n_x, 1))
    x_big = np.column_stack([matrix_ones, x])

    grau = int(input('Escolha o grau: '))
    if grau >= 2 and grau <= 5:
        if grau == 2:
            x_big = np.column_stack([x_big, x**2])
            print(x_big)
            beta = np.linalg.inv(np.matrix.transpose(x_big) @ x_big) @ np.matrix.transpose(x_big) @ y
            y_chapeu = beta[0] + (beta[1] * x) + (beta[2] * (x**2))

        elif grau == 3:
            x_big = np.column_stack([x_big, x**2])
            x_big = np.column_stack([x_big, x**3])
            beta = np.linalg.inv(np.matrix.transpose(x_big) @ x_big) @ np.matrix.transpose(x_big) @ y
            y_chapeu = beta[0] + (beta[1] * x) + (beta[2] * (x**2) + (beta[3] * (x**3)))

        elif grau == 4:
            x_big = np.column_stack([x_big, x**2])
            x_big = np.column_stack([x_big, x**3])
            x_big = np.column_stack([x_big, x**4])
            beta = np.linalg.inv(np.matrix.transpose(x_big) @ x_big) @ np.matrix.transpose(x_big) @ y
            y_chapeu = beta[0] + (beta[1] * x) + (beta[2] * (x**2) + (beta[3] * (x**3)) + (beta[4] * (x**4)))
        elif grau == 5:
            x_big = np.column_stack([x_big, x**2])
            x_big = np.column_stack([x_big, x**3])
            x_big = np.column_stack([x_big, x**4])
            x_big = np.column_stack([x_big, x**5])
            beta = np.linalg.inv(np.matrix.transpose(x_big) @ x_big) @ np.matrix.transpose(x_big) @ y
            y_chapeu = beta[0] + (beta[1] * x) + (beta[2] * (x**2) + (beta[3] * (x**3)) + (beta[4] * (x**4) + (beta[5] * (x**5))))

    y_media = np.mean(y)
    sq_e, s_yy = 0, 0
    for i in range(0, len(y)):
        sq_e = sq_e + (y[i] - y_chapeu[i])**2
        s_yy = s_yy + (y[i] - y_media)**2
    r2 = 1 - sq_e/s_yy
    r2_aj = 1 - (sq_e/(len(y) - (grau + 1)))/(s_yy/(len(y) - 1))
    print(r2, r2_aj)

    plt.plot(x, y_chapeu)
    plt.scatter(x=x, y=y, color='red', s=20, alpha=0.5)
    plt.title('               R2: ' + str(round(r2, 5)) + '\nR2 Ajustado: ' + str(round(r2_aj, 5)))
    plt.show()
