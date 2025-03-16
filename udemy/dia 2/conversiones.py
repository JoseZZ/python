num1 = 20
num2 = 30.5

print(type(num1))

num1 = num1 + num2

print(type(num1))
print(type(num2))

num3 = 5.8
print(type(num3))
num4 = int(num3)
print(num4)
print(type(num4))

edad = input("Cuántos años tienes?: ")
print("Tu edad es: " + edad)
print(type(edad))
print(edad + edad)

edad = int(edad) + 1
print(edad)

print("Tu edad el año que viene será: " + str(edad))