#!/usr/bin/python3

# lista com as pessoas, vazia por enquanto.
pessoas = []

# coloquei apenas 5 para não ficar cansativo mas pode ser qualquer valor.
for i in range(2):
    nome = input('Nome : ')
    idade = int(input('Idade : '))
    sexo = input('Sexo : ')

    # cria um dicionário com o que foi entrado e adiciona à lista.
    pessoas.append({ 'nome': nome, 'idade':idade, 'sexo':sexo })

# e para cada pessoa armazenada...
for pessoa in pessoas:
    # recupera de pessoa tanto 'chave' como 'valor'.
    for chave, valor in pessoa.items():
        print("\n\n{} => {}".format(chave, valor))
    print("--------")