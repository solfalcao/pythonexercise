resp = "S"
while resp == "S":
    estoqueAtual = int (input("Quantidade do estoque atual: "))
    qtdeMaxima = int (input("Quantidade máxima: "))
    qtdeMinima = int (input("Quantidade mínima: "))

    qtdeMedia = (qtdeMaxima + qtdeMinima) / 2

    if estoqueAtual >= qtdeMedia:
        print("Não efetuar compra")
    else:
        print("Efetuar compra")
    resp = input("\nContinua? (S/N) ")
    if resp == "N":
        break
quit()
