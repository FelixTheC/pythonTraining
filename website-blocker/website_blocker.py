from datetime import datetime as dt
import time
"""
A small skript thats Block some sites
Execute this as Admin
"""

hosts_temp = 'hosts'
host_path = r'/etc/hosts' #Linux,Mac,Windows r"C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'
website_list = ['www.facebook.de', 'facebook.com', 'www.xing.de', 'xing.de']


while True:
    #if 8 <= dt.now().hour <= 18:
    if 8 < dt.now().hour < 18:
        print("You should work ;)")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +' '+ website + '\n')
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Fun hours ...')
    time.sleep(5)
