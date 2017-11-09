import os
def insert(a):
    os.system('clear')
    print('Insertion')
    print('\nCurrent List is : \n',a)
    n=eval(input('\nEnter the number of elements to insert in the list: '))
    a1=list(range(n))
    for i in range(n):
        a1[i]=eval(input())
    a.extend(a1)
    print('\nUpdated List is : \n',a)
def delete(a):
    os.system('clear')
    print('Deletion')
    n,c=len(a),0
    print('\nCurrent List is : \n',a)
    item=eval(input('\nEnter the item to delete: '))
    for i in range(n):
        if a[i]==item:
            b=a[i]
            del a[i]
            c=1
            break
    if c==1:
        print('\nThe list after deleting %i is : ' % b,a)
    else:print('\nElement not found OR the list is empty!!')
def main():
    os.system('clear')
    a,cont=[],'y'
    while cont.lower()=='y':
        os.system('clear')
        print('LIST OPERATIONS\n1- Insertion\n2- Deletion\n3- Exit')
        print('\nCurrent List is : \n',a)
        ch=eval(input('\nEnter your choice: '))
        if ch==1:
            insert(a)
        elif ch==2:
            delete(a)
        elif ch==3:
            print('\nExiting the program...',exit())
        else: print('\nWrong choice!!')
        cont=input('\nDo you want to continue? (y/n): ')
main()
