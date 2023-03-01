import pyshorteners
import sys
import os 
import time 
logo = '''
 \u001b[32m _      ____   _____ _____ _   _ 
 | |    / __ \ / ____|_   _| \ | |
 | |   | |  | | |  __  | | |  \| |
 | |   | |  | | | |_ | | | | . ` |
 | |___| |__| | |__| |_| |_| |\  |
 |______\____/ \_____|_____|_| \_|
                                  
                                  

'''
print(logo)
username = "user"
password = "dead"
def exit():
  evil = input()
  sys.exit()

def animated(text):
  for x in text:
    sys.stdout.write(x) 
    sys.stdout.flush()
    time.sleep(0.005)

given_username = input("\u001b[32mEnter The Username : ")
if given_username == username:
  print("")
  print("")
  print("\u001b[32m[ ✔ ] CORRECT USERNAME")
  print("")
  print("")
  given_password = input("\u001b[32mEnter The Password : ")
  if given_password == password:
    print("")
    print("")
    print("\u001b[32m[ ✔ ] LOGIN SUCCESS")
  else:
    print("")
    print("")
    print("\u001b[31m[ ✘ ] WRONG PASSWORD")
    print("")
    print("")
    time.sleep(1)
    print("\u001b[31m ENTER TO EXIT")
    exit()
    
  
else:
  print("")
  print("")
  print("\u001b[31m[ ✘ ] WRONG USERNAME")
  time.sleep(1)
  print("")
  print("")
  print("\u001b[31m ENTER TO EXIT")
  exit()
os.system("clear")
print("")
print("")
print("\u001b[37mINSTALLING PYSHORTENERS FOR THIS TOOL")
time.sleep(2)
print("")
print("")
os.system("pip install pyshorteners")
print("INSTALL COMPLETE")
time.sleep(2)
os.system("clear")
logo2 = '''
   \u001b[93m __    _____   ____ __    
   / /   /  _/ | / / //_/    
  / /    / //  |/ / ,<       
 / /____/ // /|  / /| |      
/_____/___/_/ |_/_/ |_|      
                             
   _____ __  ______  ____  ________________ 
  / ___// / / / __ \/ __ \/_  __/ ____/ __ \
  \__ \/ /_/ / / / / /_/ / / / / __/ / /_/ /
 ___/ / __  / /_/ / _, _/ / / / /___/ _, _/ 
/____/_/ /_/\____/_/ |_| /_/ /_____/_/ |_|  
                                            


Author : EVILXPLOIT
T G    : t.me/Quit69
'''
animated(logo2)
print("")
print("")
link = input("\u001b[32mEnter Your Link : ")
s = pyshorteners.Shortener()
provide = s.tinyurl.short('link')
print(f"\u001b[37m Your Short Link : {provide}")