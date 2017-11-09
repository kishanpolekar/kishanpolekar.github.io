import os

class binary:
    def __init__(self):
        self.num=input('Enter the Binary number: ')
        l=len(self.num)
        for i in range(l):
            if self.num[i] in ('01.'):
                pass
            else:
                print('Invalid Binary number entered!')
                return
    def length(self,num):
        self.l=len(num)
        self.check=False
        for i in range(self.l):
            if num[i]=='.': self.check=True
        self.nor,self.inv,i=0,0,0
        if self.check==True:
            while num[i]!='.':
                self.nor+=1
                i+=1
            while i<self.l-1:
                self.inv+=1
                i+=1
        else:
            for n in num:
                self.nor+=1

    def b_to_dec(self):
        j=0
        self.decimal=0.0
        for i in range(self.nor-1,-1,-1):
            self.decimal+=int(self.num[j])*(2**i)
            j+=1
        if self.inv>0:
            j+=1
            for i in range(1,self.inv+1):
                self.decimal+=int(self.num[j])*(2**-i)
                j+=1

    def b_to_oct(self,num):
        self.octal,self.octal_nor,self.octal_inv='','',''
        o_nor=num[0:self.nor]
        if self.nor%3!=0:
            if self.nor%3==1:
                o_nor='00'+o_nor
            else:
                o_nor='0'+o_nor
        o=0
        x=len(o_nor)/3
        for i in range(x):
            o=0
            for j in range(2,-1,-1):
                o+=int(o_nor[2-j])*(2**j)
            self.octal_nor+=str(o)
            o_nor=o_nor[3:len(o_nor)]
        if self.inv>0:
            o_inv=num[self.nor+1:self.l]
            if self.inv%3!=0:
                if self.inv%3==1:
                    o_inv+='00'
                else:
                    o_inv+='0'
            o=0
            y=len(o_inv)/3
            for i in range(y):
                o=0
                for j in range(2,-1,-1):
                    o+=int(o_inv[2-j])*(2**j)
                self.octal_inv+=str(o)
                o_inv=o_inv[3:len(o_inv)]
        self.octal=self.octal_nor

    def b_to_hex(self,num):
        self.hexa,self.hexa_nor,self.hexa_inv='','',''
        h_nor=num[0:self.nor]
        if self.nor%4!=0:
            if self.nor%4==1:
                h_nor='000'+h_nor
            elif self.nor%4==2:
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
            self.hexa_nor+=str(h)
            h_nor=h_nor[4:len(h_nor)]
        if self.inv>0:
            h_inv=num[self.nor+1:self.l]
            if self.inv%4!=0:
                if self.inv%4==1:
                    h_inv+='000'
                elif self.inv%4==2:
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
                self.hexa_inv+=str(h)
                h_inv=h_inv[4:len(h_inv)]
        self.hexa=self.hexa_nor

    def display(self):
        if self.inv>0:
            print('Decimal: ',self.decimal)
            print('Octal: ',self.octal+'.'+self.octal_inv)
            print('Hexadecimal: ',self.hexa+'.'+self.hexa_inv)
        else:
            print('Decimal: ',int(self.decimal))
            print('Octal: ',self.octal)
            print('Hexadecimal: ',self.hexa)

class decimal(binary):
    def __init__(self):
        self.num=input('Enter the Decimal number: ')
        self.l=len(self.num)
        self.check=False
        for i in range(self.l):
            if self.num[i] in ('0123456789.'):
                pass
            else:
                print('Invalid Decimal number entered!')
                return
        binary.length(self,self.num)

    def d_to_bin(self):
        self.binary,self.binary_nor,self.binary_inv='','',''
        b_nor1=self.num[0:self.nor]
        b_nor=int(b_nor1)
        b_rev=''
        while b_nor>0:
            b_rev+=str(b_nor%2)
            b_nor/=2
        self.binary_nor=b_rev[::-1]
        if self.inv>0:
            count=0
            b_inv=float(self.num)-float(b_nor1)
            while count<5 and b_inv!=0:
                b_inv*=2
                q=int(b_inv%2)
                self.binary_inv+=str(q)
                b_inv-=q
                count+=1
        self.binary=self.binary_nor

    def d_to_octal(self):
        self.octal,self.octal_nor,self.octal_inv='','',''
        o_nor1=self.num[0:self.nor]
        o_nor=int(o_nor1)
        o_rev=''
        while o_nor>0:
            o_rev+=str(o_nor%8)
            o_nor/=8
        self.octal_nor=o_rev[::-1]
        if self.inv>0:
            count=0
            o_inv=float(self.num)-float(o_nor1)
            while count<5 and o_inv!=0:
                o_inv*=8
                q=int(o_inv%8)
                self.octal_inv+=str(q)
                o_inv-=q
                count+=1
        self.octal=self.octal_nor

    def d_to_hex(self):
        self.hexa,self.hexa_nor,self.hexa_inv='','',''
        h_nor1=self.num[0:self.nor]
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
        self.hexa_nor=h_rev[::-1]
        if self.inv>0:
            count=0
            h_inv=float(self.num)-float(h_nor1)
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
                self.hexa_inv+=str(q)
                count+=1
        self.hexa=self.hexa_nor

    def display(self):
        if self.inv>0:
            print('Binary: ',self.binary+'.'+self.binary_inv)
            print('Octal: ',self.octal+'.'+self.octal_inv)
            print('Hexadecimal: ',self.hexa+'.'+self.hexa_inv)
        else:
            print('Binary: ',self.binary)
            print('Octal: ',int(self.octal))
            print('Hexadecimal: ',self.hexa)

class octal(binary):
    def __init__(self):
        self.num=input('Enter the Octal number: ')
        self.l=len(self.num)
        self.check=False
        for i in range(self.l):
            if self.num[i] in ('01234567.'):
                pass
            else:
                print('Invalid Octal number entered!')
                return
        binary.length(self,self.num)

    def o_to_bin(self):
        self.binary,self.binary_nor,self.binary_inv='','',''
        b_nor=self.num[0:self.nor]
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
            self.binary_nor+=b
        if self.inv>0:
            b_inv=self.num[self.nor+1:self.l]
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
                self.binary_inv+=b
        self.binary=self.binary_nor

    def o_to_dec(self):
        j=0
        self.decimal=0.0
        for i in range(self.nor-1,-1,-1):
            self.decimal+=int(self.num[j])*(8**i)
            j+=1
        if self.inv>0:
            j+=1
            for i in range(1,self.inv+1):
                self.decimal+=int(self.num[j])*(8**-i)
                j+=1
    def o_to_hexa(self):
        self.b_hexa=self.binary+'.'+self.binary_inv
        binary.length(self,self.b_hexa)
        binary.b_to_hex(self,self.b_hexa)

    def display(self):
        if self.inv>0:
            print('Binary: ',self.binary+'.'+self.binary_inv)
            print('Decimal: ',self.decimal)
            print('Hexadecimal: ',self.hexa+'.'+self.hexa_inv)
        else:
            print('Binary: ',self.binary)
            print('Decimal: ',int(self.decimal))
            print('Hexadecimal: ',self.hexa)

class hexa(binary):
    def __init__(self):
        self.num1=input('Enter the HexaDecimal number: ')
        self.num=self.num1.upper()
        self.l=len(self.num)
        self.check=False
        for i in range(self.l):
            if self.num[i] in ('0123456789ABCDEF.'):
                pass
            else:
                print('Invalid HexaDecimal number entered!')
                return
        binary.length(self,self.num)

    def h_to_bin(self):
        self.binary,self.binary_nor,self.binary_inv='','',''
        b_nor1=self.num[0:self.nor]
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
            self.binary_nor+=b
        if self.inv>0:
            b_inv1=self.num[self.nor+1:self.l]
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
                self.binary_inv+=b
        self.binary=self.binary_nor

    def h_to_dec(self):
        j=0
        self.decimal=0.0
        for i in range(self.nor-1,-1,-1):
            h1=self.num[j]
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
            self.decimal+=int(h1)*(16**i)
            j+=1
        if self.inv>0:
            j+=1
            for i in range(1,self.inv+1):
                h1=self.num[j]
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
                self.decimal+=int(h1)*(16**-i)
                j+=1

    def h_to_oct(self):
        self.b_octal=self.binary+'.'+self.binary_inv
        binary.length(self,self.b_octal)
        binary.b_to_oct(self,self.b_octal)

    def display(self):
        if self.inv>0:
            print('Binary: ',self.binary+'.'+self.binary_inv)
            print('Decimal: ',self.decimal)
            print('Octal: ',self.octal+'.'+self.octal_inv)
        else:
            print('Binary: ',self.binary)
            print('Decimal: ',int(self.decimal))
            print('Octal: ',self.octal)

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
            b=binary()
            b.length(b.num)
            b.b_to_dec()
            b.b_to_oct(b.num)
            b.b_to_hex(b.num)
            b.display()
        elif ch==2:
            d=decimal()
            d.d_to_bin()
            d.d_to_octal()
            d.d_to_hex()
            d.display()
        elif ch==3:
            o=octal()
            o.o_to_bin()
            o.o_to_dec()
            o.o_to_hexa()
            o.display()
        elif ch==4:
            h=hexa()
            h.h_to_bin()
            h.h_to_dec()
            h.h_to_oct()
            h.display()
        else:
            print('\nWrong Choice!')
        choice=input('\nDo you want to make another calculation? (y/n): ')
main()
