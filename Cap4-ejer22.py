# Solicitar el nombre del trabajador
nombre_trabajador = input("Introduce el nombre del trabajador: ")

# Solicitar el salario por hora y la cantidad de horas trabajadas
pago_por_hora = float(input("Introduce el pago por hora: "))
horas_mes = int(input("Introduce la cantidad de horas trabajadas en el mes: "))

# Calcular el salario mensual
salario_total_mes = pago_por_hora * horas_mes

# Verificar si el salario mensual supera los $450,000
if salario_total_mes > 450000:
    print(f"Nombre del trabajador: {nombre_trabajador}")
    print(f"Salario mensual: ${salario_total_mes:.2f}")
else:
    print(f"Nombre del trabajador: {nombre_trabajador}")
