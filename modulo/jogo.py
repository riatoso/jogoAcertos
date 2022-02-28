# MODULO PRINCIPAL DE JOGO ADVINHA
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------
import PySimpleGUI as sg
import time


class Advinha:
    def jogo_advinha(self, inicio, fim):
        from random import randint
        self.inicio = inicio
        self.fim = fim

        # CRIA O LAYOUT
        sg.theme("Reddit")
        layout = [
            [sg.Text("Jogo da advinhações de numero", size=(39, 0))],
            [sg.Text(f"Digite um numero entre {self.inicio} e {self.fim}.")],
            [sg.Input(key="numero", size=5)],
            [sg.Button('Verifica')],
            [sg.Output(size=(50, 10), key="terminal")],
            [sg.Button('Sair'), sg.Button('Limpar')]
        ]
        # CRIAR A JANELA
        self.janela = sg.Window('JOGO DE ADVINHAÇÕES DE NÚMERO.', layout=layout).finalize()
        # self.janela.maximize()

        # VARIAVEL DO SORTEIO DE NUMERO
        self.sorteado = randint(inicio, fim)

        while True:
            # PASSA VALORES DE EVENTOS PARA A JANELA PARA NÃO GERAR LOOP
            self.evento, self.valores = self.janela.Read()
            self.valor = self.valores.get("numero")
            if self.evento == "Verifica":
                # print(self.sorteado, self.valor) DEBUG DOS VALORES
                while True:
                    try:
                        self.valor = int(self.valor)
                        if int(self.valor) == int(self.sorteado):
                            print(f"Escolhido {self.valor}")
                            print(f"Sorteado {self.sorteado}")
                            print("Parabens voce acertou.")
                            time.sleep(4)
                            break
                        else:
                            print("Voce errou tente novamente.")
                            time.sleep(2)
                            self.janela['numero'].update('')
                            break
                    except:
                        print("Não é um numero valido.")
                        time.sleep(2)
                        self.janela['numero'].update('')
                        break
            if self.evento == "Limpar":  # LIMPA A JANELA
                self.janela['terminal'].update('')
                continue
            if self.evento == "Sair" or sg.WIN_CLOSED:
                self.janela['terminal'].update('')
                print("Saindo...")
                time.sleep(3)
                self.janela.close()
                break
