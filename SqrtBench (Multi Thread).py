import math, time, threading
threads = 128
random = []
class myThread(threading.Thread):
   def __init__(self, thread):
      threading.Thread.__init__(self)
      self.thread = thread
   def run(self):
      runThread(self.thread)
      
def runThread(thread):
    start_time = time.time()
    b = 0
    for i in range(1+thread,32000000,thread):
        b = math.sqrt(i)
    #print(f"Duration: {time.time()-start_time}s")
    random.append(time.time()-start_time)
threadsList = []
for i in range(1,threads+1):
    threadsList.append(myThread(i))
for i in range(1,threads+1):
    threadsList[i-1].start()
print(f"\n{sum(random)/1024}s")
