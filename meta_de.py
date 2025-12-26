# given a list of tuples with category and scores, calculate the highest possible score
# a student can score from a max of three distinct categories

def max_score(scores):
    if scores:
        dict = {}
        for i in scores:
            if i[0] in dict.keys():
                dict[i[0]] = max(dict[i[0]], i[1])
            else: dict[i[0]] = i[1]
        sorted_values = sorted(dict.values())
        return sum(sorted_values[:3])
    return 0


assert(max_score([
    ('Adventure',5),
    ('Adventure',2),
    ('History',3)
]) == 8)

assert (max_score([]) == 0)

# A log entry has 2 parameters: book_id and checkout_value. given a series of log entries, check if the log stream is valid

class LogEntry:
    def __init__(self, book_id, checkout_value):
        self.book_id = book_id
        self.checkout_value = checkout_value

def check_validity(logs):
    if logs:
        dict = {}
        for log in logs:
            if log.book_id in dict and log.checkout_value == dict[log.book_id]: 
                return False
            dict[log.book_id] = log.checkout_value
        return True
    return True

assert(check_validity([LogEntry(1, True), LogEntry(2, True), LogEntry(1, False), LogEntry(2, False), LogEntry(1, True)]) == True)