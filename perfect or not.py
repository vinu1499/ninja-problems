num=int(input("Enter the num"))
sum=0
for i in range(1,num,1):
    if(num%i==0):
        sum=sum+i
        print(i)
if(num==sum):
    print("a num is perfect")
else:
     print("a num is not perfect")
