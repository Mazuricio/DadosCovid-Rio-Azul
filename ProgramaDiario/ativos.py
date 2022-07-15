import pandas as pd
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

def Ativos():
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
            
    #print(md_ativos[-1])
    if (len(md_ativos)%2) == 0:
        numero = 1
    else:
        numero = 0
    new_ativ = scipy.signal.savgol_filter(md_ativos, 15, 2)
    #print(new_ativ[-1])
    porcentos = ((new_ativ[-1] - new_ativ[-2]) / new_ativ[-2]) * 100
    ## aquio 
    p1 = ax.bar(df["Data"], df["Ativos"], alpha=0.75) #, label="Número de casos")
    ax.set_title("Casos Ativos- 30 dias")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d\n%b"))
    #porcentos = ((new_y[-1] - new_y[-2]) / new_y[-2]) * 100
    y_text = ("Casos ativos - %.f Casos(%.f%%)"%(df["Ativos"][len(df["Ativos"])-1]  ,porcentos))#('Curva de casos (+%.f%%)' % porcentos)
    plt.plot(df["Data"], new_ativ, color="r", label=y_text )
    ax.grid(axis='y')
    ## Limites ##
    iniciox = df["Data"][len(df["Data"])-30] - timedelta(days = 0.5)
    fimx = df["Data"][len(df["Data"])-1] + timedelta(days = 0.5)
    ax.set_xlim(iniciox, fimx)
    ax.legend()
    plt.savefig("Ativos.png")
    plt.savefig("Ativos.pdf")
    #return porcentos


#ativos()
#plt.show()