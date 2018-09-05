## 基于SMTP协议的邮件伪造和邮件炸弹

基于python实现

功能要求：

1. 实现DNS服务器获取功能

2. 支持目标邮件的服务器获取

3. 支持大量邮件重复发送

4. 能伪造邮件地址发送见

5. 具有可视化界面

   

   **开发python GUI界面**：

   需要通过键盘输入的内容：发送地址、发送内容、预置邮件发送数量，文件上传与预览

   Tkinter是python的标准GUI库

   **创建一个GUI程序**：
import Tkinter  #导入包
from tkinter.messagebox import showinfo,showwarning,showerror #各种类型的提示框
top=Tkinter.Tk() #顶层窗口
top.mainloop()  #运行GUI应用

**使用easygui来实现文件预览**
实现文件预览功能，创建按钮进行事件监听，弹框选择文件，读取文件内容到text控件中，返回给非界面代码处理的有file的路径，对历史文件的保存




