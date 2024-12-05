import math

# Solicitar los coeficientes de la ecuación cuadrática
coef_a = float(input("Introduce el coeficiente A: "))
coef_b = float(input("Introduce el coeficiente B: "))
coef_c = float(input("Introduce el coeficiente C: "))

# Calcular el discriminante
discriminante = coef_b**2 - 4 * coef_a * coef_c

# Resolver la ecuación cuadrática
if discriminante > 0:
    # Dos soluciones reales diferentes
    raiz_1 = (-coef_b + math.sqrt(discriminante)) / (2 * coef_a)
    raiz_2 = (-coef_b - math.sqrt(discriminante)) / (2 * coef_a)
    print("La ecuación tiene dos soluciones reales distintas:")
    print(f"x1 = {raiz_1:.2f}")
    print(f"x2 = {raiz_2:.2f}")
elif discriminante == 0:
    # Una solución real única
    raiz_1 = -coef_b / (2 * coef_a)
    print("La ecuación tiene una solución real única:")
    print(f"x1 = {raiz_1:.2f}")
else:
    # Soluciones complejas
    parte_real = -coef_b / (2 * coef_a)
    parte_imaginaria = math.sqrt(-discriminante) / (2 * coef_a)
    print("La ecuación no tiene soluciones reales. Las soluciones complejas son:")
    print(f"x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i")
    print(f"x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i")
