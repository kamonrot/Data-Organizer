from tkinter import *
from tkinter.ttk import Combobox

def func():
    midMoneyToday = 0
    midMoneyYesterday = 0
    
    midMoneyToday = float(today.get()) * float(money.get())
    midMoneyYesterday = float(yesterday.get()) * float(money.get())
    diffMoney = ((midMoneyToday - midMoneyYesterday) / midMoneyYesterday) * 100
    
    label9 = Label(wd, text=float("{:.2f}".format(midMoneyToday)), fg='black', font=('Arial', 14), width=10)
    label9.place(x=350, y=205)
    label10 = Label(wd, text=float("{:.2f}".format(midMoneyYesterday)), fg='black', font=('Arial', 14), width=10)
    label10.place(x=350, y=245)
    label11 = Label(wd, text=float("{:.2f}".format(diffMoney)), fg='black', font=('Arial', 14), width=10)
    label11.place(x=350, y=285)
    label12 = Label(wd, text='%', fg='black', font=('Arial', 14))
    label12.place(x=450, y=285)

wd = Tk()

label = Label(wd, text='Money Changer', fg='black', font=('Arial', 16))
label.place(x=30, y=10)

list = ['JPY(¥)', 'THB(฿)', 'USD($)', 'GBP(£)', 'CNY(Ұ)', 'EUR(€)', 'SGD(S$)', 'HKD(HK$)']

label1 = Label(wd, text='Input', fg='black', font=('Arial', 12))
label1.place(x=30, y=50)
input = Combobox(wd, values=list)
input.place(x=30, y=85)

label2 = Label(wd, text='Output', fg='black', font=('Arial', 12))
label2.place(x=250, y=50)
output = Combobox(wd, values=list)
output.place(x=250, y=85)

today = Entry(wd, width=21)
today.place(x=250, y=125)

yesterday = Entry(wd, width=21)
yesterday.place(x=250, y=165)

label3 = Label(wd, text='1   =', fg='black', font=('Arial', 14))
label3.place(x=195, y=125)

label4 = Label(wd, text='today', fg='black', font=('Arial', 12))
label4.place(x=430, y=125)

label5 = Label(wd, text='yesterday', fg='black', font=('Arial', 12))
label5.place(x=430, y=165)

label6 = Label(wd, text='today', fg='black', font=('Arial', 14))
label6.place(x=250, y=205)

label7 = Label(wd, text='yesterday', fg='black', font=('Arial', 14))
label7.place(x=250, y=245)

label8 = Label(wd, text='=', fg='black', font=('Arial', 14))
label8.place(x=225, y=205)

money = Entry(wd, width=22)
money.place(x=30, y=205)

button = Button(wd, text='Exchange', font=('Helvetica', 14), command=func)
button.place(x=180, y=320)

wd.title('Money Changer')
wd.geometry('510x360')
wd.mainloop()