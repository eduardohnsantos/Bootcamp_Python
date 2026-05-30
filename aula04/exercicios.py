# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

numeros = list(range(1, 11))
for numero in numeros:
    print(quadrados**2)

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")


# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")