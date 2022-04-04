from task1 import *
from task2 import*
from task3 import *

z = 0
while z == 0:
    task = int(input("Task № "))
    if task == 1:
        task1()
    elif task == 2:
        task2()
    elif task == 3:
        task3()
    else:
        print("Error")
    z = int(input("Press 0 to continue "))
