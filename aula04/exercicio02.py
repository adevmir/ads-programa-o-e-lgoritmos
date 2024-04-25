n1=float(input("Digite sua primeira nota: "))
n2=float(input("Digite sua segunda nota: "))
media=(n1+n2)/2
if media >= 7:
    result="aprovado"
elif media < 4:
    result="reprovado"
else:
    result="em exame"
print(f"Sua média é {media} e você está {result}")