# QUESTÃO 02

#Entrada de dados
print("Bem vindo(a) a Calculadora! \nSelecione a operação que você deseja realizar:")
opcao = int(input("1. Soma\n2. Subtração\n3. Divisão\n4. Multiplicação"))
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

#Calculadora e resultado
if opcao==1:
    print(n1," + ",n2," = ",n1+n2)
elif opcao==2:
    print(n1," - ",n2," = ",n1-n2)
elif opcao==3:
    print(n1," * ",n2," = ",n1*n2)
elif opcao==4:
    print(n1," / ",n2," = ",n1/n2)
else:
    print("Opção inválida!")