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
df = spark.read.csv("data/*.csv", header=True, inferSchema=True)
filtered_df = df.filter(col("Volume") > 50000000)
sorted_df = filtered_df.orderBy(asc("Date"))
sorted_df.select("Date").show()

#pandas
df = pd.concat(df_list, ignore_index=True)
df['Date'] = pd.to_datetime(df['Date'])
high_volume_dates = df[df['Volume'] > 50000000]
sorted_dates = high_volume_dates.sort_values(by='Date')
print(sorted_dates['Date'])