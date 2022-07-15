import csv
from datetime import date

hoje = date.today()
#dat = input("mes-dia: ")
#data = "2021-"+dat
#data = hoje
#novos = int(input("Novos casos: "))
#ativos = int(input("Casos Ativos: "))
#confirmados = int(input("Confirmados: "))
#mortes = int(input("Obitos: "))
#lista = [data, novos, ativos, confirmados, mortes]

def inserir(data, novos, ativos, confirmados, mortes):
    #pular = "\n"
    lista = [data, novos, ativos, confirmados, mortes] #, pular]
    with open("da.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(lista)
    file.close()

inserir(12,12,12,12,12)