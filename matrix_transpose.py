A = [[5, 4, 3],
     [4, 3, 2],
     [3, 2, 1],
     [2, 1, 0], ]

transResult = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0], ]

for a in range(len(A)):
    for b in range(len(A[0])):
        transResult[b][a] = A[a][b]

print("The transpose matrix is: ")
for res in transResult:
    print(res)

"""
The transpose matrix is: 
[5, 4, 3, 2]
[4, 3, 2, 1]
[3, 2, 1, 0]
"""
