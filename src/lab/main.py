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
from _spy.vitollino.vitollino import Cena, Sala, STYLE
from _spy.vitollino.vitollino import JOGO as j

STYLE['width'] = 1024
STYLE['min-height'] = "800px"

A_NORTE = "https://i.imgur.com/aLEjWgB.png"
A_LESTE = "https://i.imgur.com/sivjAnO.png"
A_SUL = "https://i.imgur.com/otHJhF0.png"

B_NORTE = "https://i.imgur.com/40K5493.png"
B_LESTE = "https://i.imgur.com/R3bpFXD.png"
B_OESTE = "https://i.imgur.com/dlxY8hi.png"
B_SUL = "https://i.imgur.com/eYM3Yp9.png"

C_LESTE = "https://i.imgur.com/94V79TA.png"
C_NORTE = "https://i.imgur.com/YJfnhy9.png"
C_OESTE = "https://i.imgur.com/Fzz2FNz.png"
C_SUL = "https://i.imgur.com/LFKXlB1.png"

D_NORTE = "http://i.imgur.com/1uWH7rU.png"
D_LESTE = "https://i.imgur.com/b0FcjLq.png"
D_OESTE = "https://i.imgur.com/406g75C.png"
D_SUL = "https://i.imgur.com/HQBtUoQ.png"

H_NORTE = "https://i.imgur.com/WjTtZPn.png"
H_LESTE = "https://i.imgur.com/AzvB8hs.png"
H_OESTE = "https://i.imgur.com/SIhLGCP.png"
H_SUL = "https://i.imgur.com/UVnpzzE.png"

IMG = dict(
    A_NORTE="https://i.imgur.com/aLEjWgB.png",
    A_LESTE="https://i.imgur.com/sivjAnO.png",
    A_SUL="https://i.imgur.com/otHJhF0.png",

    B_NORTE="https://i.imgur.com/40K5493.png",
    B_LESTE="https://i.imgur.com/R3bpFXD.png",
    B_OESTE="https://i.imgur.com/dlxY8hi.png",
    B_SUL="https://i.imgur.com/eYM3Yp9.png",

    C_LESTE="https://i.imgur.com/94V79TA.png",
    C_NORTE="https://i.imgur.com/YJfnhy9.png",
    C_OESTE="https://i.imgur.com/Fzz2FNz.png",
    C_SUL="https://i.imgur.com/LFKXlB1.png",

    D_NORTE="http://i.imgur.com/1uWH7rU.png",
    D_LESTE="https://i.imgur.com/b0FcjLq.png",
    D_OESTE="https://i.imgur.com/406g75C.png",
    D_SUL="https://i.imgur.com/HQBtUoQ.png",

    H_NORTE="https://i.imgur.com/WjTtZPn.png",
    H_LESTE="https://i.imgur.com/AzvB8hs.png",
    H_OESTE="https://i.imgur.com/SIhLGCP.png",
    H_SUL="https://i.imgur.com/UVnpzzE.png",
)

H_SALA = [H_NORTE, H_LESTE, H_SUL, H_OESTE]


def criarsalab():
    a_norte = Cena(img=A_NORTE)
    a_leste = Cena(img=A_LESTE, esquerda=a_norte)
    a_sul = Cena(img=A_SUL, esquerda=a_leste)
    a_norte.direita = a_leste
    a_leste.direita = a_sul
    b_leste = Cena(img=B_LESTE)
    a_leste.meio = b_leste

    b_norte = Cena(img=B_NORTE)
    b_sul = Cena(img=B_SUL, esquerda=b_leste)
    b_oeste = Cena(img=B_OESTE, esquerda=b_sul, direita=b_norte)
    b_norte.direita = b_leste
    b_norte.esquerda = b_oeste
    b_leste.direita = b_sul
    b_leste.esquerda = b_norte
    b_sul.direita = b_oeste
    b_oeste.meio = a_leste
    c_leste = Cena(img=C_LESTE)
    b_leste.meio = c_leste

    c_norte = Cena(img=C_NORTE)
    c_sul = Cena(img=C_SUL, esquerda=c_leste)
    c_oeste = Cena(img=C_OESTE, esquerda=c_sul, direita=c_norte)
    c_norte.direita = c_leste
    c_norte.esquerda = c_oeste
    c_leste.direita = c_sul
    c_leste.esquerda = c_norte
    c_sul.direita = c_oeste
    c_oeste.meio = b_leste
    d_sul = Cena(img=D_SUL)
    c_sul.meio = d_sul

    d_norte = Cena(img=D_NORTE)
    d_leste = Cena(img=D_LESTE, esquerda=d_norte)
    d_oeste = Cena(img=D_OESTE, esquerda=d_sul, direita=d_norte)
    d_norte.direita = d_leste
    d_norte.esquerda = d_oeste
    d_leste.direita = d_sul
    d_leste.esquerda = d_norte
    d_norte.meio = c_leste

    h_sala = Sala(imagensnlso=H_SALA, saidasnlso=[])
    h_sala.norte.meio = d_sul
    h_sala.leste.vai()
    a_leste.vai()


def cria_lab():
    # j.c.c(cfre=B_NORTE, cesq=B_OESTE, cdir=B_LESTE, cfun=B_SUL, cbau="_IMG_")
    j.c.c(**{"c" + k: IMG["B_" + v] for k, v in zip("fre dir fun esq".split(), "LESTE SUL OESTE NORTE".split())})
    j.c.s(j.c.cfre, j.c.cesq, j.c.cfun, j.c.cdir)
    j.c.cfre.vai()


def main():
    # criarsalab()
    cria_lab()
