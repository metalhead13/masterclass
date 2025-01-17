class Persona:
    """
    Clase Persona que utiliza métodos mágicos.
    """

    def __init__(self, nombre, edad):
        """
        Método especial que inicializa los atributos de la clase.
        Es el constructor de la clase.
        """
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        """
        Método especial que define cómo se representa la clase como cadena.
        """
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    def __add__(self, otra_persona):
        """
        Método mágico que permite sumar dos instancias de Persona.
        En este caso, devuelve una nueva Persona con la edad combinada.
        """
        nuevo_nombre = f"{self.nombre} & {otra_persona.nombre}"
        nueva_edad = self.edad + otra_persona.edad
        return Persona(nuevo_nombre, nueva_edad)

# Usar la clase Persona
juan = Persona("Juan", 30)
ana = Persona("Ana", 25)

print(juan)  # Llama automáticamente a __str__
print(ana)

# Combinar personas usando __add__
pareja = juan + ana
print(pareja)

