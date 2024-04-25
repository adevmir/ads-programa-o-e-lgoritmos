price=float(input('Digite o valor do produto: '))
desc=int(input('Digite a poncentagem de desconto do produto: '))
print(f'O valor do seu produto com desconto de {desc}% é {price*(-desc/100+1)}')