resp = "S"
while resp == "S":
    idadeMulher1 = int(input("Digite a idade da mulher1: "))
    idadeMulher2 = int(input("Digite a idade da mulher2 diferente da anterior: "))
    idadeHomem1 = int(input("Digite a idade da homem1: "))
    idadeHomem2 = int(input("Digite a idade da homem2 diferente da anterior: "))


    menorM = 0
    maiorM = 0
    if idadeMulher1 > idadeMulher2:
        menorIdadeM = idadeMulher2
        maiorIdadeM = idadeMulher1
        menorM = 2
        maiorM = 1
    if idadeMulher2 > idadeMulher1:
        menorIdadeM = idadeMulher1
        maiorIdadeM = idadeMulher2
        menorM = 1
        maiorM = 2


    menorH = 0
    maiorH = 0 
    if idadeHomem1 > idadeHomem2:
        menorIdade = idadeHomem2
        maiorIdade = idadeHomem1
        menorH = 2
        maiorH = 1
    if idadeHomem2 > idadeHomem1:
        menorIdadeH = idadeHomem1
        maiorIdadeH = idadeHomem2
        menorH = 1
        maiorH = 2
        
    if menorM == 1 and maiorH == 1:
        soma = idadeMulher1 + idadeHomem1
    if menorM == 1 and maiorH == 2:
        soma = idadeMulher1 + idadeHomem2

    if menorM == 2 and maiorH == 1:
        soma = idadeMulher2 + idadeHomem1
    if menorM == 2 and maiorH == 2:
        soma = idadeMulher2 + idadeHomem2

    if maiorM == 1 and menorH == 1:
        produto = idadeMulher1 * idadeHomem1
    if maiorM == 1 and menorH == 2:
        produto = idadeMulher1 * idadeHomem2

    if maiorM == 2 and menorH == 1:
        produto = idadeMulher2 * idadeHomem1
    if maiorM == 2 and menorH == 2:
        produto = idadeMulher2 * idadeHomem2


    print ("A soma do homem mais velho com a mulher mais nova é: ", soma)
    print ("\nO produto do homem mais novo com a mulher mais velha é: ", produto)
    resp = input("\nContinua? (S/N) ")
    if resp == "N":
        break
  
quit()



