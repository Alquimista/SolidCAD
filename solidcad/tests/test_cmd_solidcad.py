#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

from solidcad.cmd_solidcad import main

class TestConsole(TestCase):
    def test_basic(self):
        main()
