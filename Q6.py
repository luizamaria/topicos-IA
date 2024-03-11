palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

palavra = palavra.lower()
    
lista_caracteres = list(palavra)
    
lista_reversa = lista_caracteres[::-1]
    
if lista_caracteres == lista_reversa:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")