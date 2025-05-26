#Importing Tkinter Module!
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

#password= ifpcjvanhgdnilkl
#FUNCTIONALITY PART:BILL BUTTON
def clear():
      #cosmetics
      bathsoapEntry.delete(0,END)
      facecreamEntry.delete(0,END)
      hairsprayEntry.delete(0,END)
      hairgelEntry.delete(0,END)
      bodylotionEntry.delete(0,END)
      facewashEntry.delete(0,END)
      hairserumEntry.delete(0,END)
      #grocery
      riceEntry.delete(0,END)
      oilEntry.delete(0,END)
      dalEntry.delete(0,END)
      sugarEntry.delete(0,END)
      wheatEntry.delete(0,END)
      legumesEntry.delete(0,END)
      teaEntry.delete(0,END)
      #drinks
      maazaEntry.delete(0,END)
      pepsiEntry.delete(0,END)
      spriteEntry.delete(0,END)
      dewEntry.delete(0,END)
      frootiEntry.delete(0,END)
      CocaColaEntry.delete(0,END)
      fantaEntry.delete(0,END)

      #cosmetics
      bathsoapEntry.insert(0,0)
      facecreamEntry.insert(0,0)
      hairsprayEntry.insert(0,0)
      hairgelEntry.insert(0,0)
      bodylotionEntry.insert(0,0)
      facewashEntry.insert(0,0)
      hairserumEntry.insert(0,0)
      #grocery
      riceEntry.insert(0,0)
      oilEntry.insert(0,0)
      dalEntry.insert(0,0)
      sugarEntry.insert(0,0)
      wheatEntry.insert(0,0)
      legumesEntry.insert(0,0)
      teaEntry.insert(0,0)
      #drinks
      maazaEntry.insert(0,0)
      pepsiEntry.insert(0,0)
      spriteEntry.insert(0,0)
      dewEntry.insert(0,0)
      frootiEntry.insert(0,0)
      CocaColaEntry.insert(0,0)
      fantaEntry.insert(0,0)
      #cosmetics
      cosmeticpriceEntry.delete(0,END)
      grocerypriceEntry.delete(0,END)
      colddrinkpriceEntry.delete(0,END)
      #cosmetictax
      cosmetictaxEntry.delete(0,END)
      grocerytaxEntry.delete(0,END)
      colddrinktaxEntry.delete(0,END)
      #clearation of old data on following field
      nameEntry.delete(0,END)
      phoneEntry.delete(0,END)
      billnumberEntry.delete(0,END)
      textarea.delete(1.0,END)

def send_email():
      def send_gmail():
            #Helps establishing a secure connection
            try:
                  ob=smtplib.SMTP('smtp.gmail.com',587)
                  ob.starttls()
                  ob.login(senderEntry.get(),passwordEntry.get())
                  message=email_textarea.get(1.0,END)
                  ob.sendmail(senderEntry.get(),receiverEntry.get(),message)
                  ob.quit()
                  messagebox.showinfo('Success', 'Email Sent Successfully',parent=root1)
            except:
                  messagebox.showerror('Error','Something went wrong, Please try again.',parent=root1)

      if textarea.get(1.0,END)=='\n':
            messagebox.showerror('Error','Bill is empty')
      else:
            root1=Toplevel()
            root1.title('Send gmail')
            root1.config(bg='gray20')
            root1.resizable(0,0)

            senderFrame=LabelFrame(root1, text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
            senderFrame.grid(row=0, column=0, padx=40, pady=20)

            senderlabel=Label(senderFrame,text="Email", font=('arial',14,'bold'),bg='gray20',fg='white')
            senderlabel.grid(row=0, column=0,padx=10,pady=8)

            senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
            senderEntry.grid(row=0,column=1,padx=10,pady=8)

            passwordlabel=Label(senderFrame,text="Password", font=('arial',14,'bold'),bg='gray20',fg='white')
            passwordlabel.grid(row=1, column=0,padx=10,pady=8)

            passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE, show='*')
            passwordEntry.grid(row=1,column=1,padx=10,pady=8)

            recepientFrame=LabelFrame(root1, text='RECEPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
            recepientFrame.grid(row=1, column=0, padx=40, pady=20)
            
            receiverlabel=Label(recepientFrame,text="Email", font=('arial',14,'bold'),bg='gray20',fg='white')
            receiverlabel.grid(row=0, column=0,padx=10,pady=8)

            receiverEntry=Entry(recepientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
            receiverEntry.grid(row=0, column=1,padx=10,pady=8)

            messagelabel=Label(recepientFrame,text="Message", font=('arial',14,'bold'),bg='gray20',fg='white')
            messagelabel.grid(row=1, column=0,padx=10,pady=8)

            email_textarea=Text(recepientFrame, font=('arial',14,'bold'), bd=2, relief=SUNKEN, width=42, height=11)
            email_textarea.grid(row=2,column=0,columnspan=2)
            email_textarea.delete(1.0, END)
            email_textarea.insert(END,textarea.get(1.0, END).replace('=','').replace('-','').replace('\t\t\t\t\t\t\t\t','\t\t'))

            sendButton=Button(root1, text='SEND',font=('arial', 16, 'bold'),width=15,command=send_gmail)
            sendButton.grid(row=2, column=0, pady=20)

      root1.mainloop()

def print_bill():
      if textarea.get(1.0,END)=='\n':
            messagebox.showerror('Error','Bill is empty')
      else:
           file=tempfile.mktemp('.txt')
           open(file,'w').write(textarea.get(1.0,END))
           os.startfile(file,'print')

def search_bill():
      for i in os.listdir('bills/'):
            if i.split('.')[0]==billnumberEntry.get():
                  f=open(f'bills/{i}','r')
                  textarea.delete(1.0, END)
                  for data in f:
                        textarea.insert(END, data)
                  f.close()
                  break
            else:
                  messagebox.showerror('Error','Bill Number Does not Exist!')
                        
if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('confirm', 'Do you want to Save the Bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill number {billnumber} is saved successfully')
        billnumber = random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
         messagebox.showerror('Error','Customer Details required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and colddrinkpriceEntry.get()=='':
         messagebox.showerror('Error','No products are selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and colddrinkpriceEntry.get()=='0 Rs':
         messagebox.showerror('Error','No products are selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\t\t\t\t**Welcome Customer**\n')
        textarea.insert(END, f'\n\n Bill Number: {billnumber}')
        textarea.insert(END, f'\n Customer Name: {nameEntry.get()}')
        textarea.insert(END, f'\n Customer Phone Number: {phoneEntry.get()}')
        textarea.insert(END, '\n======================================================================================')
        textarea.insert(END, '\n Product\t\t\t\tQuantity\t\t\t\t\tPrice')
        textarea.insert(END, '\n======================================================================================')
        #Cosmetics Bill part 
        if bathsoapEntry.get()!='0':
              textarea.insert(END,F'\n Bath soap\t\t\t\t{bathsoapEntry.get()}\t\t\t\t\t{soapprice} Rs')
        if hairsprayEntry.get()!='0':
              textarea.insert(END,F'\n Hair Spray\t\t\t\t{hairsprayEntry.get()}\t\t\t\t\t{hairsprayprice} Rs')
        if facecreamEntry.get()!='0':
              textarea.insert(END,F'\n Face Cream\t\t\t\t{facecreamEntry.get()}\t\t\t\t\t{facecreamprice} Rs')
        if facewashEntry.get()!='0':
              textarea.insert(END,F'\n Face Wash\t\t\t\t{facewashEntry.get()}\t\t\t\t\t{facewashprice} Rs')
        if bodylotionEntry.get()!='0':
              textarea.insert(END,F'\n Body Lotion\t\t\t\t{bodylotionEntry.get()}\t\t\t\t\t{bodylotionprice} Rs')
        if hairgelEntry.get()!='0':
              textarea.insert(END,F'\n Hair Gel\t\t\t\t{hairgelEntry.get()}\t\t\t\t\t{hairgelprice} Rs')
        #Grocery Bill part
        if riceEntry.get()!='0':
              textarea.insert(END,F'\n Rice\t\t\t\t{riceEntry.get()}\t\t\t\t\t{riceprice} Rs')
        if dalEntry.get()!='0':
              textarea.insert(END,F'\n Dal\t\t\t\t{dalEntry.get()}\t\t\t\t\t{dalprice} Rs')
        if oilEntry.get()!='0':
              textarea.insert(END,F'\n Oil\t\t\t\t{oilEntry.get()}\t\t\t\t\t{oilprice} Rs')
        if wheatEntry.get()!='0':
              textarea.insert(END,F'\n Wheat\t\t\t\t{wheatEntry.get()}\t\t\t\t\t{wheatprice} Rs')
        if sugarEntry.get()!='0':
              textarea.insert(END,F'\n Sugar\t\t\t\t{sugarEntry.get()}\t\t\t\t\t{sugarprice} Rs')
        if legumesEntry.get()!='0':
              textarea.insert(END,F'\n Legumes\t\t\t\t{legumesEntry.get()}\t\t\t\t\t{legumesprice} Rs')
        if teaEntry.get()!='0':
              textarea.insert(END,F'\n Tea\t\t\t\t{teaEntry.get()}\t\t\t\t\t{Teaprice} Rs')
        #Cold drink Bill part
        if maazaEntry.get()!='0':
              textarea.insert(END,F'\n Maaza\t\t\t\t{maazaEntry.get()}\t\t\t\t\t{maazaprice} Rs')
        if spriteEntry.get()!='0':
              textarea.insert(END,F'\n Sprite\t\t\t\t{spriteEntry.get()}\t\t\t\t\t{spriteprice} Rs')
        if dewEntry.get()!='0':
              textarea.insert(END,F'\n Dew\t\t\t\t{dewEntry.get()}\t\t\t\t\t{dewprice} Rs')
        if pepsiEntry.get()!='0':
              textarea.insert(END,F'\n Pepsi\t\t\t\t{pepsiEntry.get()}\t\t\t\t\t{pepsiprice} Rs')
        if frootiEntry.get()!='0':
              textarea.insert(END,F'\n Frooti\t\t\t\t{frootiEntry.get()}\t\t\t\t\t{frootiprice} Rs')
        if CocaColaEntry.get()!='0':
              textarea.insert(END,F'\n Coca Cola\t\t\t\t{CocaColaEntry.get()}\t\t\t\t\t{cocacolaprice} Rs')
        if fantaEntry.get()!='0':
              textarea.insert(END,F'\n Fanta\t\t\t\t{fantaEntry.get()}\t\t\t\t\t{fantaprice} Rs')
        textarea.insert(END, '\n======================================================================================')
        
        #Tax Bill Part
        if cosmetictaxEntry.get()!='0.0 Rs':
              textarea.insert(END,f'\n Cosmetic Tax\t\t\t\t\t\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
              textarea.insert(END,f'\n Grocery Tax\t\t\t\t\t\t\t\t\t{grocerytaxEntry.get()}')
        if colddrinktaxEntry.get()!='0.0 Rs':
              textarea.insert(END,f'\n Cold Drink Tax\t\t\t\t\t\t\t\t\t{colddrinktaxEntry.get()}')
        textarea.insert(END,f'\n\n Total Bill \t\t\t\t\t\t\t\t\t{totalbill} Rs')
        textarea.insert(END, '\n======================================================================================')
        save_bill()
        
#FUNCTIONALITY Part:TOTAL BUTTON
def total():
    #cosmetic price widget calculation part
    global soapprice,hairsprayprice,facecreamprice,facewashprice,bodylotionprice,hairgelprice
    global riceprice,dalprice,legumesprice,wheatprice,oilprice,Teaprice,sugarprice
    global maazaprice,pepsiprice,spriteprice,dewprice,frootiprice,cocacolaprice,fantaprice
    global totalcosmeticprice,totalcolddrinkprice,totalgroceryprice,cosmetictax,grocerytax,colddrinktax
    global totalbill
    soapprice=float(bathsoapEntry.get())*35 #per 75 gram
    facecreamprice=float(facecreamEntry.get())*90 #per 80 gram
    facewashprice=float(facewashEntry.get())*55 #per 110 ml
    hairsprayprice=float(hairsprayEntry.get())*99 #per 150 gram
    hairgelprice=float(hairgelEntry.get())*99 #per 100 ml
    bodylotionprice=float(bodylotionEntry.get())*150 #per 300 ml
    #Total cosmetic price
    totalcosmeticprice = soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    #cosmetictax calculation
    cosmetictax = totalcosmeticprice*0.5
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, str(cosmetictax)+ ' Rs')

    #grocery price calculation
    riceprice=float(riceEntry.get())*20 #per kg
    oilprice=float(oilEntry.get())*120 #per litre
    dalprice=float(dalEntry.get())*110 #per 1kg
    wheatprice=float(wheatEntry.get())*150 #per kg
    sugarprice=float(sugarEntry.get())*160 #per kg
    legumesprice=float(legumesEntry.get())*125 #per kg
    Teaprice=float(teaEntry.get())*100 #per 800 gram
    #Total grocery price
    totalgroceryprice=riceprice+oilprice+dalprice+wheatprice+sugarprice+legumesprice+Teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, str(totalgroceryprice)+' Rs')
    #Grocery Tax Calculation
    grocerytax=totalgroceryprice*0.3
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax)+' Rs')

    #cold-drink price calculation
    maazaprice=float(maazaEntry.get())*40 # per a 100 ml bottle
    pepsiprice=float(pepsiEntry.get())*50 # per a 130 ml bottle
    spriteprice=float(spriteEntry.get())*35 # per a 100ml bottle
    dewprice=float(dewEntry.get())*60 # per a 160 ml bottle
    frootiprice=float(frootiEntry.get())*60 # per a 150 ml bottle
    cocacolaprice=float(CocaColaEntry.get())*60 # per a 100 ml bottle
    fantaprice=float(fantaEntry.get())*55 #per a 120 ml bottle
    #Total cold drink Price
    totalcolddrinkprice=maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocacolaprice+fantaprice
    colddrinkpriceEntry.delete(0, END)
    colddrinkpriceEntry.insert(0,str(totalcolddrinkprice)+ ' Rs')
    #Cold drink tax calculation
    colddrinktax=totalcolddrinkprice*0.4
    colddrinktaxEntry.delete(0, END)
    colddrinktaxEntry.insert(0, str(colddrinktax)+' Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinkprice+cosmetictax+grocerytax+colddrinktax


#GUI
#for creating a blank default sized window
root = Tk()

#for setting a title on the top of the window
root.title('Retail Billing System')

#for changing the size of the window 
root.geometry('1278x685')

#for setting the icon or logo in the window 
root.iconbitmap('iconpurple.ico')

#Creating a object variable named "headinglabel" and adding the heading-label through the label class and beautifying it.
#relief attribute is used to set the style of a widget which possibly is a 3-D effect arround the outside of the widget.
headinglable = Label(root, text = 'Retail Billing System', font = ('Times New Roman',30,'bold'), bg = 'gray20', fg = 'gold', bd = 12, relief = GROOVE)

#Setting the heading label at the top dimension
headinglable.pack(fill = X, pady = 10)

#CUSTOMER DETAILS FRAME
#For creating the customer detail containing widget that includes Name, Phone Number, Bill Number and a search button to search the associated invoice information.
customer_details_frame = LabelFrame(root, text = 'Customer Details', font = ('Times New Roman',15,'bold'), fg = 'gold', bd = 8, relief = GROOVE, bg = 'gray20')
customer_details_frame.pack(fill=X)

#for creating the label Name, beautifying and adjusting it.
nameLabel = Label(customer_details_frame, text = 'Name', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
nameLabel.grid(row = 0, column = 0, padx = 20, pady = 2)

#for creating the entry field for the label 'Name'.
nameEntry = Entry(customer_details_frame, font = ('Times New Roman', 15), bd = 7, width = 22)
nameEntry.grid(row = 0 , column = 1, padx= 8)

#for creating the label Phone, beautifying and adjusting it.
phoneLabel = Label(customer_details_frame, text = 'Phone', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
phoneLabel.grid(row = 0, column = 2, padx = 20, pady = 2)

#for creating the entry field for the label 'Phone'
phoneEntry = Entry(customer_details_frame, font = ('Times New Roman', 15), bd = 7, width = 22)
phoneEntry.grid(row = 0 , column = 3, padx = 8)

#for creating the label Bill Number, beautifying and adjusting it.
billnumberLabel = Label(customer_details_frame, text = 'Bill Number', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
billnumberLabel.grid(row = 0, column = 4, padx = 20, pady = 2)

#for creating the entry field for the label 'Bill Number'.
billnumberEntry = Entry(customer_details_frame, font = ('Times New Roman', 15), bd = 7, width = 22)
billnumberEntry.grid(row = 0, column = 5, padx= 8)

#for creating the search button to search the data regarding the Bill or assigned invoice number.
searchButton = Button(customer_details_frame, text = 'SEARCH', font = ('Times New Roman',13, 'bold'), bd = 7, width = 10,command=search_bill)
searchButton.grid(row = 0, column = 6, padx = 20, pady = 8)

#PRODUCT DETAILS FRAME
#for creating a product frame to add 3 widget inside it for product lable with their entry field.
productsFrame = Frame(root)
productsFrame.pack(fill=X)

#for creating the cosmetics frame
cosmeticsFrame = LabelFrame(productsFrame, text = 'Cosmetics',font = ('Times New Roman',15,'bold'), fg = 'gold', bd = 8, relief = GROOVE, bg = 'gray20')
cosmeticsFrame.grid(row = 0, column = 0, pady = 8)

#for creating the Bath Soap Label.
bathsoapLabel = Label(cosmeticsFrame,  text = 'Bath Soap', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
bathsoapLabel.grid(row = 0, column = 0,  padx = 10, pady = 9, sticky = 'w')

bathsoapEntry = Entry(cosmeticsFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
bathsoapEntry.grid(row = 0, column = 1, padx = 10, pady = 9)
bathsoapEntry.insert(0,0)

#for creating the Face Cream Soap Label.
facecreamLabel = Label(cosmeticsFrame,  text = 'Face Cream', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
facecreamLabel.grid(row = 1, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Face Cream Label
facecreamEntry = Entry(cosmeticsFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
facecreamEntry.grid(row = 1, column = 1, padx = 10, pady = 9)
facecreamEntry.insert(0,0)

#for creating the Face Wash Label.
facewashLabel = Label(cosmeticsFrame,  text = 'Face Wash', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
facewashLabel.grid(row = 2, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Face wash Label
facewashEntry = Entry(cosmeticsFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
facewashEntry.grid(row = 2, column = 1, padx = 10, pady = 9)
facewashEntry.insert(0,0)

#for creating the Hair Spray Label.
hairsprayLabel = Label(cosmeticsFrame,  text = 'Hair Spray', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
hairsprayLabel.grid(row = 3, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Hair Spray Label
hairsprayEntry = Entry(cosmeticsFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
hairsprayEntry.grid(row = 3, column = 1, padx = 10, pady = 9)
hairsprayEntry.insert(0,0)

#for creating the Hair Serum Label.
hairserumLabel = Label(cosmeticsFrame,  text = 'Hair Serum', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
hairserumLabel.grid(row = 4, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Hair Serum Label
hairserumEntry = Entry(cosmeticsFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
hairserumEntry.grid(row = 4, column = 1, padx = 10, pady = 9)
hairserumEntry.insert(0,0)

#for creating the Hair Gel Label.
hairgelLabel = Label(cosmeticsFrame,  text = 'Hair Gel', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
hairgelLabel.grid(row = 5, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Hair Gel Label
hairgelEntry = Entry(cosmeticsFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
hairgelEntry.grid(row = 5, column = 1, padx = 10, pady = 9)
hairgelEntry.insert(0,0)

#for creating the Body Lotion Label.
bodylotionLabel = Label(cosmeticsFrame,  text = 'Body Lotion', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
bodylotionLabel.grid(row = 6, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Body Lotion Label
bodylotionEntry = Entry(cosmeticsFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
bodylotionEntry.grid(row = 6, column = 1, padx = 10, pady = 9)
bodylotionEntry.insert(0,0)

#GROCERY LABEL FRAME
#for creating the Grocery frame
groceryFrame = LabelFrame(productsFrame, text = 'Grocery',font = ('Times New Roman',15,'bold'), fg = 'gold', bd = 8, relief = GROOVE, bg = 'gray20')
groceryFrame.grid(row = 0, column = 1, padx = 8)

#for creating the Rice Label.
riceLabel = Label(groceryFrame,  text = 'Rice', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
riceLabel.grid(row = 0, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Rice.
riceEntry = Entry(groceryFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
riceEntry.grid(row = 0, column = 1, padx = 10, pady = 9)
riceEntry.insert(0,0)

#for creating the oil Label.
oilLabel = Label(groceryFrame,  text = 'Oil', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
oilLabel.grid(row = 1, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Oil.
oilEntry = Entry(groceryFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
oilEntry.grid(row = 1, column = 1, padx = 10, pady = 9)
oilEntry.insert(0,0)

#for creating the Dal Label.
dalLabel = Label(groceryFrame,  text = 'Dal', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
dalLabel.grid(row = 2, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Dal.
dalEntry = Entry(groceryFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
dalEntry.grid(row = 2, column = 1, padx = 10, pady = 9)
dalEntry.insert(0,0)

#for creating the wheat Label.
wheatLabel = Label(groceryFrame,  text = 'Wheat', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
wheatLabel.grid(row = 3, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Oil.
wheatEntry = Entry(groceryFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
wheatEntry.grid(row = 3, column = 1, padx = 10, pady = 9)
wheatEntry.insert(0,0)

#for creating the Sugar Label.
sugarLabel = Label(groceryFrame,  text = 'Sugar', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
sugarLabel.grid(row = 4, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Sugar.
sugarEntry = Entry(groceryFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
sugarEntry.grid(row = 4, column = 1, padx = 10, pady = 9)
sugarEntry.insert(0,0)

#for creating the legumes Label.
legumesLabel = Label(groceryFrame,  text = 'Legumes', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
legumesLabel.grid(row = 5, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label legumes.
legumesEntry = Entry(groceryFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
legumesEntry.grid(row = 5, column = 1, padx = 10, pady = 9)
legumesEntry.insert(0,0)

#for creating the Tea Label.
teaLabel = Label(groceryFrame,  text = 'Tea', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
teaLabel.grid(row = 6, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Tea.
teaEntry = Entry(groceryFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
teaEntry.grid(row = 6, column = 1, padx = 10, pady = 9)
teaEntry.insert(0,0)

#DRINKS LABEL FRAME
#for creating the Drinks frame
colddrinksFrame = LabelFrame(productsFrame, text = 'Cold Drinks',font = ('Times New Roman',15,'bold'), fg = 'gold', bd = 8, relief = GROOVE, bg = 'gray20')
colddrinksFrame.grid(row = 0, column = 2)

#for creating the maaza Label.
maazaLabel = Label(colddrinksFrame,  text = 'Maaza', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
maazaLabel.grid(row = 0, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Maaza.
maazaEntry = Entry(colddrinksFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
maazaEntry.grid(row = 0, column = 1, padx = 10, pady = 9)
maazaEntry.insert(0,0)

#for creating the pepsi Label.
pepsiLabel = Label(colddrinksFrame,  text = 'Pepsi', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
pepsiLabel.grid(row = 1, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label pepsi.
pepsiEntry = Entry(colddrinksFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
pepsiEntry.grid(row = 1, column = 1, padx = 10, pady = 9)
pepsiEntry.insert(0,0)

#for creating the Sprite Label.
spriteLabel = Label(colddrinksFrame,  text = 'Sprite', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
spriteLabel.grid(row = 2, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label sprite.
spriteEntry = Entry(colddrinksFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
spriteEntry.grid(row = 2, column = 1, padx = 10, pady = 9)
spriteEntry.insert(0,0)

#for creating the Dew Label.
dewLabel = Label(colddrinksFrame,  text = 'Dew', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
dewLabel.grid(row = 3, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label sprite.
dewEntry = Entry(colddrinksFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
dewEntry.grid(row = 3, column = 1, padx = 10, pady = 9)
dewEntry.insert(0,0)

#for creating the frooti label
frootiLabel = Label(colddrinksFrame,  text = 'Frooti', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
frootiLabel.grid(row = 4, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label frooti.
frootiEntry = Entry(colddrinksFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
frootiEntry.grid(row = 4, column = 1, padx = 10, pady = 9)
frootiEntry.insert(0,0)

#for creating the CocaCola label
CocaColaLabel = Label(colddrinksFrame, text = 'Coca Cola', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
CocaColaLabel.grid(row = 5, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label Coca Cola.
CocaColaEntry = Entry(colddrinksFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
CocaColaEntry.grid(row = 5, column = 1, padx = 10, pady = 9)
CocaColaEntry.insert(0,0)

#for creating the fanta label
fantaLabel = Label(colddrinksFrame, text = 'Fanta', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
fantaLabel.grid(row = 6, column = 0, padx = 10, pady = 9, sticky = 'w')

#for creating the entry field for the Label fanta.
fantaEntry = Entry(colddrinksFrame, font = ('Times New Roman', 15, 'bold'), width = 10, bd = 5)
fantaEntry.grid(row = 6, column = 1, padx = 10, pady = 9)
fantaEntry.insert(0,0)

#for creating the Bill area.
billFrame = Frame(productsFrame, bd =8, relief = GROOVE)
billFrame.grid(row = 0, column = 3,pady = 4, padx = 8)

billareaLabel = Label(billFrame, text = 'Bill Area', font = ('Times New Roman',15, 'bold'), bd = 7, relief = GROOVE)
billareaLabel.pack()

scrollbar = Scrollbar(billFrame, orient = VERTICAL)
scrollbar.pack(side = RIGHT, fill = Y)
textarea = Text(billFrame, height = 21.5, width = 86, yscrollcommand = scrollbar.set)
textarea.pack()
scrollbar.config(command = textarea.yview)

#BILL MENU FRAME
#for creating the bill menu frame
billmenuFrame = LabelFrame(root, text = 'Bill Menu',font = ('Times New Roman',15,'bold'), fg = 'gold', bd = 8, relief = GROOVE, bg = 'gray20')
billmenuFrame.pack(fill = X, pady = 4)

#for creating the cosmetic price label
cosmeticpriceLabel = Label(billmenuFrame, text = 'Cosmetic Price', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
cosmeticpriceLabel.grid(row = 0, column = 0, padx = 10, pady = 8, sticky = 'w')

#for creating the entry field for the Label cosmetic price.
cosmeticpriceEntry = Entry(billmenuFrame, font = ('Times New Roman', 15, 'bold'), width = 20, bd = 5)
cosmeticpriceEntry.grid(row = 0, column = 1, padx = 10, pady = 8)

#for creating the grocery price label
grocerypriceLabel = Label(billmenuFrame, text = 'Grocery Price', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
grocerypriceLabel.grid(row = 1, column = 0, padx = 10, pady = 8, sticky = 'w')

#for creating the entry field for the Label grocery price.
grocerypriceEntry = Entry(billmenuFrame, font = ('Times New Roman', 14, 'bold'), width = 20, bd = 5)
grocerypriceEntry.grid(row = 1, column = 1, padx = 10, pady = 8)

#for creating the colddrink price label
colddrinkpriceLabel = Label(billmenuFrame, text = 'Cold Drink Price', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
colddrinkpriceLabel.grid(row = 2, column = 0, padx = 10, pady = 8, sticky = 'w')

#for creating the entry field for the Label colddrink price.
colddrinkpriceEntry = Entry(billmenuFrame, font = ('Times New Roman', 15, 'bold'), width = 20, bd = 5)
colddrinkpriceEntry.grid(row = 2, column = 1, padx = 10, pady = 8)

#for creating the cosmetic tax label
cosmetictaxLabel = Label(billmenuFrame, text = 'Cosmetic Tax', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
cosmetictaxLabel.grid(row = 0, column = 2, padx = 10, pady = 8, sticky = 'w')

#for creating the entry field for the Label cosmetic tax.
cosmetictaxEntry = Entry(billmenuFrame, font = ('Times New Roman', 15, 'bold'), width = 20, bd = 5)
cosmetictaxEntry.grid(row = 0, column = 3, padx = 10, pady = 8)

#for creating the grocery tax label
grocerytaxLabel = Label(billmenuFrame, text = 'Grocery Tax', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
grocerytaxLabel.grid(row = 1, column = 2, padx = 10, pady = 8, sticky = 'w')

#for creating the entry field for the Label grocery tax.
grocerytaxEntry = Entry(billmenuFrame, font = ('Times New Roman', 15, 'bold'), width = 20, bd = 5)
grocerytaxEntry.grid(row = 1, column = 3, padx = 10, pady = 8)

#for creating the cold drink tax label
colddrinktaxLabel = Label(billmenuFrame, text = 'Cold Drink Tax', font = ('Times New Roman', 15, 'bold'),bg = 'gray20', fg = 'white')
colddrinktaxLabel.grid(row = 2, column = 2, padx = 10, pady = 8, sticky = 'w')

#for creating the entry field for the Label cold drink tax.
colddrinktaxEntry = Entry(billmenuFrame, font = ('Times New Roman', 15, 'bold'), width = 20, bd = 5)
colddrinktaxEntry.grid(row = 2, column = 3, padx = 10, pady = 8)

#for creating the button frame
buttonFrame = Frame(billmenuFrame, bd = 8, relief = GROOVE)
buttonFrame.grid(row = 0, column = 4, rowspan = 3)

#for creating a button containing label 'Total'.
totalButton = Button(buttonFrame, text = 'Total', font = ('Times New Roman',15,'bold'),bg = 'gray20', fg = 'white', bd = 5, width = 9, pady = 8, command=total)
totalButton.grid(row = 0,  column = 0, pady = 20, padx = 10)

#for creating a button containing label 'Bill'.
billButton = Button(buttonFrame, text = 'Bill', font = ('Times New Roman',15,'bold'),bg = 'gray20', fg = 'white', bd = 5, width = 9, pady = 8, command=bill_area)
billButton.grid(row = 0,  column = 1, pady = 20, padx = 10)

#for creating a button containg label 'Email'.
emailButton = Button(buttonFrame, text = 'Email', font = ('Times New Roman',15,'bold'),bg = 'gray20', fg = 'white', bd = 5, width = 9, pady = 8, command=send_email)
emailButton.grid(row = 0,  column = 2, pady = 20, padx = 10)

#for creating a button containg label 'Print'.
printButton = Button(buttonFrame, text = 'Print', font = ('Times New Roman',15,'bold'),bg = 'gray20', fg = 'white', bd = 5, width = 9, pady = 8, command=print_bill)
printButton.grid(row = 0,  column = 3, pady = 20, padx = 10)

#for creating a button containg label 'Clear'.
clearButton = Button(buttonFrame, text = 'Clear', font = ('Times New Roman',15,'bold'),bg = 'gray20', fg = 'white', bd = 5, width = 9, pady = 8, command=clear)
clearButton.grid(row = 0,  column = 4, pady = 20, padx = 10)

#FUNCTIONALITY [BACKEND]

#for holding the window on the screen for a user-desired period of time
root.mainloop()