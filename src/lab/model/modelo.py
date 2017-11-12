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

"""Main database with redis.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
__author__ = 'carlo'
from uuid import uuid4
import os
# import redis
from walrus import DateTimeField, IntegerField, TextField, Database, Model, ListField, json, datetime
import logging as log

redis_url = os.getenv('REDISTOGO_URL', 'localhost')

db = Database(host=redis_url, port=6379, db=0)  # ,  decode_responses=True)


class User(Model):
    __database__ = db
    user_id = TextField(primary_key=True)
    nome = TextField(index=True, default=u"__NONE__")
    escola = TextField(index=True, default=u"__NONE__")
    genero = TextField(index=True, default=u"__NONE__")
    serie = IntegerField(index=True, default=0)
    idade = IntegerField(index=True, default=0)
    score = ListField(as_json=True)
    data = DateTimeField(default=datetime.datetime(1, 2, 1, 0, 0, 0, 0))


class Score(Model):
    __database__ = db
    casa = TextField(index=True)
    carta = TextField(index=True)
    ponto = TextField(index=True)
    move = TextField(index=True)
    valor = IntegerField(index=True)
    data = DateTimeField()


class Banco:
    def __init__(self):

        # self.banco = redis.from_url(redis_url,  decode_responses=True)
        self.banco = User

    def __setitem__(self, key, **value):
        self.banco.create(user_id=key, **value)

    def __getitem__(self, key):
        banco = self.banco.load(key)
        '''
        class Redis:
            def __init__(self, redis_):
                self._redis = redis_

            @staticmethod
            def append(data):
                banco.rpush(key, data)

            def __eq__(self, other):
                return self._redis == other

            @property
            def value(self):
                return self._redis

            @staticmethod
            def all():
                return banco.lrange(key, 0, -1)

        '''
        return banco  # Redis(self.banco.lrange(key, 0, -1))

    def delete(self, *args):
        for rec in args:
            self.banco.load(rec).delete()

    def create(self, **value):
        key = str(uuid4())
        self.banco.create(user_id=key, **value)
        return key

    def save(self):
        self.banco.save()

    def append(self, key, value):
        user = self.banco.load(key)
        user.score.append(json.dumps(value))
        return key

    def retrieve(self, key):
        user = self.banco.load(key)
        log.debug('/database/retrieve %s', str(user.__dict__))
        values = {key: getattr(user, key) for key in "nome escola genero serie idade data".split()}
        values["score"] = [json.loads(item.decode("utf-8")) for item in user.score[:]]
        return values


import unittest


class BancoTest(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()

    def test_esquerda(self):
        """Cena esquerda vai é chamado."""
        zval = {'nome': 'eur', 'escola': 'ela', 'genero': 'masculino', 'serie': 9, 'idade': 15,
                'data': datetime.datetime(2017, 11, 2, 0, 0),
                'score': [{'carta': 0, 'move': [1, 2]}, {'carta': 3, 'move': [3, 9]}]}
        #  self.banco.delete(1, 2)
        b = self.banco
        a = b.create(nome="eu")
        b[a].idade = 2
        b[a].save()
        assert b[a].nome == "eu", "falhou em recuperar b[a]: %s" % str(b[a].nome)
        z = b.create(nome="eur", escola="ela", idade=15, serie=9, genero="masculino", data=datetime.datetime(2017, 11, 2))
        assert b[z].escola == "ela", "falhou em recuperar b[a]: %s" % str(b[z].escola)
        assert b[z].idade == 15, "falhou em recuperar b[1]: %s" % str(b[z].idade)
        b.append(z, dict(carta=0, move=(1, 2)))
        b.append(z, dict(carta=3, move=(3, 9)))
        assert b.retrieve(z) == zval, "falhou em recuperar b[c]: %s" % str(b.retrieve(z))
        self.banco.delete(a, z)


if __name__ == "__main__":
    unittest.main()
else:
    DRECORD = Banco()
