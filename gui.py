import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo,showwarning,showerror #各种类型的提示框
from tkinter.scrolledtext import ScrolledText

global list
list=[]
class App:
    entry1 = None
    entry2 = None
    text4 = None
    def __init__(self,top):
        # 放置label和键盘输入框
        text1 = Label(top, text="发送地址: ").grid(row=0, sticky=W)
        App.entry1 = Entry(top)  # 实例化一个输入框
        App.entry1.grid(column=0, row=0)
        text2 = Label(top, text="邮件发送数目: ").grid(row=1, sticky=W)
        App.entry2 = Entry(top)  # 实例化一个输入框
        App.entry2.grid(column=0, row=1)
        text3 = Label(top, text="发送内容:").grid(row=2, sticky=W)
        # 文本框text组件
        App.text4 = ScrolledText(top, width=40, height=10)
        App.text4.grid(sticky=W)
        # 发送键
        button2 = Button(top, width=15, text='发送', command=self.show_entry_fields).grid(row=5, column=0, pady=4)

        # 监听键盘事件,按确定后
    def show_entry_fields(self):
         list.append(App.entry1.get())
         list.append(App.entry2.get())
         s=App.text4.get("0.0", "end")
         list.append(s.strip())
         print(list)


#顶层窗口
top=tk.Tk()
top.geometry('400x300')#设置初始化窗口大小
top.title("MailBomb")#设置名称
app=App(top)
top.mainloop()

