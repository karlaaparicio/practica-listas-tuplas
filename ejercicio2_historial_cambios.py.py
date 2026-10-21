# Nombre completo: [Karla Aparicio]
# Grupo: [952]
# Fecha de realización: [20-10-2026]
# Descripción del problema: Historial de cambios en una hoja de cálculo. Se usa
# una lista como pila (stack) donde cada cambio es una tupla (celda, valor).
# Se puede registrar un cambio y deshacer uno o varios cambios. Al deshacer, se
# informa cuál era el valor anterior de la celda, que es el que se restaura.


def registrar_cambio(historial, celda, valor):
    """Apila un cambio (celda, valor) en el historial."""
    historial.append((celda, valor))


def valor_actual(historial, celda):
    """Valor vigente de una celda según el historial (None si está vacía)."""
    for c, v in reversed(historial):
        if c == celda:
            return v
    return None


def hoja_actual(historial):
    """Estado de la hoja (diccionario celda -> valor) según el historial."""
    hoja = {}
    for celda, valor in historial:  # el último cambio de cada celda gana
        hoja[celda] = valor
    return hoja


def deshacer_cambio(historial, cantidad=1):
    """Deshace los últimos `cantidad` cambios (por defecto, uno).

    Devuelve una lista de tuplas (celda, valor_deshecho, valor_restaurado),
    donde valor_restaurado es el valor anterior de la celda (None = vacía).
    """
    deshechos = []
    for _ in range(cantidad):
        if not historial:
            print("No hay más cambios que deshacer.")
            break
        celda, valor_deshecho = historial.pop()
        valor_anterior = valor_actual(historial, celda)
        deshechos.append((celda, valor_deshecho, valor_anterior))
    return deshechos


if __name__ == "__main__":
    historial_cambios = []

    # Ejemplo del documento
    registrar_cambio(historial_cambios, 'A1', 10)
    registrar_cambio(historial_cambios, 'B2', 20)
    print(historial_cambios)             # [('A1', 10), ('B2', 20)]
    deshacer_cambio(historial_cambios)
    print(historial_cambios)             # [('A1', 10)]

    # Simulación más completa, con deshacer múltiple
    print("\n--- Simulación ---")
    registrar_cambio(historial_cambios, 'B2', 20)
    registrar_cambio(historial_cambios, 'A1', 15)   # A1 pasa de 10 a 15
    registrar_cambio(historial_cambios, 'C3', 30)
    print("Historial:", historial_cambios)
    print("Hoja:", hoja_actual(historial_cambios))

    print("\nDeshacer 1 cambio:", deshacer_cambio(historial_cambios))
    print("Hoja:", hoja_actual(historial_cambios))

    print("\nDeshacer 2 cambios:", deshacer_cambio(historial_cambios, 2))
    print("Historial:", historial_cambios)
    print("Hoja:", hoja_actual(historial_cambios))

    print("\nDeshacer 5 cambios (más de los que hay):")
    print(deshacer_cambio(historial_cambios, 5))
    print("Historial:", historial_cambios)
