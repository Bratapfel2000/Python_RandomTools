import time

def counter_and_timer():
    start = time.time()
    for i in range(1000):
        print(i)
    end = time.time()
    print(end - start)
counter_and_timer()
