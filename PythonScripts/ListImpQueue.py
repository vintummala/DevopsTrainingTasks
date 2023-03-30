#!/usr/bin/env python


#This File implements Queues using List collections.
#Functions implemented are 
#Queue_put()
#Queue_get()
#Queue_size()
#Queue_empty()
#Queue_full()

#Initializing a queue
list_queue = []

#Set Queue Max Size
queue_max = 5

#Insert Values to the queue
#Queue can hold Maximum 5 elements

def Queue_put(Lqueue,fname):
    x=Queue_size(Lqueue)
    print("Queue Length is" + str(x))
    if Queue_full(Lqueue) :
         print("Queue is full")
    else:
         print("x value is" + str(x))
         print (Lqueue)
         Lqueue[x:x+1] = [fname]
         return Lqueue

#Pop values from queue
def Queue_get(Lqueue):
    x = Queue_size(Lqueue)
    y = 1
    if Queue_empty(Lqueue):
         print("Queue is Empty")
    else:
        print("Queue value is " + Lqueue[0])
        Lqueue = Lqueue[1:]
        return Lqueue



#Get the size of queue
def Queue_size(Lqueue):
    count = 0
    for x in Lqueue:
         count = count + 1

    return count

#Check if Queue is Empty or not
def Queue_empty(Lqueue):
    x = Queue_size(Lqueue);
    if x == 0:
        return True
    else:
        return False

#Check if Queue is full or not
def Queue_full(Lqueue):
    x = Queue_size(Lqueue);
    if x == queue_max:
        return True
    else:
        return False

#Invoking the functions

print(len(list_queue))
Queue_put(list_queue,"Hello")
Queue_put(list_queue,"Hello 1")
Queue_put(list_queue,"Hello 2")
Queue_put(list_queue,"Hello 3")
Queue_put(list_queue,"Hello 4")
Queue_put(list_queue,"Hello 5")

#Invoking queue size
size = Queue_size(list_queue)
print("Queue Length is ", str(size))

#Invoking queue pop function
list_queue = Queue_get(list_queue)
#list_queue = Queue_get(list_queue)
#list_queue =Queue_get(list_queue)
#list_queue = Queue_get(list_queue)
#list_queue = Queue_get(list_queue)
#list_queue = Queue_get(list_queue)
print(Queue_empty(list_queue))
