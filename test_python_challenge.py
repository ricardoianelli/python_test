# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:17:59 2019

@author: RICARDO
"""


import pytest
import python_challenge as pc

def test_expected_get_current_facts_1():
    expected = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('gabriel', 'telefone', '56789-1010', True),  
        ('gabriel', 'telefone', '98888-1111', True), 
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
    ]
    actual = pc.get_current_facts(pc.facts, pc.schema)
    message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
    # Complete the assert statement
    assert actual == expected, message
  
def test_expected_get_current_facts_2():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
        ('gabriel', 'endereço', 'av rio branco, 109', False),
    ]
    
    expected = [
        ('gabriel', 'telefone', '56789-1010', True),  
        ('gabriel', 'telefone', '98888-1111', True), 
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
    ]
    actual = pc.get_current_facts(facts, pc.schema)
    message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
    # Complete the assert statement
    assert actual == expected, message
  
def test_expected_get_current_facts_3():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
        ('gabriel', 'telefone', '56789-1010', False),
        ('gabriel', 'endereço', 'av rio branco, 109', False),
        ('gabriel', 'endereço', 'av rio branco, 109', True),
    ]
    
    expected = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('gabriel', 'telefone', '98888-1111', True), 
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
    ]
    actual = pc.get_current_facts(facts, pc.schema)
    message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
    # Complete the assert statement
    assert actual == expected, message
  
def test_get_current_facts_format_1():
    facts = [
        ('gabriel', 'av rio branco, 109', True),
        ('gabriel', 'telefone', '56789-1010', True),  
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
    ]
    with pytest.raises(IndexError):
        pc.get_current_facts(facts, pc.schema)
      
def test_get_current_facts_format_2():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('gabriel', 'telefone', '56789-1010'),  
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
    ]
    with pytest.raises(IndexError):
        pc.get_current_facts(facts, pc.schema)
      
def test_get_current_facts_format_3():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('gabriel', 'telefone', '56789-1010', True),  
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', True),
    ]
    with pytest.raises(IndexError):
        pc.get_current_facts(facts, pc.schema)
      
def test_get_current_facts_format_4():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('gabriel', 'telefone', '56789-1010', True),  
        ('joão', 'endereço', 'rua bob, 88', True),
        ('telefone', '234-5678', True),
    ]
    with pytest.raises(IndexError):
        pc.get_current_facts(facts, pc.schema)
  