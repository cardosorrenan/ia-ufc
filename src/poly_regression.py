from functions_poly_regression import *


x, y = open_csv_aero('../datasets/aero.dat')
degree = get_degree()
y_final = regression(degree, x, y)
r2, r2_aj = output_quality(y, y_final)

plt.plot(x, y_final, linewidth=3, color='blue')
plt.title('R2: {} / R2 Adj: {}\n'.format(round(r2, 3), round(r2_aj, 3)))
plt.scatter(x=x, y=y, color='red', s=20, alpha=0.5)
plt.savefig('plot_output/poly_regression.png')
