import csv
import matplotlib.pyplot as plt
import os

# Listas
fechas = []
temperaturas = []


# FUNCION PARA LEER EL CSV
def leer_datos():

    try:
        with open("datos/monthly.csv", "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            next(lector)

            for i, fila in enumerate(lector):

                if i > 200:
                    break

                fecha = fila[1]
                temperatura = float(fila[2])

                fechas.append(fecha)
                temperaturas.append(temperatura)

    except FileNotFoundError:
        print("No se encontró el archivo.")

    except ValueError:
        print("Error en los datos del archivo.")


# FUNCION PROMEDIO
def calcular_promedio(lista):

    return sum(lista) / len(lista)


# FUNCION RESULTADOS
def mostrar_resultados():

    print("\n----- ANALISIS CLIMATICO -----\n")

    print(f"Temperatura promedio: {calcular_promedio(temperaturas):.2f} °C")
    print(f"Temperatura máxima: {max(temperaturas):.2f} °C")
    print(f"Temperatura mínima: {min(temperaturas):.2f} °C")


# FUNCION GRAFICO
def generar_grafico():

    plt.figure(figsize=(10,5))

    plt.plot(fechas, temperaturas)

    plt.title("Evolución de la temperatura")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura")

    plt.xticks(rotation=45)

    plt.tight_layout()

    os.makedirs("resultados", exist_ok=True)

    plt.savefig("resultados/grafico_temperaturas.png")

    plt.show()


# PROGRAMA PRINCIPAL
leer_datos()

if len(temperaturas) > 0:

    mostrar_resultados()

    generar_grafico()

else:
    print("No hay datos para analizar.")
