from array import array

#EX-1. positive indexing

arr=array('i',[10,20,30,40,50])
print(arr[0])      #first element
print(arr[2])      #thitrd element
print(arr[4])      #fifth element

#EX-2. negative indexing

arr=array('i',[10,20,30,40,50])
print(arr[-1])      #last element
print(arr[-2])      #second last  element
print(arr[-5])      #fifth element

#EX-3. modify element using index

arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

#EX-4. index error

arr=array('i',[10,20,30])
print(arr[5]) #error.index out of range