import urllib2
import urllib
import re
import os
import json

res= urllib2.urlopen("http://www.ishadowsocks.net/")
con =  res.read().decode("utf-8")
pattern = re.compile('<section id="free">(.*?)</section>',re.S)
result  = re.search(pattern,con)

items = re.findall("<h4>(.*?)</h4>",result.group(0))
pwd = items[2][4:12]
print 'init shadowsocks password'
print pwd

with open('gui-config.json','r') as ff:
	d = json.load(ff)
	d["configs"][0]["password"]=pwd

with open('gui-config.json','w') as f:
	json.dump(d,f)
print "open shadowsocks success , please close this window"
os.popen("Shadowsocks.exe")
eixt()
