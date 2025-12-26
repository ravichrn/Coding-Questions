#Given Source and destination, write a SQL query to find the distinct routes travelled
select distinct least(source, destination) as location1, greatest(source, destination) as location2
from flights;

#Given an array of numbers, move all zeroes to then end
def move_zeroes(nums):
    cnt = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i], nums[cnt] = nums[cnt], nums[i]
            cnt += 1

#Modify string with count of characters
def modify_string(s):
    if not s: return ""
    count = 1
    res = []
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            res.append(s[i-1])
            res.append(str(count))
            count = 1
    res.append(s[i-1])
    res.append(str(count))
    return ''.join(res)


#Given a directory containing csv files with dates and sales volume of Tesla cars, read the files into a dataframe and output the dates with volume exceeding 50 million in total in ascending order of dates
df_updated = df
    .withColumn("date_col", col("date_col").cast("DateType")) # Cast date column
    .withColumn("volume_col", col("volume_col").cast("DoubleType")) # Cast volume column
    .groupBy("date_col")
    .agg(sum("volume_col").alias("total_volume"))
             

#pandas
df = pd.concat(df_list, ignore_index=True)
df['date_col'] = pd.to_datetime(df['date_col'])
df['volume_col'] = df['volume_col'].astype(float)
df_updated = df.groupby('date_col').agg(total_volume=('volume_col', 'sum'))

#get kth highest element in an array with duplicates
def find_kth_highest_sort(arr, k):
    """
    Time complexity: O(n log n) due to sorting.
    Space complexity: O(1) or O(n) depending on sort implementation.
    """
    if k < 1 or k > len(arr):
        return None
    
    arr.sort(reverse=True)
    return arr[k - 1]

#heap
import heapq

def find_kth_highest_heap(arr, k):
    """
    Time complexity: O(n log k) as each of the n elements is processed with a heap operation (log k).
    Space complexity: O(k) to store the heap.
    """
    if k < 1 or k > len(arr):
        return None
    
    min_heap = []
    for num in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
            
    return min_heap[0]