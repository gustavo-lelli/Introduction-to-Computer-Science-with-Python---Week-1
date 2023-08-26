seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = seg // (3600*24)
seg = seg % (3600*24)
h = seg // 3600
seg = seg % 3600
minutos = seg // 60
seg = seg % 60

print(dias, "dias,", h, "horas,", minutos, "minutos e", seg, "segundos.")

