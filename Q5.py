import re

print('Bem vindo ao contador de palavras!')

cont = {}
palavras = []
while True:
    opcao = int(input("""\nQual operação você deseja realizar?
        1 - Inserir um texto
        2 - Verificar a frequência de uma palavra
        3 - Limpar dados
        4 - Sair\n"""))
    if opcao==1:
        txt = str(input('Digite o texto:\n'))
        print('Texto salvo.')
    elif opcao==2:
        palavras = re.split("[,. \n]",txt)
        print('Segue abaixo a frequência de cada palavra:')
        for x in palavras:
            cont[x] = palavras.count(x)
        print(cont)
    elif opcao==3:
        txt =''
        palavras.clear()
        cont.clear()
    elif opcao==4:
        break
    else:
        print('Opção Inválida!')