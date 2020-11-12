from bs4 import BeautifulSoup
from random import choice
import urllib
import re
import os,sys,time
import requests
import webbrowser
import pyautogui
import utils as ut 
import csv
log_state = 'log.txt'
log_file = open(log_state,'a')
log_file.write('process strted at: '+time.ctime()+'\r\n' )
data,dists = ut.get_district()
path = os.getcwd()
for district in dists:
    sfile = "{}.csv".format(district)
    fields = ['Name','Mobile number','adress'] 
    #log_file.write(district+'  process strted at:  '+time.ctime()+'\r\n')
    max_num = data['{}'.format(district)]
    service_count = 1
    page_number = 1
    #max_num = data['{}'.format(district)]
    os.chdir(os.path.join(path,'CDATA'))
    with open(sfile, 'a',encoding='utf-8',newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
            # writing the fields 
        csvwriter.writerow(fields)
        os.chdir(path)
        while True:
            if page_number>max_num:
                break
            log_file.write('page{} process strted at: '.format(page_number)+time.ctime()+'\r\n' )
            url="https://www.justdial.com/%s/Lawyers/nct-10296083/page-%s" % (district,page_number)
            ut.get_html(url,page_number)
            time.sleep(5)
            page = open('temp{}.htm'.format(page_number),'r',encoding='utf-8')
            #page = urllib.request.urlopen(req , proxy , timeout=5)
            #time.ctime(1)
            # page=urllib2.urlopen(url)
            soup = BeautifulSoup(page.read(), "html.parser")
            services = soup.find_all('li', {'class': 'cntanr'})
            # Iterate through the 10 results in the page
            for service_html in services:
                # Parse HTML to fetch data
                name = ut.get_name(service_html)
                phone = ut.get_phone_number(service_html)
                #rating = get_rating(service_html)
                #count = get_rating_count(service_html)
                address = ut.get_address(service_html)
                #location = get_location(service_html)
                #data = [name, phone, address]
                # creating a csv writer object        
                csvwriter.writerow([name, phone, address])
                page.close()
                time.sleep(2)
            os.system("taskkill /im firefox.exe /f")
            os.remove("temp{}.htm".format(page_number))       
            page_number+=1    
        log_file.write('page{} process ended at: '.format(page_number)+time.ctime()+'\r\n' )
        print('page{} process ended at: '.format(page_number)+time.ctime())
        #page_number+=1
        csvfile.close()
        os.chdir(path)
    log_file.write(district+'  process ended at: '+time.ctime()+'\r\n')
print('process completed success fully')