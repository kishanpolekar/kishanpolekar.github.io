n=eval(input('Enter a number : '))
c=0
while n>1:
    if n%2==0:
        n/=2
        c+=1
    else:
        n=(3*n)+1
        c+=1
print('It takes %d step(s) to reach 1 using Collatz Conjecture!' % c)
