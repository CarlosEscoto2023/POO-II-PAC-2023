"""Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40."""

Horas = float(input("Introduzca el numero de horas trabajadas: "))
Tarifa = float(input("Introduzca la tarifa: "))

if(Horas > 40):
    salario = 40 * Tarifa
    horas_extra = Horas - 40
    salario_extra = horas_extra * (1.5 * Tarifa)
    salario = salario + salario_extra
else:
    salarioalario=(Horas)*Tarifa
print(f"El salario total es: ${salario}")
    
