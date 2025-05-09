def atm_voraz(cantidad):
    denominaciones = [100000, 50000, 20000, 10000]
    disponibles = {100000: 50, 50000: 100, 20000: 200, 10000: 300}
    resultado = {}

    if cantidad % 10000 != 0:
        return "La cantidad debe ser divisible por 10000."

    for billete in denominaciones:
        max_billetes_necesarios = cantidad // billete
        billetes_a_usar = min(max_billetes_necesarios, disponibles[billete])
        if billetes_a_usar > 0:
            resultado[billete] = billetes_a_usar
            cantidad -= billetes_a_usar * billete

    if cantidad > 0:
        return "No hay suficientes billetes para entregar el monto solicitado."
    else:
        return resultado


def main():
    try:
        cantidad = int(input("Ingrese la cantidad a retirar (múltiplo de 10000): "))
        resultado = atm_voraz(cantidad)
        print("\nResultado:")
        if isinstance(resultado, dict):
            for denominacion, cantidad in resultado.items():
                print(f"${denominacion}: {cantidad} billete(s)")
        else:
            print(resultado)
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")


if __name__ == "__main__":
    main()
