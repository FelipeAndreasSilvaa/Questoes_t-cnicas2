# Definindo as sequências e seus próximos elementos
def sequencias():
    # a) Números ímpares
    seq_a = [1, 3, 5, 7]
    proximo_a = seq_a[-1] + 2

    # b) Potências de 2
    seq_b = [2, 4, 8, 16, 32, 64]
    proximo_b = seq_b[-1] * 2

    # c) Quadrados dos números inteiros
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    proximo_c = (len(seq_c)) ** 2  # 7²

    # d) Quadrados dos números pares
    seq_d = [4, 16, 36, 64]
    proximo_d = (len(seq_d) + 1) * 2 ** 2  # 10²

    # e) Sequência de Fibonacci
    seq_e = [1, 1, 2, 3, 5, 8]
    proximo_e = seq_e[-1] + seq_e[-2]

    # f) Sequência com múltiplos e incrementos
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    proximo_f = seq_f[-1] + 1 if seq_f[-1] % 2 == 1 else seq_f[-1] + 2

    return (proximo_a, proximo_b, proximo_c, proximo_d, proximo_e, proximo_f)

# Chamada da função e impressão dos resultados
resultados = sequencias()
print(f"Próximo elemento de a): {resultados[0]}")
print(f"Próximo elemento de b): {resultados[1]}")
print(f"Próximo elemento de c): {resultados[2]}")
print(f"Próximo elemento de d): {resultados[3]}")
print(f"Próximo elemento de e): {resultados[4]}")
print(f"Próximo elemento de f): {resultados[5]}")
