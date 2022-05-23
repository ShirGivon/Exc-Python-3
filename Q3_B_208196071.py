from itertools import combinations


# Function name: maxProfit(A)
# Input: the A list
# Output: the max difference from two elements -> two sales
def maxProfit(A):
    # initialize
    maxi = 0
    lst1 = list(combinations(A, 4))
    # find the max from the 4 combinations, (a,b),(c,d) ->
    # find the max difference between a -> b, c->d
    for (a, b, c, d) in lst1:
        if - c + d - a + b > maxi:
            maxi = -a + b - c + d
    # find the max from the 2 combinations
    # find the max difference between a -> b, the check if there is only one (no (c,d))
    lst2 = list(combinations(A, 2))
    for (a, b) in lst2:
        if -a + b > maxi:
            maxi = -a + b
    return maxi


if __name__ == '__main__':
    A = [5, 2, 10]
    print(maxProfit(A))
    B = [7, 2, 4, 8, 7]
    print(maxProfit([7, 2, 4, 8, 7]))
    C = [1, 2, 1, 2]
    print(maxProfit(C))
