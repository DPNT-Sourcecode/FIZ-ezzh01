# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:18:26 2019

@author: Ottavio
"""

def sum_(int_1, int_2):
    assert 0 <= int_1 <= 100, "int_1 should be between 0 and 100"
    assert 0 <= int_2 <= 100, "int_2 should be between 0 and 100"
    assert isinstance(int_1, int), "int_1 should be an integer"
    assert isinstance(int_2, int), "int_2 should be an integer"
    return int_1 + int_2