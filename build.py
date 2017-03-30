# -*- coding: UTF8 -*-
from pybuilder.core import use_plugin, init, Author, task
import os
import sys
SRC = os.path.join(os.path.dirname(__file__), "src")
DOC = os.path.join(os.path.dirname(__file__), "docs")
sys.path.append(SRC)
from vitollino import __version__


use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.unittest")
# use_plugin("python.coverage")
use_plugin("python.distutils")
# use_plugin('pypi:pybuilder_header_plugin')
use_plugin("exec")

url = 'https://github.com/labase/vitollino'
description = "Please visit {url}".format(url=url)
authors = [Author('Carlo Oliveira', 'carlo@ufrj.br')]
license = 'GNU General Public License v2 (GPLv2)'
summary = "A project to teach primary and secondary students to program web games in Python."
version = __version__
default_task = ['analyze', 'publish', 'buid_docs']  # , 'post_docs']
# default_task = ['analyze']  # , 'post_docs']


@init
def initialize(project):
    project.set_property('distutils_classifiers', [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Bottle',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: Portuguese (Brazilian)',
        'Topic :: Education',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'])
    # header = open('header.py').read()
    project.set_property('dir_source_main_python', '.')
    project.set_property('dir_source_unittest_python', 'tests')
    # project.set_property('pybuilder_header_plugin_expected_header', header)
    project.set_property('pybuilder_header_plugin_break_build', True)


@task
def post_docs(project, logger):
    from subprocess import call
    result = call(['curl', '-X', 'POST', 'http://readthedocs.org/build/vitollino'])
    logger.info("Commit hook @ http://readthedocs.org/build/vitollino: %d" % result)


@task
def buid_docs(project, logger):
    from subprocess import check_output
    result = check_output(['make', '-C', DOC, 'html'])
    logger.info(result)

@task
def prepare_for_gae(project, logger):
    import shutil
    shutil.copy("src/client/__init__.py", "src")
    logger.info(" copy src/client/__init__.py to src")
