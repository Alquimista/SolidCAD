#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

import solidcad

class TestCube(TestCase):
    def test_is_solid_object(self):
        obj = solidcad.Cube()
        self.assertTrue(isinstance(obj,solidcad.solid.Solid))