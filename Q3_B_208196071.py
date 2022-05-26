from itertools import combinations


# Function name: maxProfit(A)
# Input: the A list
# Output: the max income from two sales on the A list of stocks
def maxProfit(A):
    # initialize the helpers
    maxi = 0
    lst1 = list(combinations(A, 4))
    # find the max from the 4 combinations, (a,b),(c,d) ->
    # find the max difference between a -> b,  c -> d
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
