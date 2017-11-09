for i in range(1,101):
    if i%3==0:
        if i%5==0:
            print('FizzBuzz')
            continue
        print('Fizz')
        continue
    elif i%5==0:
        print ('Buzz')
        continue
    else:
        print(i)
