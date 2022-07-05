import threading
import requests
from colorama import Fore
from colorama import init
import os
from datetime import datetime

init(convert=True)

def GetTokens():
    l = open('tokens.txt','r').read().strip(' ').split('\n')
    return l

TOKENS = GetTokens()
API = f"https://discord.com/api/oauth2/authorize"

def InvalidsONLY(*, token):
    global valids
    r = requests.post(API, headers={'Authorization': f'{token}'})
    response = r.content.decode('utf-8')

    if r'{"client_id": ["This field is required"], "scope": ["This field is required"]}' in response:
        token_check = True
        v = 'Valid'

    else:
        token_check = False
        v = 'Invalid'
        

    if token_check:
        s = 'N/A'


    if v == 'Invalid':
        print(f"{token}")

def ValidsONLY(*, token):
    global valids
    r = requests.post(API, headers={'Authorization': f'{token}'})
    response = r.content.decode('utf-8')

    if r'{"client_id": ["This field is required"], "scope": ["This field is required"]}' in response:
        token_check = True
        v = 'Valid'

    else:
        token_check = False
        v = 'Invalid'
        

    if token_check:
        s = 'N/A'


    if v == 'Valid':
        print(f"{token}")


valids = 0

def Check(*, token):
    global valids
    r = requests.post(API, headers={'Authorization': f'{token}'})
    response = r.content.decode('utf-8')

    if r'{"client_id": ["This field is required"], "scope": ["This field is required"]}' in response:
        token_check = True
        v = 'Valid'
        valids += 1

    else:
        token_check = False
        v = 'Invalid'

    if token_check:
        with open('valid.txt','w')as w:
            w.write(f'{token}\n')


    if v == 'Valid':
        file = open("tokens.txt","r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
  
        for i in CoList:
            if i:
                Counter += 1
                
        now = datetime.now()
        print(f"{Fore.CYAN} [{Fore.RESET}{now.strftime('%H:%M:%S')}{Fore.CYAN}]{Fore.GREEN} [{Fore.RESET}+{Fore.GREEN}] {Fore.CYAN}| {Fore.RESET}{token}  {Fore.CYAN}       |{Fore.RESET} [{valids}/{Counter}]")


    if v == 'Invalid':
        file = open("tokens.txt","r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
  
        for i in CoList:
            if i:
                Counter += 1

        now = datetime.now()
        print(f"{Fore.CYAN} [{Fore.RESET}{now.strftime('%H:%M:%S')}{Fore.CYAN}]{Fore.RED} [{Fore.RESET}-{Fore.RED}] {Fore.CYAN}| {Fore.RESET}{token}  {Fore.CYAN}       |{Fore.RESET} [{valids}/{Counter}]")
        

def Start():
        os.system('title DISCORD TOKEN CHECKER - SUPER#1000')
        os.system('cls & mode 146,34')
        print()
        print(f'''{Fore.LIGHTRED_EX}
                    ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░██████╗░
                    ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗██╔══██╗
                    ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝██████╔╝
                    ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗██╔══██╗
                    ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║██║░░██║
                    ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
        ''')
        print(f"  {Fore.RESET}___________________________________________________________________\n")
        print("  - DEVELOPMENT: \n")
        print(f"{Fore.YELLOW}  [i] {Fore.CYAN}| {Fore.RESET}Discord: SUPER#1000")
        print(f"{Fore.YELLOW}  [i] {Fore.CYAN}| {Fore.RESET}Development: Python Development\n")
        print(f"  {Fore.RESET}___________________________________________________________________\n")
        print("  - CONTINUE: ")
        file = open("tokens.txt","r")
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")
  
        for i in CoList:
            if i:
                Counter += 1

        print(f"\n{Fore.LIGHTBLUE_EX}  [?] {Fore.CYAN}| {Fore.RESET}Are you ready to check {Counter} tokens? (Y/N)")
        confirm = input("  Selection: ")

        if confirm == 'Y':
            os.system('cls')
            with open('tokens.txt','r')as q:
                lines = len(q.readlines())

            amount = lines

            for t in TOKENS:
                th = threading.Thread(target=Check(token=t))
                th.start()

        now = datetime.now()
        print(f"\n{Fore.CYAN} [{Fore.RESET}{now.strftime('%H:%M:%S')}{Fore.CYAN}]{Fore.YELLOW} [{Fore.RESET}i{Fore.YELLOW}] {Fore.RESET}| Scanned {Counter} discord tokens. | {valids}/{Counter} are verified!")
        print(f"\n\n    {Fore.CYAN}[{Fore.RESET}1.{Fore.CYAN}]{Fore.RESET} Print all valid discord tokens{Fore.RESET}.")
        print(f"    {Fore.CYAN}[{Fore.RESET}2.{Fore.CYAN}]{Fore.RESET} Print all invalid discord tokens{Fore.RESET}.")
        print(f"    {Fore.CYAN}[{Fore.RESET}3.{Fore.CYAN}]{Fore.RESET} Exit application.")
        sx = input('    Selection: ')

        if sx == '1':
            os.system('cls')
            with open('tokens.txt','r')as q:
                lines = len(q.readlines())

            amount = lines

            for t in TOKENS:
                th = threading.Thread(target=ValidsONLY(token=t))
                th.start()
            
            print(f"\n{Fore.CYAN}[{Fore.RESET}{now.strftime('%H:%M:%S')}{Fore.CYAN}]{Fore.GREEN} [{Fore.RESET}+{Fore.GREEN}] {Fore.CYAN}| {Fore.RESET}Printed all valid discord tokens, click ENTER to close!")
            input('')

        if sx == '2':
            os.system('cls')
            with open('tokens.txt','r')as q:
                lines = len(q.readlines())

            amount = lines

            for t in TOKENS:
                th = threading.Thread(target=InvalidsONLY(token=t))
                th.start()
            
            print(f"\n{Fore.CYAN}[{Fore.RESET}{now.strftime('%H:%M:%S')}{Fore.CYAN}]{Fore.RED} [{Fore.RESET}-{Fore.RED}] {Fore.CYAN}| {Fore.RESET}Printed all invalid discord tokens, click ENTER to close!")
            input('')


if __name__ == '__main__':
    Start()
