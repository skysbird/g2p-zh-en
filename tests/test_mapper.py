#!/usr/bin/env python

"""Tests for `g2p_zh_en` package."""


import unittest
import logging

from g2p_zh_en.mapper import EnMapper,PinyinMapper
from pypinyin import pinyin, lazy_pinyin, Style
from g2p_en import G2p
g2p = G2p()

logging.basicConfig(level=logging.DEBUG)


class TestG2p_zh_en(unittest.TestCase):
    """Tests for `g2p_zh_en` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.pinyin_mapper = PinyinMapper()
        self.en_mapper = EnMapper()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_pinyin(self):
        """Test something."""
        pout = lazy_pinyin('这个页面使用javascript和PHP语言开发而成', style=Style.TONE3, neutral_tone_with_five=True)
        out = self.pinyin_mapper.convert(pout)
        print(out)

    def test_001_eng(self):
        """Test something."""
        pout = g2p('this page is developed by Javascript and PHP')
        out = self.en_mapper.convert(pout)
        print(out)
        
if __name__ == '__main__':
    unittest.main()