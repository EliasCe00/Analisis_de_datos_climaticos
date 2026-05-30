import csv
import matplotlib.pyplot as plt
import os

# Se utilizan listas porque permiten almacenar múltiples valores
# y recorrerlos fácilmente para realizar cálculos y gráficos.
fechas = []
temperaturas = []


# FUNCION PARA LEER EL CSV
def leer_datos():

    try:
        # Se abre el archivo CSV en modo lectura.
        # encoding="utf-8" evita problemas con caracteres especiales.
        with open("datos/monthly.csv", "r", encoding="utf-8") as archivo:

            # csv.reader permite leer el archivo fila por fila.
            lector = csv.reader(archivo)

            # Se omite la primera fila porque contiene los encabezados.
            next(lector)

            # enumerate permite contar las filas mientras se recorren.
            # Se limita la lectura a 200 registros para evitar
            # gráficos demasiado pesados o difíciles de visualizar.
            for i, fila in enumerate(lector):

                if i > 200:
                    break

                # Se extraen únicamente las columnas necesarias.
                fecha = fila[1]
                temperatura = float(fila[2])

                # Los datos se almacenan en listas separadas
                # para facilitar cálculos y visualización.
                fechas.append(fecha)
                temperaturas.append(temperatura)

    # Manejo de errores para evitar que el programa se detenga
    # abruptamente si ocurre un problema con el archivo.
    except FileNotFoundError:
        print("No se encontró el archivo.")

    except ValueError:
        print("Error en los datos del archivo.")


# FUNCION PROMEDIO
def calcular_promedio(lista):

    # Se reutiliza una función para evitar repetir lógica
    # y mejorar la organización del código.
    return sum(lista) / len(lista)


# FUNCION RESULTADOS
def mostrar_resultados():

    print("\n----- ANALISIS CLIMATICO -----\n")

    # Se utilizan funciones integradas de Python para
    # obtener indicadores estadísticos básicos.
    print(f"Temperatura promedio: {calcular_promedio(temperaturas):.2f} °C")
    print(f"Temperatura máxima: {max(temperaturas):.2f} °C")
    print(f"Temperatura mínima: {min(temperaturas):.2f} °C")


# FUNCION GRAFICO
def generar_grafico():

    # figsize permite definir un tamaño más cómodo
    # para mejorar la visualización del gráfico.
    plt.figure(figsize=(10,5))

    # Se genera un gráfico de líneas para representar
    # la evolución de la temperatura en el tiempo.
    plt.plot(fechas, temperaturas)

    plt.title("Evolución de la temperatura")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura")

    # Se rotan las fechas para evitar superposición de texto.
    plt.xticks(rotation=45)

    # Ajusta automáticamente espacios y márgenes del gráfico.
    plt.tight_layout()

    # Se crea automáticamente la carpeta resultados
    # en caso de que no exista previamente.
    os.makedirs("resultados", exist_ok=True)

    # El gráfico se guarda como imagen para conservar
    # los resultados obtenidos durante el análisis.
    plt.savefig("resultados/grafico_temperaturas.png")

    plt.show()


# PROGRAMA PRINCIPAL

# Primero se cargan los datos del archivo.
leer_datos()

# Se verifica que existan datos antes de procesarlos.
# Esto evita errores en funciones como max(), min() o promedio.
if len(temperaturas) > 0:

    mostrar_resultados()

    generar_grafico()

else:
    print("No hay datos para analizar.")
