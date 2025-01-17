# === módulo_ejemplo.py ===
"""
Este es un módulo de ejemplo. Contiene una función y una clase que se pueden usar desde otros archivos.
"""

def saludar(nombre):
    """
    Función para saludar a un usuario por su nombre.
    """
    return f"¡Hola, {nombre}! Bienvenido."

class Calculadora:
    """
    Clase para realizar operaciones matemáticas básicas.
    """
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

# === usar_modulo.py ===
"""
Archivo que importa y usa el módulo "módulo_ejemplo".
"""

# Importar el módulo
import módulo_ejemplo

# Usar la función del módulo
print(módulo_ejemplo.saludar("Carlos"))

# Crear una instancia de la clase y usarla
calc = módulo_ejemplo.Calculadora()
print(f"5 + 3 = {calc.sumar(5, 3)}")
print(f"5 - 3 = {calc.restar(5, 3)}")

# También puedes importar partes específicas del módulo
from módulo_ejemplo import saludar

print(saludar("María"))

