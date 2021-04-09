horasMensais = int(input("Digite a quantidade de horas trabalhadas no mês: "))
valorHora = float(input("Digite o valor da hora trabalhada: "))

jornada = 40

horasSemanais = horasMensais / 4

if horasSemanais <= jornada:
    salarioTotal = horasMensais * valorHora

if horasSemanais > jornada:
    horasExtras = (horasSemanais - jornada) * 4

    salarioHoraExtra = (valorHora * 1.5) * horasExtras

    salario = (jornada * 4) * valorHora

    salarioTotal = salario + salarioHoraExtra

    print ("Você recebeu R$: ", salarioHoraExtra, "pelas horas extras")

print ("O salário final do funcionário é R$: ", salarioTotal)
    
    
