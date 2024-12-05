# Solicitar las ventas de los tres departamentos y el salario base de los vendedores
ventas_depto_1 = float(input("Introduce las ventas del Departamento 1: "))
ventas_depto_2 = float(input("Introduce las ventas del Departamento 2: "))
ventas_depto_3 = float(input("Introduce las ventas del Departamento 3: "))
salario_base = float(input("Introduce el salario base de los vendedores: "))

# Calcular el total de ventas
total_ventas = ventas_depto_1 + ventas_depto_2 + ventas_depto_3

# Calcular el umbral del 33% de las ventas totales
umbral_ventas = 0.33 * total_ventas

# Determinar el salario final de los vendedores en cada departamento
if ventas_depto_1 > umbral_ventas:
    salario_final_1 = salario_base + (0.2 * salario_base)
else:
    salario_final_1 = salario_base

if ventas_depto_2 > umbral_ventas:
    salario_final_2 = salario_base + (0.2 * salario_base)
else:
    salario_final_2 = salario_base

if ventas_depto_3 > umbral_ventas:
    salario_final_3 = salario_base + (0.2 * salario_base)
else:
    salario_final_3 = salario_base

# Mostrar los resultados
print(f"Salario de vendedores del Departamento 1: ${salario_final_1:.2f}")
print(f"Salario de vendedores del Departamento 2: ${salario_final_2:.2f}")
print(f"Salario de vendedores del Departamento 3: ${salario_final_3:.2f}")
