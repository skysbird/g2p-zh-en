#!/usr/bin/env python

"""Tests for `g2p_zh_en` package."""


import unittest
import logging
from g2p_zh_en.g2p_zh_en import G2P

logging.basicConfig(level=logging.DEBUG)

class TestG2p_zh_en(unittest.TestCase):
    """Tests for `g2p_zh_en` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.g2p = G2P()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def atest_000_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "测试，我喜欢在家看NBA")
        print(out)

    def test_001_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "Hello this is测试 a test page.")
        print(out)

    def atest_002_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "这个页面使用")
        print(out)

    def atest_003_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "北京奥运会是在2008年8月8日举办的")
        print(out)

    def atest_004_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "伦敦奥运会是在2008年8月8日举办的,花了将近150060元")
        print(out)

    def atest_005_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "测试一个美元符号的情况$100元")
        print(out)


    def atest_100_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "hello,this is an english test! 混合一点中文$☺️ test",language='en-us')
        print(out)

    def atest_200_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "混合一点中文")
        print(out)

    def test_300_something(self):
        """Test something."""
        out = self.g2p.g2p(text = "hello,this is a test Javascript!!",language='en-us')
        print(out)

if __name__ == '__main__':
    unittest.main()
