# Function name: maxProfit(A)
# Input: the A list (n - the length of the A list)
# Output: the max income from unlimited sales on the A list of stocks
def maxProfit(A):
    n = len(A)
    sum_of_diff = 0
    for i in range(1, n):
        # we want to find the ups and down's of the stocks
        # when it goes up or down we will sum the diff
        if A[i] > A[i - 1]:
            sum_of_diff += A[i] - A[i - 1]
    return sum_of_diff
