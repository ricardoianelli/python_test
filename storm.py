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

def get_names(facts):
    names = []
    for fact in facts:
        if not (fact[0] in names):
            names.append(fact[0])
    return names
          
def filter_by_entity(facts, entity):
    return [fact for fact in facts if fact[0] == entity]

def filter_by_attribute(facts, attribute):
    return [fact for fact in facts if fact[1] == attribute[0]]

def filter_by_active(facts):
    filtered_facts = []
    for fact in facts:
        if fact[3]:
            filtered_facts.append(fact)
        else:
            previousFact = (fact[0], fact[1], fact[2], True)
            if previousFact in filtered_facts:
                filtered_facts.remove(previousFact)
    return filtered_facts

def filter_facts(facts, schema):
    facts = filter_by_active(facts)
    names = get_names(facts)
    current_facts = []
    for entity in names:
        filtered_by_entity = filter_by_entity(facts, entity)
        fully_filtered = []
        for attr in schema:
            filtered_by_attr = filter_by_attribute(filtered_by_entity, attr)
            if attr[2] == 'one' and len(filtered_by_attr) > 0:
                filtered_by_attr = [filtered_by_attr[-1]]
            fully_filtered = fully_filtered + filtered_by_attr
            
        current_facts = current_facts + fully_filtered
    current_facts.sort()
    return current_facts

def get_current_facts(facts, schema):
    return filter_facts(facts, schema)
     
current_facts = get_current_facts(facts, schema)
