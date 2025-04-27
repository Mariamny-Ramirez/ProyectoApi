def encontrar_estados_equivalentes(estados, finales, transiciones, alfabeto):
    # Inicializar la tabla de pares de estados
    tabla = [[False for _ in range(estados)] for _ in range(estados)]

    # Marcar estados distinguibles si uno es final y el otro no
    for i in range(estados):
        for j in range(i + 1, estados):
            es_final_i = i in finales
            es_final_j = j in finales
            if es_final_i != es_final_j:
                tabla[i][j] = True

    # Comparar transiciones y marcar diferencias
    cambios = True
    while cambios:
        cambios = False
        for i in range(estados):
            for j in range(i + 1, estados):
                if not tabla[i][j]:
                    for simbolo in alfabeto:
                        if simbolo not in transiciones[i] or simbolo not in transiciones[j]:
                            continue  # Evitar accesos inválidos
                        trans_i = transiciones[i][simbolo]
                        trans_j = transiciones[j][simbolo]
                        if tabla[min(trans_i, trans_j)][max(trans_i, trans_j)]:
                            tabla[i][j] = True
                            cambios = True
                            break

    # Obtener pares de estados equivalentes
    equivalentes = []
    for i in range(estados):
        for j in range(i + 1, estados):
            if not tabla[i][j]:
                equivalentes.append((i, j))
    return equivalentes


def main():
    estados = int(input("Ingrese el número total de estados: "))
    num_finales = int(input("Ingrese el número de estados finales: "))

    finales = []
    print("Ingrese los estados finales:")
    for _ in range(num_finales):
        estado_final = int(input())
        if estado_final >= estados or estado_final < 0:
            print(f"Error: El estado final {estado_final} no es válido.")
            return
        finales.append(estado_final)

    alfabeto = set()
    entrada_alfabeto = input("Ingrese los símbolos del alfabeto (ejemplo: a b c): ")
    for c in entrada_alfabeto:
        if c != ' ':
            alfabeto.add(c)

    if not alfabeto:
        print("Error: El alfabeto no puede estar vacío.")
        return

    transiciones = {}
    print("\nIngrese las transiciones:")
    for i in range(estados):
        print(f"Estado {i}:")
        transiciones[i] = {}
        for simbolo in alfabeto:
            destino = int(input(f"  Para símbolo '{simbolo}' -> Estado destino: "))
            if destino >= estados or destino < 0:
                print(f"Error: Estado destino {destino} no válido.")
                return
            transiciones[i][simbolo] = destino

    print("\nTransiciones ingresadas:")
    for i in range(estados):
        print(f"Estado {i}:", end=" ")
        for simbolo in alfabeto:
            print(f"{simbolo}->{transiciones[i][simbolo]}", end="  ")
        print()

    equivalentes = encontrar_estados_equivalentes(estados, finales, transiciones, alfabeto)

    print("\nEstados equivalentes encontrados: ", end="")
    if not equivalentes:
        print("Ninguno")
    else:
        for par in equivalentes:
            print(f"({par[0]}, {par[1]})", end=" ")
    print()


if __name__ == "__main__":
    main()
