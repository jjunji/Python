import threading

# 0 ~ 10000 == 500500
# 전역변수

g_result = 0
lock = threading.Lock()

def thread_main(*args):
	global g_result
	global lock

	result = 0

	for arg in args:
		result += args:
		print(arg)

	lock.acquire()
	g_result += result
	lock.release()

n = 10000
offset = n//4

li = [e for e in range(n+1)]

threads = []

for i in range(4):
	th = threading.Thread(target = thread_main, args = li[offset * i+1 : offset * (i+1) + 1]
	th.start()
	threads.append(th)

for 
