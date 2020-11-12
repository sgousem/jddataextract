from bs4 import BeautifulSoup
import urllib
import re,glob
import os,sys,time
import requests
import csv
sfile = "sample.csv"
fields = ['name','state','email', 'number', 'address']
with open(sfile, 'a',encoding='utf-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields)
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
    csvfile.close()
print('process completed')