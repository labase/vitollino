#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Vittolino
# Copyright 2011-2017 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__, `GPL <http://is.gd/3Udt>`__.
#
# Vittolino é um software livre, você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF), na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA, sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>
"""
Gerador de labirintos e jogos tipo 'novel'.
"""
from browser import document, html

DOC_PYDIV = document["pydiv"]
ppcss = 'https://codepen.io/imprakash/pen/GgNMXO'
STYLE = {'position': "absolute", 'width': 300, 'left': 0, 'top': 0, 'background': "white"}
PSTYLE = {'position': "absolute", 'width': 300, 'left': 0, 'bottom': 0, 'background': "white"}
LIMBOSTYLE = {'position': "absolute", 'width': 300, 'left': 10000, 'bottom': 0, 'background': "white"}
ISTYLE = {'opacity': "inherited", 'height': 30, 'left': 0, 'top': 0, 'background': "white"}
STYLE["min-height"] = "300px"
IMAGEM = ""
NSTYLE = {'position': "absolute", 'width': "80%", 'left': "20%", 'top': 0, 'margin': "0%",
          "min-height": "5%", "cursor": "n-resize"}
SSTYLE = {'position': "absolute", '': "80%", 'left': "20%", 'bottom': 0, 'margin': "0%",
          "min-height": "5%", "cursor": "s-resize"}
LSTYLE = {'position': "absolute", 'width': "5%", 'right': 0, 'top': "20%", 'margin': "0%",
          "min-height": "80%", "cursor": "e-resize"}
OSTYLE = {'position': "absolute", 'width': "5%", 'left': 0, 'top': "20%", 'margin': "0%",
          "min-height": "80%", "cursor": "w-resize"}


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class SalaCenaNula:
    def __init__(self):
        self.esquerda, self.direita = [None] * 2
        self.salas = [None] * 5
        self.cenas = [None] * 4
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas

    def _init(self):
        self._init = lambda _=0, s=self: self
        self.esquerda, self.direita = [SalaCenaNula()] * 2
        self.salas = [SalaCenaNula()] * 5
        self.cenas = [SalaCenaNula()] * 4
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        return self

    def vai(self):
        pass

NADA = SalaCenaNula()._init()


class Elemento:
    limbo = html.DIV(style=LSTYLE)

    def __init__(self, img="", x=0, y=0, w="10px", h="10px", tit="", alt="", act=None, tel=DOC_PYDIV, **kwargs):
        self.img, self.x, self.y, self.tit, self.alt = img, x, y, tit, alt
        self.act = act if act else lambda _=0: None
        self.tela = tel
        self.opacity = 0
        self.style = dict(PSTYLE)
        self.style["min-width"], self.style["min-height"] = w, h
        self.elt = html.DIV(Id=tit, style=self.style)
        if img:
            self.img = html.IMG(src=img)
            self.elt <= self.img
        self.elt.onclick = lambda _=0: self.act()
        self.tela <= self.elt
        self.c(**kwargs)

    def entra(self, cena, x=None, y=None):
        self.elt.x, self.elt.x = x if not None else self.x, y if not None else self.y
        cena.bota(self)

    @classmethod
    def c(cls, **kwarg):
        return [setattr(cls, nome, Elemento(img) if isinstance(img, str) else img) for nome, img in kwarg.items()]


class Portal(Elemento):

    def __init__(self, img="", x=0, y=0, w="10px", h="10px", tit="", alt="", act=None, tel=DOC_PYDIV, **kwargs):
        super().__init__(img, x, y, tit, alt, act, tel)
        self.opacity = 0
        self.style = dict(PSTYLE)
        self.style["min-width"], self.style["min-height"] = w, h
        self.elt = html.DIV(Id=tit, style=self.style)
        self.elt.onclick = lambda _=0: self.act()
        self.tela <= self.elt
        self.c(**kwargs)
    pass

    def p(self, cena, tit="", alt="", x=0, y=0, w="10px", h="10px", img=""):
        self.tit.text, self.alt.text = tit, alt
        cena.act = lambda _=0: self.go.click()
        return cena


class Labirinto:
    def __init__(self, salas):
        salas = [s or NADA for s in salas]
        self.salas = salas
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        for indice, sala in enumerate(self.salas[1:]):
            self.centro.cenas[indice].sai(sala.cenas[indice])
            indice_oposto = (indice + 2) % 4
            sala.cenas[indice_oposto].sai(self.centro.cenas[indice_oposto])


class Sala:
    def __init__(self, imagensnlso, saidasnlso):
        self.cenas = [Cena(img) if img else NADA for img in imagensnlso]
        self.norte, self.leste, self.sul, self.oeste = self.cenas
        [cena.sai(saida) for cena, saida in zip(self.cenas, saidasnlso)]
        for esquerda in range(4):
            cena_a_direita = (esquerda + 1) % 4
            self.cenas[esquerda].direita = self.cenas[cena_a_direita]
            self.cenas[cena_a_direita].esquerda = self.cenas[esquerda]


class Cena:
    """
    Use para construir uma cena.
    ::

        from _spy.vitollino import Cena
    
        cena_esq = Cena(img="esq.jpg")
        cena_mei = Cena(img="mei.jpg", cena_esq)
        cena_mei.vai()
        
    :param str img: URL da imagem
    :param Cena esquerda: Cena que está à esquerda desta
    :param Cena direita: Cena que está à direita desta
    :param Cena meio: Cena que está à frente desta
    :param vai: Função a ser chamada no lugar da self.vai nativa
    """

    def __init__(self, img=IMAGEM, nome='', esquerda=NADA, direita=NADA, meio=NADA, vai=None, **kwargs):
        self.img = img
        self.esquerda, self.direita, self.meio = esquerda or NADA, direita or NADA, meio or NADA
        self.portal(esquerda, direita, meio)
        self.vai = vai or self.vai
        self.cena = html.IMG(src=self.img, width=300, style=STYLE, title=nome)
        Cena.cenas(**kwargs)

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

    def portal(self, esquerda=None, direita=None, meio=None):
        self.esquerda, self.direita, self.meio = esquerda or NADA, direita or NADA, meio or NADA

    @classmethod
    def cenas(cls, **cenas):
        for nome, imagem in cenas.items():
            setattr(Cena, nome, Cena(imagem))

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

    def sai(self, saida):
        self.meio = saida

    def vai(self):
        INVENTARIO.desmonta()
        tela = DOC_PYDIV
        tela.html = ""
        tela <= self.cena
        tela <= self.divesq
        tela <= self.divmeio
        tela <= self.divdir
        INVENTARIO.monta()
        INVENTARIO.cena = self
        return self


@singleton
class Popup:
    def __init__(self, tela=DOC_PYDIV):
        self.tela = tela
        self.popup = html.DIV(Id="__popup__", Class="overlay")
        div = html.DIV(Class="popup")
        self.h2 = html.H2()
        a = html.A("&times;", Class="close", href="#")
        self.go = html.A(Class="button", href="#popup")
        self.alt = html.DIV(Class="content")
        self.tit = html.H1()
        self.popup <= div
        div <= self.h2
        div <= a
        div <= self.content
        tela <= self.popup

    def d(self, cena, tit="", alt="", x=0, y=0, w="10px", h="10px", img=""):
        self.tit.text, self.alt.text = tit, alt
        cena.act = lambda _=0: self.go.click()
        return cena


@singleton
class Inventario:
    def __init__(self, tela=DOC_PYDIV):
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


INVENTARIO = Inventario()


# def virgem():
#     def cria_inventario():
#         global INVENTARIO
#         INVENTARIO = Inventario()
#
#     if not INVENTARIO:
#         cria_inventario()
#     return INVENTARIO


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


def main():
    # Bloco()
    # CenaPrincipal()
    return Bloco()


def __setup__():
    document.head <= html.STYLE(CSS, type="text/css", media="screen")

if "__main__" in __name__:
    main()

CSS = '''
h1 {
  text-align: center;
  font-family: Tahoma, Arial, sans-serif;
  color: #06D85F;
  margin: 80px 0;
}

.box {
  width: 40%;
  margin: 0 auto;
  background: rgba(255,255,255,0.2);
  padding: 35px;
  border: 2px solid #fff;
  border-radius: 20px/50px;
  background-clip: padding-box;
  text-align: center;
}

.button {
  font-size: 1em;
  padding: 10px;
  color: #fff;
  border: 2px solid #06D85F;
  border-radius: 20px/50px;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease-out;
}
.button:hover {
  background: #06D85F;
}

.overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  transition: opacity 500ms;
  visibility: hidden;
  opacity: 0;
}
.overlay:target {
  visibility: visible;
  opacity: 1;
}

.popup {
  margin: 70px auto;
  padding: 20px;
  background: #fff;
  border-radius: 5px;
  width: 30%;
  position: relative;
  transition: all 5s ease-in-out;
}

.popup h2 {
  margin-top: 0;
  color: #333;
  font-family: Tahoma, Arial, sans-serif;
}
.popup .close {
  position: absolute;
  top: 20px;
  right: 30px;
  transition: all 200ms;
  font-size: 30px;
  font-weight: bold;
  text-decoration: none;
  color: #333;
}
.popup .close:hover {
  color: #06D85F;
}
.popup .content {
  max-height: 30%;
  overflow: auto;
}
'''