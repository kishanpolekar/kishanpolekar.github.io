
import time
import os
import sys
import ntplib
import json
import pickle
from urllib.request import urlopen
from time import ctime
from random import randrange

#----------------------------CLASSES----------------------------

class Customer:
    def __init__(self):
        self.cid=None
        self.cpassword=None
        self.cname=None
        self.cage=0
        self.cbirthday=None
        self.cphone=None

    def storeData(self):
        self.cid=input('Enter your User ID: ')
        c1=open("customer.dat","rb")
        c=Customer()
        status=False
        try:
            while True:
                c=pickle.load(c1)
                if c.cid==self.cid:
                    print('User ID already taken! Try a different user ID!\n')
                    status=True
        except EOFError:
            f1.close()
        pass if !status else self.storeData()
        password1=input('Enter your password: ')
        password2=input('Confirm your password: ')
        if password1==password2:
            self.cpassword=password1
        else:
            print('Passwords do not match! You will be redirected to the sign up page again.')
            redirecting()
            customer_sign_up()
        self.cname=input('Enter your full name: ')
        self.cage=int(input('Enter your age: '))
        birthday1=input('Enter your birth date in MMM/DD/YYYY format: ')
        birthday2=birthday1[:3].upper()+birthday1[3:]
        self.cbirthday=birthday2.replace('/','')
        self.cphone=input('Enter your 10-digit contact number: ')

    def displayCustomer(self):
        print('\nCustomer ID: ',self.cid)
        print('Name: ',self.cname)
        print('Age: ',self.cage)
        print('Birthday: ',self.cbirthday)
        print('Phone: ',self.cphone)
        print()

class Flight:
    def __init__(self):
        self.fnumber=None
        self.fairline=None
        self.fdate=None
        self.fdeparttime=None
        self.farrivetime=None
        self.fdepart=None
        self.farrive=None
        self.ffirst=0
        self.ffirstprice=0
        self.ffirstnos=[]
        self.fbusiness=0
        self.fbusinessprice=0
        self.fbusinessnos=[]
        self.feconomy=0
        self.feconomyprice=0
        self.feconomynos=[]

    def storeData(self):
        self.fnumber=input('\nEnter the flight number: ')
        f1=open("flight.dat","rb")
        f=Flight()
        status=False
        try:
            while True:
                f=pickle.load(f1)
                if f.fnumber==self.fnumber:
                    print('Flight number already registered! Choose another unique number!\n')
                    status=True
        except EOFError:
            f1.close()
        pass if !status else self.storeData()
        self.fairline=input('Enter the airline: ')
        date1=input('Enter the date of the flight in MMM/DD/YYYY format: ')
        date2=date1[:3].upper()+date1[3:]
        self.fdate=date2.replace('/','')
        self.fdeparttime=input('Enter the departure time of the flight: ')
        self.fdepart=input('Enter the departure airport of the flight: ')
        self.farrivetime=input('Enter the arrival time of the flight: ')
        self.farrive=input('Enter the arrival airport of the flight: ')
        self.fbusiness=4*(int(input('Enter the number of business class rows in the flight: ')))
        self.fbusinessprice=int(input('Enter the price of one business class seat (in USD): '))
        bus_seats,first_seats,eco_seats=['A','B','E','F'],['A','B','E','F'],['A','B','C','D','E','F']
        for i in range(self.fbusiness//4):
            for j in range(4):
                self.fbusinessnos.append(str(i+1)+bus_seats[j])
        self.ffirst=4*(int(input('Enter the number of first class rows in the flight: ')))
        self.ffirstprice=int(input('Enter the price of one first class seat (in USD): '))
        for i in range(self.ffirst//4):
            for j in range(4):
                self.ffirstnos.append(str(i+1)+first_seats[j])
        self.feconomy=6*(int(input('Enter the number of economy class rows in the flight: ')))
        self.feconomyprice=int(input('Enter the price of one economy class seat (in USD): '))
        for i in range(self.feconomy//6):
            for j in range(6):
                self.feconomynos.append(str(i+1)+eco_seats[j])

    def displayFlightShort(self):
        print('\nFlight Number: ',self.fnumber)
        print('Airline: ',self.fairline)
        print('Date: ',self.fdate)
        print('From: {}\tTo: {}'.format(self.fdepart,self.arrive))
        print('Departure: {}\tArrival: {}'.format(self.fdeparttime,self.farrivetime))
        print('Economy Class fare: USD ',self.feconomyprice)

    def displayFlight(self):
        displayFlightShort()
        print('Economy Class seats available: ',self.feconomy)
        print('First Class fare: USD ',self.ffirstprice)
        print('First Class seats available: ',self.ffirst)
        print('Business Class fare: USD ',self.fbusinessprice)
        print('Business Class seats available: ',self.fbusiness)
        print()

class Booking:
    def __init__(self):
        self.bid=None
        self.bname=None
        self.bcontact=None
        self.bflightnum=None
        self.bairline=None
        self.bdate=None
        self.btime=None
        self.btraveldate=None
        self.bfrom=None
        self.bto=None
        self.bclass=None
        self.btotalseats=0
        self.bseatnumbers=[]
        self.btotalpriceUSD=0
        self.btotalpriceLocal=0

    def storeBooking(self,fnum,cusname):
        f1,f2=open("flight.dat","rb"),open("customer.dat","rb")
        f,c=Flight(),Customer()
        f=pickle.load(f1)
        c=pickle.load(f2)
        while f.fnumber!=fnum:
            f=pickle.load(f1)
        while c.cname!=cusname:
            c=pickle.load(f2)
        f1.close()

        print('\nYou\'ve chosen the following flight: \n')
        f.displayFlight()
        status1=0
        f1=open("flight.dat","ab+")
        f=pickle.load(f1)
        while status1==0:
            bclass=input('Select your preferred class (B-Business; F-First; E-Economy): ')
            if bclass.upper()=='B' or bclass.upper()=='BUSINESS':
                self.bclass='Business Class'
                self.btotalseats=int(input('Enter the number of passengers: '))
                if f.fbusiness-self.btotalseats>0:
                    print('\nThe following seats are available: ',f.fbusinessnos)
                    i=1
                    while self.btotalseats!=len(self.bseatnumbers):
                        s=input('Select seat number for passenger {}: '.format(i))
                        if s in f.fbusinessnos:
                            self.bseatnumbers.append(s)
                            f.fbusinessnos.remove(s)
                            i+=1
                        else:
                            print('Invalid seat number!')
                    f.fbusiness-=self.btotalseats
                    self.btotalpriceUSD=f.fbusinessprice*self.btotalseats
                    status1=1
                    break
                else:
                    print('\nThe specified number of seats are not available in this class. Please select another class.\n')
            elif bclass.upper()=='F' or bclass.upper()=='FIRST':
                self.bclass='First Class'
                self.btotalseats=int(input('Enter the number of passengers: '))
                if f.ffirst-self.btotalseats>0:
                    print('\nThe following seats are available: ',f.ffirstnos)
                    i=1
                    while self.btotalseats!=len(self.bseatnumbers):
                        s=input('Select seat number for passenger {}: '.format(i))
                        if s in f.ffirstnos:
                            self.bseatnumbers.append(s)
                            f.ffirstnos.remove(s)
                            i+=1
                        else:
                            print('Invalid seat number!')
                    f.ffirst-=self.btotalseats
                    self.btotalpriceUSD=f.ffirstprice*self.btotalseats
                    status1=1
                    break
                else:
                    print('\nThe specified number of seats are not available in this class. Please select another class.\n')
            elif bclass.upper()=='E' or bclass.upper()=='ECONOMY':
                self.bclass='Economy Class'
                self.btotalseats=int(input('Enter the number of passengers: '))
                if f.feconomy-self.btotalseats>0:
                    print('\nThe following seats are available: ',f.feconomynos)
                    i=1
                    while self.btotalseats!=len(self.bseatnumbers):
                        s=input('Select seat number for passenger {}: '.format(i))
                        if s in f.feconomynos:
                            self.bseatnumbers.append(s)
                            f.feconomynos.remove(s)
                            i+=1
                        else:
                            print('Invalid seat number!')
                    f.feconomy-=self.btotalseats
                    self.btotalpriceUSD=f.feconomyprice*self.btotalseats
                    status1=1
                    break
                else:
                    print('\nThe specified number of seats are not available in this class. Please select another class.\n')
            else:
                print('\nIncorrect Choice!\n')

        if status1==0:
            f1.close()
            print('\nOOPS! An error occured. Redirecting /\/\/\/\/\\')
            storeBooking(fnum,cusname)
        else:
            print('\nBOOKING CONFIRMED!!\n')
            self.bid=f.fnumber+str(randrange(11111,98989))+c.cname[:3].upper()
            self.bname=c.cname
            self.bcontact=c.cphone
            self.bflightnum=f.fnumber
            self.bairline=f.fairline
            c=ntplib.NTPClient()
            response=c.request('europe.pool.ntp.org')
            Ctime=ctime(response.tx_time).split()
            self.bdate=Ctime[1].upper()+Ctime[2]+Ctime[4]
            self.btime=f.fdeparttime
            self.btraveldate=f.fdate
            self.bfrom=f.fdepart
            self.bto=f.farrive
            if self.bdate[:3]==c.cbirthday[:3]:
                if self.bdate[:5]==c.cbirthday[:5]:
                    print('\nHAPPY BIRTHDAY!!\nSince it is your birthday, you get 20% discount on your booking!\n')
                    self.btotalpriceUSD*=0.8
                print('\nIt is your birthday Month! Enjoy 10% discount on this booking!\n')
                self.btotalpriceUSD*=0.9
            p,x,y=currency_local()
            self.btotalpriceLocal=self.btotalpriceUSD*p
            f1.close()
            f2.close()

        def displayBooking(self):
            print('\nBooking Confirmation Number (Use this for future references): ',self.bid)
            print('Name: ',self.bname)
            print('Contact Number: ',self.bcontact)
            print('Flight Number: ',self.bflightnum)
            print('Airline: ',self.bairline)
            print('Booking Date: ',self.bdate)
            print('Journet Date: ',self.btraveldate)
            print('Flight Departure Time: ',self.btime)
            print('Departure: ',self.bfrom,'\tArrival: ',self.bto)
            print('Class: ',self.bclass)
            print('Total number of passengers: ',self.btotalseats)
            print('Seat Numbers: ',self.bseatnumbers)
            print('Total fare in USD: ',self.btotalpriceUSD)
            if self.btotalpriceUSD!=self.btotalpriceLocal:
                x,to_curr,to_curr_name=currency_local()
                print('Total fare in {} = {} {}'.format(to_curr_name,to_curr,self.btotalpriceLocal)

        def currency_local():
            f = urlopen('http://freegeoip.net/json/')
            json_string = f.read()
            f.close()
            location = json.loads(json_string)
            f=open("Country Currency Code Mappings.txt","r")
            to_curr='USD'
            to_curr_name='USD'
            rec=f.readline()
            while rec:
                r=rec.split(',')
                if r[1]==location['country_code']:
                    to_curr=r[3].rstrip('\n')
                    to_curr_name=r[2]
                    break
                rec=f.readline()
            f.close()
            curl='https://currency-api.appspot.com/api/{}/{}.json'.format('USD',to_curr)
            f1=urlopen(curl)
            json_string2=json.loads(f1.read())
            f1.close()
            return(json_string2['amount'],to_curr,to_curr_name)

#----------------------------ADMIN MENU FUNCTIONS----------------------------

def newFlight():
    print('\nADD A FLIGHT\n')
    f=Flight()
    f1=open("flight.dat","ab")
    f.storeData()
    pickle.dump(f,f1)
    print('\nThe following flight has been added: ')
    f.displayFlight()
    f1.close()

def modifyFlight():
    print('\nMODIFY A FLIGHT\n')
    num=input('\nEnter the Flight Number: ')
    f1=open("flight.dat","rb")
    f2=open("newfile.dat","wb")
    f=Flight()
    status=0
    try:
        while True:
            f=pickle.load(f1)
            if f.fnumber==num:
                print('\nOriginal Flight Details : \n')
                f.displayFlight()
                print('\n\nModify the above details now... \n')
                f.storeData()
                status=1
            pickle.dump(f,f2)

    except EOFError:
        f1.close()
        f2.close()

    os.remove("flight.dat")
    os.rename("newfile.dat","flight.dat")
    if status==1:
        print('\nThe flight details have been modified! New flight details: \n')
        f.displayFlight()
    else: print('\nFlight Not Found!')

def deleteFlight():
    print('\nDELETE A FLIGHT\n')
    num=input('\nEnter the Flight Number: ')
    f1=open("flight.dat","rb")
    f2=open("newfile.dat","wb")
    f=Flight()
    status=False
    try:
        while True:
            f=pickle.load(f1)
            if f.fnumber!=num:
                pickle.dump(f,f2)
            else:
                print('\nThe following flight has been removed: \n')
                f.displayFlight()
                status=True

    except EOFError:
        f1.close()
        f2.close()

    os.remove("flight.dat")
    os.rename("newfile.dat","flight.dat")
    pass if status else print('\nFlight Not Found!')

def searchFlight():
    print('\nSEARCH FOR A FLIGHT\n')
    num=input('\nEnter the Flight Number: ')
    f1=open("flight.dat","rb")
    f=Flight()
    status=False
    try:
        while True:
            f=pickle.load(f1)
            if f.fnumber==num:
                print('Flight found!\n')
                f.displayFlight()
                status=True
    except EOFError:
        f1.close()
    pass if status else print('\nFlight Not Found!')

def displayAllFlights():
    print('\nDISPLAY ALL THE FLIGHTS\n')
    f1=open("flight.dat","rb")
    f=Flight()
    try:
        while True:
            f=pickle.load(f1)
            f.displayFlight()
    except EOFError:
        f1.close()

def displayAllFlightsDate():
    print('\nDISPLAY ALL FLIGHTS ON A PARTICULAR DATE\n')
    d1=input('\nEnter a date to search (MMM/DD/YYYY): ')
    d2=d1[:3].upper()+d1[3:]
    d=d2.replace('/','')
    f1=open("flight.dat","rb")
    f=Flight()
    status=False
    try:
        while True:
            f=pickle.load(f1)
            if f.fdate==d:
                f.displayFlightShort()
                status=True
    except EOFError:
        f1.close()
    pass if status else print('\nThere are no flights scheduled for {}.'.format(d))

def displayAllFlightsAirline():
    print('\nDISPLAY ALL FLIGHTS FOR A PARTICULAR AIRLINE\n')
    air=input('\nEnter the airline name: ')
    f1=open("flight.dat","rb")
    f=Flight()
    status=False
    try:
        while True:
            f=pickle.load(f1)
            if f.fairline.upper()==air.upper():
                f.displayFlightShort()
                status=True
    except EOFError:
        f1.close()
    pass if status else print('\nNo flights found for the specified airline.')

def displayAllFlightsDeparture():
    print('\nDISPLAY ALL FLIGHTS WITH A PARTICULAR DEPARTURE POINT\n')
    dep=input('\nEnter the departure point: ')
    f1=open("flight.dat","rb")
    f=Flight()
    status=False
    try:
        while True:
            f=pickle.load(f1)
            if f.fdepart.upper()==dep.upper():
                f.displayFlightShort()
                status=True
    except EOFError:
        f1.close()
    pass if status else print('\nNo flights found for the specified departure point.')

def displayAllFlightsArrival():
    print('\nDISPLAY ALL FLIGHTS WITH A PARTICULAR ARRIVAL POINT\n')
    arr=input('\nEnter the arrival point: ')
    f1=open("flight.dat","rb")
    f=Flight()
    status=False
    try:
        while True:
            f=pickle.load(f1)
            if f.farrive.upper()==arr.upper():
                f.displayFlightShort()
                status=True
    except EOFError:
        f1.close()
    pass if status else print('\nNo flights found for the specified arrival point.')

def displayAllBookings():
    print('\nDISPLAY ALL BOOKINGS\n')
    b1=open("booking.dat","rb")
    b=Booking()
    try:
        while True:
            b=pickle.load(b1)
            b.displayBooking()
    except EOFError:
        b1.close()

def displayABooking():
    num=input('\nEnter the Booking Number: ')
    b1=open("booking.dat","rb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bid==num:
                print('Booking found!\n')
                b.displayBooking()
                status=True
    except EOFError:
        b1.close()
    pass if status else print('\nBooking Not Found!')

def displayAllBookingsDate():
    print('\nDISPLAY ALL BOOKINGS ON A PARTICULAR DATE\n')
    d1=input('\nEnter a date to search (MMM/DD/YYYY): ')
    d2=d1[:3].upper()+d1[3:]
    d=d2.replace('/','')
    b1=open("booking.dat","rb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bdate==d:
                b.displayBooking()
                status=True
    except EOFError:
        b1.close()
    pass if status else print('\nThere are no bookings for {}.'.format(d))

def displayAllBookingsAirline():
    print('\nDISPLAY ALL BOOKINGS FOR A PARTICULAR AIRLINE\n')
    air=input('\nEnter the airline name: ')
    b1=open("booking.dat","rb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bairline.upper()==air.upper():
                b.displayBooking()
                status=True
    except EOFError:
        b1.close()
    pass if status else print('\nNo bookings found for the specified airline.')

def displayAllBookingsDeparture():
    print('\nDISPLAY ALL BOOKINGS WITH A PARTICULAR DEPARTURE POINT\n')
    dep=input('\nEnter the departure point: ')
    b1=open("booking.dat","rb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bfrom.upper()==dep.upper():
                b.displayBooking()
                status=True
    except EOFError:
        b1.close()
    pass if status else print('\nNo bookings found for the specified departure point.')

def displayAllBookingsArrival():
    print('\nDISPLAY ALL BOOKINGS WITH A PARTICULAR ARRIVAL POINT\n')
    arr=input('\nEnter the arrival point: ')
    b1=open("booking.dat","rb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bto.upper()==arr.upper():
                b.displayBooking()
                status=True
    except EOFError:
        b1.close()
    pass if status else print('\nNo bookings found for the specified arrival point.')

def displayAllCustomers():
    print('\nDISPLAY ALL THE CUSTOMERS REGISTERED\n')
    c1=open("customer.dat","rb")
    c=Customer()
    try:
        while True:
            c=pickle.load(c1)
            c.displayCustomer()
    except EOFError:
        c1.close()

def displayACustomer():
    print('\nDISPLAY DETAILS OF A PARTICULAR CUSTOMER\n')
    ch=input('Search customer based on (ID/Name/Birthday/Phone): ')
    c1=open("customer.dat","rb")
    c=Customer()
    status=False
    if ch.upper()=='ID':
        id=input('\nEnter the Customer ID: ')
        try:
            while True:
                c=pickle.load(c1)
                if c.cid==id:
                    print('Customer found!\n')
                    c.displayCustomer()
                    status=True
                    break
        except EOFError:
            c1.close()
    elif ch.upper()=='NAME':
        name=input('\nEnter the Customer\'s name: ')
        try:
            while True:
                c=pickle.load(c1)
                if c.cname==name:
                    print('Customer found!\n')
                    c.displayCustomer()
                    status=True
        except EOFError:
            c1.close()
    elif ch.upper()=='BIRTHDAY':
        bd1=input('\nEnter the Customer\'s Birthday (MMM/DD): ')
        bd2=bd1[:3].upper()+bd1[3:]
        bd=bd2.replace('/','')
        try:
            while True:
                c=pickle.load(c1)
                if c.cbirthday==bd:
                    print('Customer found!\n')
                    c.displayCustomer()
                    status=True
        except EOFError:
            c1.close()
    elif ch.upper()=='PHONE':
        phone=input('\nEnter the Customer\'s contact number: ')
        try:
            while True:
                c=pickle.load(c1)
                if c.cphone==phone:
                    print('Customer found!\n')
                    c.displayCustomer()
                    status=True
        except EOFError:
            c1.close()
    else:
        c1.close()
        print('\nIncorrect Choice!')
        redirecting()
        displayACustomer()
    c1.close()
    pass if status else print('\nCustomer Not Found!')

def displayAllBookingsCustomer():
    print('\nDISPLAY ALL BOOKINGS OF A PARTICULAR CUSTOMER\n')
    ch=input('Search customer based on (ID/Name/Birthday/Phone): ')
    b1,c1=open("booking.dat","rb"),open("customer.dat","rb")
    b=Booking()
    c=Customer()
    status1,status2=False,False
    if ch.upper()=='ID':
        id=input('\nEnter the Customer ID: ')
        try:
            while True:
                c=pickle.load(c1)
                if c.cid==id:
                    try:
                        while True:
                            b=pickle.load(b1)
                            if b.bname==c.cname:
                                print('Booking found!\n')
                                b.displayBooking()
                                status2=True
                    except EOFError:
                        b1.close()
                    status1=True
        except EOFError:
            c1.close()
    elif ch.upper()=='NAME':
        name=input('\nEnter the Customer\'s name: ')
        try:
            while True:
                c=pickle.load(c1)
                if c.cname==name:
                    try:
                        while True:
                            b=pickle.load(b1)
                            if b.bname==c.cname:
                                print('Booking found!\n')
                                b.displayBooking()
                                status2=True
                    except EOFError:
                        b1.close()
                    status1=True
        except EOFError:
            c1.close()
    elif ch.upper()=='BIRTHDAY':
        bd1=input('\nEnter the Customer\'s Birthday (MMM/DD): ')
        bd2=bd1[:3].upper()+bd1[3:]
        bd=bd2.replace('/','')
        try:
            while True:
                c=pickle.load(c1)
                if c.cbirthday==bd:
                    try:
                        while True:
                            b=pickle.load(b1)
                            if b.bname==c.cname:
                                print('Booking found!\n')
                                b.displayBooking()
                                status2=True
                    except EOFError:
                        b1.close()
                    status1=True
        except EOFError:
            c1.close()
    elif ch.upper()=='PHONE':
        phone=input('\nEnter the Customer\'s contact number: ')
        try:
            while True:
                c=pickle.load(c1)
                if c.cphone==phone:
                    try:
                        while True:
                            b=pickle.load(b1)
                            if b.bcontact==c.cphone:
                                print('Booking found!\n')
                                b.displayBooking()
                                status2=True
                    except EOFError:
                        b1.close()
                    status1=True
        except EOFError:
            c1.close()
    else:
        b1.close()
        c1.close()
        print('\nIncorrect Choice!')
        redirecting()
        displayAllBookingsCustomer()
    b1.close()
    c1.close()
    if status1==True:
        if status2==True:
            pass
        else: print('\nCustomer found but has no bookings!')
    else: print('\nCustomer not found!')

def changeAdminPass():
    print('\nCHANGE THE ADMIN PASSWORD\n')
    f=open("admin.dat","wb")
    admin_pass=input('\nEnter the new admin password : ')
    pickle.dump(admin_pass,f)
    f.close()

#----------------------------CUSTOMER MENU FUNCTIONS----------------------------

def newBooking(name):
    print('\nMAKE A NEW BOOKING\n')
    dep=input('Enter the departure airport: ')
    arr=input('Enter the arrival airport: ')
    d1=input('\nEnter a date to search (MMM/DD/YYYY): ')
    d2=d1[:3].upper()+d1[3:]
    d=d2.replace('/','')
    f1=open("flight.dat","rb")
    f=Flight()
    status1,status2,available=False,False,[]
    try:
        while True:
            f=pickle.load(f1)
            if f.fdepart.upper()==dep.upper() and f.farrive.upper()==arr.upper():
                if f.fdate==d:
                    f.displayFlightShort()
                    available.append(f.fnumber)
                    status1,status2=True,True
                status1=True
    except EOFError:
        f1.close()
    f1.close()
    status3=True
    if status1:
        while status2 and status3:
            fnum=input('\nEnter the flight number to confirm: ')
            if fnum in available:
                b1=open("booking.dat","ab")
                b=Booking()
                b.storeBooking(fnum,name)
                pickle.dump(b,b1)
                b.displayBooking()
                b1.close()
                status3=False
            else: print('\nInvalid flight number! Please select again.')
        if !status2:
            view=input('\nNo flights found for the specified date. View flights for the same route but different date? (Y/N): ')
            while (view.upper()=='Y' or view.upper()=='YES') and status3:
                f1=open("flight.dat","rb")
                try:
                    while True:
                        f=pickle.load(f1)
                        if f.fdepart.upper()==dep.upper() and f.farrive.upper()==arr.upper():
                            f.displayFlightShort()
                            available.append(f.fnumber)
                except EOFError:
                    f1.close()
                f1.close()
                fnum=input('\nEnter the flight number to confirm: ')
                if fnum in available:
                    b1=open("booking.dat","ab")
                    b=Booking()
                    b.storeBooking(fnum,name)
                    pickle.dump(b,b1)
                    b.displayBooking()
                    b1.close()
                    status3=False
                else: print('\nInvalid flight number! Please select again.')
    else: print('\nNo flights found!\n')

def modifyBooking():
    print('\nMODIFY AN EXISTING BOOKING\n')
    id=input('\nEnter the booking confirmation number: ')
    b1=open("booking.dat","rb")
    b2=open("newfile.dat","wb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bid==id:
                f1=open("flight.dat","ab+")
                f=Flight()
                try:
                    while True:
                        f=pickle.load(f1)
                        if f.fnumber==b.bflightnum:
                            if b.bclass=='Business Class':
                                f.fbusiness+=b.btotalseats
                                f.fbusinessnos.append(b.bseatnumbers)
                                f.fbusinessnos.sort()
                            elif b.bclass=='First Class':
                                f.ffirst+=b.btotalseats
                                f.ffirstnos.append(b.bseatnumbers)
                                f.ffirstnos.sort()
                            else:
                                f.feconomy+=b.btotalseats
                                f.feconomynos.append(b.bseatnumbers)
                                f.feconomynos.sort()
                except EOFError:
                    f1.close()
                f1.close()
                print('\nBooking found!\nModify the booking now...\n')
                b.storeBooking(b.bflightnum,b.bname)
                status=True
            pickle.dump(b,b2)
    except EOFError:
        b1.close()
        b2.close()
    os.remove("booking.dat")
    os.rename("newfile.dat","booking.dat")

    print('\nBooking details modified!') if status else print('\nBooking not found!')

def cancelBooking():
    print('\nCANCEL A BOOKING\n')
    id=input('\nEnter the booking confirmation number: ')
    b1=open("booking.dat","rb")
    b2=open("newfile.dat","wb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bid!=id:
                pickle.dump(b,b2)
            else:
                f1=open("flight.dat","ab+")
                f=Flight()
                try:
                    while True:
                        f=pickle.load(f1)
                        if f.fnumber==b.bflightnum:
                            if b.bclass=='Business Class':
                                f.fbusiness+=b.btotalseats
                                f.fbusinessnos.append(b.bseatnumbers)
                                f.fbusinessnos.sort()
                            elif b.bclass=='First Class':
                                f.ffirst+=b.btotalseats
                                f.ffirstnos.append(b.bseatnumbers)
                                f.ffirstnos.sort()
                            else:
                                f.feconomy+=b.btotalseats
                                f.feconomynos.append(b.bseatnumbers)
                                f.feconomynos.sort()
                except EOFError:
                    f1.close()
                f1.close()
                print('\nThe following booking has been cancelled:\n')
                b.displayBooking()
                status=True
    except EOFError:
        b1.close()
        b2.close()
    os.remove("booking.dat")
    os.rename("newfile.dat","booking.dat")

    pass if status else print('\nBooking not found!')

def searchBooking():
    displayABooking()

def viewAllBookings(name):
    print('\nVIEW ALL MY BOOKINGS\n')
    b1=open("booking.dat","rb")
    b=Booking()
    status=False
    try:
        while True:
            b=pickle.load(b1)
            if b.bname==name:
                print('Booking found!\n')
                b.displayBooking()
                status=True
    except EOFError:
        b1.close()
    pass if status else print('\nNo Bookings Found!')

def viewProfile(name):
    print('\nVIEW MY PROFILE\n')
    c1=open("customer.dat","rb")
    c=Customer()
    while c.cname!=name:
        c=pickle.load(c1)
    c1.close()
    c.displayCustomer()

def editProfile(name):
    print('\nEDIT MY PROFILE\n')
    c1=open("customer.dat","ab+")
    c=Customer()
    while c.cname!=name:
        c=pickle.load(c1)
    c.storeData()
    c1.close()

def changeCustomerPass(name):
    print('\nCHANGE MY PASSWORD\n')
    password1=input('Enter new password: ')
    password2=input('Confirm new password: ')
    c1=open("customer.dat","ab+")
    c=Customer()
    while c.cname!=name:
        c=pickle.load(c1)
    if password1==password2:
        c.cpassword=password1
    else:
        print('Passwords do not match! Please try again.')
        c1.close()
        changeCustomerPass()
    c1.close()

#----------------------------ADMIN & CUSTOMER FUNCTIONS----------------------------

def admin_login():
    print('\nADMIN LOGIN\n')
    login=input('\nEnter the admin password : ')
    f=open("admin.dat","rb")
    admin_pass=pickle.load(f)
    status=0
    try:
        if login==admin_pass:
                status=1
    except EOFError:
            f.close()
    f.close()
    return(status)

def customer_login():
    print('\nCUSTOMER LOGIN\n')
    id=input('\nEnter the user ID : ')
    f=open("customer.dat","rb")
    status,attempt=0,3
    c=Customer()
    try:
        while True:
            c=pickle.load(f)
            while c.cid==id and attempt>0:
                password=input('Enter the Password: ')
                if c.cpassword=password:
                    status=1
                else:
                    print('Incorrect password! Try Again! {} attempts remaining.\n'.format(attempt-=1))
    except EOFError:
        f.close()
    f.close()
    return(status,c.cname)

def customer_sign_up():
    print('\nCUSTOMER SIGN UP\n')
    c=Customer()
    c.storeData()
    f=open("customer.dat","ab")
    pickle.dump(c,f)
    f.close()
    print('\nSign Up Successful!\n')

def admin_menu():
    print('\nADMINISTRATIONS MAIN MENU\n')
    print('1: Add a flight')
    print('2: Modify a flight')
    print('3: Delete a flight')
    print('4: Search for a flight')
    print('5: Display all the flights')
    print('6: Display all flights on a particular date')
    print('7: Display all flights for a particular airline')
    print('8: Display all flights with a particular departure point')
    print('9: Display all flights with a particular arrival point')
    print('10: Display all bookings')
    print('11: Display a particular booking')
    print('12: Display all bookings on a particular date')
    print('13: Display all bookings for a particular airline')
    print('14: Display all bookings with a particular departure point')
    print('15: Display all bookings with a particular arrival point')
    print('16: Display all the customers registered')
    print('17: Display details of a particular customer')
    print('18: Display all bookings of a particular customer')
    print('19: Change the admin password')
    print('20: Go back to main menu / LOGOUT')
    print('21: EXIT')
    a_choice=int(input('\nEnter your choice: ')
    if a_choice==1:
        redirecting()
        newFlight()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==2:
        redirecting()
        modifyFlight()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==3:
        redirecting()
        deleteFlight()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==4:
        redirecting()
        searchFlight()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==5:
        redirecting()
        displayAllFlights()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==6:
        redirecting()
        displayAllFlightsDate()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==7:
        redirecting()
        displayAllFlightsAirline()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==8:
        redirecting()
        displayAllFlightsDeparture()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==9:
        redirecting()
        displayAllFlightsArrival()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==10:
        redirecting()
        displayAllBookings()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==11:
        redirecting()
        print('\nDISPLAY A PARTICULAR BOOKING\n')
        displayABooking()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==12:
        redirecting()
        displayAllBookingsDate()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==13:
        redirecting()
        displayAllBookingsAirline()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==14:
        redirecting()
        displayAllBookingsDeparture()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==15:
        redirecting()
        displayAllBookingsArrival()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==16:
        redirecting()
        displayAllCustomers()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==17:
        redirecting()
        displayACustomer()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==18:
        redirecting()
        displayAllBookingsCustomer()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        admin_menu()
    elif a_choice==19:
        redirecting()
        changeAdminPass()
        print('\nAdmin password changed! Log in again to continue.\n')
        redirecting()
        admin_login()
    elif a_choice==20:
        redirecting()
        welcome()
    elif a_choice==21:
        exit()
    else:
        print('\nIncorrect Choice!\n')
        redirecting()
        admin_menu()

def customer_menu(name):
    print('\nCUSTOMER MAIN MENU\n')
    print('1: Make a new booking')
    print('2: Modify an existing booking')
    print('3: Cancel a booking')
    print('4: Search for a booking')
    print('5: View all my bookings')
    print('6: View my profile')
    print('7: Edit my profile')
    print('8: Change my password')
    print('9: Go back to main menu / LOGOUT')
    print('10: EXIT')
    c_choice=int(input('\nEnter your choice: '))
    if c_choice==1:
        redirecting()
        newBooking(name)
        k=input('\n\nPress any key to continue... ')
        redirecting()
        customer_menu()
    elif c_choice==2:
        redirecting()
        modifyBooking()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        customer_menu()
    elif c_choice==3:
        redirecting()
        cancelBooking()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        customer_menu()
    elif c_choice==4:
        redirecting()
        print('\nSEARCH FOR A BOOKING\n')
        searchBooking()
        k=input('\n\nPress any key to continue... ')
        redirecting()
        customer_menu()
    elif c_choice==5:
        redirecting()
        viewAllBookings(name)
        k=input('\n\nPress any key to continue... ')
        redirecting()
        customer_menu()
    elif c_choice==6:
        redirecting()
        viewProfile(name)
        k=input('\n\nPress any key to continue... ')
        redirecting()
        customer_menu()
    elif c_choice==7:
        redirecting()
        editProfile(name)
        k=input('\n\nPress any key to continue... ')
        redirecting()
        customer_menu()
    elif c_choice==8:
        redirecting()
        changeCustomerPass(name)
        print('\nPassword changed! Log in again to continue.\n')
        redirecting()
        customer_login()
    elif c_choice==9:
        redirecting()
        welcome()
    elif c_choice==10:
        exit()
    else:
        print('\nIncorrect Choice!\n')
        redirecting()
        customer_menu()

#----------------------------GENERAL FUNCTIONS----------------------------

def loading_screen():
    print ('\tWELCOME TO')
    airline_name='/\/\/\ MID-WESTERN AIRLINES'
    toolbar_width=len(airline_name)

    #setup toolbar
    sys.stdout.write('%s' % ('' * toolbar_width))
    sys.stdout.flush()

    for i in range(toolbar_width):
        time.sleep(0.12)
        # update the bar
        sys.stdout.write(airline_name[i])
        sys.stdout.flush()

    sys.stdout.write('\n')

def redirecting():
    print('\nREDIRECTING')
    red='/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\'
    toolbar_width=len(red)

    #setup toolbar
    sys.stdout.write('%s' % ('' * toolbar_width))
    sys.stdout.flush()

    for i in range(toolbar_width):
        time.sleep(0.05)
        # update the bar
        sys.stdout.write(red[i])
        sys.stdout.flush()

    os.system('clear')
    print('/\/\/\ MID-WESTERN AIRLINES\n')
    current_time()
    location()

def current_time():
    c=ntplib.NTPClient()
    response=c.request('europe.pool.ntp.org')
    Ctime=ctime(response.tx_time).split()
    print ('\nCurrent date and time: {0} {1} {2}, {4}. {3}\n'.format(Ctime[0],Ctime[1],Ctime[2],Ctime[3],Ctime[4]))

def location():
    f = urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string) #json.loads converts byte stream to dict
    print('Your current location is: {},{},{}'.format(location['city'],location['region_code'],location['country_code']))
    airport_url='http://maps.googleapis.com/maps/api/geocode/json?address=airport,{}&sensor=false'.format(location['city'])
    f1 = urlopen(airport_url)
    json_string1 = f1.read()
    f1.close()
    location1 = json.loads(json_string1)['results']
    print('Nearest airport: ',location1[0]['formatted_address'])
    print()

#----------------------------MENU----------------------------

def welcome():
    os.system('clear')
    loading_screen()
    current_time()
    location()

    print('1 --> ADMINISTRATIONS\n2 --> CUSTOMERS\n3 --> EXIT')
    choice=int(input('\nEnter Your Choice:'))
    if choice==1:
        redirecting()
        st=admin_login()
        if st==1:
            print('\nLOGIN SUCCESSFUL!\n')
            redirecting()
            admin_menu()
        else:
            print('\nINCORRECT PASSWORD! LOGIN FAILED! \n')
            time.sleep(2)
            welcome()
    elif choice==2:
        redirecting()
        print('\n1: New Customer\n2: Existing Customer')
        choice1=int(input('\nEnter your choice: '))
        if choice1==1:
            redirecting()
            customer_sign_up()
            redirecting()
        elif choice1==2: pass
        else:
            print('\nIncorrect Choice!\n')
            redirecting()
            welcome()
        st,name=customer_login()
        if st==1:
            print('\nLOGIN SUCCESSFUL!\n')
            redirecting()
            customer_menu(name)
        else:
            print('\nINVALID USERNAME OR INCORRECT PASSWORD ENTERED MORE THAN 3 TIMES! LOGIN FAILED! \n')
            time.sleep(2)
            welcome()
    elif choice==3:
        exit()
    else:
        print('\nIncorrect Choice!\n')
        redirecting()
        welcome()

def main():
    welcome()
main()
