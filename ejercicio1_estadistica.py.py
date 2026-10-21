# Nombre completo: [Karla Aparicio]
# Grupo: [952]
# Fecha de realización: [20-10-2026]
# Descripción del problema: Estadística básica. Clase Estadistica que recibe una
# lista de números naturales (puede tener repetidos) y calcula la frecuencia de
# cada número (lista de tuplas), la moda y muestra un histograma.


class Estadistica:
    def __init__(self, numeros):
        self.numeros = list(numeros)

    def frecuencia(self):
        """Devuelve una lista de tuplas (numero, veces), ordenada por número."""
        resultado = []
        for numero in sorted(set(self.numeros)):
            resultado.append((numero, self.numeros.count(numero)))
        return resultado

    def moda(self):
        """Devuelve el valor más repetido (si hay empate, el menor).
        Devuelve None si la lista está vacía."""
        mejor = None
        for numero, veces in self.frecuencia():
            if mejor is None or veces > mejor[1]:
                mejor = (numero, veces)
        return None if mejor is None else mejor[0]

    def histograma(self):
        """Imprime una línea por número con un asterisco por cada aparición."""
        for numero, veces in self.frecuencia():
            print(f"{numero} {'*' * veces}")


if __name__ == "__main__":
    lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])

    print("Frecuencia:", lista.frecuencia())
    print("Moda:", lista.moda())
    print("Histograma:")
    lista.histograma()
