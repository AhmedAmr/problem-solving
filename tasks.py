import os
import sys
import inspect
from invoke import task

rootdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, rootdir)


@task
def req_compile(ctx):
    '''
    Compile Python requirements without upgrading.
    '''
    ctx.run('pip-compile requirements/requirements.in')


@task
def req_upgrade(ctx):
    '''
    Compile Python requirements with upgrading.
    '''
    ctx.run('pip3-compile -U requirements/requirements.in')


@task
def build(ctx):
    '''
    Install all dependencies.
    '''
    ctx.run('pip3 install -r requirements/requirements.txt')


@task
def rebuild(ctx):
    '''
    Compile and rebuild the environment dependencies
    '''
    ctx.run('inv req-compile && inv build')
