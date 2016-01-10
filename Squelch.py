#!/usr/local/bin/python
import cookielib
import urllib
import urllib2

# Store the cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add  header
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)

#urllib2.install_opener(opener)


payload = { '__ac_name' : 'xxxxxx', '__ac_password' : 'xxxxxx' }


data = urllib.urlencode(payload)

def Squelch(url):
    req = urllib2.Request(url, data)
    resp = urllib2.urlopen(req)


url = []
## BUILDING URL
for i in range (1,3):
    A = "https://zenoss.com/zport/dmd/Devices/Server/Linux/xxxx/poll/devices/host%s.com/manage_editDevice?productionState=300" %(i)
    url.extend([A])

