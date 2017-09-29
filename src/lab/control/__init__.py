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

"""Handle http requests.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

# make sure the default templates directory is known to Bottle
templates_dir = os.path.join(project_home, 'views/')
if templates_dir not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, templates_dir)

"""
import os
import sys
import logging as log
from bottle import TEMPLATE_PATH

from lab import HERE

LOG_LEVEL = int(os.getenv("LABASELOG", log.ERROR))

log.basicConfig(level=LOG_LEVEL)
project_home = HERE  # os.path.join(here, "src/")
if project_home not in sys.path:
    sys.path = [project_home] + sys.path
templates_dir = os.path.join(project_home, 'views/')
if templates_dir not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, templates_dir)
