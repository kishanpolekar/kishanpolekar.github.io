def check(num):
    s1=0
    while num>0:
        r=num%10
        s1+=r**2
        num//=10
    return s1

def main():
    n=int(input('Enter the number of terms : '))
    numb,i=1,1
    while i<=n:
        s,c=0,0
        number=numb
        while (s!=1 and c<=1000):
            s=check(number)
            number=s
            c+=1
        if s==1:
            print(numb, end=" ")
            i+=1
        numb+=1
    print()
main()
