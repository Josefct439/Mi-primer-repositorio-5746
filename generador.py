import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingresa la cantidad de caracteres: "))
password = ""

for i in range(longitud):
    caracter = random.choice(caracteres)
    password = password + caracter

print("Esta es tu password: " + password)
