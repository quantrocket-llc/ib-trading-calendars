#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import versioneer

setup(
    name='ib-trading-calendars',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Trading calendars for Interactive Brokers-supported exchanges',
    maintainer='QuantRocket LLC',
    maintainer_email='support@quantrocket.com',
    url='https://github.com/quantrocket-llc/ib-trading-calendars',
    license='Apache 2.0',
    packages=['ib_trading_calendars'],
    install_requires=[
        'trading_calendars>=1.7.0'
    ]
)
