str = input("Digite a string: ")
def diminuir(str):
    max = 2 # Numero Maximo de caracteres Permitidos.
    if len(str) > max:
        return str[:max]
    else:
        return str

uf = diminuir(str)
print (uf)