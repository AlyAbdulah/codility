def solution(A, K):
    NA = A
    if len(A) > 0:
        NA.insert(0, A[len(A) - 1])
        NA.pop()
        if K > 1:
            solution(NA, K - 1)
    return NA