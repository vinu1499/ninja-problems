n=int(input("Enter the num"))
sum=0
q=0
while(n!=0):
    rem=n%10
    sum=rem+sum*10
    q=n//10
    n=q
print(sum)




///another method
n=int(input())
sum=0

pow=1
while(n>=pow):
    rem=(n//pow)%10
    sum=rem+sum*10
    pow=pow*10
print(sum)
