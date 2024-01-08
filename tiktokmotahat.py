
import random
import requests
import time
from uuid import uuid4
uid = uuid4()
from rich.console import Console
from rich.table import Table
import threading
import requests
import random
import threading
O = '\x1b[38;5;208m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
K = '\x1b[2;35m'
B = '\x1b[2;36m'
E = '\x1b[1;31m'
Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
C1 = '\x1b[2;35m'
G = '\x1b[1;35m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
M = '\x1b[1;37m'
S = '\x1b[1;33m'
U = '\x1b[1;37m'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
import requests
import sys
import os
import time
import pyfiglet
print(O + ' ')
table = Table(title='Tools Check tiktok Accounts Email', style='red')

console = Console()
console.print(table)
XF = Console()
token = input(O + ' -Enter Your Tokne : ')
ID = input(O + ' -Enter Your ID : ')
print('                    ')
import requests
def sui():
  while True:
    try:
        user = '1234567890.asdfghjklqwertyuiopzxcvbnm'
        num = ('Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley', 'Jennifer', 'Joshua', 'Amanda', 'David', 'Daniel', 'James', 'Robert', 'John', 'Joseph', 'Andrew', 'Ryan', 'Brandon', 'Jason', 'Justin', 'Sarah', 'William', 'Jonathan', 'Stephanie', 'Brian', 'Nicole', 'Nicholas', 'Anthony', 'Heather', 'Elizabeth', 'Megan', 'Adam', 'Eric', 'Melissa', 'Kevin', 'Steven', 'Thomas')
        rang = str(''.join(random.choice(num) for i in range(1)))
        name = ''.join(random.choice(user) for i in range(6))
        username = name
        email = name + '@gmail.com'
        res = requests.get(f'''https://GmailandTiktokandzaid.zaidbot.repl.co/2/email={email}''').text
        if '"Dev":"@T_65F","Email":"Good"' in res:
            print(f'''{O}Good Email : {email}''')
        api = requests.get(f'''https://api.dlyar-dev.tk/info-tiktok.json?user={username}''').json()
        if api['status'] == True:
            name = api['name']
            followers = api['followers']
            following = api['following']
            like = api['likes']
            id = api['id']
            code = api['code-country']
            country = api['country']
            tlg = f'''𓊆ارهابي جابلك حساب تيكتوك𓊇\n\n⋘─────━𓌹𓏺ِِٰٕٓHP𓌺━─────⋙\n❖ - 𝖓𝖆𝖒𝖊 : {name}\n❖ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : {username}\n❖️ - 𝖊𝖒𝖆𝖎𝖑 : {email}\n❖️ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 :  {followers}\n❖ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 : {following}\n❖️ - 𝖑𝖎k𝖊 :  {like}\n❖️ - 𝖎𝖉 : {id}\n\n⋘─────━𓌹𓏺ِِٰٕٓHP𓌺━─────⋙\  '''
            tlg = f'''\n ����رهابي جابلك حساب تيكتوك𓊇\n\n⋘─────━𓌹𓏺ِِٰٕٓHP𓌺━─────⋙\n❖ - 𝖓𝖆𝖒𝖊 : {name}\n❖ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : {username}\n❖️ - 𝖊𝖒𝖆𝖎𝖑 : {email}\n❖️ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 :  {followers}\n❖ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 : {following}\n❖️ - 𝖑𝖎k𝖊 :  {like}\n❖️ - 𝖎𝖉 : {id}\n\n⋘─────━𓌹HP𓌺━─────⋙\n❖ - '''
            requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(tlg))
            print(tlg)
        else:
            print(f''' Bad Gmail : {email}''')
    except:
        print(f''' Bad Gmail : {email}''')
sui()
