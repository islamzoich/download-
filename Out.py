import requests
import pyfiglet
import os
os.system("pip install pyfiglet ")
os.system("pip install requests")
os.system("clear")
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
ss = pyfiglet.figlet_format('jhenm',font='colossal') 
print(ss) 
i=input("\033[2;36menter the eamil : ")
print("---------------------")
url = "https://www.instagram.com/api/v1/web/accounts/check_email/" 


headers = {

	 'accept': '*/*',

	 'accept-encoding': 'gzip, deflate, br',

	 'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',

	 'content-length': '30',

	 'content-type': 'application/x-www-form-urlencoded',

	 'cookie': 'csrftoken=OuvUFtGYLThj0EEZJg62u6bYHxbcXd4b; mid=ZTt78QABAAEbwUSWuNXI7n-622E_; ig_did=3ED5E3B2-A5DF-4087-BFD4-C6C6843F8E5E; ig_nrcb=1; dpr=2.768749952316284; datr=53s7Ze2JEvyfBQKo_WxnTLki',

	 'dpr': '2.76875',

	 'origin': 'https://www.instagram.com',

	 'referer': 'https://www.instagram.com/accounts/signup/email/',

	 'sec-ch-prefers-color-scheme': 'dark',

	 'sec-ch-ua': '"Chromium";v="95", ";Not A Brand";v="99"',

	 'sec-ch-ua-mobile': '?1',

	 'sec-ch-ua-model': '"22021211RG"',

	 'sec-ch-ua-platform': '"Android"',

	 'sec-ch-ua-platform-version': '"13.0.0"',

	 'sec-fetch-dest': 'empty',

	 'sec-fetch-mode': 'cors',

	 'sec-fetch-site': 'same-origin',

	 'user-agent': 'Mozilla/5.0 (Linux; Android 13; 22021211RG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36',

	 'viewport-width': '391',

	 'x-asbd-id': '129477',

	 'x-csrftoken': 'OuvUFtGYLThj0EEZJg62u6bYHxbcXd4b',

	 'x-ig-app-id': '1217981644879628',

	 'x-ig-www-claim': '0',

	 'x-instagram-ajax': '1009525636',

	 'x-requested-with': 'XMLHttpRequest',

} 


data = {

	 'email': f'{i}',

}



r=requests.post(url,headers=headers,data=data).text
if "email_is_taken" in r:
	print("\033[1;31mNo, he is shagged ")
else:
	print("\033[2;32mok man")

