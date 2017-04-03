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
from _spy.circus.braser import Braser


class Circus:
    """
    Interface com o engenho de games Phaser.
    """
    _instance = None
    BRASER = None

    def __init__(self):
        self._init()
        self.gamer = Circus.BRASER
        self.gamer.subscribe(self)
        self.game = self.gamer.game

    def _init(self):
        Circus.BRASER = Braser(800, 600)

    @classmethod
    def created(cls):
        cls._instance = cls()
        cls.created = lambda *_: cls._instance
        return cls._instance

    def preload(self):
        pass

    def create(self):
        pass

    def spritesheet(self, name, img, x=0, y=0, s=1):
        """
        
        :param name: 
        :param img: 
        :param x: 
        :param y: 
        :param s: 
        :return: 
        """
        self.game.load.spritesheet(name, img, x, y, s)

    def group(self):
        return self.game.add.group()

    def enable(self, item):
        self.game.physics.arcade.enable(item)

    def start_system(self):
        self.game.physics.startSystem(self.gamer.PHASER.Physics.ARCADE)

    def tween(self, sprite, time, tfunction="Linear", autostart=True, delay=0, repeat=-1, yoyo=False, **kwd):
        """
        
        :param sprite: 
        :param time: 
        :param tfunction: 
        :param autostart: 
        :param delay: 
        :param repeat: 
        :param yoyo: 
        :param kwd: 
        :return: 
        """
        return self.game.add.tween(sprite).to(dict(kwd), time, tfunction, autostart, delay, repeat, yoyo)

    def image(self, name, img):
        """
        
        :param name: 
        :param img: 
        :return: 
        """
        return self.game.load.image(name, img)

    def sprite(self, name, x=0, y=0):
        """
        
        :param name: 
        :param x: 
        :param y: 
        :return: 
        """
        return self.game.add.sprite(x, y, name)

    def update(self):
        pass


class Actor(Circus):
    """
    Define um ator, personagem ou cenário.
    """
    def _init(self):
        pass
