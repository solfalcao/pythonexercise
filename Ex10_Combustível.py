resp = "S"
while resp == "S":
    qtdeLitros = int (input("Qual a qtde de litros: "))
    tipoCombustivel = input("A - álcool\nG - gasolina\nEscolha o tipo do combústivel : ")


    if tipoCombustivel == "A":
        valorPagamento = qtdeLitros * 3.9
        
    if tipoCombustivel == "G":
        valorPagamento = qtdeLitros * 4.3

    print ("O valor a ser pago é R$ ", valorPagamento)
    
    resp = input("\nContinua? (S/N) ")
    if resp == "N":
        break
quit()
