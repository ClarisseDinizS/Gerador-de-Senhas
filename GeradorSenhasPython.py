import random

cMax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cMin = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
cEsp = "!@#$%&*"

composicao = cMax + cMin + numeros + cEsp
digitos = 15

senha1 = "".join(random.sample(composicao,digitos))
senha2 = "".join(random.sample(composicao,digitos))
senha3 = "".join(random.sample(composicao,digitos))

print("Senha 1: " + senha1)
print("Senha 2: " + senha2)
print("Senha 3: " + senha3)