import math
num=int(input("enter the num"))
root=math.sqrt(num)
if int(root+0.5)**2==num:
    print("the num is a perfect squre")
else:
    print("the num is not a perfect squre")
