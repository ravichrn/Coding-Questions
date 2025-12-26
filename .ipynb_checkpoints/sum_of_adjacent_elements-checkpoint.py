###Given a array of arrays with each element either 0 or 1, replace each element with the sum of elements within the specified radius 'r' for the respective element
###Athletic Python Interview Question

import itertools
import math

# def sum_arr(arr, r):
#     rows = len(arr)
#     cols = len(arr[0])
    
#     res_arr=[]
#     if r < max(rows, cols):
#         for i in range(rows):
#             row = []
#             for j in range(cols):
#                 val = 0
#                 lim = max(i+r, j+r)
#                 per=list(itertools.permutations(range(lim+1),2))
#                 com=list(itertools.combinations_with_replacement(range(lim+1),2))
#                 tot = set(per+com)

#                 for k in tot:
#                     if k[0]<rows and k[1]<cols and math.sqrt(((k[0]-i)**2)+((k[1]-j)**2)) < r+1:
#                         val+=arr[i][j]
#                 row.append(val)
#             res_arr.append(row)

#         return res_arr
#     return 0

def sum_arr(arr, r):
    rows, cols = len(arr), len(arr[0])

    #build 2D prefix matrix
    ps = [[0] * (cols+1) for _ in range(rows+1)]
    for i in range(rows):
        for j in range(cols):
            ps[i+1][j+1] = arr[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]

    #sum inside the circle radius for each cell
    result = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            total = 0
            #scan bounding box of radius
            r1 = max(0, i-r)
            c1 = max(0, j-r)
            r2 = min(rows-1, i+r)
            c2 = min(cols-1, j+r)

            #sum of any rectangle in O(1)
            total = (ps[r2+1][c2+1]
                     -ps[r1][c2+1]
                    -ps[r2+1][c1]
                    +ps[r1][c1]
                    )
            result[i][j] = total
    return result

test_arr = [[1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1]]
rad = 1

sum_arr(test_arr, rad)
