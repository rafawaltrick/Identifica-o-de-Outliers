import numpy as np

# Dados das transações
valores = [10.20, 14.10, 14.10, 14.40, 14.40, 14.50, 14.50, 14.60, 14.70, 14.70, 14.70, 14.90, 15.10, 15.90, 16.40]

# Calculando o quartil 1 (Q1) e quartil 3 (Q3)
q1 = np.percentile(valores, 25)
q3 = np.percentile(valores, 75)

# Calculando o intervalo interquartil (IQR)
iqr = q3 - q1

# Definindo os limites inferior e superior para identificar outliers
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Identificando outliers
outliers = [valor for valor in valores if valor < limite_inferior or valor > limite_superior]

if outliers:
    print("Os outliers identificados são:", outliers)
else:
    print("Não foram encontrados outliers.")
