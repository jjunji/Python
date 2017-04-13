import threading

g_result = 0

class mythread(threading.Thread):
    def run(self):
	for i in range(10000001):
	    g_result += i

