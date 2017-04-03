#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Vittolino
# Copyright 2011-2017 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Vittolino é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>
"""
Gerador de labirintos e jogos tipo 'novel'.
"""
from browser import document, html

STYLE = {'position': "absolute", 'width': 300, 'left': 0, 'top': 0, 'background': "white"}
ISTYLE = {'opacity': "inherited", 'height': 30, 'left': 0, 'top': 0, 'background': "white"}
STYLE["min-height"] = "300px"
IMAGEM = ""


class Labirinto:
    def __init__(self, salas):
        self.salas = salas
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        for indice, sala in enumerate(self.salas[1:]):
            self.centro.cenas[indice].meio = sala.cenas[indice]
            indice_oposto = (indice + 2) % 4
            sala.cenas[indice_oposto].meio = self.centro.cenas[indice_oposto]


class Sala:
    def __init__(self, imagensnlso, saidasnlso):
        self.cenas = []
        for img in imagensnlso:
            self.cenas.append(Cena(img))
        self.norte, self.leste, self.sul, self.oeste = self.cenas
        for cena, saida in enumerate(saidasnlso):
            self.cenas[cena].meio = saida
        for esquerda in range(4):
            cena_a_direita = (esquerda + 1) % 4
            self.cenas[esquerda].direita = self.cenas[cena_a_direita]
            self.cenas[cena_a_direita].esquerda = self.cenas[esquerda]


class Cena:
    def __init__(self, img=IMAGEM, esquerda=None, direita=None, meio=None, vai=None):
        self.img, self.esquerda, self.direita = img, esquerda, direita
        self.meio = meio
        self.vai = vai or self.vai
        self.cena = html.IMG(src=self.img, width=300, style=STYLE)

        self.divesq = divesq = html.DIV(style=STYLE)
        divesq.style.width = 100
        divesq.style.opacity = 0.3
        divesq.onclick = self.vai_esquerda

        self.divmeio = divmeio = html.DIV(style=STYLE)
        divmeio.style.width = 100
        divmeio.style.opacity = 0.2
        divmeio.onclick = self.vai_meio
        divmeio.style.left = 100

        self.divdir = divdir = html.DIV(style=STYLE)
        divdir.style.opacity = 0.1
        divdir.style.width = 100
        divdir.onclick = self.vai_direita
        divdir.style.left = 200

    def vai_direita(self, _=0):
        self.divdir.style.opacity = 0.8
        if self.direita:
            self.direita.vai()

    def vai_esquerda(self, _=0):
        self.divesq.style.opacity = 0.8
        if self.esquerda:
            self.esquerda.vai()

    def vai_meio(self, _=0):
        self.divmeio.style.opacity = 0.8
        if self.meio:
            self.meio.vai()

    def vai(self):
        INVENTARIO.desmonta()
        tela = document["pydiv"]
        tela.html = ""
        tela <= self.cena
        tela <= self.divesq
        tela <= self.divmeio
        tela <= self.divdir
        INVENTARIO.monta()
        INVENTARIO.cena = self
        return self


class Inventario:
    def __init__(self, tela=document["pydiv"]):
        self.tela = tela
        self.cena = None
        self.inventario = {}
        self.opacity = 0
        self.style = dict(STYLE)
        self.style["min-height"] = "30px"
        self.bolsa = html.DIV(Id="__inv__", style=self.style)
        self.bolsa.onclick = self.mostra
        self.limbo = html.DIV(style=self.style)
        self.limbo.style.left = "4000px"
        self.mostra()
        tela <= self.bolsa

    def inicia(self):
        self.inventario = {}
        self.bolsa.html = ""
        self.cena = None
        self.opacity = 0
        self.mostra()

    def desmonta(self, _=0):
        self.limbo <= self.bolsa

    def monta(self, _=0):
        self.tela <= self.bolsa

    def mostra(self, _=0):
        self.opacity = abs(self.opacity - 0.5)
        self.bolsa.style.opacity = self.opacity

    def bota(self, nome_item, item, acao):
        item_img = html.IMG(Id=nome_item, src=item, width=30, style=ISTYLE)
        Dropper(item_img)
        item_img.onclick = acao
        self.inventario[nome_item] = acao
        self.bolsa <= item_img

    def tira(self, nome_item):
        item_img = document[nome_item]
        self.inventario.pop(nome_item, None)
        self.limbo <= item_img


INVENTARIO = None


def virgem():
    def cria_inventario():
        global INVENTARIO
        INVENTARIO = Inventario()

    if not INVENTARIO:
        cria_inventario()
    return INVENTARIO


class Dropper:
    def __init__(self, dropper):
        dropper.ondragstart = self.drag_start
        dropper.onmouseover = self.mouse_over

    def mouse_over(self, ev):
        ev.target.style.cursor = "pointer"

    def drag_start(self, ev):
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'


class Droppable:
    def __init__(self, droppable, dropper_name, action=None):
        droppable.ondragover = self.drag_over
        droppable.ondrop = self.drop
        self.dropper_name = dropper_name
        self.action = action if action else lambda *arg: None

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()

    def drop(self, ev):
        ev.preventDefault()
        src_id = ev.data['text']
        elt = document[src_id]
        elt.style.cursor = "auto"
        if self.dropper_name == src_id:
            self.action(elt, self)


class Folha:
    def __init__(self, texto, html, tela, left):
        style = {'position': "absolute", 'width': 80, 'height': 80, 'left': left, 'top': 10, 'background': "yellow"}
        fid = "folha%d" % left
        self.folha = html.DIV(texto, Id=fid, style=style, draggable=True)
        tela <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over

    def mouse_over(self, ev):
        ev.target.style.cursor = "pointer"

    def drag_start(self, ev):
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'


class Suporte:
    def __init__(self, bloco, html, tela, left, certa):
        style = {'position': "absolute", 'width': 80, 'height': 80, 'left': left, 'top': 100, 'background': "grey"}
        self.folha = html.DIV("............ ............", style=style)
        self.left = left
        self.certa = certa
        tela <= self.folha
        self.folha.ondragover = self.drag_over
        self.folha.ondrop = self.drop
        self.bloco = bloco

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()

    def drop(self, ev):
        ev.preventDefault()
        src_id = ev.data['text']
        elt = document[src_id]
        elt.style.left = self.left
        elt.style.top = 100
        elt.draggable = False  # don't drag any more
        elt.style.cursor = "auto"
        certa = True
        if src_id != self.certa:
            elt.style.background = "red"
            certa = False
            self.bloco.conta_peça(certa)


class Bloco:
    def __init__(self):
        self.monta = lambda *_: None
        ordem = "10 410 310 210 110".split()
        texto = "" \
                "Era uma vez|" \
                "de nós três|" \
                "por cima|" \
                "deu um salto|" \
                "um gato pedrêz|" \
                "".split("|")
        tela = document["pydiv"]
        tela.html = ""
        self.pecas_colocadas = []
        print(list(enumerate(ordem)))
        for pos, fl in enumerate(ordem):
            Suporte(self, html, tela, pos * 100 + 10, "folha" + fl)
        for pos, tx in enumerate(texto):
            Folha(tx, html, tela, pos * 100 + 10)

    def começa_de_novo(self):
        pass

    def conta_peça(self, valor_peça):
        self.pecas_colocadas += valor_peça
        if len(self.pecas_colocadas) == 4:
            if all(self.pecas_colocadas):
                input("O texto está certo.")
            else:
                vai = input("Tentar de novo?")
                if vai == "s":
                    self.começa_de_novo()

    def nao_monta(self):
        pass

    def vai(self):
        self.monta()
        self.monta = self.nao_monta
        # self.centro.norte.vai()


def ofiuco():
    # Bloco()
    # CenaPrincipal()
    return Bloco()


virgem()

if "__main__" in __name__:
    ofiuco()
