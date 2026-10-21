# Nombre completo: [karla Aparicio Garduno]
# Grupo: [952]
# Fecha de realización: [20-10-2026
# Descripción del problema: Navegación en un almacén. El almacén es una matriz
# (lista de listas) con celdas vacías '.', obstáculos '#' y productos 'P'. Un
# robot inicia en (0, 0) y sigue una lista de movimientos (R, D, L, U). La
# función devuelve True solo si los movimientos son válidos (no salen del
# almacén ni chocan con obstáculos), recogen todos los productos y el robot
# termina de vuelta en el punto de inicio.

MOVIMIENTOS = {
    'R': (0, 1),    # derecha
    'D': (1, 0),    # abajo
    'L': (0, -1),   # izquierda
    'U': (-1, 0),   # arriba
}


def verificar_recogida_productos(almacen, movimientos, solo_retorno=False):
    """Verifica la ruta del robot.

    solo_retorno=False (por defecto): L y U se permiten en cualquier momento,
        como en el ejemplo del documento.
    solo_retorno=True: L y U solo se permiten cuando ya se recogieron todos
        los productos (es decir, únicamente para regresar al inicio).
    """
    if not almacen or not almacen[0]:
        return False

    filas = len(almacen)
    columnas = len(almacen[0])

    # Posiciones (fila, columna) de todos los productos
    productos = set()
    for f in range(filas):
        for c in range(columnas):
            if almacen[f][c] == 'P':
                productos.add((f, c))

    posicion = (0, 0)
    if almacen[0][0] == '#':
        return False

    recogidos = set()
    if posicion in productos:
        recogidos.add(posicion)

    for mov in movimientos:
        if mov not in MOVIMIENTOS:
            return False
        if solo_retorno and mov in ('L', 'U') and recogidos != productos:
            return False

        df, dc = MOVIMIENTOS[mov]
        f, c = posicion[0] + df, posicion[1] + dc

        if not (0 <= f < filas and 0 <= c < columnas):   # fuera del almacén
            return False
        if almacen[f][c] == '#':                         # obstáculo
            return False

        posicion = (f, c)
        if posicion in productos:
            recogidos.add(posicion)

    return recogidos == productos and posicion == (0, 0)


if __name__ == "__main__":
    almacen = [
        ['.', '.', '#', 'P'],
        ['.', '#', '.', '.'],
        ['P', '.', 'P', '.'],
        ['#', '.', '#', '.'],
    ]

    movimientos_correctos = ['D', 'D', 'R', 'R', 'U', 'R', 'U',
                             'D', 'L', 'D', 'L', 'L', 'U', 'U']
    print(verificar_recogida_productos(almacen, movimientos_correctos))  # True

    # Casos adicionales
    print("Falta un producto:      ",
          verificar_recogida_productos(almacen, ['D', 'D', 'U', 'U']))        # False
    print("Choca con obstáculo:    ",
          verificar_recogida_productos(almacen, ['R', 'R']))                  # False
    print("Se sale del almacén:    ",
          verificar_recogida_productos(almacen, ['U']))                       # False
    print("No regresa al inicio:   ",
          verificar_recogida_productos(almacen, movimientos_correctos[:-1]))  # False
    print("Modo estricto (L/U solo al retornar):",
          verificar_recogida_productos(almacen, movimientos_correctos,
                                       solo_retorno=True))                    # False
