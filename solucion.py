# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
        
    # Parte 1:Triángulo Decreciente
    for i in range(m - 1, 0, -1):
        print(s * i)

    # Parte 2:Triángulo Creciente
    for i in range(1, m + 1):
        print(s * i)
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    pass
