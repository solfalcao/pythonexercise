resp = "S"
while resp == "S":
    contaCliente = int (input("Digite o número da sua conta: "))
    saldo = float (input("Digite o valor do saldo R$: "))
    debito = float (input("Digite o valor do debito R$: "))
    credito = float (input("Digite o valor do credito R$: "))

    saldoAtual = (saldo - debito) + credito
    

    if saldoAtual >= 0:
        print("Saldo Positivo ")
    else:
        print("Saldo Negativo ")
    resp = input("\nContinua? (S/N) ")
    if resp == "N":
        break
quit()
