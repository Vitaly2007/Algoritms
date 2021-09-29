def binary_search(lst, k):
    left = 1
    right = len(lst)-1
    while left <= right:
        m = (left+right) >> 1
        if lst[m] == k:
            return m
        elif lst[m] > k:
            right = m-1
        else:
            left = m+1
    return -1

def printElem():
    lst_out= []
    lst = list(map(int, input().split()))
    s = list(map(int, input().split()))
    for elem in s[1:]:
        j = binary_search(lst, elem)
        lst_out.append(j)
    print(*lst_out)