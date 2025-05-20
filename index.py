import os
print('\n  install colorama package ... ')
os.system('pip install colorama')

from colorama import init, Fore, Back, Style
from modules.home import *
from modules.laravel import *
from modules.module import *
from modules.service import *
import sys
init() 


showCommends()
print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
while(True):
    try:
        enter = input(Fore.RED+'\n |-> ')
        if enter == '1':
            ChoosingLaravelStructure()
        if enter == '2':
            listCommends()
        if enter == '3':
            listCommendsService()
        elif enter == '4':
            devolper()
        elif enter == '5':
            sys.exit()       
        else:
            showCommends()
    except KeyboardInterrupt:
        sys.exit()
