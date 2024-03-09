def merge_int(arr):
    if arr:
        arr = sorted(arr)
        res = []
        for i in arr:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
    else: return 0

merge_int(intervals)

intervals = [[15,18],[1,3],[8,10],[2,6]]
