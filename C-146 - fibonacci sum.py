# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:26:48 2024

@author: occup
"""

from tkinter import *
root = Tk()
root.title("Fibonacci series")
root.geometry("800x600")

label_title = Label(root,text = "Fibonacci Series for Sunflower")
label_series = Label(root)
label_flower = Label(root)
label_count = Label(root)

def fib_count():
    num = 10
    n1 = 0 
    n2 = 1
    n3_sum  = 0
    label_series["text"] = ""
    counter = 1
    while (counter<=num):
        print(n3_sum)
        label_series["text"] = label_series["text"] + str(n3_sum) + " "
        
        n1=n2
        n2=n3_sum
        n3_sum = n1+n2
        counter = counter+1

    label_flower["text"] = "Flower is bloomed"
    label_count["text"] = "The count on right direction is " + str(n1) + " and the count in the left direction is " + str(n2) + " and the total count is " + str(n3_sum) 
 
btn = Button( root, text = "Show series", command=fib_count)






label_title.pack()
label_series.pack()
label_flower.pack()
label_count.pack()

btn.pack()
root.mainloop()