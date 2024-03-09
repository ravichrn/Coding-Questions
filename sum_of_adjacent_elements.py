###Given a array of arrays with each element either 0 or 1, replace each element with the sum of elements within the specified radius 'r' for the respective element
###Athletic Python Interview Question

import itertools
import math

def sum_arr(arr, r):
    rows = len(arr)
    cols = len(arr[0])
    
    res_arr=[]
    if r < max(rows, cols):
        for i in range(rows):
            row = []
            for j in range(cols):
                val = 0
                lim = max(i+r, j+r)
                per=list(itertools.permutations(range(lim+1),2))
                com=list(itertools.combinations_with_replacement(range(lim+1),2))
                tot = set(per+com)

                for k in tot:
                    if k[0]<rows and k[1]<cols and math.sqrt(((k[0]-i)**2)+((k[1]-j)**2)) < r+1:
                        val+=arr[i][j]
                row.append(val)
            res_arr.append(row)

        return res_arr
    return 0

test_arr = [[1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1]]
rad = 1
