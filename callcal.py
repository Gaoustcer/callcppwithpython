from ctypes import cdll
from time import time
def callcppinterface():
    start = time()
    lib = cdll.LoadLibrary('CppCode/libcalculate.so')
    obj = lib.Test_new()
    lib.callfunction(obj)
    end = time()
    print("Time cost for python call",end - start)

import threading
from time import time
from multiprocessing import Process
processlist = []
for _ in range(5):
    p = Process(target=callcppinterface)
    p.start()
    processlist.append(p)
for p in processlist:
    p.join()

# callcppinterface()
# vectorthread = []
# N = 16
# for _ in range(N):
#     vectorthread.append(threading.Thread(target=callcppinterface))
# for i in range(N):
#     vectorthread[i].start()
# for i in range(N):
#     vectorthread[i].join()
# start = time()
# callcppinterface()
# end = time()
# print("Call one time",end - start)