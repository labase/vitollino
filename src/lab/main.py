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
from _spy.vitollino.vitollino import STYLE, INVENTARIO, Cena, Elemento
from _spy.vitollino.vitollino import Popup as Texto
from _spy.vitollino.vitollino import JOGO as j
Cena._cria_divs = lambda *_: None
STYLE['width'] = 1024
STYLE['min-height'] = "800px"
INVENTARIO.elt.style.width = 1024

IMG = dict(
    A_NORTE="https://i.imgur.com/aLEjWgB.png",
    A_LESTE="https://i.imgur.com/sivjAnO.png",
    A_SUL="https://i.imgur.com/otHJhF0.png",

    B_NORTE="https://i.imgur.com/40K5493.png", B_LESTE="https://i.imgur.com/R3bpFXD.png",
    B_OESTE="https://i.imgur.com/dlxY8hi.png", B_SUL="https://i.imgur.com/eYM3Yp9.png",

    C_LESTE="https://i.imgur.com/94V79TA.png", C_NORTE="https://i.imgur.com/YJfnhy9.png",
    C_OESTE="https://i.imgur.com/Fzz2FNz.png", C_SUL="https://i.imgur.com/LFKXlB1.png",

    D_NORTE="http://i.imgur.com/1uWH7rU.png",  D_LESTE="https://i.imgur.com/b0FcjLq.png",
    D_OESTE="https://i.imgur.com/406g75C.png", D_SUL="https://i.imgur.com/HQBtUoQ.png",

    E_NORTE="https://i.imgur.com/uNkTVGg.png", E_SUL="http://i.imgur.com/bculg4O.png",
    E_LESTE="https://i.imgur.com/lUi1E1v.png", E_OESTE="https://i.imgur.com/bPBT1d7.png",
    F_NORTE="https://i.imgur.com/iHsggAa.png", F_SUL="http://i.imgur.com/euNeDGs.png",
    F_LESTE="https://i.imgur.com/NqSCDQR.png", F_OESTE="https://i.imgur.com/hG4mgby.png",

    G_NORTE="https://i.imgur.com/XDIASJa.png", G_SUL="https://i.imgur.com/ARQZ8CX.png",
    G_LESTE="https://i.imgur.com/pJOegNT.png", G_OESTE="http://i.imgur.com/9IhOYjO.png",

    H_NORTE="https://i.imgur.com/WjTtZPn.png", H_LESTE="https://i.imgur.com/AzvB8hs.png",
    H_OESTE="https://i.imgur.com/SIhLGCP.png", H_SUL="https://i.imgur.com/UVnpzzE.png",

    I_NORTE="https://i.imgur.com/RSdQSH1.png", I_SUL="https://i.imgur.com/UGCRJ0d.png",
    I_LESTE="https://i.imgur.com/jSn4zsl.png", I_OESTE="https://i.imgur.com/eG43vn5.png",

    J_NORTE="https://i.imgur.com/MMO11Dv.png", J_SUL="https://i.imgur.com/RkWPb8Z.png",
    J_LESTE="https://i.imgur.com/btv0qfO.png", J_OESTE="https://i.imgur.com/lDezYKu.png",

    K_NORTE="https://i.imgur.com/Tx9Q6vW.png", K_SUL="https://i.imgur.com/rrI94Xh.png",
    K_LESTE="https://i.imgur.com/R6gON2E.png", K_OESTE="https://i.imgur.com/Mn69uua.png",

    L_NORTE="https://i.imgur.com/oAu9lkN.png", L_SUL="https://i.imgur.com/xTjd7UV.png",
    L_LESTE="https://i.imgur.com/JMQAGvc.png", L_OESTE="http://i.imgur.com/UJBMKY7.png",

    M_NORTE="https://i.imgur.com/qoHwGLW.png", M_SUL="https://i.imgur.com/5P3U1Ai.png",
    M_LESTE="http://i.imgur.com/1UXBodl.png",  M_OESTE="https://i.imgur.com/AC2KgZg.png",
    N_NORTE="https://i.imgur.com/KVlUf94.png", N_LESTE="https://i.imgur.com/f6vR0tY.png",
    N_OESTE="https://i.imgur.com/GE8IsRM.png", N_SUL="https://i.imgur.com/RfUP0ez.png",
    O_NORTE="https://i.imgur.com/lOT96Hr.png", O_SUL="https://i.imgur.com/HtRKv7X.png",
    O_LESTE="https://i.imgur.com/uvPjc14.png", O_OESTE="https://i.imgur.com/I7Gn0Xx.png",
    P_NORTE="https://i.imgur.com/OutDPac.png", P_SUL="https://i.imgur.com/sAIhp4b.png",
    P_LESTE="https://i.imgur.com/dc2Ol59.png", P_OESTE="https://i.imgur.com/9IBwxjI.png",
    Q_NORTE="https://i.imgur.com/JRYlZeN.png", Q_SUL="http://i.imgur.com/4BCiuYZ.png",
    Q_LESTE="https://i.imgur.com/ek4cwBg.png", Q_OESTE="https://i.imgur.com/vmZHZmr.png",
    R_NORTE="https://i.imgur.com/qnjq624.png", R_SUL="https://i.imgur.com/nZvwdhP.png",
    R_LESTE="https://i.imgur.com/gS4rXYk.png", R_OESTE="http://i.imgur.com/2Z36mLI.png"
)
PROP= dict(
    NOTE="https://i.imgur.com/SghupND.png"
)


def cria_lab():
    def und(ch):
        return "MANSÃO_%s" % NOME[ch].replace(" ", "_") if ch in NOME else "_NOOO_"
    j.c.c(**SCENES)
    salas = {nome: [getattr(j.c, lado) for lado in lados if hasattr(j.c, lado)] for nome, lados in ROOMS.items()}
    j.s.c(**salas)
    chambers = [[getattr(j.s, und(ch)) if hasattr(j.s, und(ch)) else None for ch in line] for line in MAP]
    j.l.m(chambers)
    blqa, blqb = j.s.MANSÃO_BLOQUEIO.sul.N, j.s.MANSÃO_ARMA_DO_CRIME.norte.N
    print(blqa.img)
    blqa.fecha()
    blqb.fecha()
    j.s.MANSÃO_FACHADA.leste.vai()


class Note:
    def __init__(self):
        cena = j.s.MANSÃO_HALL.oeste
        self.implanta_livro_de_notas(cena)

    def implanta_livro_de_notas(self, cena):
        def pega_papel(_=0):
            vai = Texto(cena, "Um Livro de Notas", "Você encontra um livro de notas")
            j.i.bota(papel, "papel", vai.vai)
        papel = Elemento(
            img=PROP["NOTE"], tit="caderno de notas", vai=pega_papel, style=dict(left=100, top=250, width=40))
        # papel.entra(cena)


def main():
    # criarsalab()
    cria_lab()
    Note()
    pass


NOMES = """SALA A - FACHADA
    SALA B - HALL
    SALA C - SALA DE ESTAR
    SALA D - CENA DO CRIME
    SALA H - A CHAVE
    SALA I - FOLHA DE CADERNO
    SALA J - BLOQUEIO
    SALA E - DESPENSA
    SALA K - PANO ENSANGUENTADO
    SALA L - ESCURIDÃO
    SALA F - ENTRADA DO QUARTO
    SALA G - QUARTO
    SALA N - SALA DE TV
    SALA Q - SALA DE JANTAR
    SALA R - COZINHA
    SALA P - CORREDOR
    SALA O - SALA DE VIGILÂNCIA
    SALA M - ARMA DO CRIME""".split("\n")
CARDINAL = "NORTE LESTE SUL OESTE".split()
NOME = {line.split(" - ")[0].split()[-1]: line.split(" - ")[1].replace(" ", "_") for line in NOMES}
ROOMS = {"MANSÃO_%s" % NOME[room]: ["MANSÃO_%s_%s" % (NOME[room], k) for k in CARDINAL]
         for room in NOME.keys()}
SCENES = {"MANSÃO_%s_%s" % (NOME[room], k): IMG["%s_%s" % (room, k)]
          for k in CARDINAL for room in NOME.keys() if "%s_%s" % (room, k) in IMG}
MAP = """
ABC
--D-E-FG
--HIJKL
----M-N
----OPQR"""[1:].split("\n")
