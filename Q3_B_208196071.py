from itertools import permutations


# Function name: maxProfit(A)
# Input: the A list (n - the length of the A list)
# Output: the max difference from two elements -> What the question want's
def maxProfit(A):
    maxi = 0
    a = list(permutations(A, 2))
    print(a)
    b = list(permutations(A, 4))
    print(b)
    for (x, y, z, w) in b:
        if -x + y - z + w > maxi:
            maxi = -x + y - z + w
    for (x, y) in a:
        if -x + y > maxi:
            maxi = -x + y
    return maxi


if __name__ == '__main__':
    A = [5, 2, 10]
    print(maxProfit(A))
    B = [7, 2, 4, 8, 7]
    print(maxProfit(B))
    C = [1, 2, 1, 2]
    print(maxProfit(C))
