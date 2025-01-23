import numpy as np

def serie(x, n_terms):
    result = 6
    for n in range(1, n_terms + 1):
        term1 = (24 * ((-1)**n - 1) / (n**2 * np.pi**2)) * np.cos(n * np.pi * x / 3)
        term2 = (24 * (-1)**(n + 1) / (n * np.pi)) * np.sin(n * np.pi * x / 3)
        result += term1 + term2
    return result

def save_series_data(filename, n_terms, x_values):
    data = [(x, serie(x, n_terms)) for x in x_values]
    with open(filename, "w") as f:
        for x, y in data:
            f.write(f"{x} {y}\n")

# Valores de x para evaluar
x_values = np.linspace(-3, 3, 100)

# Generar los archivos para 2, 8 y 100 coeficientes
save_series_data("datos2.dat", 2, x_values)
save_series_data("datos8.dat", 8, x_values)
save_series_data("datos100.dat", 100, x_values)

