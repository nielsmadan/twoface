import unittest
from nose.tools import eq_

import vim_stub
import venom_stub

import twoface

class TestGreeting(unittest.TestCase):
    def test_get_greeting(self):
        result = twoface.greetings._get_greeting()

        eq_(result, "Hello World")
