# Se solicita al usuario que introduzca los datos del trabajador


identificacion_trabajador = input("Introduce el ID del trabajador: ")
nombre_completo = input("Introduce el nombre completo del trabajador: ")
horas_mensuales = float(input("Introduce la cantidad de horas laboradas en el mes: "))
tarifa_hora = float(input("Introduce el pago por hora trabajada: "))
tasa_retencion = float(input("Introduce el porcentaje de retención aplicable (%): "))

# Calcular el ingreso total
ingreso_total = horas_mensuales * tarifa_hora

# Calcular el monto de retención
descuento_retencion = (tasa_retencion / 100) * ingreso_total

# Calcular el ingreso neto
ingreso_neto = ingreso_total - descuento_retencion

# Mostrar los detalles del trabajador
print("\nDetalles del trabajador:")
print("ID del trabajador:", identificacion_trabajador)
print("Nombre completo:", nombre_completo)
print("Ingreso Total:", ingreso_total)
print("Ingreso Neto:", ingreso_neto)
