import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo,showwarning,showerror #各种类型的提示框
#顶层窗口
top=tk.Tk()
top.geometry('400x300')#设置初始化窗口大小
top.title("MailBomb")#设置名称

#监听键盘事件
def show_entry_fields():
    print("First Name: %s" % entry1.get())

#放置label和键盘输入框
text1=Label(top,text="发送地址:").grid(row=0)
entry1 = Entry(top)#实例化一个输入框
entry1.grid(row=0,column=1)



text2=Label(top,text="发送内容:").grid(row=1)
entry2 = Entry(top)#实例化一个输入框
entry2.grid(row=1,column=1)


text3=Label(top,text="邮件发送数目:").grid(row=2)
entry3 = Entry(top)#实例化一个输入框
entry3.grid(row=2,column=1)

Button(top, text='退出', command=top.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(top, text='确定', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)


text4=Label(top,text="文件上传")

text5=Label(top,text="文件预览")

top.mainloop()