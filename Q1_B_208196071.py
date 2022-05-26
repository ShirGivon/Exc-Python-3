from itertools import permutations


def permute(A):
    # we will use the permutations from itertools
    # it's returning a list of string's - so like in Q1_A, we will return:
    return sorted([list(x) for x in list(permutations(A))])

