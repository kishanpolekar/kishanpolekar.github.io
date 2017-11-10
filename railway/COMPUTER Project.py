import string
import pickle
import os
import time
from datetime import datetime
from random import randrange

#--------------------------------------------------------Classes-----------------------------------------------------
class train:
        def __init__(self):
                self.tid=0
                self.tname=None
                self.tfrom=None
                self.tto=None
                self.t1A=0 #First Class AC
                self.tseat1A=0
                self.tprice1A=0
                self.t2A=0 #AC-Two Tier
                self.tseat2A=0
                self.tprice2A=0
                self.tFC=0 #First Class
                self.tseatFC=0
                self.tpriceFC=0
                self.t3A=0 #Ac Three Tier
                self.tseat3A=0
                self.tprice3A=0
                self.t3E=0 #AC Three Tier Economy
                self.tseat3E=0
                self.tprice3E=0
                self.tCC=0 #AC Chair Car
                self.tseatCC=0
                self.tpriceCC=0
                self.tEC=0 #Executive Class Chair Car
                self.tseatEC=0
                self.tpriceEC=0
                self.tSL=0 #Sleeper Class
                self.tseatSL=0
                self.tpriceSL=0
                self.t2S=0 #Seater Class
                self.tseat2S=0
                self.tprice2S=0
                self.ttotalseats=0
                self.date=0
                self.date1=0
        def storedata(self):
                self.tid=eval(input('\nEnter the Train ID:'))
                self.tname=input('\nEnter The Train Name:')
                self.date=input('\nEnter the Starting date of the train (mm/dd/yyyy) : ')
                h1=self.date[3:5]
                h2=self.date[0:2]
                h=int(h2+h1)
                self.date1=h
                self.tfrom=input('\nEnter The Departure Station:')
                self.tto=input('Enter The Arrival Station:')
                self.t1A=eval(input('\nEnter The Number Of First Class AC Coaches (Coach Code - 1A) : '))
                self.tseat1A=self.t1A*18
                self.tprice1A=eval(input('Enter the Price For One First Class AC Coach (Coach Code - 1A) : '))
                self.t2A=eval(input('\nEnter The Number Of AC-Two Tier Coaches (Coach Code - 2A) :  '))
                self.tseat2A=self.t2A*18
                self.tprice2A=eval(input('Enter the Price For One AC-Two Tier Coach : (Coach Code - 2A) : '))
                self.tFC=eval(input('\nEnter The Number Of First Class Coaches (Coach Code - FC) : '))
                self.tseatFC=self.tFC*18
                self.tpriceFC=eval(input('Enter the Price For One First Class Coach (Coach Code - FC) : '))
                self.t3A=eval(input('\nEnter The Number Of AC Three Tier Coaches (Coach Code - 3A) : '))
                self.tseat3A=self.t3A*18
                self.tprice3A=eval(input('Enter the Price For One AC Three Tier Coach  (Coach Code - 3A) : '))
                self.t3E=eval(input('\nEnter The Number Of AC Three Tier Economy Coaches (Coach Code - 3E) : '))
                self.tseat3E=self.t3E*18
                self.tprice3E=eval(input('Enter the Price For One AC Three Tier Economy Coach (Coach Code - 3E) : '))
                self.tCC=eval(input('\nEnter The Number Of AC Chair Car Coaches (Coach Code - CC) : '))
                self.tseatCC=self.tCC*18
                self.tpriceCC=eval(input('Enter the Price For One AC Chair Car Coach (Coach Code - CC) : '))
                self.tEC=eval(input('\nEnter The Number Of Executive Class Chair Car Coaches (Coach Code - EC) : '))
                self.tseatEC=self.tEC*18
                self.tpriceEC=eval(input('Enter the Price For One Executive Class Chair Car Coach (Coach Code - EC) : '))
                self.tSL=eval(input('\nEnter The Number Of Sleeper Class Coaches (Coach Code - SL) : '))
                self.tseatSL=self.tSL*18
                self.tpriceSL=eval(input('Enter the Price For One Sleeper Class Coach (Coach Code - SL) : '))
                self.t2S=eval(input('\nEnter The Number Of Seater Class Coaches (Coach Code - 2S) : '))
                self.tseat2S=self.t2S*18
                self.tprice2S=eval(input('Enter the Price For One Seater Class Coach (Coach Code - 2S) : '))
                self.ttotalseats=self.tseat1A+self.tseat2A+self.tseatFC+self.tseat3A+self.tseat3E+self.tseatCC+self.tseatEC+self.tseatSL+self.tseat2S
        def displaytrain(self):
                print('\nTrain ID : ',self.tid)
                print('Train Name : ',self.tname)
                print('Train Departure Station : ',self.tfrom)
                print('Train Arival Station : ',self.tto)
                print('\n\nNumber OF Seats Of First Class AC Coach (Coach Code - 1A) : ',self.tseat1A  ,'\nPrice For One Coach (Coach Code - 1A) : ',self.tprice1A)
                print('\n\nNumber OF Seats Of AC-Two Tier Coach (Coach Code - 2A) : ',self.tseat2A  ,'\nPrice For One Coach (Coach Code - 2A) : ',self.tprice2A)
                print('\n\nNumber OF Seats Of First Class Coach (Coach Code - FC) : ',self.tseatFC  ,'\nPrice For One Coach (Coach Code - FC) : ',self.tpriceFC)
                print('\n\nNumber OF Seats Of AC Three Tier Coach (Coach Code - 3A) : ',self.tseat3A  ,'\nPrice For One Coach (Coach Code - 3A) : ',self.tprice3A)
                print('\n\nNumber OF Seats Of AC Three Tier Economy Coach (Coach Code - 3E) : ',self.tseat3E  ,'\nPrice For One Coach (Coach Code - 3E) : ',self.tprice3E)
                print('\n\nNumber OF Seats Of AC Chair Car Coach (Coach Code - CC) : ',self.tseatCC  ,'\nPrice For One Coach (Coach Code - CC) : ',self.tpriceCC)
                print('\n\nNumber OF Seats Of Executive Class Chair Coach (Coach Code - EC) : ',self.tseatEC  ,'\nPrice For One Coach (Coach Code - EC) : ',self.tpriceEC)
                print('\n\nNumber OF Seats Of Sleeper Class (Coach Code - SL) : ',self.tseatSL  ,'\nPrice For One Coach (Coach Code - SL) : ',self.tpriceSL)
                print('\n\nNumber OF Seats Of Seater Class (Coach Code - 2S) : ',self.tseat2S  ,'\nPrice For One Coach (Coach Code - 2S) : ',self.tprice2S)
                if self.ttotalseats!=0:
                        pass
                else:
                        self.ttotalseats=self.tseat1A+self.tseat2A+self.tseatFC+self.tseat3A+self.tseat3E+self.tseatCC+self.tseatEC+self.tseatSL+self.tseat2S
                print('\nTotal number of seats in the train : ',self.ttotalseats)
                print('\nStarting date of the train (mm/dd/yyyy) : ',self.date)
        def displaytrain1(self):
                print('\nTrain ID : ',self.tid)
                print('Train Name : ',self.tname)
                print('Train Departure Station : ',self.tfrom)
                print('Train Arival Station : ',self.tto)
                print('Train commencement date : ',self.date)
        def destination(self):
                print('\nFrom : ',self.tfrom,'\tTo : ',self.tto)
                print('Date : ',self.date)



class booking:
        def __init__(self):
                self.customid=0
                self.customname=None
                self.customnumber=None
                self.no_travelling=0
                self.childtravel=0
                self.trainid=0
                self.trainid1=0
                self.trainname=None
                self.coachtype=None
                self.coachtype1=''
                self.strting=None
                self.destination=None
                self.priceadult=0
                self.pricechild=0
                self.totalprice=0
                self.booknumber=0
                self.date=0
        def customerdata(self):

                print("Current Date & Time : " + time.strftime("%c"))
                self.booknumber=randrange(111,98989)
                self.customid=eval(input('\nEnter Customer ID : '))
                self.customname=input('Enter The Customer Name : ')
                self.customnumber=input('Enter Customers\'s Contact Number : ')
                self.no_travelling=eval(input('Enter Total Number of People travelling : '))
                self.childtravel=eval(input('Enter The Number of Childern Travelling : '))

                f1=open("test.dat","ab")
                try:
                    while True:

                                self.strting=input('\nEnter the Departure Station : ')
                                self.destination=input('Enter the Destination Station : ')
                                self.date=input('Enter the date of the journey (mm/dd/yyyy) : ')
                                g1=self.date[3:5]
                                g2=self.date[0:2]
                                g=int(g2+g1)
                                f=open("train.dat","rb")
                                t=train()
                                status=0
                                status3=0
                                try:
                                        while True:
                                                t=pickle.load(f)
                                                if t.tfrom==self.strting and t.tto==self.destination and t.date1==g :
                                                    t.displaytrain1()
                                                    status=1
                                                pickle.dump(t,f1)


                                except EOFError:
                                        f.close()


                                if status==1:

                                                status1=0
                                                self.trainid=eval(input('\n\nEnter Train ID For More Information : '))
                                                f3=open("train.dat","rb")
                                                f4=open("train1.dat","ab")
                                                status1=0
                                                status2=0
                                                try:
                                                        while True:
                                                                t=pickle.load(f3)
                                                                if t.tid==self.trainid:
                                                                        t.displaytrain()
                                                                        status1=eval(input('\nEnter (1 To Select Train / 0 for another Train) : '))
                                                                        while status1==1:
                                                                                self.coachtype=input('\nEnter The COACH CODE (in caps) in which you wish to travel : ')
                                                                                self.trainname=t.tname
                                                                                if self.coachtype=='1A':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tprice1A
                                                                                        self.pricechild=(self.childtravel*t.tprice1A)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseat1A=t.tseat1A-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='First Class AC Coach (Coach Code - 1A)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='2A':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tprice2A
                                                                                        self.pricechild=(self.childtravel*t.tprice2A)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseat2A=t.tseat2A-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='AC-Two Tier Coach (Coach Code - 2A)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='FC':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tpriceFC
                                                                                        self.pricechild=(self.childtravel*t.tpriceFC)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseatFC=t.tseatFC-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='First Class Coach (Coach Code - FC)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='3A':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tprice3A
                                                                                        self.pricechild=(self.childtravel*t.tprice3A)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseat3A=t.tseat3A-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='AC Three Tier Coach (Coach Code - 3A)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='3E':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tprice3E
                                                                                        self.pricechild=(self.childtravel*t.tprice3E)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseat3E=t.tseat3E-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='AC Three Tier Economy Coach (Coach Code - 3E)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='CC':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tpriceCC
                                                                                        self.pricechild=(self.childtravel*t.tpriceCC)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseatCC=t.tseatCC-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='AC Chair Car Coach (Coach Code - CC)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='EC':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tpriceEC
                                                                                        self.pricechild=(self.childtravel*t.tpriceEC)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseatEC=t.tseatEC-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='Executive Class Chair Coach (Coach Code - EC)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='SL':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tpriceSL
                                                                                        self.pricechild=(self.childtravel*t.tpriceSL)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseatSL=t.tseatSL-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='Sleeper Class (Coach Code - SL)'
                                                                                        status2=1
                                                                                        break
                                                                                elif self.coachtype=='2S':
                                                                                        self.priceadult=(self.no_travelling-self.childtravel)*t.tprice2S
                                                                                        self.pricechild=(self.childtravel*t.tprice2S)/2
                                                                                        self.totalprice=self.priceadult+self.pricechild
                                                                                        t.tseat2S=t.tseat2S-self.no_travelling
                                                                                        t.ttotalseats=t.ttotalseats-self.no_travelling
                                                                                        pickle.dump(t,f1)
                                                                                        pickle.dump(t,f4)
                                                                                        self.coachtype1='Seater Class (Coach Code - 2S)'
                                                                                        status2=1
                                                                                        break
                                                                                else:
                                                                                        print('\nThere is no such coach available!')
                                                                                        status1=0
                                                                        if status2==1:
                                                                                print("\nYour booking has been made\n")
                                                                                status3=1
                                                                                break




                                                except EOFError:
                                                    f3.close()
                                                    f4.close()

                                                self.trainid1=self.trainid
                                if status3==1:
                                        break
                                else:pass
                                if status3==1:
                                        pass

                                else:
                                        print('\n\nThere is no train available with the specified destination for the given date. Please select one of the following : \n\n')
                                        f4=open("train.dat","rb")
                                        try:
                                                while True:
                                                        t=pickle.load(f4)
                                                        t.destination()
                                        except EOFError:f4.close()



                except EOFError:
                    f1.close()




        def displaybooking(self):
                print("\n\nBooking id : ",self.booknumber)
                print("\nCustomer ID : ",self.customid)
                print("Customer Name : ",self.customname)
                print("Customer\'s Contact Number : ",self.customnumber)
                print("Date of the journey (mm/dd/yyyy) : ",self.date)
                print("Total Passangers : ",self.no_travelling)
                print("Children Travelling : ",self.childtravel)
                print("Train ID : ",self.trainid1)
                print("Train Name : ",self.trainname)
                print("Preferred Coach : ",self.coachtype1)
                print("Departure Station : ",self.strting)
                print("Arrival Station : ",self.destination)
                print("\nTotal Fare : ",self.totalprice)








#------------------------------FUNCTIONS--------------------------------------------------------------------------------

def admin():
    print('\n\nADMIN LOGIN\n')
    print("\n\nCurrent Date & Time : " + time.strftime("%c"))
    login=input('\nEnter the admin password : ')
    f=open("admin.dat","rb")
    admin_pass=pickle.load(f)
    status=0
    try:
            if login==admin_pass:
                    status=1
                    return(status)
            else:
                    print(' \nWRONG PASSWORD ! LOGIN FAILED. \n')
    except EOFError:
            f.close()
    f.close()
def admin_change():
    print('\n\nADMIN CHANGE PASSWORD\n')
    print("\n\nCurrent Date & Time : " + time.strftime("%c"))
    f=open("admin.dat","wb")
    admin_pass=input('\nEnter the new admin password : ')
    pickle.dump(admin_pass,f)
    f.close()

def newtrain():
        print('\nADDING A TRAIN\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        f=open("train.dat","ab")
        t=train()
        t.storedata()
        pickle.dump(t,f)
        f.close()

def displayalltrain():
        print('\n\nDISPLAYING ALL TRAINS\n\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        f=open("train.dat","rb")
        t=train()
        try:
                while True:
                        t=pickle.load(f)
                        t.displaytrain()
        except EOFError:
                f.close()

def displaytrainsondate():
        print('\n\nDISPLAYING ALL TRAINS ON A PARTICULAR DATE\n\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        d=input('\nEnter the date to be searched (mm/dd/yyyy) :')
        f=open("train1.dat","rb")
        status=0
        t=train()
        try:
                while True:
                        t=pickle.load(f)
                        if t.date==d:
                                t.displaytrain()
                                status=1
        except EOFError:
            f.close()
        if status==0:print('\nTrain Not Found!')

def displaytrainsdepart():
        print('\n\nDISPLAYING DETAILS OF ALL THE TRAINS HAVING A PARTICULAR DEPARTURE POINT\n\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        d=input('\nEnter the departure point to be searched :')
        f=open("train.dat","rb")
        status=0
        t=train()
        try:
                while True:
                        t=pickle.load(f)
                        if t.tfrom==d:
                                t.displaytrain()
                                status=1
        except EOFError:
            f.close()
        if status==0:print('\nTrain Not Found!')

def displaytrainsarrive():
        print('\n\nDISPLAYING DETAILS OF ALL THE TRAINS HAVING A PARTICULAR ARRIVAL POINT\n\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        d=input('\nEnter the arrival point to be searched :')
        f=open("train.dat","rb")
        status=0
        t=train()
        try:
                while True:
                        t=pickle.load(f)
                        if t.tto==d:
                                t.displaytrain()
                                status=1
        except EOFError:
            f.close()
        if status==0:print('\nTrain Not Found!')

def searchtrainadmin():
        print('\nSEARCHING A TRAIN\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        id=eval(input('\nEnter Train ID to be searched : '))
        f=open("train.dat","rb")
        status=0
        t=train()
        try:
                while True:
                        t=pickle.load(f)
                        if t.tid==id:
                                t.displaytrain()
                                status=1
        except EOFError:
            f.close()
        if status==0:print('\nTrain Not Found!')

def modifytrain():
        print('\nMODIFYING A PARTICULAR TRAIN DETAILS\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        id=eval(input('\nEnter Train ID to be modified : '))
        f1=open("train.dat","rb")
        f2=open("newfile.dat","wb")
        t=train()
        status=0
        try:
                while True:
                        t=pickle.load(f1)
                        if t.tid==id:
                                print('\nOriginal Train Details : \n')
                                t.displaytrain()
                                print('\n\nModify the above details now... \n')
                                t.storedata()
                                status=1
                        pickle.dump(t,f2)

        except EOFError:
                f1.close()
                f2.close()

        os.remove("train.dat")
        os.rename("newfile.dat","train.dat")
        if status==1:print('\nThe train details have been modified!')
        else: print('\nTrain Not Found!')

def deletetrain():
        print('\nDELETING A TRAIN\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        id=eval(input('\nEnter Train ID to be removed : '))
        f1=open("train.dat","rb")
        f2=open("newfile.dat","wb")
        t=train()
        status=0
        try:
                while True:
                        t=pickle.load(f1)
                        if t.tid!=id:
                                pickle.dump(t,f2)
                        else:
                                print('\nThe following train has been removed : \n\n')
                                t.displaytrain()
                                status=1
        except EOFError:
                f1.close()
                f2.close()
        os.remove("train.dat")
        os.rename("newfile.dat","train.dat")
        if status==1:
                print("\nTrain details have been Removed!")
        else: print("\nThe specific Train was Not Found!")

def newbook():
        print('\n\nBOOKING\n\n')
        f=open("booking.dat","ab")
        b=booking()
        b.customerdata()
        pickle.dump(b,f)
        b.displaybooking()
        f.close()

def modifybooking():
        print('\n\nMODIFYING A PARTICULAR BOOKING\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        id=eval(input('\nEnter the Booking ID to be modified : '))
        f1=open("booking.dat","rb")
        f2=open("newfile.dat","wb")
        b=booking()
        status=0
        try:
                while True:
                        b=pickle.load(f1)
                        if b.booknumber==id:
                                print('\nBooking found!\n')
                                print('\nModify the booking details now... \n')
                                b.customerdata()
                                status=1
                        pickle.dump(b,f2)

        except EOFError:
                f1.close()
                f2.close()

        os.remove("booking.dat")
        os.rename("newfile.dat","booking.dat")
        if status==1:print('\nThe specified booking has been modified!')
        else: print('\nBooking Not Found!')

def cancelbooking():
        print('\n\nCANCEL A PARTICULAR BOOKING\n')
        print("\n\nCurrent Date & Time : " + time.strftime("%c"))
        id=eval(input('\nEnter Booking ID to be cancelled : '))
        f1=open("booking.dat","rb")
        f2=open("newfile1.dat","wb")
        f3=open("train1.dat","rb")
        f4=open("newfile2.dat","wb")
        b=booking()
        t=train()
        status=0
        try:
                while True:
                        b=pickle.load(f1)
                        t=pickle.load(f3)
                        if b.booknumber!=id:
                                pickle.dump(b,f2)
                                pickle.dump(t,f4)
                        else:
                                print('\nThe following booking has been cancelled : \n\n')
                                b.displaybooking()
                                if b.coachtype=='1A':
                                        t.tseat1A=t.tseat1A+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='2A':
                                        t.tseat2A=t.tseat2A+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='FC':
                                        t.tseatFC=t.tseatFC+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='3A':
                                        t.tseat3A=t.tseat3A+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='3E':
                                        t.tseat3E=t.tseat3E+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='CC':
                                        t.tseatCC=t.tseatCC+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='EC':
                                        t.tseatEC=t.tseatEC+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='SL':
                                        t.tseatSL=t.tseatSL+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                elif b.coachtype=='2S':
                                        t.tseat2S=t.tseat2S+b.no_travelling
                                        t.ttotalseats=t.ttotalseats+b.no_travelling
                                        pickle.dump(t,f4)
                                status=1
        except EOFError:
                f1.close()
                f2.close()
                f3.close()
                f4.close()
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        os.remove("booking.dat")
        os.rename("newfile1.dat","booking.dat")
        os.remove("train1.dat")
        os.rename("newfile2.dat","train1.dat")
        if status==1:
                pass
        else: print("\nThe specific booking was Not Found!")

def searchbooking():
        print('\nSEARCHING FOR A PARTICULAR BOOKING\n')
        print("Current Date & Time : " + time.strftime("%c"))
        cont=input('\nEnter The Customer\'s Contact Number to be searched : ')
        f=open("booking.dat","rb")
        status=0
        b=booking()
        try:
                while True:
                        b=pickle.load(f)
                        if b.customnumber==cont:
                                b.displaybooking()
                                status=1
        except EOFError:
            f.close()
        if status==0:print('\nCustomer Not Found!')


#-------------------------------------------------------------------MENU---------------------------------------------------
def main():

        q='Y'
        while q.upper()=='Y' or q.upper()=='YES':
                pic='''
        _________
           | |
        ___|_|___
        ___|_|___          _   _      _       _          __    __
           / /      /\    | | | |    | |     | |    /\   \ \  / /
         _/ /      /  \   | | | |    | |  _  | |   /  \   \ \/ /
          \ \     /    \  | | | |    | | | | | |  /    \   \  /
           \ \   /  /\  \ | | | |___ | |_| |_| | /  /\  \  / /
            \_\ /__/  \__\|_| |_____||_________|/__/  \__\/_/


                '''
                print(' ',pic,' ')
                print("\n\nCurrent Date & Time : " + time.strftime("%c"))
                print('1 --> ADMINISTRATIONS')
                print('2 --> CUSTOMERS')
                print('3 --> EXIT')
                choice=eval(input('\nEnter Your Choice:'))
                if choice==1:
                    st=admin()
                    if st==1:
                        print('\n1 --> For adding a train')
                        print('2 --> For displaying all the trains')
                        print('3 --> For searching a train')
                        print('4 --> For modifying a particular train')
                        print('5 --> For deleting a particular train')
                        print('6 --> For displaying details of all the trains on a particular date')
                        print('7 --> For displaying details of all the trains having a particular departure point')
                        print('8 --> For displaying details of all the trains having a particular arrival point')
                        print('9 --> For changing admin password')
                        print('10 --> Exit')
                        choice2=eval(input('\nEnter Your Choice:'))
                        if choice2==1:
                                newtrain()
                        elif choice2==2:
                                displayalltrain()
                        elif choice2==3:
                                searchtrainadmin()
                        elif choice2==4:
                                modifytrain()
                        elif choice2==5:
                                deletetrain()
                        elif choice2==6:
                                displaytrainsondate()
                        elif choice2==7:
                                displaytrainsdepart()
                        elif choice2==8:
                                displaytrainsarrive()
                        elif choice2==9:
                                admin_pass=admin_change()
                        elif choice2==10:
                                exit()
                        else:
                                print('\nWrong Choice!\n')
                    else:pass
                elif choice==2:
                        print("1 --> To make a new booking")
                        print("2 --> To modify a particular booking")
                        print("3 --> To cancel a particular booking")
                        print("4 --> To search a particular booking")
                        print("5 --> Exit")
                        ch=eval(input('\nEnter your choice:'))
                        if ch==1:
                                newbook()
                        elif ch==2:
                                searchbooking()
                                modifybooking()
                        elif ch==3:
                                searchbooking()
                                cancelbooking()
                        elif ch==4:
                                searchbooking()
                        elif ch==5:
                                exit()
                        else:
                                print('\nWrong Choice!\n')
                elif choice==3:
                        exit()
                else:
                                print('\nWrong Choice!\n')
                q=input('\nDo you want to continue? (Y/N) : ')

main()
