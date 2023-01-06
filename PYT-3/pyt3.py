"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
de masa corporal calculado redondeado con dos decimales.
"""
# Create input for data of weight user
weight = float(input('enter your weight in kilograms: '))

# Create input for data of height user
height = float(input('enter your height in meters: '))

# Calculate IMC
imc = weight / (height**2)

# Show the user his imc
print(round(imc, 2))