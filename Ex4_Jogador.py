resp = "S"
while resp == "S":
    nFase1 = float (input("Digite sua nota da fase 1: "))
    nFase2 = float (input("Digite sua nota da fase 2: "))

    media = (nFase1 + nFase2) / 2
    

    if media >= 8:
        print("Média das duas fases: ", media, "\nJogador avaliou a experiência sendo BOA.")
    else:
        print("Média das duas fases: ", media, "\nJogador avaliou a experiência sendo REGULAR.")
    resp = input("\nContinua? (S/N) ")
    if resp == "N":
        break
quit()
