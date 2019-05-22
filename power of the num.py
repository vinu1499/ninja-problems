n=int(input("Enter the num :"))
power=int(input("Enter the power :"))
r=power**20
if(r%n==0):
    print(n,"is perfect power of",power)
else:
    print(n,"is not perfect power of",power)

