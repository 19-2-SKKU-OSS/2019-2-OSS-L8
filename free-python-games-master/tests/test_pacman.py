import random
import runpy
import sys

import mockturtle

sys.modules['turtle'] = sys.modules['mockturtle']


def test_pacman():
    random.seed(0)
    mockturtle.events[:] = (
        [('timer', True), ('key Up',)] * 600
        + [('timer', True)] * 3000
    )
    runpy.run_module('freegames.pacman')
