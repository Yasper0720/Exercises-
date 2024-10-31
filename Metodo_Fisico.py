# Parámetros del sistema
m = 1.0     # Masa de la partícula
k = 1.0     # Constante del resorte (Fuerza restauradora F = -k * x)
dt = 0.01   # Paso de tiempo
t_total = 10.0  # Tiempo total de simulación

# Condiciones iniciales
x0 = 1.0    # Posición inicial
v0 = 0.0    # Velocidad inicial

# Inicializar variables
x = x0      # Posición en el instante actual
v = v0      # Velocidad en el instante actual
t = 0.0     # Tiempo inicial

# Método de Verlet
while t < t_total:
    # Imprimir los resultados actuales
    print(f"Tiempo: {t:.2f}, Posición: {x:.4f}, Velocidad: {v:.4f}")
    
    # Calcular la aceleración en función de la posición (a = F/m, F = -k * x)
    a = -k * x / m
    
    # Aplicar el método de Verlet
    x_new = x + v * dt + 0.5 * a * dt**2  # Nueva posición
    a_new = -k * x_new / m  # Nueva aceleración basada en la nueva posición
    v = v + 0.5 * (a + a_new) * dt  # Actualizar la velocidad

    # Avanzar en el tiempo
    x = x_new
    t += dt
