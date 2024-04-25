name=input('Digite seu nome: ')
sal=float(input('Digite seu salario atual: '))
up=int(input('Digite o percentual de aumento do salario: '))
print(f'{name} seu novo salario com aumento é {sal+(sal*up/100)}')