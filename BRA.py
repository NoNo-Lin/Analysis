import requests
from bs4 import BeautifulSoup
import re
import time
yahoo = time.strftime("%Y-%m-%d", time.localtime())
while True:
	rgy = open(yahoo+".txt", 'w')
	resp = requests.get('網址')
	soup = BeautifulSoup(resp.text,'html5lib')
	#print(resp.text)
	#print(soup.prettify())
	dateex = []
	timeex = []
	periodex = []
	#將爬蟲的資料分割#
	for idx, tr in enumerate(soup.find_all('tr', 'even')):
		if idx != 0:
			tds = tr.find_all('td')
			
			#print(tds[0].contents[0])
			iningg = (tds[1].contents[0])
			periodex.append(tds[0].contents[0])
			iningg1 = iningg.find(" ")
			dateex.append(iningg[:5])
			timeex.append(iningg[6:11])
	b=soup.find_all('i',class_=re.compile("pk-no\d"))
	d=b
	# for i in d:
	#     print(i.string)
	c,e=[],[]
	for i in d:
		if len(c)<10:
			c.append(i.string)
		else :
			e.append(c)
			c=[]
			c.append(i.string)
	#for ii in range(len(e)):
		#print(dateex[ii])
		#print(timeex[ii])
		#print('現在是第'+periodex[ii]+"期"+str(ii)+':',e[ii][0],e[ii][1])
	#利用時間切割並
	
	ig = 0
	
	stud=['one','two','three','four','fives','six','seven','eight','nine','ten']
	for i in range(len(stud)):
		locals()[stud[i]] = []
	
	for i in range(len(e)):
		if timeex[i] == "23:57":
				#print("結束"+str(i))
				break
		else:
			#print(timeex[i])
			one.append(e[i][0])
			two.append(e[i][1])
			three.append(e[i][2])
			four.append(e[i][3])
			fives.append(e[i][4])
			six.append(e[i][5])
			seven.append(e[i][6])
			eight.append(e[i][7])
			nine.append(e[i][8])
			ten.append(e[i][9])
			ig = ig+1
	#print(i)
	c = ["1","2","3","4","5","6","7","8","9","10"]
	nogood = [0,"編號 : 1","編號 : 2","編號 : 3","編號 : 4","編號 : 5","編號 : 6","編號 : 7","編號 : 8","編號 : 9","編號 : 10"]
	###宣告變數###
	for i in range(len(c)):
		locals()["one"+c[i]] = 0
	for i in range(len(c)):
		locals()["two"+c[i]] = 0
	for i in range(len(c)):
		locals()["three"+c[i]] = 0
	for i in range(len(c)):
		locals()["four"+c[i]] = 0
	for i in range(len(c)):
		locals()["fives"+c[i]] = 0
	for i in range(len(c)):
		locals()["six"+c[i]] = 0
	for i in range(len(c)):
		locals()["seven"+c[i]] = 0   
	for i in range(len(c)):
		locals()["eight"+c[i]] = 0   
	for i in range(len(c)):
		locals()["nine"+c[i]] = 0   
	for i in range(len(c)):
		locals()["ten"+c[i]] = 0   
	###分析數值###
	print("---"*15)
	print("第一名數值分析")
	print("---"*15)
	rgy.write("---"*15+"\n")
	rgy.write("第一名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in one:
		locals()["one"+i] += 1
	for i in range(1,11):
		xone = ('{percent:.2%}'.format(percent=round(float(locals()["one"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["one"+str(i)],xone))
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["one"+str(i)],xone))
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第二名數值分析")
	print("---"*15)
	rgy.write("第二名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in two:
		locals()["two"+i] += 1
	for i in range(1,11):
		xtwo = ('{percent:.2%}'.format(percent=round(float(locals()["two"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["two"+str(i)],xtwo))
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["two"+str(i)],xtwo))
		#print("編號: "+str(i)+" 勝率")
		#print(('{percent:.2%}'.format(percent=round(float(locals()["two"+str(i)]/ig),4))))
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第三名數值分析")
	print("---"*15)
	rgy.write("第三名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in three:
		locals()["three"+i] += 1
	for i in range(1,11):
		xthree = ('{percent:.2%}'.format(percent=round(float(locals()["three"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["three"+str(i)],xthree))
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["three"+str(i)],xthree)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第四名數值分析")
	print("---"*15)
	rgy.write("第四名數值分析\n")
	for i in four:
		locals()["four"+i] += 1
	for i in range(1,11):
		xfour = ('{percent:.2%}'.format(percent=round(float(locals()["four"+str(i)]/ig),4)))
		ddgg = nogood[i]
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["four"+str(i)],xfour)) 
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["four"+str(i)],xfour)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第五名數值分析")
	print("---"*15)
	rgy.write("第五名數值分析\n")
	for i in fives:
		locals()["fives"+i] += 1
	for i in range(1,11):
		xfives = ('{percent:.2%}'.format(percent=round(float(locals()["fives"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["fives"+str(i)],xfives)) 
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["fives"+str(i)],xfives)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第六名數值分析")
	print("---"*15)
	rgy.write("第六名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in six:
		locals()["six"+i] += 1
	for i in range(1,11):
		xsix = ('{percent:.2%}'.format(percent=round(float(locals()["six"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["six"+str(i)],xsix)) 
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["six"+str(i)],xsix)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第七名數值分析")
	print("---"*15)
	rgy.write("第七名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in seven:
		locals()["seven"+i] += 1
	for i in range(1,11):
		xseven = ('{percent:.2%}'.format(percent=round(float(locals()["seven"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["seven"+str(i)],xseven)) 
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["seven"+str(i)],xseven)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第八名數值分析")
	print("---"*15)
	rgy.write("第八名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in eight:
		locals()["eight"+i] += 1
	for i in range(1,11):
		xeight = ('{percent:.2%}'.format(percent=round(float(locals()["eight"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["eight"+str(i)],xeight)) 
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["eight"+str(i)],xeight)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第九名數值分析")
	print("---"*15)
	rgy.write("第九名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in nine:
		locals()["nine"+i] += 1
	for i in range(1,11):
		xnine = ('{percent:.2%}'.format(percent=round(float(locals()["nine"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["nine"+str(i)],xnine)) 
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["nine"+str(i)],xnine)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("第十名數值分析")
	print("---"*15)
	rgy.write("第十名數值分析\n")
	rgy.write("---"*15+"\n")
	for i in ten:
		locals()["ten"+i] += 1
	for i in range(1,11):
		xten = ('{percent:.2%}'.format(percent=round(float(locals()["ten"+str(i)]/ig),4)))
		rgy.write("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} \n".format(i,locals()["ten"+str(i)],xten)) 
		print("編號: {:<5} 中獎次數: {:<5} 勝率: {:<5} ".format(i,locals()["ten"+str(i)],xten)) 
	print("---"*15)
	rgy.write("---"*15+"\n")
	print("目前總期數 : {0}".format(ig))
	print("---"*15)
	rgy.write("目前總期數 : {0}".format(ig))
	rgy.write("---"*15+"\n")
	
	rgy.close()
	print ("離開請輸入exit，重新執行請輸入reboot")
	egg = input("請輸入想執行的動作: ")
	
	if egg == "reboot":
		print("程式重新執行")
		print("---"*15)
	elif egg == "exit":
		print("程式關閉")
		break