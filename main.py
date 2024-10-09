import tkinter

import ttkbootstrap as ttk
import ttkbootstrap.dialogs
from ttkbootstrap.constants import *


from tkinter import *
import tkinter as tk

inputNumber = 0

printableText = ""




def check_type(var, get):
    try:
        var = get.get()
        int(var)
        #The value entered was a number.
        return 1

    except ValueError:
        #The value entered was a string.
        print('Stop')

    return 0

def valid():
    factor_list = []
    factor_list2 = []
    printlist = []

    inputNumber = entry1.get()

    if check_type(inputNumber, entry1) == 1:
        textbox.delete(0.0, 'end')
        #print("its right")
        #x = inputNumber

        #print(inputNumber)

        #get_factors()
        for i in range(1, int(inputNumber) + 1):
            if int(inputNumber) % i == 0:
                factor_list.append(i)
                factor_list2.append(i)

        numFactors = len(factor_list)
        #print(numFactors)

        #print(factor_list)
        #print(factor_list2)

        list1Multiple = 0

        list2Multiple = 0

        for r in range(numFactors):
            list2Multiple = 0
            for n in range(numFactors):

                if factor_list[list1Multiple] * factor_list2[list2Multiple] == int(inputNumber):
                    print(factor_list[list1Multiple], " x ", factor_list2[list2Multiple])
                    printableText = str(factor_list[list1Multiple]) + " x " + str(factor_list2[list2Multiple])



                    printlist.append(printableText)

                    #textbox.insert(0.0, printlist)
                    textbox.insert('end', (str(printableText) + "\n"))






                list2Multiple = list2Multiple + 1
            list1Multiple = list1Multiple + 1
        print(printlist)

    else:
        label3 = ttkbootstrap.dialogs.dialogs.Messagebox.show_error(message="I Told You To Use Numbers", title="Warning!", alert=True)

        print("toe warrior")





root = ttk.Window(title="Minecraft SurfaceArea", themename="darkly",resizable =(False, False), size=(330, 200))




label = ttk.Label(text="Put The Amount of blocks you have Here")
label.grid(row=0, column=2,sticky="NSEW")

entry1 = ttk.Entry(root, textvariable = inputNumber)
entry1.grid(row=1, column=2)

label1 = ttk.Label(text="Output Here")
label1.grid(row=2, column=2,)



textbox = ttk.Text(name='toe', width=16, height=5)
textbox.grid(row=3, column=2)


b2 = ttk.Button(root, text="Submit", bootstyle="info-outline", command=valid)
b2.grid(row=5, column=1)




root.mainloop()
