from random import randint
c='Y'
head,tail=0,0
print('Coin Flip Simulation\n')
while c.upper()=='Y':
    ch=randint(0,1)
    if ch==0:
        head+=1
        print("\nIt's a HEAD!")
    else:
        tail+=1
        print("\nIt's a TAIL")
    print("Total HEADS : ",head)
    print("Total TAILS : ",tail)
    c=input("\nDo you want to continue? (Y/N) : ")
