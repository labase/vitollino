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
import json
import unittest
from _spy.vitollino import Cena, Jogo
from unittest.mock import MagicMock, call
from _spy.vitollino import JOGO as j
from _spy.vitollino.vitollino import NoEv
from browser import ajax
import browser

I = "_IMG_"
MAPA = [["sala_" + s if s else "" for s in l.split(",")]
        for l in "a,b,c,,,,,,_,,d,,e,f,g_,,h,i,j,k,l,,_,,,,m,,n,_,,,,o,p,q,r".split("_")]

SALAS = [chr(i) for i in range(ord('a'), ord('z') + 1)]


class TNoEv:
    def __init__(self, x=-100, y=-200):
        self.x = x
        self.y = y

    def stopPropagation(self):
        pass


class CenaTest(unittest.TestCase):
    def setUp(self):
        self.gui = MagicMock()
        self.gui.__le__ = MagicMock(name="APPEND", return_value=MagicMock(name="ELT"))
        self.pdiv = MagicMock(name="PDIV")
        # DOC_PYDIV = None #.__le__ = self.pdiv
        self.meio = Cena("_IMG_", nome="meio")
        self.app = Cena("_IMG_", self.gui, self.meio, nome="app")

    def tearDown(self):
        self.gui = self.pdiv = self.meio = self.app = None

    def test_esquerda(self):
        """Cena esquerda vai é chamado."""
        self.app.vai_esquerda()
        self.gui.vai.assert_called_once_with()
        self.app.vai_meio()
        # self.pdiv.assert_called_with(ANY)

    def test_sala_kwargs(self):
        """Monta salas usando kwargs."""
        sala = j.c.s(I, I, I, I, sala_a=(I, I, I, I))
        outrasala = j.c.s(I, sala.sul, I, I, sala_b=(I, I, j.s.sala_a.sul, self.gui))
        assert sala.norte
        assert outrasala.norte
        assert j.s.sala_a.norte
        self.assertEqual(j.s.sala_b.sul.direita, self.gui, j.s.sala_b.sul.direita)
        j.s.sala_b.sul.vai_direita()
        self.gui.vai.assert_called_once_with()

    def test_sala_nomeado(self):
        """Monta salas usando direções nomeadas."""
        sala = j.c.s(n=I, s=I, sala_c=(I, I, I, I))
        outrasala = j.c.q(s=sala.sul, l=self.gui, sala_d=(I, I, j.s.sala_c.sul, sala.norte))
        assert sala.norte
        assert outrasala.norte
        assert j.s.sala_c.norte
        self.assertEqual(j.s.sala_d.norte.esquerda, sala.norte, j.s.sala_d.norte.esquerda)
        outrasala.sul.vai_esquerda()
        self.gui.vai.assert_called_once_with()

    def test_portal(self):
        """Adiciona portal"""
        self.meio.elt = MagicMock(name="ELT")
        self.meio.elt.__le__ = MagicMock(name="ELT__le__")
        p = j.p(self.meio, N=self.app)
        assert p.cena == self.meio
        self.meio.elt.__le__.assert_called_once_with(p.elt)
        assert "cursor" in p.style, "O estilo do portal é {p.style}"
        assert p.style["cursor"] == "n-resize", "O estilo do cursor é {p.style['cursor']}"

    def test_portal_estilizado(self):
        """Adiciona portal com estilo"""
        self.meio.elt = MagicMock(name="MEIOPDIVEST")
        self.meio.elt.__le__ = MagicMock(name="PDIVEST")
        p = self.meio.portal(N=self.app, style=dict(left=222))
        self.meio.elt.__le__.assert_called_once_with(p.elt)
        assert "cursor" in p.style, "O estilo do portal é {p.style}"
        assert p.style["cursor"] == "n-resize", "O estilo do cursor é {p.style['cursor']}"
        assert p.style["left"] == 222, "O estilo do cursor é p.style['cursor'] {}".format(p.style["left"])

    def test_portal_nao_estilizado(self):
        """Adiciona portal sem estilo"""
        self.meio.elt = MagicMock(name="MEIOPDIVEST")
        self.meio.elt.__le__ = MagicMock(name="PDIVEST")
        p = self.meio.portal(O=self.app)
        self.meio.elt.__le__.assert_called_once_with(p.elt)
        assert "cursor" in p.style, "O estilo do portal é {p.style}"
        assert p.style["cursor"] == "w-resize", "O estilo do cursor é p.style['cursor'] {}".format(p.style["cursor"])
        assert p.style["left"] == 0, "O estilo do cursor é p.style['cursor'] {}".format(p.style["left"])

    def test_notifica_portal(self):
        """Adiciona notificação ao portal"""
        self.meio.elt = MagicMock(name="MEIONOTI")
        self.meio.elt.__le__ = MagicMock(name="NOTI")
        p = j.n.texto("oi", "ok")(self.meio.portal)(O=self.app)
        assert p.texto.tit == "oi"
        self.meio.elt.__le__.assert_called_with(p.texto.elt)
        texto_vai, p.texto.vai = p.texto.vai,  MagicMock(name="TEXTONOTI")
        p.texto.vai.side_effect = texto_vai
        self.app.vai = MagicMock(name="DESTNOTI")
        p.vai()
        # p.texto.vai.assert_called() TODO: fix
        self.app.vai.assert_not_called()
        j.t.POP._close(None)
        # self.app.vai.assert_called() TODO: fix
        assert "cursor" in p.style, "O estilo do portal é {p.style}"
        assert p.style["cursor"] == "w-resize", "O estilo do cursor é p.style['cursor'] {}".format(p.style["cursor"])
        assert p.style["left"] == 0, "O estilo do cursor é p.style['cursor'] {}".format(p.style["left"])

    def test_notifica_portal_decorado(self):
        """Adiciona decorador de notificação ao portal"""
        self.meio.elt = MagicMock(name="MEIONOTI")
        self.meio.elt.__le__ = MagicMock(name="NOTI")
        @j.n.texto("oi", "ok")
        def decorado(origem, **k):
            return origem.portal(**k)
        p = decorado(self.meio, O=self.app)
        assert p.texto.tit == "oi"
        self.meio.elt.__le__.assert_called_with(p.texto.elt)
        texto_vai, p.texto.vai = p.texto.vai,  MagicMock(name="TEXTONOTI")
        p.texto.vai.side_effect = texto_vai
        self.app.vai = MagicMock(name="DESTNOTI")
        p.vai()
        # p.texto.vai.assert_called() TODO: fix
        self.app.vai.assert_not_called()
        j.t.POP._close(None)
        # self.app.vai.assert_called() TODO: fix
        assert "cursor" in p.style, "O estilo do portal é {p.style}"
        assert p.style["cursor"] == "w-resize", "O estilo do cursor é p.style['cursor'] {}".format(p.style["cursor"])
        assert p.style["left"] == 0, "O estilo do cursor é p.style['cursor'] {}".format(p.style["left"])

    def test_decora_portal(self):
        """Adiciona portal decora"""

        @j.p(N=self.meio, S=self.app)
        class Acena(Cena):
            ...

        self.meio.vai = MagicMock()
        self.meio.elt.__le__ = self.pdiv
        a = Acena("img")
        assert hasattr(a, "elt"), a
        assert a.N == self.meio, "%s != %s" % (a.N.img, self.meio.img)
        assert a.S == self.app
        b = Acena("img")
        assert hasattr(b, "elt")
        assert b.N == self.meio
        assert b.S == self.app
        # self.meio.vai.assert_called_once_with(ANY)


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


class SalaTest(unittest.TestCase):
    def setUp(self):
        self.uma = MagicMock()
        self.outra = MagicMock()

    @staticmethod
    def _cria_cenas_sala():
        """Cenas e sala c criadas."""
        j.c.c(cfre="_IMG_", cesq="_IMG_", cdir="_IMG_", cfun="_IMG_", cbau="_IMG_")
        return j.s(n=j.c.cfre, l=j.c.cesq, s=j.c.cfun, o=j.c.cdir)

    def test_cria_cenas_sala(self):
        """Cenas e sala c criadas."""
        self._cria_cenas_sala()
        j.c.cesq.vai = self.uma
        assert j.c.cfun.O == j.c.cesq
        j.c.cfun.O()
        j.c.cesq.vai.assert_called_once_with(NoEv())

    def test_conecta_sala(self):
        """Cenas e sala c, d conectadas."""
        c = self._cria_cenas_sala()
        j.c.c(dfre="_IMG_", desq="_IMG_", ddir="_IMG_", dfun="_IMG_", dbau="_IMG_")
        d = j.s(n=j.c.dfre, l=j.c.desq, s=j.c.dfun, o=j.c.ddir)
        j.l(c, d, d, d, d)
        j.c.dfun.vai = self.uma
        assert j.c.cfun.N == j.c.dfun
        j.c.cfun.N()
        j.c.dfun.vai.assert_called_once_with(NoEv())
        j.c.cfre.vai = self.outra
        assert j.c.dfre.N == j.c.cfre
        j.c.dfre.N()
        j.c.cfre.vai.assert_called_once_with(NoEv())

    def test_mapeia_sala(self):
        """Cenas e sala c, d mapeadas."""
        c = self._cria_cenas_sala()
        j.c.c(efre="_IMG_", eesq="_IMG_", edir="_IMG_", efun="_IMG_")
        d = j.s(n=j.c.efre, l=j.c.eesq, s=j.c.efun, o=j.c.edir)
        j.l.m([[c, d], [d, c]])
        j.c.efun.vai = self.uma
        assert j.c.cfun.N == j.c.efun
        j.c.cfun.N()
        j.c.efun.vai.assert_called_once_with(NoEv())
        j.c.cfre.vai = self.outra
        assert j.c.efre.N == j.c.cfre
        j.c.efre.N()
        j.c.cfre.vai.assert_called_once_with(NoEv())


class SalaCTest(unittest.TestCase):
    def setUp(self):
        self.uma = MagicMock()
        self.outra = MagicMock()

    def _cria_cenas_sala(self):
        """Cenas e sala c criadas."""
        j.c.c(cfre="_IMG_", cesq="_IMG_", cdir="_IMG_", cfun="_IMG_", cbau="_IMG_")
        j.c.q(j.c.cfre, self.uma, j.c.cfun, j.c.cdir)

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
        # a.__le__.assert_called_once_with(j.a.alavanca)


class SalaCDialogoTest(unittest.TestCase):
    def setUp(self):
        self.uma = MagicMock()
        self.outra = MagicMock()
        self.uma.__le__ = self.outra.__le__ = MagicMock()

    def _cria_cenas_sala(self):
        """Cenas e sala c criadas."""
        j.c.c(cfre="_IMG_", cesq="_IMG_", cdir="_IMG_", cfun="_IMG_", cbau="_IMG_")
        j.c.s(j.c.cfre, self.uma, j.c.cfun, j.c.cdir)

    def test_decora_dialogo(self):
        """Cenas decorada com dialogo."""
        self._cria_cenas_sala()
        j.t.d(j.c.cfre, "UM", "DOIS")
        j.t.POP._open = a = MagicMock(name="Open dialog")
        j.c.cfre.vai()
        assert j.t.POP.alt.text == "DOIS", j.t.POP.alt.text
        assert j.t.POP.tit.text == "UM", j.t.POP.tit.text
        a.assert_called_once_with()

    def test_decora_dialogo_classe(self):
        """Classe Cena decorada com dialogo."""

        @j.t
        class ComBau(Cena):
            elt = Cena()
            pass

        cc = ComBau(tit="UMA", txt="DUAS")
        j.t.POP._open = a = self.uma
        assert isinstance(cc, Cena), type(cc)
        cc.vai()
        assert j.t.POP.alt.text == "DUAS", j.t.POP.alt.text
        assert j.t.POP.tit.text == "UMA", j.t.POP.tit.text
        a.assert_called_once_with()


class LabirintoTest(unittest.TestCase):
    def setUp(self):
        j.s.c(**{"sala%s" % k: ["sala%s_%s" % (k, v) for v in list("nlso")] for k in list("cnlso")})

    @staticmethod
    def test_labirinto_cruz():
        """Labirinto em Cruz."""
        lab = j.l(*[getattr(j.s, "sala%s" % k) for k in list("cnlso")])
        labnn = lab.centro.norte.N
        assert labnn == j.s.salan.norte, "%s != %s" % (labnn.img, j.s.salan.norte.img)

    @staticmethod
    def _labirinto_mapa():
        """Labirinto em Mapa."""
        c, n, l, s, o = [getattr(j.s, "sala%s" % k) for k in list("cnlso")]
        maper = [[c, n, l], [None, s, o]]
        j.l.m(maper)
        labnn = s.norte.N.img, n.sul.N.img, s.leste.N.img, o.oeste.N.img, o.norte.N.img, l.sul.N.img, l.oeste.N.img
        labdest = n.norte.img, s.sul.img, o.leste.img, s.oeste.img, l.norte.img, o.sul.img, n.oeste.img
        return labnn, labdest

    def test_labirinto_mapa(self):
        """Labirinto em Mapa."""
        labnn, labdest = self._labirinto_mapa()
        sala_a, sala_b = j.s.salas, j.s.salan
        sala_a.norte.vai()
        assert j.i.cena == sala_a.norte, "cena inicial é %s e não %s" % (j.i.cena, sala_a.norte)
        sala_a.norte.N()
        assert j.i.cena == sala_b.norte, "cena atual é %s e não %s" % (j.i.cena.img, sala_b.norte.img)
        assert labnn == labdest, "%s != %s" % (labnn, labdest)

    def test_labirinto_mapa_bloqueado(self):
        """Labirinto em Mapa com Bloqueios."""
        labnn, labdest = self._labirinto_mapa()
        sala_a, sala_b = j.s.salas, j.s.salan
        sala_a.norte.vai()
        assert j.i.cena == sala_a.norte, "cena inicial é %s e não %s" % (j.i.cena, sala_a.norte)
        sala_a.norte.N.fecha()
        sala_a.norte.N()
        assert j.i.cena == sala_a.norte, "cena atual é %s e não %s" % (j.i.cena, sala_b.norte)
        assert labnn == labdest, "%s != %s" % (labnn, labdest)


class SalaScoreTest(unittest.TestCase):
    def setUp(self):
        self.uma = MagicMock()
        self.outra = MagicMock()
        self.send = ajax.send = MagicMock(name="send")
        self.ms = 1509734320018
        browser.window.Date.now.return_value = 1509734320018

    def _cria_cenas_sala(self):
        """Cenas e sala c criadas."""
        cenas = dict(cfre="_IMG_cfre", cesq="_IMG_cesq", cdir="_IMG_cdir", cfun="_IMG_cfun", cbau="_IMG_cbau")
        cenas = {nome: dict(img=sala, score=dict(ponto=2)) for nome, sala in cenas.items()}
        j.c.c(**cenas)
        j.c.s(j.c.cfre, self.uma, j.c.cfun, j.c.cdir)

    def test_decora_dialogo(self):
        """Cenas decorada com dialogo."""
        self._cria_cenas_sala()
        j.t.d(j.c.cfre, "UM", "DOIS")
        j.t.POP._open = a = MagicMock(name="Open dialog")
        j.c.cfre.vai(ev=TNoEv(x=555, y=666))
        assert j.t.POP.alt.text == "DOIS", j.t.POP.alt.text
        assert j.t.POP.tit.text == "UM", j.t.POP.tit.text
        a.assert_called_once_with()
        call_send = json.dumps({'doc_id': '00000000000000000000', 'carta': 'cfre', 'casa': (0, 0), 'move': (-100, -100),
                                'ponto': 2, 'valor': '__JOGO__', 'tempo': self.ms})
        self.send.assert_called_once_with(call_send)

    def test_decora_dialogo_classe(self):
        """Classe Cena decorada com dialogo."""

        @j.t
        class ComBau(Cena):
            elt = Cena()
            pass

        cc = ComBau(tit="UMA", txt="DUAS")
        j.t.POP._open = a = self.uma
        assert isinstance(cc, Cena), type(cc)
        cc.vai()
        assert j.t.POP.alt.text == "DUAS", j.t.POP.alt.text
        assert j.t.POP.tit.text == "UMA", j.t.POP.tit.text
        a.assert_called_once_with()

    def _cria_bau_alavanca(self):
        """Artigos  e bau e alavanca criadas."""
        self._cria_cenas_sala()
        j.a.c(bau=dict(img="_BAU_", vai=j.c.cfun.vai, score=dict(ponto=3), style=dict(left=100, top=200)),
              alavanca=dict(img="_ALAVANCA_", score=dict(ponto=4), style=dict(left=111, top=222)))
        j.c.cesq.bota(j.a.bau)
        j.c.cbau.bota(j.a.alavanca)
        j.a.bau.vai = j.c.cbau.vai

    def test_cria_bau_alavanca(self):
        """Artigos  e bau e alavanca criadas."""
        self._cria_cenas_sala()
        self._cria_bau_alavanca()
        assert j.a.bau.style["left"] == 100, 'j.a.bau.style["left"] = %d' % j.a.bau.style["left"]
        assert j.a.bau in j.c.cesq.dentro
        ev = TNoEv(555, 666)
        j.a.bau._click(ev)
        assert j.a.alavanca in j.c.cbau.dentro
        # assert j.i.cena is j.c.cbau, "cena é %s" % j.i.cena
        call_cbau = json.dumps({'doc_id': '00000000000000000000', 'carta': 'cbau', 'casa': (0, 0), 'move': (555, 666),
                                'ponto': 2, 'valor': "__JOGO__", 'tempo': self.ms})
        call_send = json.dumps(
            {'doc_id': '00000000000000000000', 'carta': '_ALAVANCA_', 'casa': [111, 222], 'move': [-111, -111],
             'ponto': 4, 'valor': "cbau", 'tempo': self.ms})
        call_bau = json.dumps(
            {'doc_id': '00000000000000000000', 'carta': '_BAU_', 'casa': (100, 200), 'move': [-111, -111],
             'ponto': 3, 'valor': "cesq", 'tempo': self.ms})
        calls = [call(call_bau), call(call_send), call(call_cbau)]
        self.send.assert_has_calls(calls)

    def test_bota_alavanca_inventario(self):
        """Alavanca no inventário."""
        self._cria_cenas_sala()
        self._cria_bau_alavanca()
        a = MagicMock(name="Enter Inventory")
        j.i.elt = a
        j.i.elt.__le__ = MagicMock(name="Enter Elt")
        j.i.bota(j.a.alavanca)
        assert j.a.alavanca in j.i.inventario, j.i.inventario
        call_send = json.dumps(
            {'doc_id': '00000000000000000000', 'carta': '_ALAVANCA_', 'casa': [111, 222], 'move': [-111, -111],
             'ponto': 4, 'valor': "__INVENTARIO__", 'tempo': self.ms})
        self.send.assert_called_with(call_send)

    def test_bota_bau_sala_dir(self):
        """Bota o Bau na Sala Direita."""
        self._cria_cenas_sala()
        self._cria_bau_alavanca()
        a = MagicMock(name="Enter Inventory")
        j.i.elt = a
        j.i.elt.__le__ = MagicMock(name="Enter Elt")
        j.a.bau.vai = lambda *_: j.c.cdir.bota(j.a.bau)
        j.a.bau._click(TNoEv(123, 456))
        assert j.a.bau in j.c.cdir.dentro, j.c.cdir.dentro
        call_send = json.dumps({'doc_id': '00000000000000000000', 'carta': '_ALAVANCA_', 'casa': [111, 222],
                                'move': [-111, -111], 'ponto': 4, 'valor': "cbau", 'tempo': self.ms})
        call_bau = json.dumps({'doc_id': '00000000000000000000', 'carta': '_BAU_', 'casa': (100, 200),
                               'move': (123, 456), 'ponto': 3, 'valor': "cdir", 'tempo': self.ms})
        call_bau_esq = json.dumps({'doc_id': '00000000000000000000', 'carta': '_BAU_', 'casa': (100, 200),
                                   'move': [-111, -111], 'ponto': 3, 'valor': "cesq", 'tempo': self.ms})
        calls = [call(call_bau_esq), call(call_send), call(call_bau)]
        self.send.assert_has_calls(calls)


def bmain(_=0):
    suite = unittest.TestLoader().loadTestsFromTestCase(CenaTest)
    unittest.TextTestRunner(verbosity=0).run(suite)
    '''
    import HTMLTestRunner
    runner = HTMLTestRunner.HTMLTestRunner(
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test
    runner.run(CenaTest)
    # from HTMLTestRunner import main
    # main(modul)
'''
if __name__ == "__main__":
    bmain()