if __name__=='__main__':
	print("\nSave your Gmail and Password here!\n")
	mail = input("Enter your Gmail : ")
	with open('m.txt', 'w') as m:
		m.write(mail)
		m.close()
		
	pd = input("\nEnter Your Password : ")
	with open('p.txt', 'w') as p:
		p.write(pd)
		p.close()
		
	print("\n\n     Now Run mailbomb.py\n")
        
		

gmail = open('m.txt', 'r').read()
pw = open('p.txt', 'r').read()


