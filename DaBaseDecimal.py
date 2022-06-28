
import math

print("Calculadora para base 10 (decimal)\n[1] Binário para decimal\n[2] Octal para decimal\n[3] Hexadecimal para decimal\n[4] Sobre o sistema\n[0] Sair")

opcao = int(input("Digite a opção: "))
lista_de_conversao = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

i = 0
decimal = 0

if opcao == 1:
    num = int(input("Digite o número em binario para ser convertido: "))
    n = len(str(num))
    valor = num

    while n >= 0:
        resto = num % 10
        decimal +=resto*math.pow(2,i)
        n = n - 1
        i = i + 1
        num = num // 10   
    print(f"O número binário: {valor} é igual a {decimal:.0f}")

if opcao == 2:
    num = int(input("Digite o número em octal para ser convertido: "))
    n= len(str(num))
    valor = num

    while n != 0:
        resto = num %10
        decimal+=resto*math.pow(8,i)
        n = n - 1
        i = i + 1
        num = num // 10
    print(f'o numero octal : {valor} é igual a {decimal:.0f}')
    
if opcao == 3:
    num = input("Digite o numero em hexadecimal para ser convertido: ").upper()
    valor = num
    potencia = len(valor) - 1

    for i in valor:
        decimal += lista_de_conversao[i]*math.pow(16,potencia)
        potencia -= 1
    print(f'O Numero Hexadecimal : {valor} é igual a {decimal:.0f}')
if opcao == 4:
    
    print("Sistema para conversão de dados \n Alunos: Renan Garcia \n RGM: 30616654")
    print("\n Alunos: Matheus Skopek \n RGM: 29347424")

if opcao == 0:

    print('Ok, Esperamos você em uma proxima!!')

#Nome: Renan Garcia de Sousa Santos//RGM: 30616654
