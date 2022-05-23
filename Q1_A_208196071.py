def permute(A):
    # the base case - if this is an empty string
    if not A:
        return []
    # make the first item in the list, as the first letter in the A string
    list1 = [A[0]]
    # for on every char in the string
    for i in range(1, len(A)):
        # for backwards - on every char
        for j in reversed(range(len(list1))):
            # remove the current permutation
            x = list1.pop(j)
            # insert to list1 every possible "string" - in the coming for
            # we are just "playing" with all the possible chars in the string A
            for k in range(len(x) + 1):
                list1.append(x[:k] + A[i] + x[k:])
    # now list1 is a list of string's - we want it to be a list of lists (chars), so:
    return sorted([list(x) for x in list1])


if __name__ == '__main__':
    print(permute("abc"))
