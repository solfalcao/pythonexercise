salarioFixo = float (input("Digite o valor do salário fixo - R$: "))
vendas = float (input("Digite o valor das vendas - R$: "))

meta = 20000

comissao = vendas * 0.03

if vendas <= meta:
    salarioTotal = salarioFixo + comissao
else:
    bonus = 600
    salarioTotal = salarioFixo + comissao + bonus
    print ("Atingiu a meta")     

print ("O salário total é R$: ", salarioTotal)

