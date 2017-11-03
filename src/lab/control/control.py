#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Vitollino
# Copyright 2014-2017 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://j.mp/GNU_GPL3>`__.
#
# Vitollino é um software livre; você pode redistribuí-lo e/ou
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

"""Main controller with bottle.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
# from bottle import default_app, route, view, get, post, static_file, request, redirect, run, TEMPLATE_PATH
from random import randint

from bottle import default_app, view, get, post, request, static_file, run
import logging as log
import lab.model.modelo as database
P_N_O_D_E_D = "S_N_O_D_E_%03x" % randint(0x111, 0xfff) + "-%02d"
LAST = 0
SRC_DIR = ""


def retrieve_params(req):
    # print ('retrieve_params', req)
    log.debug("retrieve_params %s", str(req))
    doc_id = req.pop('doc_id')
    data = {k: req[k] for k in req}
    log.debug("param data %s", str(data))
    return {doc_id: data}


@get('/')
@view('index')
def register_screen():
    """Return a peer id to identify the user.

    :return: page with Brython client.
    """
    global LAST
    # LAST += 1
    gid = "-".join(["P_N_O_D_E", "%02d" % LAST])
    # print('game register', gid)
    log.debug('game register %s', gid)
    return dict(nodekey=P_N_O_D_E_D, lastid=LAST)


@get('/register')
@view('game')
def register_user():
    """Return a peer id to identify the user.

    :return: page with Brython client.
    """
    global LAST
    jsondata = retrieve_params(request.params)
    jsondata = list(jsondata.values())[0]
    gid = "010101"  # database.DRECORD.save(jsondata)
    log.debug('/record/register %s', str(jsondata))
    LAST = gid
    return dict(doc_id=gid, nodekey=P_N_O_D_E_D, lastid=LAST)


@post('/store')
def store():
    try:
        jsondata = retrieve_params(request.params)
        record_id = list(jsondata.keys())[0]
        score = jsondata[record_id]
        record = database.DRECORD.append(record_id, score)
        log.debug('/store: %s -> %s', record_id, score)
        return record
    except Exception:
        return "Movimento de peça não foi gravado %s" % str(request.params.values())


@get('/<filename:re:.*\.py>')
def code(filename):
    """Serves python static files.

    :param filename: python module name.
    :return: contents of the file.
    """
    log.debug('code request :/<filename/%s>', SRC_DIR + "/" + filename)
    return static_file(filename, root=SRC_DIR)


def main(direc=""):
    """Run Bottle Server

    :return: None.
    """
    global SRC_DIR
    SRC_DIR = direc
    run(host='localhost', port=8080)


application = default_app()

if __name__ == "__main__":
    main()
