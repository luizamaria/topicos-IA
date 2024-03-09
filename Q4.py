print('Bem vindo a calculadora de média!')

numeros = []
while True:
    opcao = int(input("""\nQual operação você deseja realizar?
        1 - Inserir um número
        2 - Calcular a média
        3 - Limpar dados
        4 - Sair\n"""))
    if opcao==1:
        n = float(input('\nDigite o número: '))
        numeros.append(n)
        print('Número salvo.')
    elif opcao==2:
        media = 0
        for x in numeros:
            media += x/len(numeros)
        print('\nA média dos números digitados é %s.\n' %(media))
    elif opcao==3:
        media = 0
        numeros.clear()
    elif opcao==4:
        break
    else:
        print('Opção Inválida!')