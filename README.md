[![Build Status](https://travis-ci.org/ricardoianelli/python_test.svg?branch=master)](https://travis-ci.org/ricardoianelli/python_test)

## Guia de uso

Para instalar dependências:
> pip3 install -r requirements.txt

Para executar o código:
> python3 python_challenge.py

Para executar os testes:
> python3 test_python_challenge.py

# O desafio:

Considere um modelo de informação, onde um registro é representado por uma "tupla".
Uma tupla (ou lista) nesse contexto é chamado de fato.

## Exemplo de um fato:
('joão', 'idade', 18, True)

Nessa representação, a entidade (E) 'joão' tem o atributo (A) 'idade' com o valor (V) '18'.

Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser 'False' para representar que a entidade não tem mais aquele valor associado aquele atributo.

Como é comum em um modelo de entidades, os atributos de uma entidade pode ter cardinalidade 1 ou N (muitos).

### Segue um exemplo de fatos no formato de tuplas (i.e. E, A, V, added?)
  ```python
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
```

Vamos assumir que essa lista de fatos está ordenada dos mais antigos para os mais recentes. 
Nesse schema, o atributo 'telefone' tem cardinalidade 'muitos' (one-tomany), e 'endereço' é 'one-to-one'.

```python
schema = [  
  ('endereço', 'cardinality', 'one'),  
  ('telefone', 'cardinality', 'many')    
]
```
Nesse exemplo, os seguintes registros representam o histórico de endereços que joão já teve:

```python
(  
  ('joão', 'endereço', 'rua alice, 10', True)  
  ('joão', 'endereço', 'rua bob, 88', True),  
)
```
E o fato considerado vigente (ou ativo) é o último.

O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades.  
Ou seja, quais são as informações que estão valendo no momento atual.  
A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.  

### Resultado esperado para este exemplo (mas não precisa ser nessa ordem):
```python
[  
  ('gabriel', 'endereço', 'av rio branco, 109', True),  
  ('joão', 'endereço', 'rua bob, 88', True),  
  ('joão', 'telefone', '91234-5555', True),  
  ('gabriel', 'telefone', '98888-1111', True),  
  ('gabriel', 'telefone', '56789-1010', True)  
]
```
