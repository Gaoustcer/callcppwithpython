from signal import signal,SIGPIPE,SIG_DFL
signal(SIGPIPE,SIG_DFL)
for i in range(4000):
    print(i)
if __name__ == "__main__":
    print("hello world")