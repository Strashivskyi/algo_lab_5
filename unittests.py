import unittest
from kmp import kmp_search_substring


class TestDFA(unittest.TestCase):

    def test1(self):
        self.assertEqual(['[9-12]'], kmp_search_substring('efes', 'rfgdgekesefes'))

    def test2(self):
        self.assertEqual([], kmp_search_substring("efes", "rfgdgekesfes"))

    def test3(self):
        self.assertEqual(['[9-12]', '[15-18]'], kmp_search_substring("efes", "rfgdgekesefesddefes"))

    def test4(self):
        self.assertEqual(['[21-24]'],
                         kmp_search_substring("eker",
                                              "rfgdgekesefesekedredseker dsdsa"))

    def test5(self):
        self.assertEqual(['[0-3]'], kmp_search_substring("efes", "efes"))

    def test6(self):
        self.assertEqual(['[0-3]', '[2-5]'],
                         kmp_search_substring("efef",
                                              "efefefesefes"))


if __name__ == '__main__':
    unittest.main()
