def contar_a(string):
    # Converte a string para minúsculas para facilitar a contagem
    string_lower = string.lower()
    
    # Conta a quantidade de 'a's
    quantidade_a = string_lower.count('a')
    
    # Verifica se existe 'a' na string
    existe_a = quantidade_a > 0
    
    return existe_a, quantidade_a

# Exemplo de string (você pode alterar ou permitir a entrada do usuário)
entrada = input("Digite uma string: ")

# Chama a função e obtém o resultado
existe, quantidade = contar_a(entrada)

# Exibe o resultado
if existe:
    print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
else:
    print("A letra 'a' não está presente na string.")
