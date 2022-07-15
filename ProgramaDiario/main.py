from PySimpleGUI import PySimpleGUI as sg
from desenhar import Desenhar
#layout
sg.theme("Reddit")
lauout = [
    [sg.Text("Boletim Diário", font=("Verdana", 25))],
    #Data
    [sg.Text("Dia:"), sg.Input(key="dia", size=(10, 10)), sg.Text("Mês:"), sg.Input(key="mes", size=(10, 10))],
    #primeira
    [sg.Text("Novos:"), sg.Input(key="novos",  size=(10, 15)), sg.Text("Ativos:"), sg.Input(key="ativos", size=(10, 15)), 
    sg.Text("Confirmados:"), sg.Input(key="confirmados", size=(10, 15))],
    #segunda
    [sg.Text("Suspeitos:"), sg.Input(key="suspeitos",  size=(10, 15)), sg.Text("Monitorados:"), sg.Input(key="monitorados", size=(10, 15)),
    sg.Text("Óbitos:"), sg.Input(key="obitos", size=(10, 15))],
    #terceira
    [sg.Text("Descartados:"), sg.Input(key="descartados",  size=(10, 15)), sg.Text("Recuperados:"), sg.Input(key="recuperados", size=(10, 15)), 
    sg.Text("Internados:"), sg.Input(key="internados", size=(10, 15))],
    #tabela
    [sg.Text("Casos Por Faixa etaria")],
    [sg.Text("< 1 ano"), sg.Input(key="a1", size=(10, 10)), sg.Text("41 a 50"), sg.Input(key="a50", size=(10, 10))],
    [sg.Text("1 a 10 "), sg.Input(key="a10", size=(10, 10)), sg.Text("51 a 60"), sg.Input(key="a60", size=(10, 10))],
    [sg.Text("11 a 20"), sg.Input(key="a20", size=(10, 10)), sg.Text("61 a 70"), sg.Input(key="a70", size=(10, 10))],
    [sg.Text("21 a 31"), sg.Input(key="a30", size=(10, 10)), sg.Text("71 a 80"), sg.Input(key="a80", size=(10, 10))],
    [sg.Text("31 a 40"), sg.Input(key="a40", size=(10, 10)), sg.Text("81 a 90"), sg.Input(key="a90", size=(10, 10))],
    [sg.Text("mais 90"), sg.Input(key="m90", size=(10, 10))],
    ## urbana ##
    [sg.Text("Area Rural:"), sg.Input(key="rural", size=(10, 15)), sg.Text("Area Urbana:"), sg.Input(key="urbana", size=(10, 15))],
    [sg.Button("Enviar")]
]
#janela
janela = sg.Window("Boletim Diario", lauout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Enviar":
        print(valores["dia"], valores["mes"])
        idades = [valores["a1"], valores["a10"], valores["a20"], valores["a30"], valores["a40"], valores["a50"], valores["a60"], valores["a70"],
        valores["a80"], valores["a90"], valores["m90"]]
        Desenhar(valores["dia"], valores["mes"], valores["novos"], valores["ativos"], valores["confirmados"], valores["suspeitos"], valores["monitorados"],
        valores["obitos"], valores["descartados"], valores["recuperados"], valores["internados"], idades, valores["rural"], valores["urbana"] )
