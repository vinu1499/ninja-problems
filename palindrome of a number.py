n=int(input("Enter the num"))
sum=0
q=0
rev=n
while(n!=0):
    rem=n%10
    sum=rem+sum*10
    q=n//10
    n=q
if(rev==sum):
    print("a num is palindrome")
else:
    print("a num is  not palindrome")

