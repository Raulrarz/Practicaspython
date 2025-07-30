
print("Bienvenido a la calculadora de IMC")
#Aqui se solicitan datos del usuario
nombre = input("Ingrese el nombre,apellido paterno y materno: ")
edad = int(input("ingrese su edad: "))
peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros: " ))

#Se validad que sean datos positivos
if edad <= 0 or peso <= 0 or altura <= 0:
  print("Error: Edad, peso y altura deben ser mayores a 0.")
  exit() #Evita que el programa continue si los datos son invalidos
 
# aqui se calcula el IMC
imc = peso / (altura ** 2)
# aqui se imprime el resultado del IMC
print("tu IMC es:", f"{imc:.2f}") 

#Una vez calculado el IMC, se determina la categoria
if imc < 18.9 : #peso bajo
 print("Tu IMC indica que tiene un peso bajo.")
elif 18.5 < imc < 24.99: #peso normal
 print("Tu IMC indica que tiene un peso normal.")
elif 25.0 < imc < 29.99: #sobrepeso
 print("Tu IMC indica que tiene sobrepeso.")
elif 30.0 < imc < 34.99: #obesidad
 print("Tu IMC indica que tiene obesidad.")
elif 35.99 < imc < 39.99: #obesidad media
  print("Tu IMC indica que tiene obesidad media.")
elif imc >= 40.0:  #obesidad mórbida
 print("Tu IMC indica que tiene obesidad mórbida.")

