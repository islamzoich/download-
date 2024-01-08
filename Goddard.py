import os, sys, time, marshal, py_compile
#from mahos import Enc
#___________الالوان___________#
red = '\033[91m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[33m'
E = '\033[1;31m'
G = '\033[1;32m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\x1b[38;5;208m' #ذهبي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
#___________الالوان___________#
print(f'''{B}{F}━━━━━━━━━━━━⧪━━━━━━━━━━{B}
|{Z}[+] YouTube    : {B}| أحمد الحراني
|{Z}[+] TeleGram  : {B} maho_s9    |
|{Z}[+] Instagram  : {B}ahmedalharrani |
|{Z}[+] Tool  : {B} Enc - تشفير
{F}━━━━━━━━━━━━⧪━━━━━━━━━━━━ ''')
#___________الاختيار___________#
print(f'''
{red}
[1] - تشفير مارشال
-------------------------
{blue}
[2] تشفير pyc قوي جدا
-------------------------
''')

Ahmed = int(input(f"{yellow}اختر اي تشفير -> "))
print(green+"________________________________________")
print("")
#___________التشفير___________#
if Ahmed == 1:
    try:
        file = input(yellow+'Enter the file name: ')
        Mahos = file.replace('.py', '')
    except KeyboardInterrupt:
        sys.exit()
    else:
        try:
            strng = open(file, 'r').read()
        except IOError:
            print(red+'الملف غير موجود')
            sys.exit()
        try:
            code = compile(strng, '', 'exec')
            data = marshal.dumps(code)
        except TypeError:
            print(red+'الملف مشفر حاليا')
            sys.exit()

    with open(Mahos + '-enc.py', 'w') as fileout:
        fileout.write('#Dev : @maho9s\n')
        fileout.write('import marshal\n')
        fileout.write(f'exec(marshal.loads({repr(data)}))')
    #___________حفظ للتشفير___________#
    time.sleep(3)
    print(green+'تم تشفير الملف بنجاح :' + Mahos + '-enc.py')
#___________Dev"mahos___________#
elif Ahmed == 2:
    file = input(yellow+'Enter the file name: ')
    py_compile.compile(file)
    print(green+"تم تشفير الملف بنجاح :" + file +"c")
