import tkinter as tk
from tkinter import filedialog

def buscar_palabras(archivo, palabras):
    matrices_datos = {palabra: [] for palabra in palabras}
    with open(archivo, 'r') as archivo_entrada:
        for linea in archivo_entrada:
            if "set_output" in linea:
                for palabra in palabras:
                    if palabra in linea:
                        # Obtener el valor después del símbolo ";"
                        valor = linea.split(";")[1].strip()
                        matrices_datos[palabra].append(valor)
                        break  # Se detiene la búsqueda de palabras en esta línea una vez que se encuentra una coincidencia

    return matrices_datos

# Abrir ventana de selección de archivo
root = tk.Tk()
root.withdraw()
nombre_archivo = filedialog.askopenfilename()

# Archivo de ejemplo y palabras a buscar
palabras_buscar = ['AO_API_OperatingModeCH', 'AO_MEH_HP_CompSpeedSetpManual_DK_s02', 'línea']

# Llamada a la función y muestra de resultados
matrices_datos = buscar_palabras(nombre_archivo, palabras_buscar)
if matrices_datos:
    print("Valores encontrados:")
    for palabra, valores in matrices_datos.items():
        print(f"Palabra '{palabra}': {valores}")
else:
    print("No se encontraron coincidencias.")
