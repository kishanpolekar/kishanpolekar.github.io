import os

def binary():
    num=input('Enter the Binary number: ')
    l=len(num)
    check=False
    for i in range(l):
        if num[i] in ('01.'):
            pass
        else:
            print('Invalid Binary number entered!')
            return
        if num[i]=='.': check=True
    nor,inv,i,j=0,0,0,0
    if check==True:
        while num[i]!='.':
            nor+=1
            i+=1
        while i<l-1:
            inv+=1
            i+=1
    else:
        for n in num:
            nor+=1

    decimal=0.0
    for i in range(nor-1,-1,-1):
        decimal+=int(num[j])*(2**i)
        j+=1
    if inv>0:
        j+=1
        for i in range(1,inv+1):
            decimal+=int(num[j])*(2**-i)
            j+=1

    octal,octal_nor,octal_inv='','',''
    o_nor=num[0:nor]
    if nor%3!=0:
        if nor%3==1:
            o_nor='00'+o_nor
        else:
            o_nor='0'+o_nor
    o=0
    x=len(o_nor)/3
    for i in range(x):
        o=0
        for j in range(2,-1,-1):
            o+=int(o_nor[2-j])*(2**j)
        octal_nor+=str(o)
        o_nor=o_nor[3:len(o_nor)]
    if inv>0:
        o_inv=num[nor+1:l]
        if inv%3!=0:
            if inv%3==1:
                o_inv+='00'
            else:
                o_inv+='0'
        o=0
        y=len(o_inv)/3
        for i in range(y):
            o=0
            for j in range(2,-1,-1):
                o+=int(o_inv[2-j])*(2**j)
            octal_inv+=str(o)
            o_inv=o_inv[3:len(o_inv)]
    octal=octal_nor

    hexa,hexa_nor,hexa_inv='','',''
    h_nor=num[0:nor]
    if nor%4!=0:
        if nor%4==1:
            h_nor='000'+h_nor
        elif nor%4==2:
            h_nor='00'+h_nor
        else:
            h_nor='0'+h_nor
    h=0
    x=len(h_nor)/4
    for i in range(x):
        h=0
        for j in range(3,-1,-1):
            h+=int(h_nor[3-j])*(2**j)
        if h in (10,11,12,13,14,15):
            if h==10:
                h='A'
            elif h==11:
                h='B'
            elif h==12:
                h='C'
            elif h==13:
                h='D'
            elif h==14:
                h='E'
            else:h='F'
        hexa_nor+=str(h)
        h_nor=h_nor[4:len(h_nor)]
    if inv>0:
        h_inv=num[nor+1:l]
        if inv%4!=0:
            if inv%4==1:
                h_inv+='000'
            elif inv%4==2:
                h_inv+='00'
            else:
                h_inv+='0'
        h=0
        y=len(h_inv)/4
        for i in range(y):
            h=0
            for j in range(3,-1,-1):
                h+=int(h_inv[3-j])*(2**j)
            if h in (10,11,12,13,14,15):
                if h==10:
                    h='A'
                elif h==11:
                    h='B'
                elif h==12:
                    h='C'
                elif h==13:
                    h='D'
                elif h==14:
                    h='E'
                else:h='F'
            hexa_inv+=str(h)
            h_inv=h_inv[4:len(h_inv)]
    hexa=hexa_nor

    if inv>0:
        print('Decimal: ',decimal)
        print('Octal: ',octal+'.'+octal_inv)
        print('Hexadecimal: ',hexa+'.'+hexa_inv)
    else:
        print('Decimal: ',int(decimal))
        print('Octal: ',octal)
        print('Hexadecimal: ',hexa)

def decimal():
    num=input('Enter the Decimal number: ')
    l=len(num)
    check=False
    for i in range(l):
        if num[i] in ('0123456789.'):
            pass
        else:
            print('Invalid Decimal number entered!')
            return
        if num[i]=='.': check=True
    nor,inv,i,j=0,0,0,0
    if check==True:
        while num[i]!='.':
            nor+=1
            i+=1
        while i<l-1:
            inv+=1
            i+=1
    else:
        for n in num:
            nor+=1

    binary,binary_nor,binary_inv='','',''
    b_nor1=num[0:nor]
    b_nor=int(b_nor1)
    b_rev=''
    while b_nor>0:
        b_rev+=str(b_nor%2)
        b_nor/=2
    binary_nor=b_rev[::-1]
    if inv>0:
        count=0
        b_inv=float(num)-float(b_nor1)
        while count<5 and b_inv!=0:
            b_inv*=2
            q=int(b_inv%2)
            binary_inv+=str(q)
            b_inv-=q
            count+=1
    binary=binary_nor

    octal,octal_nor,octal_inv='','',''
    o_nor1=num[0:nor]
    o_nor=int(o_nor1)
    o_rev=''
    while o_nor>0:
        o_rev+=str(o_nor%8)
        o_nor/=8
    octal_nor=o_rev[::-1]
    if inv>0:
        count=0
        o_inv=float(num)-float(o_nor1)
        while count<5 and o_inv!=0:
            o_inv*=8
            q=int(o_inv%8)
            octal_inv+=str(q)
            o_inv-=q
            count+=1
    octal=octal_nor

    hexa,hexa_nor,hexa_inv='','',''
    h_nor1=num[0:nor]
    h_nor=int(h_nor1)
    h_rev,h='',0
    while h_nor>0:
        h=int(h_nor)%16
        if h in (10,11,12,13,14,15):
            if h==10:
                h='A'
            elif h==11:
                h='B'
            elif h==12:
                h='C'
            elif h==13:
                h='D'
            elif h==14:
                h='E'
            else:h='F'
        h_rev+=str(h)
        h_nor/=16
    hexa_nor=h_rev[::-1]
    if inv>0:
        count=0
        h_inv=float(num)-float(h_nor1)
        while count<5 and h_inv!=0:
            h_inv*=16
            q=int(h_inv%16)
            h_inv-=q
            if q in (10,11,12,13,14,15):
                if q==10:
                    q='A'
                elif q==11:
                    q='B'
                elif q==12:
                    q='C'
                elif q==13:
                    q='D'
                elif q==14:
                    q='E'
                else:q='F'
            hexa_inv+=str(q)
            count+=1
    hexa=hexa_nor

    if inv>0:
        print('Binary: ',binary+'.'+binary_inv)
        print('Octal: ',octal+'.'+octal_inv)
        print('Hexadecimal: ',hexa+'.'+hexa_inv)
    else:
        print('Binary: ',binary)
        print('Octal: ',int(octal))
        print('Hexadecimal: ',hexa)

def octal():
    num=input('Enter the Octal number: ')
    l=len(num)
    check=False
    for i in range(l):
        if num[i] in ('01234567.'):
            pass
        else:
            print('Invalid Octal number entered!')
            return
        if num[i]=='.': check=True
    nor,inv,i,j=0,0,0,0
    if check==True:
        while num[i]!='.':
            nor+=1
            i+=1
        while i<l-1:
            inv+=1
            i+=1
    else:
        for n in num:
            nor+=1

    binary,binary_nor,binary_inv='','',''
    b_nor=num[0:nor]
    l_bnor=len(b_nor)
    for i in range(l_bnor):
        b=''
        if int(b_nor[i])>0:
            if int(b_nor[i])>1:
                if int(b_nor[i])>2:
                    if int(b_nor[i])>3:
                        if int(b_nor[i])>4:
                            if int(b_nor[i])>5:
                                if int(b_nor[i])>6:
                                    b='111'
                                else:
                                    b='110'
                            else:
                                b='101'
                        else:
                            b='100'
                    else:
                        b='011'
                else:
                    b='010'
            else:
                b='001'
        else:
            b='000'
        binary_nor+=b
    if inv>0:
        b_inv=num[nor+1:l]
        l_binv=len(b_inv)
        for i in range(l_binv):
            b=''
            if int(b_inv[i])>0:
                if int(b_inv[i])>1:
                    if int(b_inv[i])>2:
                        if int(b_inv[i])>3:
                            if int(b_inv[i])>4:
                                if int(b_inv[i])>5:
                                    if int(b_inv[i])>6:
                                        b='111'
                                    else:
                                        b='110'
                                else:
                                    b='101'
                            else:
                                b='100'
                        else:
                            b='011'
                    else:
                        b='010'
                else:
                    b='001'
            else:
                b='000'
            binary_inv+=b
    binary=binary_nor

    decimal=0.0
    for i in range(nor-1,-1,-1):
        decimal+=int(num[j])*(8**i)
        j+=1
    if inv>0:
        j+=1
        for i in range(1,inv+1):
            decimal+=int(num[j])*(8**-i)
            j+=1

    b_hexa=binary+'.'+binary_inv
    l_b_hexa=len(b_hexa)
    nor_hexa,inv_hexa,i,j=0,0,0,0
    if check==True:
        while b_hexa[i]!='.':
            nor_hexa+=1
            i+=1
        while i<l_b_hexa-1:
            inv_hexa+=1
            i+=1
    else:
        nor_hexa=-1
        for n in b_hexa:
            nor_hexa+=1
    hexa,hexa_nor,hexa_inv='','',''
    h_nor=b_hexa[0:nor_hexa]
    if nor_hexa%4!=0:
      if nor_hexa%4==1:
          h_nor='000'+h_nor
      elif nor_hexa%4==2:
          h_nor='00'+h_nor
      else:
          h_nor='0'+h_nor
    h=0
    x=len(h_nor)/4
    for i in range(x):
      h=0
      for j in range(3,-1,-1):
          h+=int(h_nor[3-j])*(2**j)
      if h in (10,11,12,13,14,15):
          if h==10:
              h='A'
          elif h==11:
              h='B'
          elif h==12:
              h='C'
          elif h==13:
              h='D'
          elif h==14:
              h='E'
          else:h='F'
      hexa_nor+=str(h)
      h_nor=h_nor[4:len(h_nor)]
    if inv_hexa>0:
      h_inv=b_hexa[nor_hexa+1:l_b_hexa]
      if inv_hexa%4!=0:
          if inv_hexa%4==1:
              h_inv+='000'
          elif inv_hexa%4==2:
              h_inv+='00'
          else:
              h_inv+='0'
      h=0
      y=len(h_inv)/4
      for i in range(y):
          h=0
          for j in range(3,-1,-1):
              h+=int(h_inv[3-j])*(2**j)
          if h in (10,11,12,13,14,15):
              if h==10:
                  h='A'
              elif h==11:
                  h='B'
              elif h==12:
                  h='C'
              elif h==13:
                  h='D'
              elif h==14:
                  h='E'
              else:h='F'
          hexa_inv+=str(h)
          h_inv=h_inv[4:len(h_inv)]
    hexa=hexa_nor

    if inv>0:
        print('Binary: ',binary+'.'+binary_inv)
        print('Decimal: ',decimal)
        print('Hexadecimal: ',hexa+'.'+hexa_inv)
    else:
        print('Binary: ',binary)
        print('Decimal: ',int(decimal))
        print('Hexadecimal: ',hexa)

def hexa():
    num1=input('Enter the HexaDecimal number: ')
    num=num1.upper()
    l=len(num)
    check=False
    for i in range(l):
        if num[i] in ('0123456789ABCDEF.'):
            pass
        else:
            print('Invalid HexaDecimal number entered!')
            return
        if num[i]=='.': check=True
    nor,inv,i,j=0,0,0,0
    if check==True:
        while num[i]!='.':
            nor+=1
            i+=1
        while i<l-1:
            inv+=1
            i+=1
    else:
        for n in num:
            nor+=1

    binary,binary_nor,binary_inv='','',''
    b_nor1=num[0:nor]
    b_nor=b_nor1.upper()
    l_bnor=len(b_nor)
    for i in range(l_bnor):
        b=''
        if b_nor[i]=='0':
            b='0000'
        elif b_nor[i]=='1':
            b='0001'
        elif b_nor[i]=='2':
            b='0010'
        elif b_nor[i]=='3':
            b='0011'
        elif b_nor[i]=='4':
            b='0100'
        elif b_nor[i]=='5':
            b='0101'
        elif b_nor[i]=='6':
            b='0110'
        elif b_nor[i]=='7':
            b='0111'
        elif b_nor[i]=='8':
            b='1000'
        elif b_nor[i]=='9':
            b='1001'
        elif b_nor[i]=='A':
            b='1010'
        elif b_nor[i]=='B':
            b='1011'
        elif b_nor[i]=='C':
            b='1100'
        elif b_nor[i]=='D':
            b='1101'
        elif b_nor[i]=='E':
            b='1110'
        else:
            b='1111'
        binary_nor+=b
    if inv>0:
        b_inv1=num[nor+1:l]
        b_inv=b_inv1.upper()
        l_binv=len(b_inv)
        for i in range(l_binv):
            b=''
            if b_inv[i]=='0':
                b='0000'
            elif b_inv[i]=='1':
                b='0001'
            elif b_inv[i]=='2':
                b='0010'
            elif b_inv[i]=='3':
                b='0011'
            elif b_inv[i]=='4':
                b='0100'
            elif b_inv[i]=='5':
                b='0101'
            elif b_inv[i]=='6':
                b='0110'
            elif b_inv[i]=='7':
                b='0111'
            elif b_inv[i]=='8':
                b='1000'
            elif b_inv[i]=='9':
                b='1001'
            elif b_inv[i]=='A':
                b='1010'
            elif b_inv[i]=='B':
                b='1011'
            elif b_inv[i]=='C':
                b='1100'
            elif b_inv[i]=='D':
                b='1101'
            elif b_inv[i]=='E':
                b='1110'
            else:
                b='1111'
            binary_inv+=b
    binary=binary_nor

    decimal=0.0
    for i in range(nor-1,-1,-1):
        h1=num[j]
        if h1 in ('ABCDEF'):
            if h1=='A':
                h1=10
            elif h1=='B':
                h1=11
            elif h1=='C':
                h1=12
            elif h1=='D':
                h1=13
            elif h1=='E':
                h1=14
            else:h1=15
        decimal+=int(h1)*(16**i)
        j+=1
    if inv>0:
        j+=1
        for i in range(1,inv+1):
            h1=num[j]
            if h1 in ('ABCDEF'):
                if h1=='A':
                    h1=10
                elif h1=='B':
                    h1=11
                elif h1=='C':
                    h1=12
                elif h1=='D':
                    h1=13
                elif h1=='E':
                    h1=14
                else:h1=15
            decimal+=int(h1)*(16**-i)
            j+=1

    b_octal=binary+'.'+binary_inv
    l_b_octal=len(b_octal)
    nor_octal,inv_octal,i,j=0,0,0,0
    if check==True:
        while b_octal[i]!='.':
            nor_octal+=1
            i+=1
        while i<l_b_octal-1:
            inv_octal+=1
            i+=1
    else:
        nor_octal=-1
        for n in b_octal:
            nor_octal+=1
    octal,octal_nor,octal_inv='','',''
    o_nor=b_octal[0:nor_octal]
    if nor_octal%3!=0:
      if nor_octal%3==1:
          o_nor='00'+o_nor
      else:
          o_nor='0'+o_nor
    o=0
    x=len(o_nor)/3
    for i in range(x):
      o=0
      for j in range(2,-1,-1):
          o+=int(o_nor[2-j])*(2**j)
      octal_nor+=str(o)
      o_nor=o_nor[3:len(o_nor)]
    if inv_octal>0:
      o_inv=b_octal[nor_octal+1:l_b_octal]
      if inv_octal%3!=0:
          if inv_octal%3==1:
              o_inv+='00'
          else:
              o_inv+='0'
      o=0
      y=len(o_inv)/4
      for i in range(y):
          o=0
          for j in range(2,-1,-1):
              o+=int(o_inv[2-j])*(2**j)
          octal_inv+=str(o)
          o_inv=o_inv[3:len(o_inv)]
    octal=octal_nor

    if inv>0:
        print('Binary: ',binary+'.'+binary_inv)
        print('Decimal: ',decimal)
        print('Octal: ',octal+'.'+octal_inv)
    else:
        print('Binary: ',binary)
        print('Decimal: ',int(decimal))
        print('Octal: ',octal)

def main():
    choice='y'
    while choice.lower()=='y':
        os.system('clear')
        print('NUMBER SYSTEM CALCULATOR\n')
        print('1-Binary conversions')
        print('2-Decimal conversions')
        print('3-Octal conversions')
        print('4-Hexadecimal conversions')
        ch=eval(input('\nEnter your choice: '))
        if ch==1:
            binary()
        elif ch==2:
            decimal()
        elif ch==3:
            octal()
        elif ch==4:
            hexa()
        else:
            print('\nWrong Choice!')
        choice=input('\nDo you want to make another calculation? (y/n): ')
main()
