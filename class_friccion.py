import matplotlib.pyplot as plt

class Friccion:
    def __init__(self, coef_friccion, normal):
        """
        La clase Friccion representará una situación física específica relacionada con la fricción.
        """
        self.coef_friccion = coef_friccion  # Coeficiente de fricción
        self.normal = normal  # Fuerza normal

    def __add__(self, other):
        """
        Este método __add__ permite sumar dos objetos de la clase Friccion.
        """
        if isinstance(other, Friccion):
            return Friccion(self.coef_friccion + other.coef_friccion, self.normal + other.normal)
        raise TypeError("Operando debe tener propiedades de la fuerza Friccion")

    def __sub__(self, other):
        """
        El método __sub__ en Python se utiliza para definir el operador de resta entre la clase fricción.
        """
        if isinstance(other, Friccion):
            return Friccion(self.coef_friccion - other.coef_friccion, self.normal - other.normal)
        raise TypeError("Operando debe ser una fuerza de Friccion")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Friccion(self.coef_friccion * scalar, self.normal * scalar)
        raise TypeError("El multiplicador debe ser un número")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __call__(self):
        # Calcula la fuerza de fricción
        return self.coef_friccion * self.normal

    def __setitem__(self, key, value):
        if key == 'coef_friccion':
            self.coef_friccion = value
        elif key == 'normal':
            self.normal = value
        else:
            raise KeyError("La clave debe ser 'coef_friccion' o 'normal'")

    def __getitem__(self, key):
        if key == 'coef_friccion':
            return self.coef_friccion
        elif key == 'normal':
            return self.normal
        else:
            raise KeyError("La clave debe ser 'coef_friccion' o 'normal'")

    def __str__(self):
        return f"Fuerza de fricción: {self.coef_friccion * self.normal:.2f} N"

def movimiento_con_friccion(coef_friccion, masa, velocidad_inicial, delta_t, tiempo_total):
    """
    Calcula la posición y velocidad de un objeto bajo fricción usando el método de Euler.

    Parámetros:
    - coef_friccion: Coeficiente de fricción cinética.
    - masa: Masa del objeto.
    - velocidad_inicial: Velocidad inicial del objeto.
    - delta_t: Incremento de tiempo (paso de integración).
    - tiempo_total: Tiempo total de simulación.
    """
    g = 9.81  # Aceleración debida a la gravedad (m/s^2)
    normal = masa * g  # Fuerza normal (peso del objeto)
    friccion = Friccion(coef_friccion, normal)
    
    tiempo = 0
    velocidad = velocidad_inicial
    posicion = 0
    
    tiempos = []
    posiciones = []
    velocidades = []

    while tiempo <= tiempo_total:
        # Almacena los datos para graficar
        tiempos.append(tiempo)
        posiciones.append(posicion)
        velocidades.append(velocidad)
        
        # Fuerza de fricción
        fuerza_friccion = friccion()
        aceleracion = -fuerza_friccion / masa
        
        # Método de Euler para la integración numérica
        velocidad += aceleracion * delta_t
        posicion += velocidad * delta_t
        tiempo += delta_t

    # Graficar los resultados
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(tiempos, posiciones, label='Posición (m)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posición (m)')
    plt.title('Posición vs. Tiempo')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(tiempos, velocidades, label='Velocidad (m/s)', color='orange')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title('Velocidad vs. Tiempo')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    print("Simulación de movimiento con fricción:")
    
    coef_friccion = float(input("Introduce el coeficiente de fricción: "))
    masa = float(input("Introduce la masa del objeto (kg): "))
    velocidad_inicial = float(input("Introduce la velocidad inicial del objeto (m/s): "))
    delta_t = float(input("Introduce el incremento de tiempo (s): "))
    tiempo_total = float(input("Introduce el tiempo total de simulación (s): "))

    movimiento_con_friccion(coef_friccion, masa, velocidad_inicial, delta_t, tiempo_total)

if __name__ == "__main__":
    main()

