from platform import platform
import sys , os
from tokenize import cookie_re 
from time import sleep
import asyncio
try:
    
    import colorama , pyfiglet 
    from telethon import TelegramClient , events
    import telethon

except:
    if "win" in sys.platform:
        os.system("pip install telethon pyfiglet colorama")
        import colorama , pyfiglet
        from telethon import TelegramClient , events
        import telethon
    else:
        os.system("pip3 install telethon pyfiglet colorama")
        import colorama , pyfiglet 
        from telethon import TelegramClient , events 
        import telethon


rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
mag = colorama.Fore.MAGENTA
yl = colorama.Fore.YELLOW
cm = colorama.Fore.LIGHTCYAN_EX
api_id = 5260869
api_hash = "dbf04bf7514ea76c3202375027f1fd74"
def logo():
    figlet = pyfiglet.Figlet(font="standard")
    return figlet.renderText("Remax Box ")

print (cm + logo())
print (gn + "This script Made By Maximum Radikali ")
print (bl + "Telegram Channel Is : https://t.me/RemaxBoxTeam")

print (rd + "[-] Welcome to Check Virtual Number Telegram Script [-]")
for i in range(14):
    sys.stdout.write(cm + "\r[*] waiting ")
    sleep(0.2)
    sys.stdout.write(cm + "\r[*] waiting .")
    sleep(0.2)
    sys.stdout.write(cm + "\r[*] waiting ..")
    sleep(0.2)
    sys.stdout.write('\033[D \033[D')
    sleep(0.2)
    sys.stdout.write('\033[D \033[D')
    sleep(0.2)
for x in range(8):
    sys.stdout.write('\033[D \033[D')

selector = input(yl + "\n\n[+] Please Select Option That You Want : \n-1 single number\n-2 multi numbers \n\n : ")


async def checksnumber(number):
    try:
        client = TelegramClient("testor",api_id,api_hash)
        await client.connect()
        await client.send_code_request(number)
        return (gn + "[-] Your number is not banned , Your number is correct . "+ cv ) 
    except telethon.errors.rpcerrorlist.PhoneNumberInvalidError:
        return (rd + "[=] Your number is invalid , Try again :) " + cv)
    except telethon.errors.rpcerrorlist.PhoneNumberBannedError:
        return (rd + "[&] Sorry , Your number has been banned .  " + cv)


async def checkmnumber(file):

    numberx = open("file.txt","r")
    for i in numberx:
        znm = i.strip()
        try:
            client = TelegramClient("testor",api_id,api_hash)
            await client.connect()
            await client.send_code_request(znm)
            print (gn + f"[$] Your Number : {znm}\n is Correct , Not Banned yet " + cv)
            continue
        except telethon.errors.rpcerrorlist.PhoneNumberInvalidError:
            print (rd + f"[=] Your number : {znm}\n is invalid , Try again :) " + cv)
            continue
        except telethon.errors.rpcerrorlist.PhoneNumberBannedError:
            print (yl + f"[&] Sorry , Your number : {znm}\n has been banned .  " + cv)
            continue

if selector == "1":
    print (gn + "[-] You selected first Option :)")
    number = input(mag + "[<>] Please Enter a single Number with countrycode\nEX:(+1715xxxxxxx)\n\n[-]=> ")
    if "win" in sys.platform:
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        print (loop.run_until_complete(checksnumber(number)))
    else:
        asyncio.run(checksnumber())
elif selector == "2":
    print (gn + "[-] You selected first Option :)")
    file = input(bl + "[-] Please Enter your number list of file txt\n\nEX : number.txt\n\n--> ")
    if "win" in sys.platform:
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(checkmnumber(file))
    else:
        asyncio.run(checkmnumber())
        
