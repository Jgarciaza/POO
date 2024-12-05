# Solicitar los pesos de las esferas
peso_x = float(input("Introduce el peso de la esfera X: "))
peso_y = float(input("Introduce el peso de la esfera Y: "))
peso_z = float(input("Introduce el peso de la esfera Z: "))

# Inicializar una variable para almacenar el peso máximo y el identificador de la esfera
peso_mayor = 0
esfera_mayor = ""

# Comparar los pesos para determinar la esfera más pesada
if peso_x > peso_y and peso_x > peso_z:
    peso_mayor = peso_x
    esfera_mayor = "X"
elif peso_y > peso_x and peso_y > peso_z:
    peso_mayor = peso_y
    esfera_mayor = "Y"
else:
    peso_mayor = peso_z
    esfera_mayor = "Z"

# Mostrar el resultado en pantalla
print(f"La esfera más pesada es la esfera {esfera_mayor}, con un peso de {peso_mayor} unidades.")
