# Function name: maxProfit(A)
# Input: the A list (n - the length of the A list)
# Output: the question -> answer it
def maxProfit(A):
    n = len(A)
    sum_of_diff = 0
    for i in range(1, n):
        if A[i] > A[i - 1]:
            sum_of_diff += A[i] - A[i - 1]
    return sum_of_diff


if __name__ == '__main__':
    A = [1, 2, 3]
    print(maxProfit(A))
    B = [1, 2, 1, 2]
    print(maxProfit(B))
    C = [1, 3, 2, 5, 3, 7]
    print(maxProfit(C))
    price = [100, 180, 260, 310, 40, 535, 695]
    profit = maxProfit(price)
    print(profit)
    print(maxProfit([3, 2, 1]))
