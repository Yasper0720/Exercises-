import matplotlib.pyplot as plt
import math
import numpy as np

class Friccion:
    """
    Clase que modela una situación física relacionada con la fricción.
    """
    
    def __init__(self, coef_friccion, normal):
        self.coef_friccion = coef_friccion  # Coeficiente de fricción
        self.normal = normal  # Fuerza normal
    
    def __add__(self, other):
        if isinstance(other, Friccion):
            return Friccion(self.coef_friccion + other.coef_friccion, self.normal + other.normal)
        raise TypeError("Operando debe ser de tipo 'Friccion'")

    def __sub__(self, other):
        if isinstance(other, Friccion):
            return Friccion(self.coef_friccion - other.coef_friccion, self.normal - other.normal)
        raise TypeError("Operando debe ser de tipo 'Friccion'")

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

    def calcular_fuerza_friccion(self):
        return self.coef_friccion * self.normal

    def describir_fuerza(self):
        return f"Coeficiente: {self.coef_friccion}, Normal: {self.normal}, Fricción: {self.calcular_fuerza_friccion():.2f} N"


class ColebrookFriccion(Friccion):
    """
    Clase que extiende la fricción para incluir el cálculo de fricción usando la ecuación de Colebrook.
    """
    
    def __init__(self, e, D, R):
        super().__init__(0, 0)
        self.e = e  # Rugosidad
        self.D = D  # Diámetro
        self.R = R  # Número de Reynolds

    def coeficiente_friccion_colebrook(self, x0=0.015, max_iter=10):
        """
        Método que utiliza Newton-Raphson para calcular el coeficiente de fricción según la ecuación de Colebrook.
        """
        def f(x):
            return 1 / x**0.5 + 2 * math.log10((self.e / self.D) / 3.7 + 2.51 / (self.R * x**0.5))

        def Df(x):
            return -0.5 * x**-1.5 + 2 * (-2.51 * x**-1.5 / (2 * self.R)) * math.log10(2.7182) / ((self.e / self.D) / 3.7 + 2.51 / (self.R * x * 0.5))

        iteraciones = [x0]

        for _ in range(max_iter):
            try:
                x1 = x0 - f(x0) / Df(x0)
                iteraciones.append(x1)
                x0 = x1
            except ZeroDivisionError:
                print("Error: División por cero en el cálculo de la derivada.")
                break

        return iteraciones

    def describir_colebrook(self):
        return f"Rugosidad: {self.e}, Diámetro: {self.D}, Reynolds: {self.R}"


def graficar_convergencia(iteraciones):
    """
    Función para graficar el proceso de convergencia del coeficiente de fricción de Colebrook.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(iteraciones)), iteraciones, marker='o', linestyle='-', color='b', label='Coeficiente de fricción Colebrook')
    plt.xlabel('Iteración')
    plt.ylabel('Valor de f')
    plt.title('Convergencia del método de Newton-Raphson para el coeficiente de fricción de Colebrook')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    print("Operaciones con fricción:")
    
    # Entrada de parámetros físicos
    e = float(input("Digite rugosidad e (m): "))
    D = float(input("Digite Diámetro D (m): "))
    R = float(input("Digite Número de Reynolds: "))
    max_iter = 10

    # Crear objeto de la clase ColebrookFriccion
    colebrook_friccion = ColebrookFriccion(e, D, R)

    # Mostrar detalles
    print("\n--- Detalles del cálculo de fricción Colebrook ---")
    print(colebrook_friccion.describir_colebrook())

    # Obtener las iteraciones usando Newton-Raphson
    iteraciones_colebrook = colebrook_friccion.coeficiente_friccion_colebrook(max_iter=max_iter)

    # Graficar el proceso de convergencia
    graficar_convergencia(iteraciones_colebrook)

    print("Finalizando el programa.")


if __name__ == "__main__":
    main()
