#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
from setuptools import setup

packages = [
    'analyzer'
]

requires = []

setup(
    name='html-analyzer',
    version='0.1.0',
    description='A HTML analyzer for Python 3',
    url='https://github.com/mofei2816/html-analyzer',
    author='Mervin',
    author_email='mofei2816@gmail.com',
    packages=packages,
    install_requires=requires,
    license='MIT'
)
