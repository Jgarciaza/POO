# Solicitar el valor de la compra y el color de la bolita
valor_compra = float(input("Introduce el valor de la compra: "))
color_bolita = input("Introduce el color de la bolita (BLANCO, VERDE, AMARILLO, AZUL): ").strip().upper()

# Inicializar el porcentaje de descuento
descuento = 0

# Determinar el porcentaje de descuento según el color de la bolita
if color_bolita == "BLANCO":
    descuento = 0
elif color_bolita == "VERDE":
    descuento = 10
elif color_bolita == "AMARILLO":
    descuento = 25
elif color_bolita == "AZUL":
    descuento = 50
else:
    descuento = 100

# Calcular el valor final con descuento aplicado
valor_a_pagar = valor_compra - (descuento * valor_compra / 100)

# Mostrar el resultado final
print(f"El cliente debe pagar: ${valor_a_pagar:.2f}")
