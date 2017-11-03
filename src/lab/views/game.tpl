<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!--
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

"""

-->
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <title>Superpython : Jogo do Detetive</title>
        <link rel="stylesheet" href="/style.css" type="text/css" />
        <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
        <link rel="shortcut icon" href="/images/favicon.ico" type="image/x-icon" />

        <link rel="stylesheet" href="http://esironal.github.io/cmtouch/lib/codemirror.css">
        <link rel="stylesheet" href="http://esironal.github.io/cmtouch/addon/hint/show-hint.css">
        <script src="http://esironal.github.io/cmtouch/lib/codemirror.js" type="text/javascript"></script>
        <script src="http://esironal.github.io/cmtouch/addon/hint/show-hint.js" type="text/javascript"></script>
        <script src="http://esironal.github.io/cmtouch/addon/hint/python-hint.js" type="text/javascript"></script>
        <script src="http://esironal.github.io/cmtouch/mode/python/python.js" type="text/javascript"></script>
        <script src="http://esironal.github.io/cmtouch/addon/selection/active-line.js" type="text/javascript"></script>
        <script src="http://esironal.github.io/cmtouch/addon/edit/matchbrackets.js" type="text/javascript"></script>

        <link rel="stylesheet" href="http://esironal.github.io/cmtouch/theme/neonsyntax.css">
        <link rel="stylesheet" href="http://esironal.github.io/cmtouch/theme/solarized.css">

        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/phaser/2.4.7/phaser.min.js"></script>
        <script type="text/javascript" src="https://cdn.rawgit.com/brython-dev/brython/3.3.4/www/src/brython.js"></script>

        <script type="text/python">
            from lab.views.main import main
            main({{lastid}},"{{ nodekey }}")
        </script>
        <style type="text/css">
            .center {
               width: 1000px;
               height: 800px;
               position: absolute;
               left: 50%;
               top: 50%;
               margin-left: -500px;
               margin-top: -400px;
            }
            .ncenter {
              display: table-cell;
              vertical-align: middle;
            }
        </style>
    </head>
    <body onLoad="brython({debug:1, cache:'browser', static_stdlib_import:true})" bgcolor= darkslategray>
           <div id="pydiv" class="center" title="">
                <span style="color:white">LOADING..</span>
           </div>
    </body>
</html>