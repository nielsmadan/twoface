import unittest
from nose.tools import eq_

import vim_stub
import venom_stub

OPEN_FILE_CALLS = []

def __open_file_monitor(fpath):
    OPEN_FILE_CALLS.append(fpath)

def __get_current_file_path():
    return './testfiles/foo.h'

import venom
venom.open_file = __open_file_monitor
venom.get_current_file_path = __get_current_file_path

import twoface

class TestPossibleFiles(unittest.TestCase):
    def test_find_possible_files(self):
        result = twoface.main.find_possible_files("./testfiles/foo.h")

        eq_(len(result), 2)
        eq_(result[0], "./testfiles/foo.c")
        eq_(result[1], "./testfiles/foo.cpp")


class TestExistingFiles(unittest.TestCase):
    def test_find_possible_files_all_exist(self):
        result = twoface.main.filter_existing_files( ["./testfiles/foo.h", "./testfiles/foo.cpp"])

        eq_(len(result), 2)
        eq_(result[0], "./testfiles/foo.h")
        eq_(result[1], "./testfiles/foo.cpp")

    def test_find_possible_files_some_exist(self):
        result = twoface.main.filter_existing_files( ["./testfiles/foo.hpp", "./testfiles/foo.cpp"])

        eq_(len(result), 1)
        eq_(result[0], "./testfiles/foo.cpp")

    def test_find_possible_files_none_exist(self):
        result = twoface.main.filter_existing_files( ["./testfiles/foo.hpp", "./testfiles/foo.c"])

        eq_(len(result), 0)


class TestOpenFile(unittest.TestCase):
    def setUp(self):
        global OPEN_FILE_CALLS
        OPEN_FILE_CALLS = []

    def tearDown(self):
        global OPEN_FILE_CALLS
        OPEN_FILE_CALLS = []

    def test_open_file(self):
        result = twoface.toggle_file()

        eq_(len(OPEN_FILE_CALLS), 1)
        eq_(OPEN_FILE_CALLS[0], './testfiles/foo.cpp')
