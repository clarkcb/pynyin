# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pynyin import Pynyin


class PynyinTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.pynyin = Pynyin()

    def test_yixia(self):
        yixia = 'yīxià'
        assert(self.pynyin.get_tone(yixia) == 1)
        assert(self.pynyin.get_tone(yixia[2:]) == 4)
        assert(self.pynyin.remove_tones(yixia) == 'yixia')
        assert(self.pynyin.to_ascii(yixia) == 'yixia')

    def test_shanghai(self):
        shanghai = 'shànghǎi'
        assert(self.pynyin.get_tone(shanghai) == 4)
        assert(self.pynyin.get_tone(shanghai[5:]) == 3)
        assert(self.pynyin.remove_tones(shanghai) == 'shanghai')
        assert(self.pynyin.to_ascii(shanghai) == 'shanghai')

    def test_lucha(self):
        lucha = 'lǚchá'
        assert(self.pynyin.get_tone(lucha) == 3)
        assert(self.pynyin.get_tone(lucha[2:]) == 2)
        assert(self.pynyin.remove_tones(lucha) == 'lücha')
        assert(self.pynyin.to_ascii(lucha) == 'lucha')


if __name__ == '__main__':
    unittest.main()
