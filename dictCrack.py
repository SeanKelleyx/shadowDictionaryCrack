import crypt
def testPass(Pass, salt, cryptPass):
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		if (cryptWord == cryptPass):
			print "\n[+] Found Password: "+word+"\n"
			return
	print "[-] Password Not Found."
	return
def main():
	passFile = open('password.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			if cryptPass == "!":
				print "[+] "+user + " is locked with no password in the shadow file."
			elif cryptPass == "*":
				print "[+] " + user + " is a system user with no password in the shadow file."
			elif cryptPass == "!!":
				print "[+] " + user + " has an expired password and will not be able to log in."
			elif cryptPass == "NP" or cryptPass == "null":
				print "[+] " + user + " account has no password."
			else:	
				cryptPass = cryptPass.strip("!")
				tempPass = cryptPass.split('$')
				Pass = tempPass[3]
				salt = '$'+tempPass[1]+'$'+tempPass[2]
				print "[*] Cracking Password For: " +user
				if tempPass[1] =="1":
					print "[+] Cracking MD5 encryption..."
				elif tempPass[1] == "2a" or tempPass[1] == "2y":
					print "[+] Cracking Blowfish encryption..."
				elif tempPass[1] == "5":
					print "[+] Cracking SHA-256 encryption..."
				elif tempPass[1] == "6":
					print "[+] Cracking SHA-512 encryption..."
				testPass(Pass, salt, cryptPass)
if __name__ == "__main__":
	main()
