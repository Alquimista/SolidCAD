#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase


import solidcad


class TestCube(TestCase):
    def test_is_solid_object(self):
        self.assertIsInstance(solidcad.Cube(), solidcad.solid.Solid)

    def test_defaults(self):
        self.assertEqual(
            str(solidcad.Cube()),
            "cube(size=[1,1,1], center=false);")

    def test(self):
        self.assertEqual(
            str(solidcad.Cube(18, True)),
            "cube(size=[18,18,18], center=true);")
        self.assertEqual(
            str(solidcad.Cube(18, True)),
            str(solidcad.Cube(size=18, center=True)))
        self.assertEqual(
            str(solidcad.Cube(18, True)),
            str(solidcad.Cube(18, center=True)))
        self.assertEqual(
            str(solidcad.Cube(18, True)),
            str(solidcad.Cube(center=True, size=18)))
        self.assertEqual(
            str(solidcad.Cube(18, True)),
            str(solidcad.Cube(center=True, size=[18, 18, 18])))
        self.assertNotEqual(
            str(solidcad.Cube(18, True)),
            str(solidcad.Cube(center=True, size=[18, 15, 18])))

    def test_valuer(self):
        c = solidcad.Cube()
        c.size = [25, 12, 15]
        self.assertEqual(str(c), "cube(size=[25,12,15], center=false);")


class TestSphere(TestCase):
    def test_is_solid_object(self):
        self.assertIsInstance(solidcad.Sphere(), solidcad.solid.Solid)

    def test_defaults(self):
        self.assertEqual(
            str(solidcad.Sphere()),
            "sphere($fn=0, $fa=12, $fs=2, d=2);")

    def test(self):
        self.assertEqual(
            str(solidcad.Sphere(8)),
            "sphere($fn=0, $fa=12, $fs=2, d=8);")
        self.assertEqual(
            str(solidcad.Sphere(8)),
            str(solidcad.Sphere(d=8)))
        self.assertEqual(
            str(solidcad.Sphere(8, fa=15)),
            str(solidcad.Sphere(d=8, fa=15)))
