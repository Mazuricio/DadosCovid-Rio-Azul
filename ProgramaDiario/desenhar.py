from os import XATTR_SIZE_MAX
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from ativos import Ativos
from inserir import inserir
img = Image.open("modeloNEW.png")
draw = ImageDraw.Draw(img)


# font = ImageFont.truetype(<font-file>, <font-size>)
font_numeros = ImageFont.truetype("verdana-bold-3.ttf", 60)
font_data = ImageFont.truetype("verdana.ttf", 24)
font_tabela = ImageFont.truetype("verdana.ttf", 14)
font_p = ImageFont.truetype("verdana.ttf", 20)
# draw.text((x, y),"Sample Text",(r,g,b))


def Desenhar(dia, mes, novos, ativos, confirmado, suspeitos, monitorados, obitos,descartados, recuperados, internados, listaIdade, rural, cidade):
    data = "2021-" + mes + "-" + dia
    sdata = dia + "/" + mes + "/2021"
    hora = "17:00"
    atualizado = sdata + " ás " + hora + " Horas" 
    draw.text((380, 258),atualizado,(255,255,255),font=font_data)
    inserir(data, novos, ativos, confirmado, obitos)
    Ativos()
    grafico = Image.open("Ativos.png")
    
    ### Desenhar Dados ###
    ##novos##
    draw.text((130, 365),novos,(0,0,0),font=font_numeros)
    ##ativos ##
    draw.text((355, 365),ativos,(0,0,0),font=font_numeros)
    ##Confirmados##
    draw.text((540, 365),confirmado,(0,0,0),font=font_numeros)
    ##suspeitos##
    draw.text((125, 505),suspeitos,(0,0,0),font=font_numeros)
    ##Monitorados ##
    draw.text((335, 505),monitorados,(0,0,0),font=font_numeros)
    ##Obitos##
    draw.text((575, 505),obitos,(255,255,255),font=font_numeros)
    ##Descartados##
    draw.text((90, 645),descartados,(0,0,0),font=font_numeros)
    ##recuperados ###
    draw.text((312, 645),recuperados,(0,0,0),font=font_numeros)
    ##internados##
    draw.text((575, 645),internados,(0,0,0),font=font_numeros)

    #### Casos faixa etaria ####
    total = int(ativos)
    ##
    menosp = (int(listaIdade[0])/total * 100)
    ##
    p1a10 = (int(listaIdade[1])/total * 100)
    ##
    p11a20 = (int(listaIdade[2])/total * 100)
    ##
    p21a30 = (int(listaIdade[3])/total * 100)
    ##
    p31a40 = (int(listaIdade[4])/total * 100)
    ##
    p41a50 = (int(listaIdade[5])/total * 100)
    ##
    p51a60 = (int(listaIdade[6])/total * 100)
    ##
    p61a70 = (int(listaIdade[7])/total * 100)
    ##
    p71a80 = (int(listaIdade[8])/total * 100)
    ##
    p81a90 = (int(listaIdade[9])/total * 100)
    ##
    pm90 = (int(listaIdade[10])/total * 100)
    percentual = [menosp, p1a10, p11a20, p21a30, p31a40, p41a50, p51a60, p61a70, p71a80, p81a90, pm90]

    #### Desenhar tabela####
    x1 = 255
    y1 = 778
    valor = 17.2
    x2 = 310
    for itens in listaIdade:
        draw.text((x1, y1),str(itens),(0,0,0),font=font_tabela)
        y1 += valor
    
    y1 = 778
    for ite in percentual:
        per = ("%.2f %%" % ite)
        draw.text((x2, y1),per,(0,0,0),font=font_tabela)
        y1 += valor

    #total tabela #
    draw.text((x1, 967),str(total),(0,0,0),font=font_tabela)
    draw.text((x2, 967),"100%",(0,0,0),font=font_tabela)

    #### ####

    ##áreas ##

    percentual = rural
    estimativa = 100 - int(percentual)
    pcidade = cidade

    if pcidade == None:
        pcidade = estimativa


    draw.text((135, 1007),str(percentual) + "%",(0,0,0),font=font_p)
    draw.text((275, 1007),str(pcidade) + "%",(0,0,0),font=font_p)

    img.save("EDIT.png")
    edit = Image.open("EDIT.png")

    grafico = grafico.resize((380, 310), Image.ANTIALIAS)

    colar = edit.copy()
    colar.paste(grafico, (375, 730))
    ### Precisa ajustar os gráficos, tamanho, posição ta quase certa ##
    #colar.show()
    nome = "Boletim_Covid" + str(data)
    png = nome + ".png"
    colar.save(png)
    converter = Image.open(png)
    pdf = converter.convert("RGB")
    npdf = nome + ".pdf"
    pdf.save(npdf)




'''
dia = str(input("Dia: "))
mes = str(input("Mês: "))
#hora = str(input("Hora: "))
data = "2021-" + mes + "-" + dia
sdata = dia + "/" + mes + "/2021"
hora = "17:00"

atualizado = sdata + " ás " + hora + " Horas" 
draw.text((380, 258),atualizado,(255,255,255),font=font_data)
'''
'''
##Dados##
novos = str(input("Novos casos: "))
ativos = str(input("Ativos: "))
confirmado = str(input("Casos Confirmados: "))
suspeitos = str(input("Casos Suspeitos: "))
monitorados = str(input("Monitorados: "))
obitos = str(input("Obitos: "))
descartados = str(input("Descartados: "))
recuperados = str(input("Recuperados: "))
internados = str(input("Internados: "))
inserir(data, novos, ativos, confirmado, obitos)
'''
#Ativos()


'''
###testes###
novos = "80"
ativos = "80"
confirmado = "1212"
suspeitos = "200"
monitorados = "100"
obitos = "100"
descartados = "100"
recuperados = "1123"
internados = "50"
'''
'''
### ESCREVER ###
##novos##
draw.text((130, 365),novos,(0,0,0),font=font_numeros)
##ativos ##
draw.text((355, 365),ativos,(0,0,0),font=font_numeros)
##Confirmados##
draw.text((540, 365),confirmado,(0,0,0),font=font_numeros)
##suspeitos##
draw.text((125, 505),suspeitos,(0,0,0),font=font_numeros)
##Monitorados ##
draw.text((335, 505),monitorados,(0,0,0),font=font_numeros)
##Obitos##
draw.text((575, 505),obitos,(255,255,255),font=font_numeros)
##Descartados##
draw.text((90, 645),descartados,(0,0,0),font=font_numeros)
##recuperados ###
draw.text((312, 645),recuperados,(0,0,0),font=font_numeros)
##internados##
draw.text((575, 645),internados,(0,0,0),font=font_numeros)
'''
## Caso por faixa etaria ## 
'''
print("Casos Por faixa etária")
total = int(ativos)
##
menos1 = int(input("< 1 ano: "))
menosp = (menos1/total * 100)
##
a1a10 = int(input("1 a 10:"))
p1a10 = (a1a10/total * 100)
##
a11a20 = int(input("11 a 20: "))
p11a20 = (a11a20/total * 100)
##
a21a30 = int(input("21 a 30: "))
p21a30 = (a21a30/total * 100)
##
a31a40 = int(input("31 a 40: "))
p31a40 = (a31a40/total * 100)
##
a41a50 = int(input("41 a 50: "))
p41a50 = (a41a50/total * 100)
##
a51a60 = int(input("51 a 60: "))
p51a60 = (a41a50/total * 100)
##
a61a70 = int(input("61 a 70: "))
p61a70 = (a61a70/total * 100)
##
a71a80 = int(input("71 a 80: "))
p71a80 = (a71a80/total * 100)
##
a81a90 = int(input("81 a 90: "))
p81a90 = (a81a90/total * 100)
##
mais90 = int(input("mais de 90: "))
pm90 = (mais90/total * 100)

valores = [menos1, a1a10, a11a20, a21a30, a31a40, a41a50, a51a60, a61a70, a71a80, a81a90, mais90]
percentual = [menosp, p1a10, p11a20, p21a30, p31a40, p41a50, p51a60, p61a70, p71a80, p81a90, pm90]
'''

'''
x1 = 255
y1 = 778
valor = 17.2
x2 = 310
for itens in valores:
    draw.text((x1, y1),str(itens),(0,0,0),font=font_tabela)
    y1 += valor
    

y1 = 778
for ite in percentual:
    per = ("%.2f %%" % ite)
    draw.text((x2, y1),per,(0,0,0),font=font_tabela)
    #print(per)
    y1 += valor
'''

'''
## total ##
draw.text((x1, 967),str(total),(0,0,0),font=font_tabela)
draw.text((x2, 967),"100%",(0,0,0),font=font_tabela)

##áreas ##

percentual = input("Area Rural:")
estimativa = 100 - int(percentual)
pcidade = input("Area urbana(%.2f ?):" % estimativa )

if pcidade == None:
    pcidade = estimativa


draw.text((135, 1007),str(percentual) + "%",(0,0,0),font=font_p)
draw.text((275, 1007),str(pcidade) + "%",(0,0,0),font=font_p)

img.save("EDIT.png")
edit = Image.open("EDIT.png")

grafico = grafico.resize((380, 310), Image.ANTIALIAS)

colar = edit.copy()
colar.paste(grafico, (375, 730))
### Precisa ajustar os gráficos, tamanho, posição ta quase certa ##
#colar.show()
nome = "Boletim_Covid-19-" + str(data)
png = nome + ".png"
colar.save(png)
converter = Image.open(png)
pdf = converter.convert("RGB")
npdf = nome + ".pdf"
pdf.save(npdf)
'''