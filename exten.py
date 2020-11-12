from bs4 import BeautifulSoup
import urllib
import re,glob
import os,sys,time
import requests
import csv
import pyautogui
import webbrowser
def click_fun(pageno):
    if pageno<=11:
        pyautogui.click(340,302)
    elif pageno<=101:
        pyautogui.click(365,302)
    else:
        pyautogui.click(390,302)
sfile = "ap_adv1.csv"
log = open('log.txt','a')
fields = ['name','state','email', 'number', 'address']
log.write(' process strted at: '+time.ctime()+'\r\n')
time.sleep(15)
with open(sfile, 'a',encoding='utf-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields)
    page_number = 685
    while True:
        if page_number>756:
            break
        pyautogui.click(1355,708)
        time.sleep(2)
        click_fun(page_number)
        time.sleep(10)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(5)
        extension = 'htm'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        for htm_file in all_filenames: 
            page = open(htm_file,'r',encoding='utf-8')
            soup = BeautifulSoup(page.read(), "html.parser")
            services1 = soup.find_all('div',{'class': 'question span6'})
            for div in services1: 
                data = div.find('ul',{'class': 'container details'})
                info = data.find_all('li')
                com_data = []
                for inf in info:
                    data = inf.find_all('p')        
                    #com_data = []
                    for item in data:
                        details = item.get_text()
                        com_data.append(details)
                    #id,name,state,email,mobile,address = com_data
                name = com_data[1].strip().split(':')[1]
                state = com_data[2].strip().split(':')[1]
                email = com_data[3].strip().split(':')[1]
                number = com_data[4].strip().split(':')[1]
                address = com_data[5].strip().split(':')[1]
                csvwriter.writerow([name,state,email, number, address])
            page.close()
            os.remove(htm_file)
        page_number+=1
        time.sleep(3)
        log.write('page number : {} is currently processing'.format(page_number)+time.ctime()+'\r\n')
        print('page number : {} is currently processing'.format(page_number)+time.ctime())
    csvfile.close()
log.close()
print('process completed')