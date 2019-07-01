import numpy as np
import csv
import matplotlib.pyplot as plt

X,D = np.array([]), np.array([])
with open('aerogerador.dat') as f:
    reader = csv.reader(f, delimiter='\t')
    for line in reader:
        X = np.append(X, float(line[0]))
        D = np.append(D, float(line[1]))


experimentos = []
q = 8
p = 1
O = np.ones(len(X))
W = np.random.rand(q,p+1)
X2 = np.vstack((O,np.matrix.transpose(X)))
D = np.matrix.transpose(D)
Z = W @ X2

for z in np.nditer(Z, op_flags=['readwrite']):
    z[...] = 1/(1+np.exp(z))
Z = np.vstack((O,Z))
M = D @ np.matrix.transpose(Z) @ np.linalg.inv(Z @ np.matrix.transpose(Z))
D_test = M @ Z

sq_e, s_yy = 0,0
for i in range(0,len(D)):
    sq_e = sq_e + (D[i] - D_test[i])**2
    s_yy = s_yy + (D[i] - np.mean(D))**2
r2 = 1 - sq_e/s_yy

        
plt.plot(X,D_test)
plt.scatter(x=X, y=D, color='red', s=20, alpha=0.5)

plt.show()