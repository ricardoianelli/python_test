# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:06:36 2019

@author: RICARDO
"""

from datetime import datetime

# Define base data
facts = [
    ('gabriel', 'endereço', 'av rio branco, 109', True),
    ('joão', 'endereço', 'rua alice, 10', True),
    ('joão', 'endereço', 'rua bob, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('joão', 'telefone', '234-5678', False),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
]

# Define data cardinality
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many'),
]

def dict_to_facts(dic):
    fact_list = []
    for entity, fact in dic.items():
        for attribute, values in fact.items():
            for value in values:
                fact_list.append((entity, attribute, value, True))
    return fact_list
    
def get_current_facts(facts, schema):
    many_cardionality = {attr[0]: (attr[2] == 'many') for attr in schema}
    clean_facts = {}
    
    for fact in facts:
        entity = clean_facts.get(fact[0], {})
        attr = entity.get(fact[1], [])
        if fact[3]:
            if not many_cardionality[fact[1]] and len(attr) > 0:
                attr[0] = fact[2]
            else:
                attr.append(fact[2])
        else:
            attr.remove(fact[2])
                
        entity[fact[1]] = attr
        clean_facts[fact[0]] = entity
    
    clean_facts = dict_to_facts(clean_facts)
    clean_facts.sort()
    return clean_facts
     
if __name__ == '__main__':
    print('Starting....')
    print('Date: %s' % datetime.now())
    current_facts = get_current_facts(facts, schema)
    print(current_facts)
    print('Finished.')
