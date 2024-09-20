"""Forms of assigning values"""

# Atribuição Múltipla
a, b, c = 1, 2, 3
print("Atribuição Múltipla:", a, b, c)

# Atribuição com Operadores
x = 5
x += 2  # Equivalente a x = x + 2
print("Atribuição com Operadores:", x)

# Listas e Compreensão de Listas
numeros = [i for i in range(10)]  # Cria uma lista de 0 a 9
print("Lista de Números:", numeros)


# Funções
def atribuir_valores():
    return 1, 2, 3


a, b, c = atribuir_valores()
print("Valores Atribuídos pela Função:", a, b, c)

# Dicionários
dados = {"a": 1, "b": 2, "c": 3}
print("Dicionário de Dados:", dados)
