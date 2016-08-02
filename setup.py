#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

from setuptools import setup, find_packages

packages = find_packages()

requires = []

setup(
    name='wepana',
    version='0.2.0',
    description='An analyzer for web page content powered by Python.',
    url='https://github.com/mofei2816/wepana',
    author='Mervin Zhang',
    author_email='mofei2816@gmail.com',
    packages=packages,
    install_requires=requires,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
