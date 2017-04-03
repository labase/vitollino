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
from _spy.vitollino import Cena
from unittest.mock import MagicMock  # , patch, ANY


class CenaTest(unittest.TestCase):

    def setUp(self):
        self.gui = MagicMock()
        self.app = Cena("_IMG_", self.gui, self.gui)

    def test_esquerda(self):
        """Cena esquerda vai é chamado."""
        self.app.vai_esquerda()
        self.gui.vai.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
