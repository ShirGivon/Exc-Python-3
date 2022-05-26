# Function name: dyn_calculate(A, i, j, N) - recursive function
# Input: the matrix A, the row we in - i, the column we in j, N the size of A
# Output: the max sum - without the A[0][0]
def dyn_calculate(A, i, j, N):
    # base case - we are in the last row
    if i + 1 == N:
        return 0
    # if down is bigger
    if A[i + 1][j] > A[i + 1][j + 1]:
        num = A[i + 1][j]
        return num + dyn_calculate(A, i + 1, j, N)
    # if down & right is bigger
    if A[i + 1][j] < A[i + 1][j + 1]:
        num = A[i + 1][j + 1]
        return num + dyn_calculate(A, i + 1, j + 1, N)
    # if down is equals to down & right
    if A[i+1][j] == A[i+1][j+1]:
        # we will some every possible way from this 2 - down the matrix
        num1 = A[i + 1][j] + dyn_calculate(A, i+1, j, N)
        num2 = A[i + 1][j + 1] + dyn_calculate(A, i + 1, j + 1, N)
        # we will return the max from them
        return max(num1, num2)


# Function name: solve(A)
# Input: the matrix A
# Output: uses the dyn_calculate to find max path and add it the A[0][0] number
def solve(A):
    # we are starting from the 0 row and 0 column + we add the A[0][0]
    return A[0][0] + dyn_calculate(A, 0, 0, len(A))
