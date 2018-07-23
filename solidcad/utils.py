#!/usr/bin/env python
# -*- coding=utf-8 -*-


def check_number_error(num):
    if not isinstance(num, (int, float)):
        raise AssertionError(
            'type {:s} is not numeric value'.format(type(num)))

def check_bool_error(b):
    if not isinstance(b, bool):
        raise AssertionError(
            'type {:s} is not True/False'.format(type(b)))