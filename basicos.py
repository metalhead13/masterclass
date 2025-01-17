"""
Masterclass en Python - Nivel Intermedio
Autor: Metalhead13 
Descripción: En esta clase cubriremos conceptos intermedios como manejo de excepciones, programación orientada a objetos,
decoradores, y manejo de archivos.
"""

# Parte 1: Manejo de excepciones
def manejo_excepciones():
    """
    Manejo de errores con try-except-finally.
    """
    print("=== Manejo de Excepciones ===")
    try:
        num = int(input("Ingresa un número: "))
        resultado = 10 / num
        print(f"El resultado es: {resultado}")
    except ZeroDivisionError:
        print("⚠️ No puedes dividir por cero.")
    except ValueError:
        print("⚠️ Debes ingresar un número válido.")
    finally:
        print("Bloque finally: Siempre se ejecuta, ¡se haya producido un error o no!")

# Parte 2: Programación orientada a objetos
class Persona:
    """
    Clase que representa a una persona.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        """
        Método para presentar a la persona.
        """
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Herencia
class Estudiante(Persona):
    """
    Clase Estudiante que hereda de Persona.
    """
    def __init__(self, nombre, edad, universidad):
        super().__init__(nombre, edad)
        self.universidad = universidad

    def presentar(self):
        """
        Método sobreescrito para incluir la universidad.
        """
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años, y estudio en {self.universidad}.")

# Parte 3: Decoradores
def decorador_ejemplo(funcion):
    """
    Decorador para agregar comportamiento a una función.
    """
    def envoltura(*args, **kwargs):
        print("Decorador: Antes de ejecutar la función.")
        resultado = funcion(*args, **kwargs)
        print("Decorador: Después de ejecutar la función.")
        return resultado
    return envoltura

@decorador_ejemplo
def funcion_decorada():
    print("Función principal ejecutándose.")

# Parte 4: Manejo de archivos
def manejo_archivos():
    """
    Escritura y lectura de archivos en Python.
    """
    print("=== Manejo de Archivos ===")
    # Escritura
    with open("archivo_ejemplo.txt", "w") as archivo:
        archivo.write("Hola, este es un archivo de ejemplo.\n")
        archivo.write("Escrito en Python.\n")
    print("Archivo creado y contenido escrito.")

    # Lectura
    with open("archivo_ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

# Parte 5: Uso de listas por comprensión
def listas_por_comprension():
    """
    Crear listas utilizando comprensión de listas.
    """
    print("=== Listas por Comprensión ===")
    cuadrados = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Cuadrados de números pares: {cuadrados}")

# Llamada a las funciones
if __name__ == "__main__":
    manejo_excepciones()
    print("\n=== Programación Orientada a Objetos ===")
    persona = Persona("Juan", 30)
    persona.presentar()
    estudiante = Estudiante("Ana", 20, "Universidad Nacional")
    estudiante.presentar()
    print("\n=== Decoradores ===")
    funcion_decorada()
    print("\n=== Manejo de Archivos ===")
    manejo_archivos()
    print("\n=== Listas por Comprensión ===")
    listas_por_comprension()

