import time
import threading

def calculate_sq(numbers):
    print('calculating square')
    for i in numbers:
        time.sleep(0.2)
        print('square is',i*i)
        
def calculate_cube(numbers):
    print('calculating cube')
    for i in numbers:
        time.sleep(0.2)
        print('cube is',i*i*i)
        
list=[2,3,4,5]
t=time.time()
     
t1=threading.Thread(target=calculate_sq,args=(list,))
t2=threading.Thread(target=calculate_cube,args=(list,))

t1.start()
t2.start()

t1.join()
t2.join()

print('The execution time is',time.time()-t)