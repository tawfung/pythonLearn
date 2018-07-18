#!/usr/bin/python3

my_stuff = {"key1": "value", 'key2': 'value22',
            'key3': {'123': [1, 2, "T_Race"]}}

print(my_stuff["key3"]['123'][2].upper())


x = set()
x.add(1)
x.add(2)
print(x)
