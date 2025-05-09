class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.valor_peso = valor / peso if peso != 0 else 0

    def __repr__(self):
        return f"(Peso: {self.peso}, Valor: {self.valor}, Valor/Peso: {self.valor_peso:.2f})"

def mochila_fraccionaria(objetos, capacidad, clave_orden):
    # Ordenar los objetos según la heurística
    objetos_ordenados = sorted(objetos, key=clave_orden, reverse=True)
    peso_total = 0
    valor_total = 0
    seleccionados = []

    for obj in objetos_ordenados:
        if peso_total + obj.peso <= capacidad:
            seleccionados.append((obj, 1))  # Se toma completo
            peso_total += obj.peso
            valor_total += obj.valor
        else:
            fraccion = (capacidad - peso_total) / obj.peso
            seleccionados.append((obj, fraccion))
            valor_total += obj.valor * fraccion
            break

    return seleccionados, valor_total

def main():
    print("=== Problema de la Mochila Fraccionaria ===")
    capacidad = float(input("Capacidad máxima del contenedor: "))
    n = int(input("Número de objetos: "))
    objetos = []

    for i in range(n):
        peso = float(input(f"Ingrese el peso del objeto {i+1}: "))
        valor = float(input(f"Ingrese el valor del objeto {i+1}: "))
        objetos.append(Objeto(peso, valor))

    heuristicas = {
        "Mayor valor total": lambda o: o.valor,
        "Menor peso": lambda o: -o.peso,
        "Mayor valor/peso": lambda o: o.valor_peso,
    }

    for nombre, clave in heuristicas.items():
        print(f"\n--- Heurística: {nombre} ---")
        seleccionados, valor_total = mochila_fraccionaria(objetos, capacidad, clave)
        for obj, fraccion in seleccionados:
            porcentaje = fraccion * 100
            print(f"Objeto {obj} → Fracción tomada: {porcentaje:.2f}%")
        print(f"Valor total de la carga: ${valor_total:.2f}")

if __name__ == "__main__":
    main()
