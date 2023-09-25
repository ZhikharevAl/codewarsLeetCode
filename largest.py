def largest(A):
    my_max = A[0]
    for idx in range(1, len(A)):
        if A[idx] > my_max:
            my_max = A[idx]
    return my_max


A = [-1, 2, 33, 4, 5, 6]
print(largest(A))
