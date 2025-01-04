person = {
     "first_name": "John",
     "last_name": "Doe",
     "age": 35,
     "spouse": "Jane",
     "children": ["Ralph", "Betty", "Bob"],
     "pets": {"dog": "Frieda", "cat": "Sox"},
}
print(person["pets"]["dog"])

squares = {}
for x in range(1,11):
    squares[x] = x**2
print(squares)

x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]

print(x[2]['bar']['z'])
