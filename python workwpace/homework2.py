l=[input(),input(),input()]
def f(n):return("Fizz"*(n%3==0)+"Buzz"*(n%5==0))or str(n)
n=1
while[l[0],l[1],l[2]]!=[f(n),f(n+1),f(n+2)]:n+=1
print(f(n+3))