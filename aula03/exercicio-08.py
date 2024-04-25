hr=input("Digite o horario atual no formato 'hh:mm': ").split(":")
print(f"O horario equivale a {int(hr[0])*60+int(hr[1])} minutos")