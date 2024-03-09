from queue import Queue, PriorityQueue
def reverseQueue(q,revq):
    buff=q.get()
    if not q.empty():
        reverseQueue(q,revq)
    revq.put(buff)
    return revq

def test_allocation(test_run_times, tests_to_run, machine_count):
    queue = PriorityQueue()
    for i in tests_to_run:
        queue.put(test_run_times[i])

    revq = Queue()
    reverseQueue(queue, revq)

    res_allocation = []
    
    while not revq.empty():
        run_time = revq.get()
        if len(res_allocation) < machine_count:
            res_allocation.append(run_time)
        else:
            res_allocation[-1] += run_time
            res_allocation.sort(reverse = True)
    return res_allocation

test_run_times = {'test1': 10, 'test2': 5, 'test3': 13, 'test4': 7, 'test5': 11, 'test6': 15, 'test7': 8, 'test8': 6}
tests_to_run = ['test1', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8']
machine_count = 3

test_allocation(test_run_times, tests_to_run, machine_count)
