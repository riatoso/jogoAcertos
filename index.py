# MODULO DE MAIN JOGO ADVINHA TXT
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------
import time
import PySimpleGUI as sg
from modulo.jogo import Advinha

if __name__ == "__main__":
    # CRIA O LAYOUT
    sg.theme("Reddit")
    layout = [
        [sg.Text("Tela de inserção de numeros para sorteio", size=(39, 0))],
        [sg.Text("Numero inicio:", size=10), sg.Input(key="numero1", size=10)],
        [sg.Text("Numero final:", size=10), sg.Input(key="numero2",  size=10)],
        [sg.Button('Verifica', size=10)],
        [sg.Output(size=(50, 10), key="terminal")],
        [sg.Button('Inserir', disabled=True, size=10)],
        [sg.Button('Finalizar', size=10)]
    ]
    # CRIAR A JANELA
    janela = sg.Window('JOGO DE ADVINHA INSERIR DADOS.', layout=layout).finalize()

    while True:
        evento, valores = janela.read()
        if evento == "Verifica":
            numero_inicial = valores["numero1"]
            numero_final = valores["numero2"]
            while True:
                try:
                    numero_inicial = int(numero_inicial)
                    numero_final = int(numero_final)
                    if numero_final < numero_inicial:
                        print("Numero inicial não pode ser maior que o numero final.")
                        time.sleep(2)
                        janela["terminal"].update('')
                        janela["numero1"].update('')
                        janela["numero2"].update('')
                        break
                    else:
                        print("Verificando...")
                        time.sleep(2)
                        print("insira os numeros no jogo.")
                        janela["Inserir"].update(disabled=False)
                        janela["Finalizar"].update(disabled=True)
                        break
                except:
                    print("Existem valores que não são validos.")
                    time.sleep(4)
                    janela["terminal"].update('')
                    janela["numero1"].update('')
                    janela["numero2"].update('')
                    break
        if evento == "Inserir":
            print("Inserção os numeros.")
            time.sleep(5)
            break
        if evento == 'Finalizar':
            janela["terminal"].update('')
            print("Saindo do sistema...")
            time.sleep(4)
            break
        if sg.WIN_CLOSED:
            janela.close()
            break
    janela.close()
    adv = Advinha()
    adv.jogo_advinha(numero_inicial, numero_final)
else:
    print("Voce não esta no modulo principal.")
