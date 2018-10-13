A = 1
connection= {
        A : ['B'],
        'B' : ['A', 'B', 'D'],
        'C' : ['A'],
        'D' : ['E','A'],
        'E' : ['B']
    }

for f in connection:
    print(connection['B'])
    print(connection[A])
