def prefix(s1, s2):
    i, l, l1, l2, s=0, 0, len(s1), len(s2), ""
    if l1<l2:
        l=l1
    else: l=l2
    while (i<l) and (s1[i]==s2[i]):
        s+=s1[i]
        i+=1
    return s

def main():
    s1=input("Enter the first string: ")
    s2=input("Enter the second string: ")
    print("The common prefix of '{}' and '{}' is : '{}'".format(s1, s2, prefix(s1, s2)))

main()
