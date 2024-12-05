# Solicitar al usuario las longitudes de los lados del triángulo
lado_a = float(input("Introduce la longitud del primer lado del triángulo: "))
lado_b = float(input("Introduce la longitud del segundo lado del triángulo: "))
lado_c = float(input("Introduce la longitud del tercer lado del triángulo: "))
# Calcular el perímetro del triángulo5
perimetro_triangulo = lado_a + lado_b + lado_c
# Calcular el semiperímetro del triángulo
semi_perimetro = perimetro_triangulo / 2
# Calcular el área del triángulo usando la fórmula de Herón
area_triangulo = (semi_perimetro * 
                 (semi_perimetro - lado_a) * 
                 (semi_perimetro - lado_b) * 
                 (semi_perimetro - lado_c)) ** 0.5
# Mostrar los resultados calculados
print("\nResultados del triángulo:")
print("Perímetro:", perimetro_triangulo)
print("Semiperímetro:", semi_perimetro)
print("Área:", area_triangulo)
