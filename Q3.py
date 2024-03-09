import random

print('Bem vindo!\n')

while True:
    opcao = int(input("""Qual operação você deseja realizar?
        1 - Gerar um número aleatório entre 0 e 1
        2 - Sair\n"""))
    if opcao==1:
        print('Número %s\n' %(random.random()))
    elif opcao==2:
        break
    else:
        print('Opção Inválida!\n')

