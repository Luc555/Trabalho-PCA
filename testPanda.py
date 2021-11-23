import pandas as pd
import os
pessoas = []


matricula=input('Digite a matrícula: ')
aluno=input('Digite o seu nome: ')
curso=input('Digite o seu curso: ')


def cria_df(pessoas):
    nomes_colunas = ['matricula','aluno','curso']
    df = pd.DataFrame(columns=nomes_colunas)
    df['matricula']= [matricula]
    df['aluno'] = [aluno]
    df['curso'] = [curso]
    return df

pessoas.append((cria_df(pessoas)))

print(cria_df(pessoas))