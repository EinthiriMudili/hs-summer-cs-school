def insertion_sort(A):
    for i in range (1, len(A)):
        curNum = A[i]
        for j in range (i-1, 0, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break