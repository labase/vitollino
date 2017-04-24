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
############################################################
Vitollino - Teste
############################################################

Verifica a funcionalidade da biblioteca Vitollino.

"""
import unittest
from _spy.vitollino import Cena, Jogo
from unittest.mock import MagicMock  # , patch, ANY


class CenaTest(unittest.TestCase):

    def setUp(self):
        self.gui = MagicMock()
        self.app = Cena("_IMG_", self.gui, self.gui)

    def test_esquerda(self):
        """Cena esquerda vai é chamado."""
        self.app.vai_esquerda()
        self.gui.vai.assert_called_once_with()


class JogoTest(unittest.TestCase):

    def setUp(self):
        self.uma = MagicMock()
        self.outra = MagicMock()
        self.app = Jogo()

    def test_esquerda(self):
        """Cena esquerda vai é chamado."""
        cena = self.app.cena("_IMG_", self.uma, self.outra)
        cena.vai_esquerda()
        self.uma.vai.assert_called_once_with()

    def test_sem_esquerda(self):
        """Cena esquerda vai nao é chamado, direita vai é chamado."""
        cena = self.app.cena("_IMG_", None, self.outra)
        cena.vai_esquerda()
        self.outra.vai.assert_not_called()
        cena.vai_direita()
        self.outra.vai.assert_called_once_with()

    def test_sem_direita(self):
        """Cena direita vai nao é chamado, esquerda vai é chamado."""
        cena = self.app.cena("_IMG_", self.uma)
        cena.vai_direita()
        self.uma.vai.assert_not_called()
        cena.vai_esquerda()
        self.uma.vai.assert_called_once_with()

    def test_so_com_meio(self):
        """Cena direita ou esquerda vai nao é chamado, meio vai é chamado."""
        cena = self.app.cena("_IMG_", None, None, self.uma)
        cena.vai_direita()
        self.uma.vai.assert_not_called()
        cena.vai_esquerda()
        self.uma.vai.assert_not_called()
        cena.vai_meio()
        self.uma.vai.assert_called_once_with()

    def test_redefine_vai(self):
        """Cena direita, esquerda ou meio vai nao é chamado, vai é chamado."""
        cena = self.app.cena("_IMG_", None, None, None, lambda: self.uma.vai())
        cena.vai_direita()
        self.uma.vai.assert_not_called()
        cena.vai_esquerda()
        self.uma.vai.assert_not_called()
        cena.vai_meio()
        self.uma.vai.assert_not_called()
        cena.vai()
        self.uma.vai.assert_called_once_with()

    def test_adiciona_cenas(self):
        """Novas cenas sao criadas e renomeadas."""
        cena = self.app.cena(portao="_IMG_")
        assert cena.portao, "nao criou cena portao"

    def test_navega_para_cena(self):
        """Conecta cenas e navega de uma para outra."""
        cena = self.app.cena(portao="_IMG_", porta="_IMG_")
        cena.porta.portal(None, self.outra)
        assert cena.portao, "nao criou cena portao"
        cena.porta.vai_esquerda()
        self.outra.vai.assert_not_called()
        cena.porta.vai_direita()
        self.outra.vai.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
