
    
def exibir_menu():
    print('''Escolha uma opção:
    1. INSERIR
    2. EXIBIR
    3. BUSCAR
    ''')

    
def cadastrar(pessoas):
    nome = input('Nome? ')
    idade = int(input('Idade? '))
    pessoas.append((nome, idade))
        
def listar(pessoas):
    for pessoa in pessoas:
        nome, idade = pessoa
        
    for matr in range(len(pessoas)):
        print(f'Número da matrícula: {matr}, Nome: {nome}, idade: {idade}')

        
def buscar(pessoas):
    identificador_desejado = input('Digite o nome do usuário: ')
    for pessoa in pessoas:
        nome, idade = pessoa
        if nome == identificador_desejado:
            print(f'Nome: {nome}, idade: {idade}')
            break
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')

def main():
    pessoas = []
    cod = []

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            buscar(pessoas)
        else:
            print('Opção inválida')

main()

