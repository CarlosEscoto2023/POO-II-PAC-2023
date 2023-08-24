"""Escribe un programa que use imput para pedirle
al usuario el numero de horas y la tarifa por hora
para calcular el salario bruto"""

Horas = int(input("Introduzca el numero de horas trabajadas: "))
Tarifa = float(input("Introduzca la tarifa: "))
Salario = Horas * Tarifa

print(f"Salario: ${Salario}")
