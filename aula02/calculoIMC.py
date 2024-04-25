p=float(input("digite seu peso: "))
h=float(input("digite sua altura: "))
imc=p/(h*h)
result=""
if imc < 18.5:
    result = "Indica magreza"
elif imc >= 18.5 and imc <= 24.9:
    result = "Indica peso ideal"
elif imc > 24.9 and imc < 29.9:
    result = "Indica sobrepeso"
else:
    result = "Indica obesidade"

print(f"seu imc é {imc} e indica {result}")