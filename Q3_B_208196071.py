# Function name: maxProfit(A)
# Input: the A list (n - the length of the A list)
# Output: the max difference from two elements -> What the question want's
def maxProfit(A):
    n = len(A)
    # we initialize for the start the max_diff for the first one that is possible
    max_diff = A[1] - A[0]
    # for - on every element in the list
    for i in range(n):
        # for to check the i element with all the followings in the list
        for j in range(i + 1, n):
            if A[j] - A[i] > max_diff:
                max_diff = A[j] - A[i]
    return max_diff


if __name__ == '__main__':
    A = [5, 2, 10]
    print(maxProfit(A))
    B = [7, 2, 4, 8, 7]
    print(maxProfit(B))
    C = [1, 2, 1, 2]
    print(maxProfit(C))
