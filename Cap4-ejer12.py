# Solicitar los datos del empleado
nombre_empleado = input("Introduce el nombre del empleado: ")
horas_trabajadas = int(input("Introduce el número de horas trabajadas: "))
pago_hora = float(input("Introduce el valor por hora trabajada: "))

# Inicializar variables
horas_extra = 0  # Horas extras totales
horas_extra_extensas = 0  # Horas extras que exceden de 8
salario_total = 0  # Salario final

# Calcular las horas extras si las horas trabajadas superan las 40
if horas_trabajadas > 40:
    horas_extra = horas_trabajadas - 40
    if horas_extra > 8:
        horas_extra_extensas = horas_extra - 8
        salario_total = (40 * pago_hora) + (8 * 2 * pago_hora) + (horas_extra_extensas * 3 * pago_hora)
    else:
        salario_total = (40 * pago_hora) + (horas_extra * 2 * pago_hora)
else:
    salario_total = horas_trabajadas * pago_hora

# Mostrar el resultado
print(f"El empleado {nombre_empleado} devengó un salario total de: ${salario_total:.2f}")
