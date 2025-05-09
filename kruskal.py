class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])  # compresión de caminos
        return self.padre[x]

    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if raiz_x == raiz_y:
            return False
        if self.rango[raiz_x] < self.rango[raiz_y]:
            self.padre[raiz_x] = raiz_y
        elif self.rango[raiz_x] > self.rango[raiz_y]:
            self.padre[raiz_y] = raiz_x
        else:
            self.padre[raiz_y] = raiz_x
            self.rango[raiz_x] += 1
        return True

def kruskal(n, aristas):
    aristas.sort()  # O(E log E)
    uf = UnionFind(n)
    total = 0
    mst = []
    for costo, u, v in aristas:
        if uf.unir(u, v):
            total += costo
            mst.append((u, v, costo))
    return total, mst

def main():
    print("Conexión de municipios con fibra óptica (Árbol de Recubrimiento Mínimo)")
    n = int(input("Ingrese el número de municipios: "))
    m = int(input("Ingrese el número de conexiones posibles (aristas): "))

    aristas = []
    print("Ingrese las conexiones en el formato: municipio1 municipio2 costo")
    for _ in range(m):
        u, v, costo = map(int, input("-> ").split())
        aristas.append((costo, u, v))

    costo_total, mst = kruskal(n, aristas)
    print("\nCosto total del tendido de fibra:", costo_total)
    print("Conexiones seleccionadas para el MST:")
    for u, v, costo in mst:
        print(f"{u} - {v} : {costo}")

if __name__ == "__main__":
    main()