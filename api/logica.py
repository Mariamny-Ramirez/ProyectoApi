def encontrar_estados_equivalentes(estados, finales, transiciones, alfabeto):
    tabla = [[False for _ in range(estados)] for _ in range(estados)]

    # Marcar los estados que son distinguibles (uno final, otro no)
    for i in range(estados):
        for j in range(i + 1, estados):
            es_final_i = i in finales
            es_final_j = j in finales
            if es_final_i != es_final_j:
                tabla[i][j] = True
                print(f"Marcado directo (final vs no final): ({i}, {j})")

    # Verificar si la tabla se está actualizando
    print("\n--- Tabla inicial después del marcado de finales ---")
    for row in tabla:
        print(row)

    cambios = True
    while cambios:
        cambios = False
        for i in range(estados):
            for j in range(i + 1, estados):
                if not tabla[i][j]:
                    for simbolo in alfabeto:
                        if simbolo not in transiciones[i] or simbolo not in transiciones[j]:
                            continue
                        trans_i = transiciones[i][simbolo]
                        trans_j = transiciones[j][simbolo]
                        if tabla[min(trans_i, trans_j)][max(trans_i, trans_j)]:
                            tabla[i][j] = True
                            cambios = True
                            print(f"Marcado por transición ({i}, {j}) → con símbolo '{simbolo}' → destinos ({trans_i}, {trans_j})")
                            break

    print("\n--- Tabla final ---")
    for row in tabla:
        print(row)

    equivalentes = []
    for i in range(estados):
        for j in range(i + 1, estados):
            if not tabla[i][j]:
                equivalentes.append((i, j))
    return equivalentes


if __name__ == "__main__":
    estados = 4
    finales = [2, 3]
    alfabeto = ["a", "b"]
    transiciones = {
        0: {"a": 1, "b": 2},
        1: {"a": 0, "b": 3},
        2: {"a": 2, "b": 2},
        3: {"a": 3, "b": 3}
    }

    equivalentes = encontrar_estados_equivalentes(estados, finales, transiciones, set(alfabeto))
    print("Estados equivalentes encontrados:", equivalentes)
