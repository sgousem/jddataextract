from bs4 import BeautifulSoup
import urllib
import re
import os,sys,time
import requests
import csv
def get_name(body):
    #time.sleep(1)
    return body.find('p', {'class':'fa fa-user-o'}).text
def get_email(body):
    #time.sleep(1)
    return body.find('p', {'class':'fa fa-envelope tele-dir'}).text
def get_address(body):
    #time.sleep(1)
    return body.find('p', {'class':'fa icon-info-cirleok tele-dir'}).text
def get_phone_number(body):
    #time.sleep(1)
    return body.find('p', {'class':'fa fa-mobile tele-dir'}).text
sfile = "apadv.csv"
fields = ['Name','Email','Mobile number','adress'] 
with open(sfile, 'a',encoding='utf-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields)
    page = open('apad.htm','r',encoding='utf-8')
    soup = BeautifulSoup(page.read(), "html.parser")
    services = soup.find_all('div', {'class': 'question span6'})
    for service_html in services:
                # Parse HTML to fetch data
                name = get_name(service_html)
                email = get_email(service_html)
                phone = get_phone_number(service_html)
                #rating = get_rating(service_html)
                #count = get_rating_count(service_html)
                address = get_address(service_html)
                #location = get_location(service_html)
                #data = [name, phone, address]
                # creating a csv writer object        
                csvwriter.writerow([name, email, phone, address])
print('process completed')