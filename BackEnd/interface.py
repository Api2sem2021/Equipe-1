from PySimpleGUI import PySimpleGUI as sg
from tkinter import *
from webscraping import raspar_2020_1, raspar_2020_2, raspar_2021_1

#layout
sg.theme('BlueMono')
layout = [
    [sg.Text('bem vindo a nossa interface de raspagem!!')],
    [sg.Text('essa interface tem por objetivo fazer a raspagem de dados dos grupos de API dos semestres já finalizados,')],
    [sg.Text('salvando os mesmos em um banco de dados e disponibilizando-os para consulta enquanto mantém os dados salvos!')],
    [sg.Button('raspar')],
]

#janela
janela = sg.Window('Nossa interface de raspagem', layout, element_justification='c')

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'raspar':
        raspar_2020_1()

        raspar_2020_2()

        raspar_2021_1()