def check(num):
    s1=0
    while num>0:
        r=num%10
        s1+=r**2
        num//=10
    return s1

def main():
    n=int(input('Enter a number : '))
    number=n
    s,c=0,0
    while (s!=1 and c<=10000):
        s=check(number)
        number=s
        c+=1
    if s==1:
        print('{} is a Happy number'.format(n))
    else:
        print('{} is NOT a Happy number'.format(n))
main()
