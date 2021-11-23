string ='lucastins5@gmail.com'

def f(string):
    letras_minusculas = [chr(x) for x in range(ord('a'), ord('z')+1)]
    simbolos_permitidos = [i for i in string if i not in letras_minusculas]
    print(simbolos_permitidos)
    
    if simbolos_permitidos ==['@', '.']:
        print('E-mail correto')
        return True
    else:
        print('E-mail errado')
        return False
f(string)