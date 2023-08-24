"""Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
del programa:
Introduzca las Horas: 20
Introduzca la Tarifa por hora: nueve
Error, por favor introduzca un número
Introduzca las Horas: cuarenta
Error, por favor introduzca un número"""

try:
    horas_trabajadas = float(input("Introduzca las Horas: "))
    tarifa_por_hora = float(input("Introduzca la Tarifa por hora: "))

    if horas_trabajadas <= 40:
        salario = horas_trabajadas * tarifa_por_hora
    else:
        salario_regular = 40 * tarifa_por_hora
        horas_extra = horas_trabajadas - 40
        salario_extra = horas_extra * (1.5 * tarifa_por_hora)
        salario = salario_regular + salario_extra

    print(f"El salario total es: ${salario}")

except ValueError:
    print("Error, por favor introduzca un número")
