.. _Pybuilder: http://pybuilder.github.io/
.. _Google_Cloud: https://cloud.google.com/
.. _release1_0_0:

############################
Notas de Lançamento V. 1.0.0
############################

*Vitollino*

Milestone
=========


**Catioro** - Montagem do Ambiente de Jogo 🐱

    - [ ] `Aspecto #1`_: Navegação através de portais
    - [ ] `Aspecto #2`_: Construção de mapas de labirinto
    - [ ] `Aspecto #3`_: Adiciona música e sons
    - [ ] `Aspecto #4`_: Texto decorador
    - [ ] `Aspecto #5`_: Montagem interativa com cursor móvel
    - [ ] `Aspecto #6`_: Banco de dado Redis via Walrus

Aspectos do Lançamento
======================

Destaques dos Aspectos
**********************

Início da documentação do tutorial

Aspecto #1
**********

**Navegação através de portais** :ref:`🏠 <release1_0_0>`
    A navegação entre cenários se dá através de cursores indicativos que flutuam sobre o local do portal.


Aspecto #2
**********

**Construção de mapas de labirinto** :ref:`🏠 <release1_0_0>`
    Um labirinto pode ser construído montando uma matriz de duas dimensões.
    Cada célula da matriz irá se conectar coms seus vizinhos nos quatro pontos cardeais.


Aspecto #3
**********

**Adiciona música e sons** :ref:`🏠 <release1_0_0>`
    Uma música de fundo pode ser adicionada ao jogo.


Aspecto #4
**********

**Texto decorador** :ref:`🏠 <release1_0_0>`
    Um portal pode ser decorado com um popup de texto que aparece antes de transitar para outra cena.


Aspecto #5
**********

**Montagem interativa com cursor móvel** :ref:`🏠 <release1_0_0>`
    Para facilitar a montagem de cenários pode-se habilitar um cursor inteartivo que irá fornecer
    as coordenadas e o tamanho do hot spot que irá ativar a ação quando clicado.


Aspecto #6
**********

**Banco de dado Redis via Walrus** :ref:`🏠 <release1_0_0>`
    Um banco Redis foi adicionadoao servidor. Ele é interfaceado pelo adaptador python
    definido pelo pacote Walrus.


Melhoramentos
=============

Reúne Vitollino e Braser no mesmo repositório.

Melhoramento #1
***************

Tutorial vitollino sendo portado para Restrutured Text.

Consertos
=========

Nenhum conserto notável.

Questões e Problemas Conhecidos
===============================

A funcionalidade ainda é muito simples, requer melhorias.

Uma nova versão deve integrar melhor as duas modalidades de tutorial.

Lançamentos Anteriores e Posteriores
====================================

Próximo Lançamento: A ser definido :ref:`Lançamento 1.1.0 <release1_1_0>`

