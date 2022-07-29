from multiprocessing import Process
count = 0
N = 1024 * 1024
def add():
    global count
    count += 1
processes_vec = []
for _ in range(10):
    p = Process(target=add)
    p.start()
    print("process start")
    processes_vec.append(p)
for p in processes_vec:
    p.join()
print(count)
