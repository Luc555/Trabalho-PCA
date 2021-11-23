import pandas as pd
import os
   
def exibir_menu():
    print('''\n\nEscolha uma opção:
    1. INSERIR
    2. EXIBIR
    3. BUSCAR
    ''')
 
    
def cadastrar(pessoas):
    nome = input('Preencha com o nome completo: ')
    idade = int(input('Cadastre aqui a idade: '))
    rua = input('Insira a rua: ')
    num = int(input('Registre o número do imóvel: '))
    bairro = input('Digite o bairro: ')
    cid = input('Preencha com o nome da cidade: ')
    uf = input('Digite a unidade federativa: ')
    uf= uf.upper()
    uf = uf[:2]
    tel = input('Registre o número de telefone: ')
    tel= tel[:11]

    tel = int(tel)# se contiver letras causa um ValueError
    tel = str(tel)
    celular = tel
    telFormatado = '({}) {}-{}-{}'.format(celular[0:2],
                            celular[2] ,celular[3:7], celular[7:])
    tel= telFormatado 
    email = input('Preencha com o e-mail: ')
    
    matr=0
    
    for matr in range(len(pessoas)):
        print("")
    
    def cria_df():
        nomes_colunas = ['nome', 'idade', 'rua', 'num', 'bairro', 'cid', 'uf', 'tel', 'email', 'matr']
        df = pd.DataFrame(columns=nomes_colunas)
        df['nome' ]= [nome]
        df['idade'] = [idade]
        df['rua'] = [rua]
        df['num'] = [num]
        df['bairro'] = [bairro]
        df['cid'] = [cid]
        df['uf'] = [uf,]
        df['tel'] = [tel,]
        df['email'] = [email]
        df['matr'] = [matr]

        
        return df

    df= cria_df()
    pessoas.append((df))
    linha = str(nome)+";"+str(idade)+";"+str(rua)
    
    diretorio = os.path.dirname("./Trabalho-PCA/") 
    df.to_csv(str(os.path.join(diretorio, "cadastro_alunos.csv" )), index=False)
    print("\nSalvando...")
    with open("./Trabalho-PCA/cadastro_alunos.csv", 'a+') as csv_file:
         csv_file.write(linha)
    
def get_nome(df, numero_linha):
    nome = df.at[numero_linha, 'nome']
    return nome
def get_idade(df, numero_linha):
    idade = df.at[numero_linha, 'idade']
    return idade
def get_rua(df, numero_linha):
    rua = df.at[numero_linha, 'rua']
    return rua
def get_num(df, numero_linha):
    num = df.at[numero_linha, 'num']
    return num
def get_bairro(df, numero_linha):
    bairro = df.at[numero_linha, 'bairro']
    return bairro
def get_cid(df, numero_linha):
    cid = df.at[numero_linha, 'cid']
    return cid
def get_uf(df, numero_linha):
    uf = df.at[numero_linha, 'uf']
    return uf
def get_tel(df, numero_linha):
    tel = df.at[numero_linha, 'tel']
    return tel
def get_email(df, numero_linha):
    email = df.at[numero_linha, 'email']
    return email
def get_matr(df, numero_linha):
    matr = df.at[numero_linha, 'matr']
    return matr


def listar(pessoas):
            
    for pessoa in pessoas:
        df = pessoa
        
        for i in range(len(df)):
            nome = get_nome(df, i)
            idade = get_idade(df, i)
            rua = get_rua(df, i)
            num = get_num(df, i)
            bairro = get_bairro(df, i)
            cid = get_cid(df, i)
            uf = get_uf(df, i)
            tel = get_tel(df, i)
            email = get_email(df, i)
            matr = get_matr(df, i)
                

            #print(f'Cadastro:\n {pessoas}\n')
            print(f'Matr: {matr}\nNome: {nome}\nIdade: {idade}\nRua: {rua}\nNúmero do Imóvel: {num}\nBairro: {bairro}')
            print(f'Cidade: {cid}\nEstado: {uf}\nTelefone: {tel}\nE-mail: {email}\n')
            
     
    
def buscar(pessoas):
    identificador_desejado = input('Digite o nome do usuário: ')
    for pessoa in pessoas:
        nome, idade, rua, num, bairro, cid, uf, tel, email = pessoa
        if nome == identificador_desejado:
            print(f'\nNome: {nome};\nIdade: {idade};')
            print(f'Rua: {rua};\nNúmero do Imóvel: {num};\nBairro: {bairro};')
            print(f'Cidade: {cid};\nUF: {uf};\ntelefone: {tel};\nE-mail: {email};\n\n')
            break
    else:
        print(f'Pessoa com nome não identificado {identificador_desejado} não encontrada')

def main():
    pessoas = []
   


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

