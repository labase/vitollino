#tarzan/main.py
#vader/main.py
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
Gerador de labirintos e jogos tipo 'novel
https://github.com/carlotolla/vitollino
"""
from _spy.vitollino.vitollino import STYLE, INVENTARIO, Cena, Elemento
from _spy.vitollino.vitollino import Texto
from _spy.vitollino.vitollino import JOGO
from browser import window, html
Cena._cria_divs = lambda *_: None
STYLE['width'] = 800
STYLE['min-height'] = "800px"
INVENTARIO.elt.style.width = 800
ACTIV = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/Cena_1_Quadro_{}_Momento_{}.jpg"
QUADROS = [list(range(1,3)),list(range(1,9)),[1]]
MOMENTOS = [(quadro+1, momento)
        for quadro, quadros in enumerate(QUADROS) for momento in quadros]

LEGENDAS = "vestiário abriu_o_armário o_asseio acionou_a_pia molhando_as_mãos usando_sabão" \
           " as_bactérias enxaguando secando descontaminando saindo".split()

class JogoMarcela:
    def __init__(self, legendas=LEGENDAS, momentos=MOMENTOS):
        """
        Constroi o jogo completo da Marcela.

        :param legendas: lista contendo nomes das cenas *[<nome da cena>, ...]*
        :param momentos: lista de tuplas indicando o quadro e o momento  *[(<q0>, <m0>), ... ]*
        """
        self.quadros = momentos
        telas = {nome: ACTIV.format(quadro, momento) for nome, (quadro, momento) in zip(legendas, momentos)}
        print({te: ur[-18:] for te, ur in telas.items()})
        self.cenario = self._cria_cenas(telas)
        self._ajusta_hot_points()
        self._inicia_jogo()

    def _ajusta_hot_points(self):
        style_vestiário = dict(left=429, top=112, width=109, height=300, background="white", opacity=0.5)
        style_abriu_o_armário = dict(left=429, top=112, width=109, height=300, background="white", opacity=0.5)
        style_o_asseio=dict(left=354, top=653, width=60, height=60, background="white", opacity=0.5)
        style_acionou_a_pia=dict(left=354, top=653, width=60, height=60, background="white", opacity=0.5)

        JOGO.c.vestiário.portal(L=JOGO.c.abriu_o_armário, style=style_vestiário)
        JOGO.c.abriu_o_armário.portal(L=JOGO.c.o_asseio, style=style_abriu_o_armário)
        JOGO.c.o_asseio.portal(L=JOGO.c.acionou_a_pia, style=style_o_asseio)

    def _inicia_jogo(self):
        JOGO.c.vestiário.vai()

    def _cria_cenas(self, cenas):
        """
        Cria um conjunto de objetos **Cena** a partir de um dicionário.

        Usa a função cria cenas do Vitollino: *JOGO.c.c*

        :param cenas:dicionário contendo *<nome da cena>: <url da imagem>*
        :return: cenário, uma lista de quadros criados
        """
        JOGO.c.c(**cenas)
        return []  # [self._cria_cena(quadro+1, self.quadros[quadro]) for quadro in range(0,3)]

    def _cria_cena(self, quadro, momentos):
        momentos_do_quadro = LEGENDAS  # ["C1Q{}M{}".format(quadro, momento) for momento in momentos]
        momento_atual_e_seguinte = zip(momentos_do_quadro, momentos_do_quadro[1:])
        return [getattr(JOGO.c, atual).portal(L=getattr(JOGO.c, seguinte))
        for atual, seguinte in momento_atual_e_seguinte]



def main(*_):
    JogoMarcela()
