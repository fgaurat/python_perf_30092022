import time
import threading

the_lock = threading.Lock()

def traitement_long_1():
    with the_lock:
        for i in range(10):
            print(f"traitement_long_1 {i}")
            time.sleep(0.3)

def traitement_long_2():
    with the_lock:
        for i in range(10):
            print(f"traitement_long_2 {i}")
            time.sleep(0.3)


class MonThread(threading.Thread):

    def __init__(self):
        super().__init__()


    def run(self):
        with the_lock:
            for i in range(10):
                print(f"MonThread {self.name} {i}")
                time.sleep(0.3)        

def main():
    start = time.perf_counter()
    th1 = MonThread()
    th2 = MonThread()

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(time.perf_counter()-start)

def main01():
    th1 = threading.Thread(target=traitement_long_1)
    th2 = threading.Thread(target=traitement_long_2)

    th1.start()
    th2.start()


    th1.join()
    th2.join()

    print("toto")

if __name__ == '__main__':
    main()