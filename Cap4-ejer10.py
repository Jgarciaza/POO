# Ingresar los datos del estudiante
num_inscripcion = input("Introduce el número de registro: ")
nombre_estudiante = input("Introduce el nombre completo del estudiante: ")
patrimonio = float(input("Introduce el patrimonio del estudiante: "))
estrato = int(input("Introduce el estrato socioeconómico del estudiante: "))

# Pago base de matrícula
pago_matricula = 50000

# Verificar si se aplica un incremento en el costo de matrícula
if patrimonio > 2000000 and estrato > 3:
    incremento = 0.03 * patrimonio
    pago_matricula += incremento

# Mostrar el resultado final
print(f"El estudiante con registro número {num_inscripcion} y nombre {nombre_estudiante} debe pagar: ${pago_matricula:.2f}")
