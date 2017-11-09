def check(s, ch):
    count=0
    for c in s:
        if c==ch:
            count+=1
    return count

def main():
    s=input("Enter a string: ")
    ch=input("Enter a character in the string to count: ")
    print("{} occurs {} times in {}.".format(ch, check(s, ch), s))

main()
