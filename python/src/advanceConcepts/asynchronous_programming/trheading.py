from threading import Thread, get_ident, currentThread
import time

def runMe(num):
    print("thread [{}] entered - thread id : {} - {}".format(currentThread().name, currentThread().ident, get_ident())) # both fuctions print same 
    time.sleep(2)
    print(f"this is thread method : {num}", flush=True)

if __name__ == "__main__":
    threads = []

    print(currentThread().ident, currentThread().is_alive(), currentThread().name)

    for num in range(2,20,4):
        threads.append(Thread(target=runMe, name="t-1", args=[num,]))
        num += 100
        threads.append(Thread(target=runMe, name="t-2", args=[num]))
        num += 200
        threads.append(Thread(target=runMe, name="t-3", args=[num]))

    # print(threads)

    print("Starting threads execution.")
    for i in threads:
        i.start()

    print("Joining threads.")
    for i in threads:
        i.join()