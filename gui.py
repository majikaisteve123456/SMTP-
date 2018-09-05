import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo,showwarning,showerror #各种类型的提示框
from tkinter.scrolledtext import ScrolledText
import easygui as g
import os
import shutil

global dic
dic={}
class App:
    entry1 = None
    entry2 = None
    text4 = None
    text5=None
    def __init__(self,top):
        # 放置label和键盘输入框
        text1 = Label(top, text="发送地址: ").grid(row=0, sticky=W)
        App.entry1 = Entry(top)  # 实例化一个输入框
        App.entry1.grid(column=0, row=0)
        text2 = Label(top, text="邮件发送数目: ").grid(row=1, sticky=W)
        App.entry2 = Entry(top)  # 实例化一个输入框
        App.entry2.grid(column=0, row=1)

        # 选择附件
        text5 = Label(top, text="添加附件:").grid(row=3, sticky=W)
        button0 = Button(top, width=10, text='选择附件', command=self.elect_file).grid(row=4, column=0, pady=4,sticky=W)
        button1 = Button(top, width=10, text='预览附件内容', command=self.view_file_content).grid(row=4, column=1, pady=4)
        button2 = Button(top, width=10, text='添加附件内容', command=self.add_file_content).grid(row=4, column=2, pady=4)
        button3 = Button(top, width=10, text='保存文件', command=self.save_file).grid(row=4, column=3, pady=4)

        # 文本框text组件 预览
        text5 = Label(top, text="附件预览内容:").grid(row=5, sticky=W)
        App.text5 = ScrolledText(top, width=40, height=10)
        App.text5.grid(sticky=W)
        App.text5.config(state=DISABLED)

        # 文本框text组件 实际发送内容
        text3 = Label(top, text="发送内容:").grid(row=8, sticky=W)
        App.text4 = ScrolledText(top, width=40, height=10)
        App.text4.grid(sticky=W)


        # 发送键
        button4= Button(top, width=15, text='发送', command=self.show_entry_fields).grid(row=10, column=0, pady=4)

        # 监听键盘事件,按确定后
    def show_entry_fields(self):
         dic['recevier']=App.entry1.get()
         dic['number']=App.entry2.get()
         s=App.text4.get("0.0", "end")
         dic['content']=s.strip()
         print(dic)

#选择附件
    def elect_file(self):
        msg = '浏览文件并打开'
        title = '测试'
        default = r'C:\Users\lenovo\Desktop\SMTP邮件\文件库\*'
        fileType = '全部文件'
        filePath = g.fileopenbox(msg, title, default, fileType)
        with open(filePath, encoding='utf-8', errors='ignore') as f:
            title = os.path.basename(filePath)
            msg = '文件%s的内容如下：' % title
            txt = f.read()
            App.text4.insert(END,txt)
            dic['filepath']=filePath

#将附件中的内容添加到预览框中
    def view_file_content(self):
        if dic[filepath]=='':
              messagebox.showinfo(title='警告', message='未选择附件')
        else:
            #打开文件，将文件内容添加到预览框中
              with open(dic[filepath], encoding='utf-8', errors='ignore') as f:
                  txt = f.read()
                  App.text5.config(state=NORMAL)
                  App.text5.insert(END, txt)
                  App.text5.config(state=DISABLED)

    def add_file_content(self):
        if dic[filepath]=='':
              messagebox.showinfo(title='警告', message='未选择附件')
        else:
            #打开文件，将文件内容添加到预览框中
              with open(dic[filepath], encoding='utf-8', errors='ignore') as f:
                  txt = f.read()
                  App.text4.insert(END, txt)

    def save_file(self):
        if dic[filepath]=='':
              messagebox.showinfo(title='警告', message='未选择附件')
        else:
              shutil.copy(dic[filepath],r'C:\Users\lenovo\Desktop\SMTP邮件\文件库\*')


#顶层窗口
top=tk.Tk()
top.geometry('500x650')#设置初始化窗口大小
top.title("MailBomb")#设置名称
app=App(top)
top.mainloop()

