minSal=float(input('Digite o valor do salario minimo: '))
hourTrab=int(input('Digite a quantidade de horas trabalhadas neste mes: '))
sal=(minSal*0.2)*hourTrab
liquidSal=sal*0.9
print(f'Seu salario bruto é {sal} e seu salario liquido é {liquidSal}')