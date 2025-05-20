from colorama import init, Fore, Back, Style
import os



def showText():
    os.system('cls')
    print(Fore.GREEN+"""
       ** laravel install and project **
       
        """)

def showCommends():
    showText()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' install laravel ')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' add module to project ')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' add service to project ')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' developer ')
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' Exit ')

def devolper():
    os.system('cls')
    print(Fore.GREEN+"""
author -> ali shojaee
telegram -> @alishojaee90
email -> alishojaee@gmail.com
[!] Help develop this package
        """)
    print(Fore.LIGHTBLACK_EX+' Plase enter back to home ...')

