# '''
# why threads are faster?
# threads will share the memory 
# process needs separate memory allocation

# concerency?
# teacher checking the note books 
# student A 
# student B 
# student C 

# concurency:
# A
# B
# C
# A
# B
# C
# one at time 
# rapidly check=jing
# what is concurency ?
# appears simultaneously

# parallesim:
# cashier 1 --> coustomer 1
# cashier 2 --> coustomer 2
# cashier 3 --> coustomer 3

# '''
# #creation of threads:
# import threading 

# #function created
# def display():
#     print("hello") 
# #thread object(created)
# t = threading.Thread(target=display)
# t.start()   



# #multiple threads:
# import threading 

# def task():
#     print("Thread is running")

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)
# t3 = threading.Thread(target=task)
# t1.start()
# t2.start()
# t3.start()

# main thread 
# + t1
# + t2
# + t3


# all executes immediately

# #threade in loops 

# def number():
#     for i










# import threading
# def even ():
#     for i in range (0,10,2):
#         print("even",i)


# def odd ():
#     for i in range (1,10,2):
#         print("odd",i)  
    
    
# t1=threading.Thread(target=even)
# t2=threading.Thread(target=even)
# t1.start()
# t2.start()

#naming of threads 

# import threading


# def task():

#     print(threading.current_thread().name)

# t = threading.Thread(target=task,name="student_Thread")

# t.start()

#passing arguments 
# import threading
# def square (n):
#     print(n*n)
# t=threading.Thread(target=square,
#                    args=(5,))
# t.start()

# # to delay the threads 
# import time 
# print("before delay")
# time.sleep(3)
# print("after delay")

# import threading
# import time 


# def task ():
#     for i in range(5):
#         print(i)
#         time.sleep

# t = threading.Thread(target=task)        
# t.start()


# # retry mechanism 
# while True:
#     try:
#         connect()

#     except:
#         time.sleep(5)   



# import threading 
# import time 
# def task():
#     time.sleep(3)
#     print("Thread Finished")

# t = threading.Thread(target=task)
# t.start()    
# t.join()
# print("main thread ends here")


#multiple threads with join
import threading
# def task(name):
#     print(name,"started")
#     time.sleep(2)
#     print(name,"Finished")

# t1 = threading.Thread (
#     target=task,args=("A",))
# t2 = threading.Thread (
#     target=task,args=("B",))
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("All threads completed")

import time



def download_file(file):
    print("Downloading",file)
    time.sleep(2)
    print(file,"finished")
files =[
      "movie.mp4",
      "song.mp3"
      "image.jpg"
]  
thread=[]     
for f in files:
    t = threading.Thread(
    target=download_file,
    args=(f,)
    )    
    thread.append(t)
    t.start()
for t in thread:
    t.join()
    print("All downloads finished")

