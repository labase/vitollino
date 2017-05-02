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
Fachada para acessar a API do vitollino.
"""
from . import Cena, Sala, Elemento, Popup, Labirinto, INVENTARIO


class Jogo:
    def __init__(self):
        self.cena = self.c = Cena
        self.sala = self.s = Sala
        self.algo = self.a = Elemento
        self.texto = self.t = Popup
        self.labirinto = self.l = Labirinto
        self.inventario = self.i = INVENTARIO
        pass

JOGO = Jogo()