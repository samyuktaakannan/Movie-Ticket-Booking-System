import json
from tkinter import *
from datetime import datetime
from functools import partial
from PIL import ImageTk,Image
booking={}

def bill():
    with open('bookings.json','r') as file:
        a=json.load(file)
    bills=Tk()
    bills.geometry("1000x2000+10+20")
    bills.state("zoomed")
    bills['bg']='deepskyblue'
    heading = Label(bills,text="Ticket Confirmation",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(bills,bg="black",height=1,width=500)
    style1.pack(pady=10)
    for i in a:
        label = Label(bills, text=(i+" : "+a[i]), fg="Black", font=("verdana",16,'bold'))
        label.pack(pady=16)
    label1=Label(bills,text="Thanks for booking!!", fg="Black", font=("verdana",16,'bold'))
    label1.pack(pady=16)
    bills.mainloop()

def seats(i):
    booking['Time']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    def receive():
        z=enter.get()
        booking['Number of Seats']=z
        booking['Total cost']=str(int(z)*150)
        with open('bookings.json','w') as file:
            json.dump(booking,file)
        file.close()
        bill()
    seats=Tk()
    seats.geometry("1000x2000+10+20")
    seats.state("zoomed")
    seats['bg']='deepskyblue'
    heading = Label(seats,text="SEATS",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(seats,bg="black",height=1,width=500)
    style1.pack(pady=10)
    name = Label(seats, text="Enter number of seats", font=('arial',30,'bold'),fg="deepskyblue",bg="black")
    name.place(x=600,y=150)
    enter = Entry(seats, bd = 5,fg="black")
    enter.place(x=600,y=230)
    okButton = Button(seats, text="OK", bd=5, font=('arial',25,'bold'),fg="white",bg="black",command=receive)
    okButton.place(x=660,y=300)
    seats.mainloop()
    

def vikramtimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("vikram.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==4):
        for i in pls[4]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def jurassictimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("jurassic.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)

def charlietimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("charlie.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def dontimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("don.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def adadetimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("adade.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def ejurassictimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("ejurassic.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def topguntimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("topgun.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==4):
        for i in pls[4]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def drtimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("dr.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def samrattimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("samrat.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def janhittimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("janhit.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def antetimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("ante.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
def majortimes(num,i):
    booking['Theatre Name']=i
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    heading = Label(t,text="Timings",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=10)
    style1 = Label(t,bg="black",height=1,width=500)
    style1.pack(pady=10)
    button_dict={}
    with open("major.json",'r') as file:
        a=json.load(file)
    pls=[]
    for i in a.values():
        pls.append(i)
    if(num==0):
       for i in pls[0]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    
    if(num==1):
        for i in pls[1]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
            
    if(num==2):
        for i in pls[2]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    if(num==3):
        for i in pls[3]:
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(seats,i))
            button_dict[i].pack(pady=16)
    

def tamilmovies(num,name):
    booking['Name of Movie']=name
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    if num==0:
        heading = Label(t,text="Vikram (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("vikram.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(vikramtimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
    
    elif num==1:
        heading = Label(t,text="Jurassic World: Dominion (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("jurassic.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(jurassictimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
            
    elif num==2:
        heading = Label(t,text="777 Charlie (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("charlie.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(charlietimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
    
    elif num==3:
        heading = Label(t,text="Don (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("don.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(dontimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
            
    elif num==4:
        heading = Label(t,text="Adade Sundara (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("adade.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(adadetimes,b,i))
            button_dict[i].pack(pady=16)   
            b=b+1

def englishmovies(num,name):
    booking['Name of Movie']=name
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    if num==0:
        heading = Label(t,text="Jurassic World: Dominion (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("ejurassic.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(ejurassictimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
    
    elif num==1:
        heading = Label(t,text="Top Gun: Maverick (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("topgun.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(topguntimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
            
    elif num==2:
        heading = Label(t,text="Doctor Strange: In The Multiverse Of Madness (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("dr.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(drtimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
            
def hindimovies(num,name):
    booking['Name of Movie']=name
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    if num==0:
        heading = Label(t,text="Samrat Prithviraj (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        
        with open("samrat.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(samrattimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
    
    elif num==1:
        heading = Label(t,text="Janhit Mein Jaari (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("janhit.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(janhittimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
            
def telugumovies(num,name):
    booking['Name of Movie']=name
    with open('bookings.json','w') as file:
        json.dump(booking,file)
    t=Tk()
    t.geometry("1000x2000+10+20")
    t.state("zoomed")
    t['bg'] = "deepskyblue"
    if num==0:
        heading = Label(t,text="Ante Sundaraniki (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("ante.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(antetimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1
    
    elif num==1:
        heading = Label(t,text="MAJOR (movie theatres)",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
        heading.pack(pady=10)
        style1 = Label(t,bg="black",height=1,width=500)
        style1.pack(pady=10)
        button_dict={}
        with open("major.json",'r') as file:
            a=json.load(file)
        b=0
        for i in list(a.keys()):
            button_dict[i] = Button(t, text=i, fg="Black", font=("verdana",16,'bold'),command=partial(majortimes,b,i))
            button_dict[i].pack(pady=16)
            b=b+1

def tamil():
    tamils=Tk()
    tamils.geometry("1000x2000+10+20")
    tamils.state("zoomed")
    tamils['bg'] = "deepskyblue"
    heading = Label(tamils,text="Tamil Movies",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=12)
    style1 = Label(tamils,bg="black",height=1,width=500)
    style1.pack(pady=12)
    with open("movies.json",'r') as file:
        a=json.load(file)
    tm=a['Tamil']
    z = Button(tamils, text=tm[0], fg="Black", font=("verdana",18,'bold'),command=partial(tamilmovies,0,tm[0]))
    z.pack(pady=18)
    
    b = Button(tamils, text=tm[1], fg="Black", font=("verdana",18,'bold'),command=partial(tamilmovies,1,tm[1]))
    b.pack(pady=18)
    
    c= Button(tamils, text=tm[2], fg="Black", font=("verdana",18,'bold'),command=partial(tamilmovies,2,tm[2]))
    c.pack(pady=18)
    
    d= Button(tamils, text=tm[3], fg="Black", font=("verdana",18,'bold'),command=partial(tamilmovies,3,tm[3]))
    d.pack(pady=18)
    
    e= Button(tamils, text=tm[4], fg="Black", font=("verdana",18,'bold'),command=partial(tamilmovies,4,tm[4]))
    e.pack(pady=18)
    tamils.mainloop()
    
def english():
    englishs=Tk()
    englishs.geometry("1000x2000+10+20")
    englishs.state("zoomed")
    englishs['bg'] = "deepskyblue"
    heading = Label(englishs,text="English Movies",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=12)
    style1 = Label(englishs,bg="black",height=1,width=500)
    style1.pack(pady=12)
    button_dict={}
    with open("movies.json",'r') as file:
        a=json.load(file)
    tm= a['English']
    z = Button(englishs, text=tm[0], fg="Black", font=("verdana",18,'bold'),command=partial(englishmovies,0,tm[0]))
    z.pack(pady=18)
    
    b = Button(englishs, text=tm[1], fg="Black", font=("verdana",18,'bold'),command=partial(englishmovies,1,tm[1]))
    b.pack(pady=18)
    
    c= Button(englishs, text=tm[2], fg="Black", font=("verdana",18,'bold'),command=partial(englishmovies,2,tm[2]))
    c.pack(pady=18)
    englishs.mainloop()
        
def hindi():
    hindis=Tk()
    hindis.geometry("1000x2000+10+20")
    hindis.state("zoomed")
    hindis['bg'] = "deepskyblue"
    heading = Label(hindis,text="Hindi Movies",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=12)
    style1 = Label(hindis,bg="black",height=1,width=500)
    style1.pack(pady=12)
    button_dict={}
    with open("movies.json",'r') as file:
        a=json.load(file)
    tm=a['Hindi']
    z = Button(hindis, text=tm[0], fg="Black", font=("verdana",18,'bold'),command=partial(hindimovies,0,tm[0]))
    z.pack(pady=18)
    
    b = Button(hindis, text=tm[1], fg="Black", font=("verdana",18,'bold'),command=partial(hindimovies,1,tm[1]))
    b.pack(pady=18)  
    hindis.mainloop()
        
def telugu():
    telugus=Tk()
    telugus.geometry("1000x2000+10+20")
    telugus.state("zoomed")
    telugus['bg'] = "deepskyblue"
    heading = Label(telugus,text="Telugu Movies",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.pack(pady=12)
    style1 = Label(telugus,bg="black",height=1,width=500)
    style1.pack(pady=12)
    button_dict={}
    with open("movies.json",'r') as file:
        a=json.load(file)
    tm=a['Telugu']
    z = Button(telugus, text=tm[0], fg="Black", font=("verdana",18,'bold'),command=partial(telugumovies,0,tm[0]))
    z.pack(pady=18)
    
    b = Button(telugus, text=tm[1], fg="Black", font=("verdana",18,'bold'),command=partial(telugumovies,1,tm[1]))
    b.pack(pady=18)  
    telugus.mainloop()
        

def language():
    root=Tk()
    root.geometry('1000x2000+10+20')
    root.state('zoomed')
    root.title('BookyMyShow')
    root['bg'] = "deepskyblue"
    heading = Label(root,text="BookMyShow - Entertainment Ki Nayi Bhasha",font=('verdana',25,'bold'),fg="black",bg="deepskyblue")
    heading.place(x=400,y=5)
    style1 = Label(root,bg="black",height=1,width=500)
    style1.place(x=0,y=50)
    date = Label(root,text=datetime.now(),font=('verdana',10,'bold'),bg="deepskyblue")
    date.place(x=640,y=50)
    frame1 = LabelFrame(root,text=" Movie Language",width=425,height=425,font=('verdana',30,'bold'),borderwidth=3,relief=RIDGE,highlightthickness=4,bg="deepskyblue",highlightcolor="deepskyblue",highlightbackground="deepskyblue",fg="black")
    frame1.place(x=500,y=90)
            
    tamilm = Button(root, text="Tamil", fg="Black", font=("verdana",18,'bold'),command=tamil)
    tamilm.place(x=670,y=170)  

    hindim = Button(root,text="Hindi",font=('verdana',18,'bold'),command=hindi)
    hindim.place(x=670,y=250)


    englishm = Button(root,text="English",font=('verdana',18,'bold'),command=english)
    englishm.place(x=660,y=330)
            

    telugum = Button(root,text="Telugu",font=('verdana',18,'bold'),command=telugu)
    telugum.place(x=660,y=410)
            
    root.mainloop()

    

ws = Tk()
ws.title("window")

width= ws.winfo_screenwidth()
height= ws.winfo_screenheight()

ws.geometry("%dx%d" % (width, height))
ws.title('BookMyShow Login Page')
ws.resizable(False, False)

imgTemp = Image.open("movies.jpg")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)

label = Label(ws,image=img)
label.pack(side='top',fill=Y,expand=True)
heading = Label(ws,text="Login Page",font=('verdana',30,'bold'),fg="black",bg="white")
heading.place(x=600,y=50)
label1_tk = Label(ws, text="Name", font=('arial',30,'bold'),fg="black",bg="white")
label1_tk.place(x=650,y=150)

entry1_tk = Entry(ws, bd = 9,fg="black")
entry1_tk.place(x=650,y=230)

label1_tk = Label(ws, text="Password",font=('arial',30,'bold'),fg="black",bg="white")
label1_tk.place(x=625,y=300)

entry2_tk = Entry(ws, bd = 9, show="*")
entry2_tk.place(x=650,y=380)

loginButton = Button(ws, text="Login", bd=5, font=('arial',25,'bold'),fg="white",bg="black",command=language)
loginButton.place(x=660,y=450)
ws.mainloop()