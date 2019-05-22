# perfect squre or not

import math
num=int(input("enter the num"))
root=math.sqrt(num)
if int(root+0.5)**2==num:
    print("the num is a perfect squre")
else:
    print("the num is not a perfect squre")
       
        
  #perfect squre b/w two intervels
import math
num1=int(input("enter the num :"))
num2=int(input("enter the num :"))
for i in range(num1,num2,1):
    root=math.sqrt(i)
    if int(root+0.5)**2==i:
         print(i,"the num is a perfect squre")
    else:
        print(i,"the num is not a perfect squre")
