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
from unittest.mock import MagicMock
from webtest import TestApp
from lab.control.control import application
import lab.model.modelo as model
import lab.control.control as sv_ctl
import lab as labcc
from pathlib import Path
CLIENT = str(Path(labcc.HERE).parent)
sv_ctl.SRC_DIR = CLIENT
sv_ctl.P_N_O_D_E_D = "S_N_O_D_E_%03x"


class WebServerTest(unittest.TestCase):
    """
    Testa o servidor web principal.
    """
    def setUp(self):
        self.app = TestApp(application)
        self.db = model.DRECORD = MagicMock(name="DRECORD")
        self.gid = 10101
        self.db.append.return_value = self.gid
        self.db.save.return_value = self.gid
        self.pontos = {'doc_id': '00000000000000000000', 'carta': '_ALAVANCA_', 'casa': [111, 222],
                       'move': [-111, -111], 'ponto': 4, 'valor': "cbau"}  # , 'tempo': win.Date.now()}

    def tearDown(self):
        self.app = None

    def test_score_points(self):
        """envia um registro de pontos."""
        h = {'Content-type': 'application/json', 'Authorization': 'JWT eyJ0eX'}
        resp = self.app.post_json('/store', self.pontos, headers=h)  # log in and get a cookie
        assert resp.status == '200 OK'        # fetch a page successfully
        assert resp.content_type == 'text/html'
        assert resp.content_length > 0
        self.db.append.assert_called_once_with(self.pontos.pop('doc_id'), self.pontos)
        resp.mustcontain(str(self.gid))

    def test_register_user(self):
        """registra um usuário."""
        user = dict(doc_id=1, ano=1, user="eu", idade=2, sexo="masculino")
        resp = self.app.get('/register', user)  # log in and get a cookie

        assert resp.status == '200 OK'        # fetch a page successfully
        assert resp.content_type == 'text/html'
        assert resp.content_length > 0
        user.pop("doc_id")
        self.db.save.assert_called_once_with({k: str(u) for k, u in user.items()})
        resp.mustcontain('<div id="pydiv" class="center" title="">')
        resp.mustcontain('main(10101,"S_N_O_D_E_%03x")')

    def test_registro(self):
        """obtem a tela de registro."""
        resp = self.app.get('/')  # log in and get a cookie

        assert resp.status == '200 OK'        # fetch a page successfully
        assert resp.content_type == 'text/html'
        assert resp.content_length > 0
        resp.mustcontain('<html>')
        assert 'form' in resp

    def test_registro_again(self):
        """obtem a tela de registro de novo."""
        resp = self.app.get('/')  # log in and get a cookie

        assert resp.status == '200 OK'        # fetch a page successfully
        assert resp.content_type == 'text/html'
        assert resp.content_length > 0
        resp.mustcontain('<html>')
        assert 'form' in resp


if __name__ == '__main__':
    unittest.main()
