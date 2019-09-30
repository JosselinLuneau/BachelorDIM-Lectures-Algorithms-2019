#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""

import pytest
import S1_aglotools as algo

# Exercice 1
def test_averrage_above_zero():
        assert algo.average_above_zero(algo.array) == 6.125

# Errors
def test_averrage_valueError_list():
        with pytest.raises(ValueError):
                algo.average_above_zero(8)

def test_averrage_valueError_empty_list():
        with pytest.raises(ValueError):
                algo.average_above_zero([])

def test_averrage_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        algo.average_above_zero([0,0,0,0])

def test_averrage_negative_array_values():
        with pytest.raises(ZeroDivisionError):
                algo.average_above_zero([-2,-3,-8,-7])

def test_averrage_char_list():
        with pytest.raises(ValueError):
                algo.average_above_zero(['1', 'e'])

# Exercice 2
def test_max_value():
        assert algo.max_value(algo.array) == (10, 8)

# Errors
def test_max_value_valueError_list():
        with pytest.raises(ValueError):
                algo.max_value(8)

def test_max_value_valueError_empty_list():
        with pytest.raises(ValueError):
                algo.max_value([])

def test_max_value_char_list():
        with pytest.raises(ValueError):
                algo.max_value(['1', 'e'])