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
from browser import window, document

PHASER = window.Phaser
BraserGame = PHASER.Game


class Braser:
    """
    Brython object-oriented  wrapper for js Phaser.

    :param x: Canvas width.
    :param y: Canvas height.
    :param mode: Canvas mode.
    :param name: Game name.
    :param keyargs: Extra arguments
    """
    PHASER = window.Phaser

    def __init__(self, x=800, y=600, mode=None, name="pydiv", **_):
        mode = mode or PHASER.CANVAS
        document[name].html = ""
        self.game = BraserGame.new(x, y, mode, name,
                                   {"preload": self.preload, "create": self.create, "update": self.update})
        self.subscribers = []

    def subscribe(self, subscriber):
        """
        Subscribe elements for game loop.

        :param subscriber:
        """
        self.subscribers.append(subscriber)

    def preload(self, *_):
        """
        Preload element.

        """
        for subscriber in self.subscribers:
            subscriber.preload()

    def create(self, *_):
        """
        Create element.

        """
        for subscriber in self.subscribers:
            subscriber.create()

    def update(self, *_):
        """
        Update element.

        """
        for subscriber in self.subscribers:
            subscriber.update()
