# QUESTÃO 01

#Entrada de dados + atribuição de variável (input sempre retorna um str)
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
print()

#Saída de dados (concatenação do print com , - elementos separados por padrão por espaço e finalizando o print com \n)
print('Bem vindo!')
print('Olá,', nome, 'sua idade é',idade,'. Até mais!')
print('Olá,', nome, 'sua idade é',idade,'. Até mais!', sep='-',end='...')
print()