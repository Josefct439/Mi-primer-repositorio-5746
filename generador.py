import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
def gen_pass(longitud):
    password = ""
    
    for i in range(longitud):
        caracter = random.choice(caracteres)
        password = password + caracter
    
    return("Esta es tu password: " + password)
