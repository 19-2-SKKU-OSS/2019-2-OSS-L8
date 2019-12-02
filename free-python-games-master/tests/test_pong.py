import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_pong_1():
    random.seed(0)
    mockturtle.events[:] = (
        [('timer',), ('key s',)] * 8
        + [('timer', True)] * 600
    )
    runpy.run_module('freegames.pong')

def test_pong_2():
    random.seed(1)
    mockturtle.events[:] = (
        [('timer',), ('key k',)] * 12
        + [('timer', True)] * 600
    )
    runpy.run_module('freegames.pong')
