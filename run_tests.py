#!/usr/bin/env python

import os

for f in os.listdir('./benchmark'):
    if f.endswith('.py'):
        test_name = f[:-3]
        print('Running test : ', test_name.upper())
        os.system('python -m benchmark.' + test_name)
