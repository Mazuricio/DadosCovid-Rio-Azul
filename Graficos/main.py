from Novos import novos
from ativos import ativos
import csv
from datetime import date
import pandas as pd
arquivos = "historico.csv"
hoje = date.today()
# Main serve para gerar os dois graficos e salvar as imagens e os resultados ##
## O grafico dos ativos misturou e não esta sendo salvo, fazer pelo proprio script ##

dfh = pd.read_csv("historico.csv")
dfh["Data"] = pd.to_datetime(dfh['Data'])
df = pd.read_csv("dados.csv")
df["Data"] = pd.to_datetime(df['Data'])

dfhoje = dfh["Data"][len(dfh["Data"])-1].strftime('%d/%m/%Y')
fhoje = df["Data"][len(df["Data"])-1].strftime('%d/%m/%Y')

if dfhoje < fhoje:
    print('Salvados Dados em historico.csv')
    dadosnv = novos()
    print("Imagem novos.png e novos.pdf salvos")
    
    dadosat = ativos()



    listao = [df["Data"][len(df["Data"])-1]]

    for itens in dadosnv:
        listao.append(itens)

    listao.append(dadosat)

    with open(arquivos, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(listao)
    print("Dados Salvos")
else:
    print("Não há dados para atualizar")



