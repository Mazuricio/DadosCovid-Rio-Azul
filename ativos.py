import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.stats import norm
import scipy.signal
from datetime import date, timedelta

df = pd.read_csv("dados.csv")
df["Data"] = pd.to_datetime(df['Data'])#converte dada string pra data mesmo
mesdia = []
for dd in df["Data"]:
    mesdia.append(str(dd)[5:10])

#novos = dados["NovosCasos"]
#ativos = dados["Ativos"]


fig, ax = plt.subplots()

def ativos():
    md_ativos = []
    conta = 0
    fim = len(df["Ativos"])
    for itens in df["Ativos"]:
        if conta == 0:
            md_ativos.append(df["Ativos"][0]/2)
        conta += 1
        if conta < fim:
            new = (df["Ativos"][conta] + df["Ativos"][conta-1]) / 2
            md_ativos.append(new)
    new_ativ = scipy.signal.savgol_filter(md_ativos, 43, 2)
    porcentos = ((new_ativ[-1] - new_ativ[-2]) / new_ativ[-2]) * 100
    ## aquio 
    p1 = ax.bar(df["Data"], df["Ativos"], alpha=0.75) #, label="Número de casos")
    dfhoje = df["Data"][len(df["Data"])-1].strftime('%d/%m/%Y')
    ax.set_title("Casos Ativos - (" + str(dfhoje) + ")" )
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d\n%b"))
    #porcentos = ((new_y[-1] - new_y[-2]) / new_y[-2]) * 100
    y_text = ("Casos ativos - %.f Casos(+%.f%%)"%(df["Ativos"][len(df["Ativos"])-1]  ,porcentos))#('Curva de casos (+%.f%%)' % porcentos)
    plt.plot(df["Data"], new_ativ, color="r", label=y_text )
    ax.grid(True)
    iniciox = df["Data"][len(df["Data"])-25]
    fimx = df["Data"][len(df["Data"])-1] + timedelta(days = 0.5)
    ax.set_xlim(iniciox, fimx)
    #ax.set_ylim(0, 40)
    ax.legend()
    plt.savefig("Ativos.png")
    plt.savefig("Ativos.pdf")
    #plt.clf() ## limpa o grafico ##
    return porcentos


ativos()
plt.show()