#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""

import pytest
import S1_aglotools as algo

def test_averrage_above_zero():
        assert algo.average_above_zero(algo.array) == 6.125

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0