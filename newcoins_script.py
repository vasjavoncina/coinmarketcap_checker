from model import Coins
import smtplib
from email.message import EmailMessage
#from selenium import webdriver
#from bs4 import BeautifulSoup
import time
import requests
import re
import os

###########################################################################
###########################################################################

DATA = "newcoins.json"

try:
    shramba = Coins.nalozi_stanje(DATA)
except FileNotFoundError:
    shramba = Coins()

###########################################################################
###########################################################################


def grab_coin_links_2():
    coins = []
    url = "https://coinmarketcap.com/new/"
    odziv = requests.get(url)
    vsebina = odziv.text
    with open(f'CMC.html', 'w') as f:
        f.write(vsebina)

    with open(f'CMC.html', 'r') as f:
        vsebina = f.read()
        vzorec = r'"/currencies/(.+?)/"'
        for zadetek in re.finditer(vzorec, vsebina):
            link = "https://coinmarketcap.com" + zadetek[0][1:-1]
            coins.append(link)
    os.remove("CMC.html")
    return coins


def add_new_coin(coin_link):
    shranjeni1 = len(shramba.coins)
    name = coin_link.split("/")[-2]
    shramba.add_coin(coin_link, name)
    shranjeni2 = len(shramba.coins)
    if shranjeni1 < shranjeni2:
        to = ["peter.peternik123@gmail.com"]
        for mail in to:
            email_alert("NOV COIN", coin_link, mail)
    else:
        pass


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    user = "vasja.voncina123@gmail.com"
    msg["from"] = user
    password = "dyphwqvtshlbunmf"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit


def program():
    for coin_link in grab_coin_links_2():
        add_new_coin(coin_link)
        shramba.shrani_stanje(DATA)


###########################################################################
###########################################################################


if __name__ == '__main__':
    i = 0
    while True:
        try:
            program()
            print("success, now waiting...")
            time.sleep(60)
            i+=1
        except ValueError:
            print("failure of the system baby")


###########################################################################
###########################################################################





















#def grab_coin_links(): #+html za testiranje:
    #B = []
    #PATH = 'C:\Program Files (x86)\chromedriver.exe'
    #opt = webdriver.ChromeOptions()
    #opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    #driver = webdriver.Chrome(executable_path=PATH, options=opt)
    #driver.get("https://coinmarketcap.com/new/")
    #content = driver.page_source
    #soup = BeautifulSoup(content)
    #cas = time.asctime().split(' ')
    #ura = cas[-2].replace(':', ';')
    #
    #with open (f"html/{ura}.html", "w") as ena:
    #    print(soup, file= ena)
    #A = driver.find_elements_by_class_name("cmc-link")
    #for element in A:
    #    link = element.get_attribute("href")
    #    if r"https://coinmarketcap.com/currencies/" in link:
    #        B.append(link)
    #driver.close()
    #return B
