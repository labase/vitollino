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
# from _spy.vitollino.vitollino import DOC_PYDIV
from unittest.mock import MagicMock  # , patch, ANY
from _spy.vitollino import JOGO as j


class CenaTest(unittest.TestCase):
    def setUp(self):
        self.gui = MagicMock()
        self.gui.__le__ = MagicMock(name="APPEND", return_value=MagicMock(name="ELT"))
        self.pdiv = MagicMock(name="PDIV")
        # DOC_PYDIV = None #.__le__ = self.pdiv
        self.meio = Cena("_IMG_")
        self.app = Cena("_IMG_", self.gui, self.meio)

    def test_esquerda(self):
        """Cena esquerda vai é chamado."""
        self.app.vai_esquerda()
        self.gui.vai.assert_called_once_with()
        self.app.vai_meio()
        # self.pdiv.assert_called_with(ANY)


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
        cena = self.app.cena("_IMG_", None, None, None, vai=lambda: self.uma.vai())
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


class SalaCTest(unittest.TestCase):
    def setUp(self):
        self.uma = MagicMock()
        self.outra = MagicMock()

    def _cria_cenas_sala(self):
        """Cenas e sala c criadas."""
        j.c.c(cfre="_IMG_", cesq="_IMG_", cdir="_IMG_", cfun="_IMG_", cbau="_IMG_")
        j.c.s(j.c.cfre, self.uma, j.c.cfun, j.c.cdir)

    def test_cria_cenas_sala(self):
        """Cenas e sala c criadas."""
        self._cria_cenas_sala()
        j.c.cfun.vai_esquerda()
        self.uma.vai.assert_called_once_with()

    def _cria_bau_alavanca(self):
        """Artigos  e bau e alavanca criadas."""
        self._cria_cenas_sala()
        j.a.c(bau="_IMG_", alavanca="_IMG_")
        j.c.cesq.bota(j.a.bau)
        j.c.cbau.bota(j.a.alavanca)
        j.a.bau.act = j.c.cbau.vai

    def test_cria_bau_alavanca(self):
        """Artigos  e bau e alavanca criadas."""
        self._cria_cenas_sala()
        self._cria_bau_alavanca()
        assert j.a.bau in j.c.cesq.dentro
        j.a.bau.elt.onclick()
        assert j.a.alavanca in j.c.cbau.dentro
        # assert j.i.cena is j.c.cbau, "cena é %s" % j.i.cena

    def test_bota_alavanca_inventario(self):
        """Alavanca no inventário."""
        self._cria_cenas_sala()
        self._cria_bau_alavanca()
        a = MagicMock(name="Enter Inventory")
        j.i.elt = a
        j.i.elt.__le__ = MagicMock(name="Enter Elt")
        j.i.bota(j.a.alavanca)
        assert j.a.alavanca in j.i.inventario, j.i.inventario
        a.__le__.assert_called_once_with(j.a.alavanca)


class SalaCDialogoTest(unittest.TestCase):
    def setUp(self):
        self.uma = MagicMock()
        self.outra = MagicMock()

    def _cria_cenas_sala(self):
        """Cenas e sala c criadas."""
        j.c.c(cfre="_IMG_", cesq="_IMG_", cdir="_IMG_", cfun="_IMG_", cbau="_IMG_")
        j.c.s(j.c.cfre, self.uma, j.c.cfun, j.c.cdir)

    def test_decora_dialogo(self):
        """Cenas decorada com dialogo."""
        self._cria_cenas_sala()
        j.t.d(j.c.cfre, "UM", "DOIS")
        j.t.POP.go = a = MagicMock(name="Open dialog")
        assert j.t.POP.alt.text == "DOIS"
        assert j.t.POP.tit.text == "UM"
        j.c.cfre.act()
        a.click.assert_called_once_with()

    def test_decora_dialogo_classe(self):
        """Classe Cena decorada com dialogo."""
        @j.t
        class ComBau(Cena):
            pass
        cc = ComBau(tit="UMA", txt="DUAS")
        j.t.POP.go = a = self.uma
        assert j.t.POP.alt.text == "DUAS"
        assert j.t.POP.tit.text == "UMA"
        cc.act()
        a.click.assert_called_once_with()
