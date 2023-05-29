import itertools

a = [1,2,3]
b = ['a','b']

p = list(itertools.permutations(a)) #μεταθέσεις όλων
#[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

p = list(itertools.combinations(a,2))
#[(1, 2), (1, 3), (2, 3)]

p = list(itertools.combinations_with_replacement(a,2))
#[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

p = list(itertools.product(a,b))
#[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
print(p)