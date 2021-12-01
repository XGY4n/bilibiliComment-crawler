# -*- coding: gbk -*-
#MADE BY BILIBILI XGY4N
import requests
import time
import json
import tkinter as tk
from tkinter import filedialog
import getpass



#------------------------------------?????--------------------------------------------------------------------------------
name=getpass.getuser()
root = tk.Tk()
root.withdraw()

print("please select the place will data save")
time.sleep(3)
Folderpath = filedialog.askdirectory() 
#Filepath = filedialog.askopenfilename() 

print('Folderpath:',Folderpath)
#print('Filepath:',Filepath)

#----------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------BV to AV-------------------------------------------------------------------
table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr={}
for i in range(58):
	tr[table[i]]=i
s=[11,10,3,8,4,6]
xor=177451812
add=8728348608

def dec(x):
	r=0
	for i in range(6):
		r+=tr[x[s[i]]]*58**i
	return (r-add)^xor

#def enc(x):
	x=(x^xor)+add
	r=list('BV1  4 1 7  ')
	for i in range(6):
		r[s[i]]=table[x//58**i%58]
	return ''.join(r)
#-----------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------??----------------------------------------------------------------------------
def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    r = requests.get(url, timeout=30,headers=headers)
    r.raise_for_status()
    r.endcodding = 'utf-8'
    #print(r.text)
    return r.text
#----------------------------------------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------??????---------------------------------------------------------
def get_content(url):
    comments = []
    html = get_html(url)

    try:
        s=json.loads(html)
    except:
        print("jsonload error")

    num=len(s['data']['replies']) 
    # print(num)
    i=0
    while i<num:
        comment=s['data']['replies'][i]

        InfoDict={} 
        
        InfoDict['Uname']=comment['member']['uname'] 
        InfoDict['Like']=comment['like'] 
        InfoDict['Content']=comment['content']['message'] 
        InfoDict['Time']=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(comment['ctime']))  
        
        comments.append(InfoDict)
        i=i+1
    # print(comments)
    return comments
#-------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------???????????----------------------------------------------------------------
def Out2File(dict,j):
    
    
    
    with open(Folderpath+'\\BiliBiliComments.txt', 'a',encoding='utf-8') as f:
        i=0
        
        f.write("!########################################!\n")
        f.write('!############AV number : av{}########!\t\n'.format(av))
        f.write('!############BV number : {}######!\t\n'.format(x))
        f.write("!########################################!\n")
        f.write('!~~~~~~~~page {}~~~~~~~~!\n'.format(j))
        j=j+1
        for comment in dict:
            i=i+1
            
            try:
                f.write('name：{}\t  like：{}\t \n say：{}\t  time：{}\t \n '.format(comment['Uname'], comment['Like'], comment['Content'], comment['Time']))
                f.write("-----------------\n")
            except:
                print("out2File error")
        print('finish')

x=input("please enter BV number :")
av=dec(x)
print("AV number is: AV"+str(av))
print("connect to the url call(YOUR CRAWLING DATA WILL SAVE AS "+Folderpath+"!!) :\n" )
print("https://api.bilibili.com/x/v2/reply?pn= (here should the page of webside) &type=1&oid="+str(av))

if __name__ == '__main__':
    e=0
    page=1
    j=1
    while e == 0 :
        url = "https://api.bilibili.com/x/v2/reply?pn="+ str(page)+"&type=1&oid="+str(av)
        try:
            print()
            # print(url)
            content=get_content(url)
            print("page:",page)
            
            Out2File(content,j)#B??????????
            j=j+1
            page=page+1
            
            if page%10 == 0:
                time.sleep(5)
        except:
            e=1

import  os
os.system( 'pause' )

            #https://api.bilibili.com/x/v2/reply/subject/interaction-status?type=1&oid=205633395 &sort=2 455803935 339957539 BV14h411v79M 
            # c\\Users\\mmm\\Desktop\\py hold\\
