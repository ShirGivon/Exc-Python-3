import itertools

# Function name: maxProfit(A)
# Input: the A list (n - the length of the A list)
# Output: the max difference from two elements -> What the question want's
def maxProfit(A):
    max_profit = 0
    my_combinations = list(itertools.combinations(A, 4))
    for (x, y, z, w) in my_combinations:
        if (-x + y - z + w) > max_profit:
            max_profit = (-x + y - z + w)
    my_combinations = list(itertools.combinations(A, 2))
    for (x, y) in my_combinations:
        if (-x + y) > max_profit:
            max_profit = (-x + y)
    return max_profit


if __name__ == '__main__':
    A = [5, 2, 10]
    print(maxProfit(A))
    B = [7, 2, 4, 8, 7]
    print(maxProfit([7, 2, 4, 8, 7]))
    C = [1, 2, 1, 2]
    print(maxProfit(C))
