import threading
import time

def student(name):
    print(name,"started exam")
    time.sleep(3)
    print(name,"submitted paper")
t = threading.Thread(target=student,args=("fayu",))    
t.start()

t.join()
print("exam completed successfully")