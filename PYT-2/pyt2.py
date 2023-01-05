"""
Escribir un programa que pregunte al usuario por el numero de horas trabajadas 
y el coste por hora. Despues debe mostrar por pantalla la paga que le corresponde.
"""

# create variable to enter number of hours worked
hours = int(input('please enter number of hours worked: '))

# create variable to enter cost for hour 
price = int(input('please enter price for hour: '))

# Total to price
print(f'the payment corresponds to ${hours*price}')


