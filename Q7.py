import random

print("Bem-vindo ao jogo de adivinhação!\n")
print ("Adivinhe um número entre 1 e 20!")

numero_secreto = random.randint(1, 20)

palpite = input("Tente adivinhar o número (entre 1 e 30): ")
    
if palpite.isdigit():
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
    else:
        print(f"Que pena! O número correto era: {numero_secreto}")
else:
    print("O valor informado não é um inteiro :( Tente novamente")