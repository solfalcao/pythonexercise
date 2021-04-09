# ler 3 valores numéricos diferentes e mostrar o menor e maior valor

resp = "S"
while resp == "S":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número diferente do primeiro: "))
    num3 = int(input("Digite o terceiro número diferente dos dois anteriores: "))


    if num1 > num2 and num2 < num3:
            menor = num2
    if num2 > num3 and num3 < num1:
            menor = num3
    if num3 > num1 and num1 < num2:
            menor = num1


    if num1 < num2 and num2 > num3:
            maior = num2
    if num2 < num3 and num3 > num1:
            maior = num3
    if num3 < num1 and num1 > num2:
            maior = num1

    print ("\n\nO maior número é: ", maior)
    print ("\nO menor número é: ", menor)
    resp = input("\nContinua? (S/N) ")
    if resp == "N":
        break
  
quit()



