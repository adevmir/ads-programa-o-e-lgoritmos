n1=float(input("Digite sua primeira nota: "))
n2=float(input("Digite sua segunda nota: "))
n3=float(input("Digite sua terceira nota: "))
media=(n1+n2+n3)/3
if media >= 7:
    result="aprovado"
else:
    result="reprovado"
print(f"Sua média é {media} e você foi {result}")