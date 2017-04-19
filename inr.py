############################################################################################################################################
# SCRIPT : inr.py                                                                                                              #
# Created By : Abhishek Alevoor                                                                                                             #
# PURPOSE : Script to retrieve INR fluctuation status                                                                                                  #
#############################################################################################################################################
#!/usr/bin/python
import json
import urllib2
import smtplib
from email.mime.multipart import MIMEMultipart

# Store Old data
f_r=open("current-data.txt",'r')
p_value=f_r.read()
f_r.close()
p_value = float(p_value)
p_value = round(p_value,5)

url = 'http://www.floatrates.com/daily/eur.json'
class LoadJson:
    def __init__(self, envurl):
        global data
        data = json.load(urllib2.urlopen(envurl))

obj = LoadJson('%s' %(url))
inr_rate = data['inr']['rate']
inr_rate = round(inr_rate,5)
fob=open("current-data.txt",'w')
fob.write('%s' %(inr_rate))
fob.close()

diff=(inr_rate - p_value)

# Email Logic
if diff != '0.0':
    m = MIMEMultipart()
    m['Subject'] = 'Fluctuation:- Current INR rate : %s'%(inr_rate)
    m['From'] = 'updates-100'
    m['To'] = 'xxxx@gmail.com'
    s = smtplib.SMTP('localhost')
    s.sendmail('xxxxx@gmail.com', 'xxxx@gmail.com',  m.as_string())
    s.quit
