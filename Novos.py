# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.ndimage.measurements import label
import scipy.signal
from datetime import date, datetime, timedelta
hoje = datetime.today().strftime('%d/%m/%Y')
df = pd.read_csv("dados.csv")
df["Data"] = pd.to_datetime(df['Data'])#converte dada string pra data mesmo
mesdia = []
for dd in df["Data"]:
    mesdia.append(str(dd)[5:10])

Novos = df["Novos"]
#ativos = dados["Ativos"]


fig, ax = plt.subplots()

def media_movel(lista, dias): ## 15 dias
    resultado = []
    conta = 0
    inicio = dias
    fim = len(lista) +1
    for itens in lista:
           if inicio < fim:
              soma = sum(lista[conta:inicio])/len(lista[conta:inicio])
              resultado.append(soma)
              conta += 1
              inicio += 1
    return resultado   


### novos ####
def novos():
    x = df["Data"]
    y = df["Novos"]
    md_y = []
    conta = 0
    fim = len(y)
    ##### Criar lista com curva de dados #Média entre um dia e outro#
    for itens in y:
        if conta == 0:
            md_y.append(y[0]/2)
        conta += 1
        if conta < fim:
            new = (y[conta] + y[conta-1]) / 2
            md_y.append(new)

    ### par ou impar #### Precisa para a suavização, precisa ter um numero impar 
    if (len(md_y)%2) == 0:
        numero = 1
    else:
        numero = 2
    ####
    new_y = scipy.signal.savgol_filter(md_y, len(md_y)-numero, 2) #para suavizar a curva de dados
    
    ### Casos Diarios ###
    por = ((Novos[len(Novos)-1] - Novos[len(Novos)-2]) / Novos[len(Novos)-2] ) * 100
    texto = ("Casos Diários(%.f%%)" %por) 
    ax.bar(df["Data"], df["Novos"], alpha=0.90) #, label=texto)
    ## Ultimo dados
    dfhoje = df["Data"][len(df["Data"])-1].strftime('%d/%m/%Y')
    titulo = "Novos Casos(" + str(dfhoje) + ")"
    ax.set_title(titulo) # seta o titulo
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d\n%b")) #formata a data da escala
    ### Curva de casos ###
    
    porcentos = ((new_y[-1] - new_y[-2]) / new_y[-2]) * 100 # calcula a porcentagem da curva de casos
    y_text = ('Curva de casos - %.f Casos(+%.f%%)' %(y[len(y)-1] ,porcentos))
    plt.plot(df["Data"], new_y, color="r", label=y_text ) ## Plota a curva de casos

    ### Média Movel ####
    new_mdmv = media_movel(df["Novos"], 14) #Pede a media movel de 14 dias
    # suavização da curva de media movel #
    if (len(new_mdmv)%2) == 0:
        numero = 1
    else:
        numero = 2
    new_mv = scipy.signal.savgol_filter(new_mdmv, len(new_mdmv)-numero, 2)
    ## Comparação da média movel a 14 dias e media movel atual em % ##
    quatorze = new_mdmv[len(new_mdmv)-15]
    porcentagem = ((new_mdmv[-1] - quatorze) / quatorze) * 100

    ## plotar a curva de media movel ##
    md_text = ("Média Móvel - %.f Casos(+%.f%%)" %(new_mdmv[-1], porcentagem))
    quanto = len(df["Data"]) -len(new_mdmv)
    plt.plot(df["Data"][quanto:], new_mv, color="black", label=md_text)


    ## Configurações do grafico ##
    ax.grid(True)
    iniciox = df["Data"][len(df["Data"])-25] - timedelta(days= 0.5) # Define 30 dias de dados #
    fimx = df["Data"][len(df["Data"])-1] + timedelta(days = 0.5) #Define hoje #
    ax.set_xlim(iniciox, fimx) #seta o limite #
    ax.set_ylim(0, 75)
    ax.legend() # ativa a legenda
    ## salva ##
    plt.savefig("Novos.png")
    plt.savefig("Novos.pdf")
    resultados = [new_mdmv[-1], quatorze, porcentagem, porcentos]
    #plt.clf() ## limpa o grafico ##
    return resultados
    
#print(df["Data"])
novos()
plt.show()
