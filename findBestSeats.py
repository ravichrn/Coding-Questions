def findBestSeats(seats):
    prev_seat=0
    max_dist=0
    max_index=0
    next_seat=0
    num=0
    for index, val in enumerate(seats):
        if val:
            prev_seat=0
        else:
            prev_seat+=1
            num=0
            for i in seats[index+1:]:
                while not i:
                    num+=1
                    break
                else:
                    break
        
        dist = max(prev_seat, num)
        if dist>max_dist:
            max_dist = dist
            max_index = index
    return max_index

seats = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
findBestSeats(seats)
