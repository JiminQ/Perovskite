#-*- encoding=UTF-8 -*-  
__author__ = 'Jo'  

import pandas as pd

from KRRcode import open_database
from NNcode import screen_3criteria as sc
from NNcode import first_screening as fs
from NNcode import prediction_watersplitting


perovskite,values,data_total=open_database.read_database() #3 dataframe
screening_data=sc.screening(data_total)                    #23 data after screening

data_total['water_splitting']=None 
for i in screening_data.index:
    data_total['water_splitting'].iloc[i-1]=1

from tkinter import *  
import tkinter
root = Tk(className='Perovskite Water-splitting')  
root.geometry('400x380') 

l1 = Label(root, text="A_ion：")
l1.pack()  
A_ion_text = StringVar()
A_ion = Entry(root, textvariable = A_ion_text)
A_ion_text.set("")
A_ion.pack()

l2 = Label(root, text="B_ion：")
l2.pack()  
B_ion_text = StringVar()
B_ion = Entry(root, textvariable = B_ion_text)
B_ion_text.set("")
B_ion.pack()


l3 = Label(root, text="anion：\n(please choose from(O2N,ON2,N3,O3,O2S,O2F,OFN))")
l3.pack()  
anion_text = StringVar() 
anion = Entry(root, textvariable = anion_text)
anion_text.set("")
anion.pack()

l4 = Label(root, text="mass：")
l4.pack()  
mass_text = StringVar()
mass = Entry(root, textvariable = mass_text)
#mass_text.set()
mass.pack()

l5 = Label(root, text="volume：")
l5.pack()  
volume_text = StringVar()
volume = Entry(root, textvariable = volume_text)
volume_text.set('')
volume.pack()

def get_data():
    mylist=[]
    A=A_ion_text.get()
    B=B_ion_text.get()
    N=anion_text.get()
    M=mass_text.get()
    V=volume_text.get()
    
    
    anion=str(N)
    A_ion=str(A)
    B_ion=str(B)
    volume=float(V)
    mass=float(M)
    #density=mass/volume 
    
    
    your_data,comment=fs.input_screening(A_ion,B_ion,anion,mass,volume)
    text.insert(tkinter.END,comment)
    
    if comment=='The molecule is not in our database, so we need to predict':
        prediction_watersplitting.model()
        heat_of_formation=prediction_watersplitting.prediction_hof(data_total,your_data)
        VB_dir=prediction_watersplitting.prediction_on_dir_VB(data_total,your_data)
        CB_dir=prediction_watersplitting.prediction_on_dir_CB(data_total,your_data)
        VB_ind=prediction_watersplitting.prediction_on_indir_VB(data_total,your_data)
        CB_ind=prediction_watersplitting.prediction_on_indir_CB(data_total,your_data)
        gllbsc_dir_gap=CB_dir-VB_dir
        gllbsc_ind_gap=CB_ind-VB_ind
        E0=-4.5
        if (heat_of_formation<=0.21) & (gllbsc_ind_gap >= 1.4) & (gllbsc_ind_gap <= 3.1)& (CB_ind <= 0 - E0) & (VB_ind >= 1.23 - E0) | (gllbsc_dir_gap >= 1.4) & (gllbsc_dir_gap <= 3.1) & (CB_dir <= 0 - E0) & (VB_dir >= 1.23 - E0):
            comment2='Yes,it can do water-slpitting'
            text.insert(tkinter.END,comment2)
        else:
            comment2='No,it can\'t do water-splitting.'
            text.insert(tkinter.END,comment2)
            
    return


Button(root, text="ok", command = get_data,bd = 4).pack(padx=5, pady=5)
b2 = Button(root, text='quit', command=root.quit,bd=4)
b2.pack(padx=5, pady=5)

aa="water-splitting ability\n"
text=tkinter.Text(root,width=20,height=20)
text.pack(fill=tkinter.X,side=tkinter.BOTTOM  )
text.insert(tkinter.END, aa)  
#text.insert(tkinter.END, 'this Row finished...\n') 
text.see(tkinter.END)

text.update()



    
def hello():  
    print('hello') 
def about():
    w = Label(root,text="Jimin Qian\nXueqiao Zhang\nYming Sui\nThanks!")
    w.pack(side=TOP)
    

menubar = Menu(root)   
filemenu = Menu(menubar,tearoff=0)  
filemenu.add_command(label="Open", command=hello)  
filemenu.add_command(label="Save", command=hello)  
filemenu.add_separator()  
filemenu.add_command(label="Exit", command=root.quit)  
menubar.add_cascade(label="File", menu=filemenu)  
 
editmenu = Menu(menubar, tearoff=0)  
editmenu.add_command(label="Cut", command=hello)  
editmenu.add_command(label="Copy", command=hello)  
editmenu.add_command(label="Paste", command=hello)  
menubar.add_cascade(label="Edit",menu=editmenu)   
helpmenu = Menu(menubar, tearoff=0)  
helpmenu.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=helpmenu)  
  
root.config(menu=menubar)  

root.mainloop()  


