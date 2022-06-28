
print("Calculadora decimal para outras base\n[1] Decimal para binário\n[2] Decimal para octal\n[3] Decimal para hexadecimal\n[4] Sobre o sistema\n[0] Sair")

num = int(input("Digite o decimal a ser convertido: "))
opcao = int(input("Digite a opção: "))
numero = num
string = ""


if opcao == 1:
    numero_digitado = num
    quociente = 1
    lista = []
    while quociente >= 1:
        resto = num%2
        lista.insert(0,resto)
        quociente = num // 2
        num = quociente

    binario = ''.join([str(item) for item in lista])
    print(f"O decimal: {numero_digitado} em binário é: {binario} ")


elif opcao == 2:
    while num > 0:
        re = num % 8 
        num = num // 8
        string = str(re) + string
        
    print(f"O decimal: {numero} em octal é: {string}")

elif opcao == 3:
    he = ''
    letras = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    
    while(num!=0):
        c = num%16
        he = letras[c] + he
        num = int(num/16)
        
    print(f"O decimal {num} em hexadecimal é: {he}")
    
elif opcao == 4:
    print("\n Alunos: \n Renan Garcia - RGM: 30616654")
    print("\n Alunos: \n Matheus Skopek - RGM: 29347424")
    
elif opcao == 0:
    print("Fim")

#Nome: Renan Garcia de Sousa Santos//RGM: 30616654