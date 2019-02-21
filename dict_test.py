from random import randint


x = {}

y =     {
    'name':'Surskit',
    'cp':161,
    'hp':491,
    'dust':8001
}
x['pet'] = [y]

# x.values() = y
print(type(x.values()))
print(x.values())
print(x.items())
print(x.keys())