def para(x):
    print("holaaaa",x+x)
para(2)

import time
inicio=time.time()
lista = [i for i in range(10000000) if i%2==0]

fin=time.time()
print(fin-inicio)

class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

mi_perro = Perro("Toby", "Bulldog")
mi_perro.ladra()
mi_perro.camina(10)