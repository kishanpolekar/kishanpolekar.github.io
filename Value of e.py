n=eval(input('Enter the number of terms: '))
x=eval(input('Enter the accuracy: '))
sum,f=1.0,1.0
fl='%.'+str(x)+'f'
for i in range(1,n+1):
    f*=i
    sum+=1/f
print(fl % sum)
