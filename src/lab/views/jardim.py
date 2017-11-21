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
Gerador de labirintos e jogos tipo *novel*.

`Vitollino em Github <https://github.com/carlotolla/vitollino>`_

ROTEIRO DO GAME JARDIM RADICAL

Sequência de forma lógica para o funcionamento do jogo, ou seja, “costurar” as histórias das cenas.

.. author Carlo Oliveira
"""
from _spy.vitollino.vitollino import STYLE, INVENTARIO, Cena
from _spy.vitollino.vitollino import JOGO

Cena._cria_divs = lambda *_: None
STYLE['width'] = 800
STYLE['min-height'] = "800px"
INVENTARIO.elt.style.width = 800
ACTIV = "https://activufrj.nce.ufrj.br/studio/labase/{}.jpg?disp=inline&size=G"
QUADROS = [list(range(1, 3)), list(range(1, 9)), [1]]

LOCAIS = ['abrico', 'academia', 'aleiapalmeiras', 'bambus', 'bambuzal', 'bromeliario', 'cascata', 'clarisse', 'comoro',
          'entrada', 'gruta', 'guarita', 'herborizada', 'insetivoras', 'jambeiros', 'japones', 'lago', 'macaco',
          'mexicano', 'mirante', 'narciso', 'orquidario', 'ossanha', 'palmeiras', 'pesquisa', 'portal', 'portao',
          'relogio', 'serpabrandao', 'tartarugas', 'tetis', 'tomjobim', 'vitoriaregia', 'xochipili']
MOMENTOS = lz = {l: ["#".join([l, z, l, z]), True, dict(left=0, top=0, width=100, height=100)]
                 for l, z in zip(LOCAIS, LOCAIS[1:])}


class Config:
    """
    **CONFIGURA**
        Dicionário de configuração das cenas.

        ::

            CONFIGURA = dict(origem=["vestiário#armário#Asseio#Por o avental", True, dict(left=429))

        ===============================  ==============  =========
        Origem, Destino, Título e Texto  Com Popup       Hot Spot
        ===============================  ==============  =========
        "Origem#Destino#Título#Texto"    True or False   {"top":1}
        ===============================  ==============  =========

        **Origem, Destino, Título e Texto**
            String com partes separadas por **#**

            **Origem**
                Nome da cena de origem, precisa ser uma chave de **CONFIGURA**

            **Destino**
                Nome da cena de destino, precisa ser uma chave de **CONFIGURA**

            **Título**
                Título do popup de texto

            **Texto**
                Texto do popup de texto

        **Com Popup**
            Determina se vai aparecer o popup de texto na transição de cenas

        **Hot Spot**
            Dicionário com as dimensões do hot spot que vai receber o click

            ::

                dict(left=429, top=112, width=109, height=300)


    """
    CONFIGURA = {
        'origem': ['abrico#academia#abrico#academia', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'abrico': ['abrico#academia#abrico#academia', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'academia': ['academia#aleiapalmeiras#academia#aleiapalmeiras', True,
                     {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'aleiapalmeiras': ['aleiapalmeiras#bambus#aleiapalmeiras#bambus', True,
                           {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'bambus': ['bambus#bambuzal#bambus#bambuzal', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'bambuzal': ['bambuzal#bromeliario#bambuzal#bromeliario', True,
                     {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'bromeliario': ['bromeliario#cascata#bromeliario#cascata', True,
                        {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'cascata': ['cascata#clarisse#cascata#clarisse', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'clarisse': ['clarisse#comoro#clarisse#comoro', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'comoro': ['comoro#entrada#comoro#entrada', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'entrada': ['entrada#gruta#entrada#gruta', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'gruta': ['gruta#guarita#gruta#guarita', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'guarita': ['guarita#herborizada#guarita#herborizada', True,
                    {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'herborizada': ['herborizada#insetivoras#herborizada#insetivoras', True,
                        {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'insetivoras': ['insetivoras#jambeiros#insetivoras#jambeiros', True,
                        {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'jambeiros': ['jambeiros#japones#jambeiros#japones', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'japones': ['japones#lago#japones#lago', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'lago': ['lago#macaco#lago#macaco', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'macaco': ['macaco#mexicano#macaco#mexicano', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'mexicano': ['mexicano#mirante#mexicano#mirante', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'mirante': ['mirante#narciso#mirante#narciso', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'narciso': ['narciso#orquidario#narciso#orquidario', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'orquidario': ['orquidario#ossanha#orquidario#ossanha', True,
                       {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'ossanha': ['ossanha#palmeiras#ossanha#palmeiras', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'palmeiras': ['palmeiras#pesquisa#palmeiras#pesquisa', True,
                      {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'pesquisa': ['pesquisa#portal#pesquisa#portal', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'portal': ['portal#portao#portal#portao', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'portao': ['portao#relogio#portao#relogio', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'relogio': ['relogio#serpabrandao#relogio#serpabrandao', True,
                    {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'serpabrandao': ['serpabrandao#tartarugas#serpabrandao#tartarugas', True,
                         {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'tartarugas': ['tartarugas#tetis#tartarugas#tetis', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'tetis': ['tetis#tomjobim#tetis#tomjobim', True, {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'tomjobim': ['tomjobim#vitoriaregia#tomjobim#vitoriaregia', True,
                     {'left': 0, 'top': 0, 'width': 100, 'height': 100}],
        'vitoriaregia': ['vitoriaregia#xochipili#vitoriaregia#xochipili', True,
                         {'left': 0, 'top': 0, 'width': 100, 'height': 100}]}


class PreviaDoMomento:
    """
    Cria um proxi para a cena que ativa os portais somente quando é montrada pelo comando vai.

    **self.destino**
        nome da cena que surge ao clicar no portal.

    **self._destino**
        objeto cena referente à cena destino, recuperada como atributo da classe Cena.

    :param jogo: Instância da classe JogoMarcela
    :param destino: nome da cena destino
    """

    def __init__(self, jogo, destino):
        """
        """
        self.destino, self.jogo = destino, jogo
        self._destino = getattr(JOGO.c, destino)
        self.nome = self._destino.nome

    def vai(self, *_, **__):
        """
        Mostra a cena destino e configura o portal nela.

        :param _: captura lista de argumento para evitar erros
        :param __: captura dicionário de argumento para evitar erros
        :return: Nenhum
        """
        self.jogo.configura_momentos(self.destino)
        self._destino.vai(*_, **__)


class JogoJardim:
    """
    Constroi o jogo completo do Jardim.

    :param legendas: lista contendo nomes das cenas *[<nome da cena>, ...]*
    """

    def __init__(self, legendas=LOCAIS):
        self.quadros = legendas
        telas = {nome: ACTIV.format(nome) for nome in legendas}
        print({te: ur[-18:] for te, ur in telas.items()})
        self._cria_cenas(telas)
        self._inicia_jogo()

    def configura_momentos(self, cena):
        """
        Configura a cena do momento para ativar seu portal segundo os dados em **CONFIGURA**.

        **configura_portal_com_texto**
            Portal decorado com texto.

            **@JOGO.n.texto**
                decorador que adiciona um popup de texto. A ação do portal acontece quando se fecha o popup.

            .. code-block:: python

                um_portal = configura_portal_com_texto("vestiário", "armário", hot_spot=dict(left=10, top=90)):


        :param cena: Nome do momento a ser configurado, tem que ser chave de **CONFIGURA**.
        :return: Proxi da cena construída pela classe interna **PreviaDoMomento**.
        """
        origem_destino_titulo_texto, com_texto, hot = Config.CONFIGURA[cena]
        origem, destino, titulo, texto = origem_destino_titulo_texto.split("#")
        origem = getattr(JOGO.c, origem)
        debug = False

        @JOGO.n.texto(titulo, texto)
        def configura_portal_com_texto(origem_, destino_, hot_spot=hot):
            """
            Portal decorado com texto.

            @JOGO.n.texto
                decorador que adiciona um popup de texto. A ação do portal acontece quando se fecha o popup.

            .. code-block:: python

                um_portal = configura_portal_com_texto("vetiário", "armário", hot_spot=dict(left=10, top=90)):

            :param origem_: A cena que vai conter o portal.
            :param destino_: A cena que vai surgir da ação do portal.
            :param hot_spot: Dicionário que vai configurar o hot spot clicável
            :return: Portal criado
            """
            return origem_.portal(L=destino_, style=hot_spot, debug_=debug)

        def configura_portal_sem_texto(origem_, destino_, hot_spot=hot):
            """
            Portal sem texto.

            .. code-block:: python

                um_portal = configura_portal_sem_texto("vestiário", "armário", hot_spot=dict(left=10, top=90)):

            :param origem_: A cena que vai conter o portal.
            :param destino_: A cena que vai surgir da ação do portal.
            :param hot_spot: Dicionário que vai configurar o hot spot clicável
            :return: Portal criado
            """
            return origem_.portal(L=destino_, style=hot_spot)

        previo_destino = PreviaDoMomento(self, destino)

        if com_texto:
            portal_decorado = configura_portal_com_texto(origem, previo_destino)
        else:
            portal_decorado = configura_portal_sem_texto(origem, previo_destino)

        if debug:
            self._decorador_do_vai_do_texto(portal_decorado)

        return previo_destino

    @staticmethod
    def _decorador_do_vai_do_texto(port):
        """
        Decorador do texto para refinamento, publica as dimensões do cursor no popup de texto.

        :param port: portal que vai ser decorado
        :return: Nenhum
        """
        formato_do_texto_no_popup = "dict(left={left}, top={top}, width={width}, height={height})"
        metodo_vai_original = port.texto.vai

        def decorador_do_metodo_vai_do_texto(*a):
            """
            Intercepta o método vai original, adicionando as dimensões no texto do popup.

            :param a: Argumentos originais do vai
            :return: Nenhum
            """
            port.texto.txt = formato_do_texto_no_popup.format(
                **{k: v[:-2] for k, v in dict(left=port.elt.style.left, top=port.elt.style.top,
                                              width=port.elt.style.width, height=port.elt.style.minHeight).items()})
            metodo_vai_original(*a)

        port.texto.vai = lambda *a: decorador_do_metodo_vai_do_texto(*a)

    def _inicia_jogo(self):
        """
        Configura o momento inicial e ativa a primeira tela.

        :return: Nenhum
        """
        self.configura_momentos("origem").vai()

    @staticmethod
    def _cria_cenas(cenas):
        """
        Cria um conjunto de objetos **Cena** a partir de um dicionário.

        Usa a função cria de criar cenas do Vitollino: *JOGO.c.c*

        :param cenas:dicionário contendo *<nome da cena>: <url da imagem>*
        :return: cenário, uma lista de quadros criados
        """
        JOGO.c.c(**cenas)


def main(*_):
    """
    Chamada do jogo, feita a partir do HTML.

    :param _: Parametros recebidos do HTML
    :return: Instância do Jogo da Marcela
    """
    return JogoJardim()
