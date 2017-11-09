def passcheck(s):
    n=0
    if len(s)<8:
        return False
    else:
        if s.isalnum():
            for c in s:
                if c.isdigit():
                    n+=1
            if n<3:
                return False
        else: return False
        return True

def main():
    p=input("Enter a password: ")
    print("Valid password!") if (passcheck(p)) else print("Invalid Password!")

main()
