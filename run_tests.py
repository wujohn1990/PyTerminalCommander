# -*- coding: utf-8 -*-

import sys
import unittest

import PyTerminalCommander.tests.super_move

res = unittest.TextTestRunner().run(PyTerminalCommander.tests.Tests)
sys.exit(len(res.failures))
