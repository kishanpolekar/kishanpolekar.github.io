def getNumber(uppercaseLetter):
    stdnumber=""
    for ch in uppercaseLetter:
        if ch.isalpha():
            if ch.lower() in ('abc'):
                stdnumber+='2'
            elif ch.lower() in ('def'):
                stdnumber+='3'
            elif ch.lower() in ('ghi'):
                stdnumber+='4'
            elif ch.lower() in ('jkl'):
                stdnumber+='5'
            elif ch.lower() in ('mno'):
                stdnumber+='6'
            elif ch.lower() in ('pqrs'):
                stdnumber+='7'
            elif ch.lower() in ('tuv'):
                stdnumber+='8'
            else: stdnumber+='9'
        else: stdnumber+=ch
    return stdnumber

def main():
    s=input("Enter a string: ")
    print(getNumber(s))

main()
