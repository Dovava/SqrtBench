import math, time
start_time = time.time()
b = 0
for i in range(32000000):
    b = math.sqrt(i)
print(f"Duration: {time.time()-start_time}s")
