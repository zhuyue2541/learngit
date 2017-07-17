import os
au=[]
#a=os.system("git log -3 >>a.txt")
author=os.popen('''git log -3 --pretty="%H" ''')
au=author.read().splitlines()
print au
f=file("log.txt","w")
for a in au:
	f.write(a+"\n")
f.close()