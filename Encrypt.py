from Crypto.Cipher import DES
def sv():
    global a,b
    a=a.get(1.0,END)
    Key=DES.new("1234abcd")     #1234abcd is the key. Key can be any value but should be same during encryption and decryption. 
    temp=len(a)
    temp1=temp%8
    res=8-temp1
    for i in range(0,res):
        a=a +" "
    cry=Key.encrypt(a)
    f=open(b.get(),"w")
    f.write(cry)
    f.close()

from Tkinter import *
r=Tk()
Label(r,text="Enter the string").grid(row=0,column=0)
a=Text(r)
a.grid(row=0,column=1)
Label(r,text="Enter the filename").grid(row=1,column=0)
b=Entry(r)
b.grid(row=1,column=1)
Button(r,text="save",command=sv).grid(row=2,column=1)
r.mainloop()
