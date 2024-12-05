import math
# Solicitar al usuario que introduzca la medida de un lado del triángulo equilátero
longitud_lado = float(input("Introduce la medida de un lado del triángulo equilátero: "))
# Calcular el perímetro del triángulo
perimetro_triangulo = 3 * longitud_lado
# Calcular la altura del triángulo
altura_triangulo = (math.sqrt(3) / 2) * longitud_lado
# Calcular el área del triángulo
area_triangulo = (math.sqrt(3) / 4) * (longitud_lado ** 2)
# Mostrar los resultados calculados
print("\nResultados del triángulo equilátero:")
print("Perímetro:", perimetro_triangulo)
print("Altura:", altura_triangulo)
print("Área:", area_triangulo)
