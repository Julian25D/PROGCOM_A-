"""PROGOM_A_PRUEBA_DIAGNOSTICA_HUGODIAZ.ipynb

#Calcular base de un triángulo
base=float(input("Ingrese la base del triángulo: "))
altura=float(input("Ingresa la altura del triángulo: "))
print(f"El área del triángulo es: {base*altura/2} ")

#Convierta grados Celsius a Fahrenheit
num=int(input("Ingrese la temperatura en grados Celsius: "))
print(f"La temperatura en grados Fahrenheit es: {num*+32} ")

#Desarrolle un programa que calcule el promedio de tres números ingresados por el usuario
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))
print(f"El promedio de los números es: {(num1+num2+num3)/3} ")

#Escriba un programa que calcule el perímetro y área de un círculo dado su radio
rad=float(input("Ingrese el radio del círculo: "))
print(f"El perímetro del círculo es: {2*3.1416*rad} ")
print(f"El área del círculo es: {3.1416*rad**2} ")

#Cree un programa que resuelva una ecuación cuadrática (ax² + bx + c = 0) pidiendo los valores de a, b y c
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))
print(f"La ecuación es: {a}x²+{b}x+{c}=0 ")
print(f"El resultado a la ecuación es: {(-b+(b**2-4*a*c)**1/2)/(2*a)} y {(-b-(b**2-4*a*c)**1/2)/(2*a)}")

#Desarrolle un programa que determine si un número es par o impar
num=int(input("Ingrese un número: "))
if num%2==0:
    print(f"{num} es un número par ")
else:
    print(f"{num} es un número impar ")

#Creé un programa que determine si un año es bisiesto
año=int(input("Ingrese el año: "))
print(f"{año} es un año bisiesto") if año%4==0 and año%100!=0 else print(f"{año} no es un año bisiesto ")

#Escribe un programa que solicite el nombre del usuario y determine si una persona pertenece a la tercera edad (70 años o más) y si se cumple la condición, imprima que se le da prioridad en la fila
nam=input("Ingrese su nombre: ")
e=int(input("Ingrese su edad: "))
if e>=70:
  print(f"{nam}, se encuentra en el rango de preferencia en fila, continúe ")
else:
  print(f"{nam}, no se encuntra en el rango de preferencia en la fila. Continue en espera ")

#Desarrolla un programa que compare tres números y muestre el mayor.
nuum1=float(input("Ingrese el primer número:"))
num2=float(input("Ingrese el segundo número:"))
num3=float(input("Ingrese el tercer número: "))
print(f"El número mayor es: {num1}") if num1>num2 and num2>num3 else print(f"el número mayor es: {num2}") if num2>num1 and num2>num3 else print(f"el número mayor es: {num3}")

#Cree un programa que determine si un triángulo es equilátero, isósceles o escaleno según sus lados
la1=float(input("Ingrese el primer lado del triángulo: "))
la2=float(input("Ingrese el segundo lado del triángulo: "))
la3=float(input("Ingrese el tercer lado del triángulo: "))
if la1==la2 and la2==la3:
  print("el triángulo es equilátero ")
else:
  if la1==la2 or la2==la3 or la1==la3:
    print("El triángulo es isósceles ")
  else:
    print("El triángulo es escaleno  3")

