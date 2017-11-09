count,s,num=0,0,2
n=eval(input("Enter the number of prime numbers to add: "))
print("The first %d prime numbers are: \n" % n)
while count<n:
    c=0
    for i in range(2,(num/2)+1):
        if num%i==0:
            c=1
            break
    if c==0:
        count+=1
        s+=num
        print('%d,' % num, end=' ')
    num+=1
print('\n\nSum= %d' % s)
