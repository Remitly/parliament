import unittest
from nose.tools import raises, assert_equal, assert_true, assert_false

# import parliament
from parliament.misc import make_simple_list


class TestMakeList(unittest.TestCase):
    def test_make_list_list(self):
        original = [1,2,3]
        new = make_simple_list(original)
        assert_equal(original, new)

    def test_make_simple_list_single_element_list(self):
        original = [3]
        new = make_simple_list(original)
        assert_equal(original, new)

    def test_make_simple_list_empty_list(self):
        original = []
        new = make_simple_list(original)
        assert_equal(original, new)

    def test_make_simple_list_non_list(self):
        original = 1
        new = make_simple_list(original)
        assert_equal([1], new)
