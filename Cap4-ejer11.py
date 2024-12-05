# Solicitar al usuario que ingrese tres números enteros diferentes
num_a = int(input("Introduce el primer número entero: "))
num_b = int(input("Introduce el segundo número entero: "))
num_c = int(input("Introduce el tercer número entero: "))

# Determinar el mayor de los tres números usando la función max()
numero_mayor = max(num_a, num_b, num_c)

# Mostrar el resultado
print(f"El mayor de los tres números ingresados es: {numero_mayor}")
