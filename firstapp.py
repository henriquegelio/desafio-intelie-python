# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Considere um modelo de informação, onde um registro é representado por uma "tupla".
# Uma tupla (ou lista) nesse contexto é chamado de fato.

# Exemplo de um fato:
# ('joão', 'idade', 18, True)

# Nessa representação, a entidade (E) 'joão' tem o atributo (A) 'idade' com o valor (V) '18'.

# Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser 'False'
# para representar que a entidade não tem mais aquele valor associado aquele atributo.


# Como é comum em um modelo de entidades, os atributos de uma entidade pode ter cardinalidade 1 ou N (muitos).

# Segue um exemplo de fatos no formato de tuplas (i.e. E, A, V, added?)

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

# Vamos assumir que essa lista de fatos está ordenada dos mais antigos para os mais recentes.


# Nesse schema,
# o atributo 'telefone' tem cardinalidade 'muitos' (one-to-many), e 'endereço' é 'one-to-one'.
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]


# Nesse exemplo, os seguintes registros representam o histórico de endereços que joão já teve:
#  (
#   ('joão', 'endereço', 'rua alice, 10', True)
#   ('joão', 'endereço', 'rua bob, 88', True),
# )
# E o fato considerado vigente (ou ativo) é o último.


# O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades.
# Ou seja, quais são as informações que estão valendo no momento atual.
# A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.

def challenge(fatos, esquema):
    lista = list()
    for i in esquema:
        if i[0] == "endereço":
            endereco = i[2]
        elif i[0] == "telefone":
            telefone = i[2]

    for i in fatos:
        if i[1] == "endereço":
            if endereco == "many":
                if i[3]:
                    lista.append(i)
                else:
                    res = []
                    for j in lista:
                        if i[0] != j[0]:
                            res.append(j)
                        elif i[0] == j[0] and i[1] != j[1]:
                            res.append(j)
                        elif i[0] == j[0] and i[1] == j[1] and i[2] != j[2]:
                            res.append(j)
                    lista = res
            elif endereco == "one":
                if i[3]:
                    res = []
                    for j in lista:
                        if i[0] != j[0]:
                            res.append(j)
                        elif i[0] == j[0] and i[1] != j[1]:
                            res.append(j)
                    lista = res
                    lista.append(i)
                else:
                    lista = [j for j in lista if i[0] != j[0] or (i[0] == j[0] and i[1] != j[1])]
        elif i[1] == "telefone":
            if telefone == "many":
                if i[3]:
                    lista.append(i)
                else:
                    res = []
                    for j in lista:
                        if i[0] != j[0]:
                            res.append(j)
                        elif i[0] == j[0] and i[1] != j[1]:
                            res.append(j)
                        elif i[0] == j[0] and i[1] == j[1] and i[2] != j[2]:
                            res.append(j)
                    lista = res
            elif telefone == "one":
                if i[3]:
                    res = []
                    for j in lista:
                        if i[0] != j[0]:
                            res.append(j)
                        elif i[0] == j[0] and i[1] != j[1]:
                            res.append(j)
                    lista = res
                    lista.append(i)
                else:
                    lista = [j for j in lista if i[0] != j[0] or (i[0] == j[0] and i[1] != j[1])]
    return lista


resultado = challenge(facts, schema)
print(resultado)
