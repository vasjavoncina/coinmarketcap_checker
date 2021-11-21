from email.message import EmailMessage
import smtplib
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    user = "vasja.voncina123@gmail.com"
    msg["from"] = user
    password = "vzjszdongqpaemfd"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit

to = ["vasja.voncina123@gmail.com", "peter.peternik123@gmail.com"]

#for mail in to:
#    email_alert("haj", "wassap dawg", mail)

def grab_html():
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=PATH, options=opt)
    driver.get("https://coinmarketcap.com/new/")



    content = driver.page_source
    soup = BeautifulSoup(content)
    with open ("html/ena.txt", "w") as ena:
        print(soup, file= ena)
    driver.close()


A = time.localtime()
print(A)
B = time.gmtime()
print(B)
C = time.asctime().split(' ')
print(C[-2])

