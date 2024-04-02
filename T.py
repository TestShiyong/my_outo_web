import threading

# 创建一个互斥锁
lock = threading.Lock()

def func():
    # 获取锁
    lock.acquire()
    try:
        # 访问共享资源
        print("Accessing shared resource")
    finally:
        # 释放锁
        lock.release()

# 创建多个线程并启动
threads = []
for _ in range(5):
    t = threading.Thread(target=func)
    # threads.append(t)
    t.start()

# 等待所有线程执行完成
for t in threads:
    t.join()
