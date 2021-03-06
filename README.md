# DadosCovid-Rio-Azul

Scripts em Python para Criar graficos sobre os dados da Covid-19 da cidade de Rio Azul-Paraná

Os scripts utilizam as seguintes bibliotecas: **Pandas**, **Numpy**, **Matplotlib**, **Scipy**, além de outras bibliotecas padrões do Python

Os dados são coletados manualmente no facebook da Secrétaria Municípal de Saúde de Rio Azul, devido ao fato de que lá os dados não são disponibilidados diariamente, e o uso de dados diferentes desta pagina poderiam sugerir algum "manipulação" dos dados comparado com os dados da Secrétaria.

Estes scripts foram disponibilados para a Secrétaria Municipal de Saúde de Rio azul, a qual utilizou para monitorar e divulgar a situação da Covid-19 no municipio.

## Graficos ## 
Inicialmente criados para estudos, estes funcionam gerando imagens de cada gráfico
Os scripts funcionam da seguinte forma:

*Main.py* -> Este gera os dois graficos, mas somente são usados para guardar os dados encontrados no arquivo **historico.csv***

*Novos.py* -> Este gera o gráfico em barra dos novos casos, junto uma curva média de dados, e outra curva com a média móvel, gráfico salvo em Novos.png e Novos.pdf

*ativos.py* -> Este gera o gráfico em barra dos casos ativos junto com uma curva média, grafico salvo em Ativos.png e Ativos.pdf

![Novos](Novos.png)
![Ativos](Ativos.png)


## Programa Diario ## 

Programa criado para auxiliar/automatizar a divulgação do boletim diario pela Secrétaria Municipal de Saude de Rio Azul.
Anteriormente a imagem do boletim era feita manualmente Como uma apresentação de slides.
O Designer apenas foi organizado comparado ao  utilizado anteriormente pela Secrétaria, para não confundir a população.
Programa utiliza do **PySimpleGui** para criar janelas, ficando de facil utilização.

![Boletim](boletim_exemplo.png)
