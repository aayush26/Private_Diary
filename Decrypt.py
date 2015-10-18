from Crypto.Cipher import DES

def op():
    global a,b
    Key=DES.new("1234abcd")		#1234abcd is the key. Key can be any value but should be same during encryption and decryption. 
    f=open(b.get(),"r")
    temp=f.read()
    print temp
    a.insert(1.0,Key.decrypt(temp))

from Tkinter import *
r=Tk()
Label(r,text="Enter the string").grid(row=0,column=0)
a=Text(r)
a.grid(row=0,column=1)
Label(r,text="Enter the filename").grid(row=1,column=0)
b=Entry(r)
b.grid(row=1,column=1)
Button(r,text="open",command=op).grid(row=2,column=2)
r.mainloop()
