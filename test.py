#coding:utf-8   #强制使用utf-8编码格式
import threading
import time
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender='xidianbtest@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='18292884508@163.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
my_pass='tsw123'
lock=threading.Lock()


def mail(num,receiver,content,from_name,from_add):
    ret=True
    try:
        # server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        # server.login(from_add, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
        server=smtplib.SMTP('localhost')
        server.set_debuglevel(1)
        for i in range(num):
            msg=MIMEText(content,'plain','utf-8')

            #msg['From'] = my_sender
            # msg['To'] = receiver

            msg['From'] = formataddr([from_name,from_add]) #括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["18292884508",receiver])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']="纯洁小天使" #邮件的主题，也可以说是标题

            server.sendmail(from_add,[receiver,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
        return ret
    return ret


class mail_process(threading.Thread):
    def __init__(self,n,reciever,content,from_name,from_add):
        threading.Thread.__init__(self)
        self.num=n
        self.receiver=reciever
        self.content=content
        self.from_name=from_name
        self.from_add=from_add

    def run(self):
        for i in range(5):
            mail(self.num,self.receiver,self.content,self.from_name,self.from_add)


def send(email_num,receiver,content,from_name,from_add):
    #p = mail_process(10,server)

    # ret = mail(server)
    # if ret:
    #     print("ok")
    # else:
    #     print("failed")

    thread_num = 10
    threads=[]
    for i in range(thread_num):
        threads.append(mail_process(email_num,receiver,content,from_name,from_add))
        #threads.append(mail_process(10,"xidianbtest2@163.com","hello","西电教务处","xd@edu.cn"))
    for t in threads:
        t.start()

