import os,pickle

class Product:
    def __init__(self):
        self.id=0
        self.name=None
        self.price=0.0
        self.qty=0
        self.__totalValue=0.0

    def newProduct(self):
        self.id=int(input('\nEnter the ID of the item: '))
        self.name=input('Enter the name of the item: ')
        self.price=float(input('Enter the price of ONE unit of the item: '))
        self.qty=int(input('Enter the quantity of the item(s) added to the inventory: '))
        self.__totalValue+=(self.price*self.qty)

    def modifyProduct(self):
        id=int(input('\nEnter the product ID to be modified : '))
        f1=open("product.dat","rb")
        f2=open("newfile.dat","wb")
        status=0
        try:
            while True:
                self=pickle.load(f1)
                if self.id==id:
                    print('\nProduct found!\nModify the product details now... \n')
                    self.__totalValue-=self.price*self.qty
                    self.newProduct()
                    status=1
                pickle.dump(self,f2)

        except EOFError:
            f1.close()
            f2.close()

        os.remove("product.dat")
        os.rename("newfile.dat","product.dat")
        if status==1:print('\nThe specified product details have been modified!')
        else: print('\nProduct Not Found!')

    def deleteProduct(self):
        id=int(input('\nEnter the product ID to be deleted : '))
        f1=open("product.dat","rb")
        f2=open("newfile.dat","wb")
        status=0
        try:
            while True:
                    self=pickle.load(f1)
                    if self.id!=id:
                        pickle.dump(self,f2)
                    else:
                        print('\nProduct found!\nDeleting the following product now... \n')
                        self.__totalValue-=self.price*self.qty
                        self.displayProduct()
                        status=1

        except EOFError:
            f1.close()
            f2.close()

        os.remove("product.dat")
        os.rename("newfile.dat","product.dat")
        if status==1: pass
        else: print('\nProduct Not Found!')

    def searchProduct(self):
        nid=input('\nSearch for the product based on name or ID? ')
        if nid.lower()=='name':
            name=input('\nEnter the name of the product to be searched: ')
            f=open("product.dat","rb")
            status=0
            try:
                while True:
                    self=pickle.load(f)
                    if self.name.lower()==name.lower():
                        print('\nProduct found!\nProduct details are: \n')
                        self.displayProduct()
                        status=1
            except EOFError:
                f.close()
            if status==0:
                print('\nProduct Not Found!')

        elif nid.lower()=='id':
            id=int(input('\nEnter the ID of the product to be searched: '))
            f=open("product.dat","rb")
            status=0
            try:
                while True:
                    self=pickle.load(f)
                    if self.id==id:
                        print('\nProduct found!\nProduct details are: \n')
                        self.displayProduct()
                        status=1
            except EOFError:
                f.close()
            if status==0:
                print('\nProduct Not Found!')
        else:
            print('\nIncorrect Input!\n')
            self.searchProduct()

    def displayProduct(self):
        print('\nProduct ID: {}\nProduct Name: {}\nUnit Price: ${}\nQuantity in hand: {}\nTotal price of the items: ${}\n'.format(self.id,self.name,self.price,self.qty,self.__totalValue))

    def displayInventory(self):
        TotalItems,TotalValue=0,0.0
        f=open("product.dat","rb")
        try:
            while True:
                self=pickle.load(f)
                TotalItems+=self.qty
                TotalValue+=self.price*self.qty
        except EOFError:
            f.close()

        print('\nThe total number of items in the inventory are: {}.\nThe total value of these products is: ${}.'.format(TotalItems,TotalValue))

    def displayAll(self):
        f=open("product.dat","rb")
        try:
            while True:
                self=pickle.load(f)
                self.displayProduct()
        except EOFError:
                f.close()

def main():
    choice='Y'
    while choice.lower()=='y':
        os.system('clear')
        print('PRODUCT INVENTORY\n\n1-Adding a new product\n2-Modifying an existing product\n3-Deleting a product\n4-Searching a product\n5-Display the total inventory value\n6-Display all items and their information\n7-Delete all items from inventory\n8-Exit')
        ch=int(input('\nEnter your choice: '))
        os.system('clear')
        print('PRODUCT INVENTORY')
        if ch==1:
            print('\nADD A NEW PRODUCT\n')
            p=Product()
            f=open("Product.dat","ab")
            p.newProduct()
            pickle.dump(p,f)
            print('\nProduct added to inventory: \n')
            p.displayProduct()
            f.close()
        elif ch==2:
            print('\nMODIFY A PRODUCT INFORMATION\n')
            p=Product()
            p.modifyProduct()
        elif ch==3:
            print('\nDELETING A PRODUCT\n')
            p=Product()
            p.deleteProduct()
        elif ch==4:
            print('\nSEARCHING A PRODUCT\n')
            p=Product()
            p.searchProduct()
        elif ch==5:
            print('\nDISPLAY TOTAL INVENTORY VALUE\n')
            p=Product()
            p.displayInventory()
        elif ch==6:
            print('\nDISPLAY ENTIRE INVENTORY\n')
            p=Product()
            p.displayAll()
        elif ch==7:
            print('\nEMPTY INVENTORY\n')
            sure=input('Are you sure you want to empty the inventory? (Y/N): ')
            if sure.lower()=='y' or sure.lower()=='yes':
                f=open("product.dat","wb")
                f.close()
                print('\nInventory is empty now!\n')
            else: print('\nAlright... Nothing done!\n')
        elif ch==8:
            print('\nExiting the inventory...\n')
            exit()
        else: print('\nWrong Choice!!\n')
        choice=input('\nDo you want to continue? (y/n): ')
main()
