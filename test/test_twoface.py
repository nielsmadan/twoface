import unittest
from nose.tools import eq_

import vim_stub
import venom_stub

import twoface

class TestPossibleFiles(unittest.TestCase):
    def test_find_possible_files(self):
        result = twoface.main.find_possible_files("./testfiles/foo.h")

        eq_(len(result), 2)
        eq_(result[0], "./testfiles/foo.c")
        eq_(result[1], "./testfiles/foo.cpp")


class TestOpenFile(unittest.TestCase):
    def setUp(self):
        self.open_file_called = []

        def __open_file_monitor(fpath):
            self.open_file_called.append(fpath)

        def __get_current_file_path():
            return './testfiles/foo.h'

        import venom
        venom.open_file = __open_file_monitor
        venom.get_current_file_path = __get_current_file_path

    def tearDown(self):
        self.open_file_called = []

    def test_open_file(self):
        result = twoface.toggle_file()

        eq_(len(self.open_file_called), 1)
        eq_(self.open_file_called[0], './testfiles/foo.cpp')
