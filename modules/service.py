import os 
from colorama import init, Fore, Back, Style
import time
from modules.home import *
from modules.helpers import *

current_dir = os.getcwd()
serviceFolder = os.path.join(current_dir , 'services')
projectFolder = os.path.join(current_dir , 'projects')
pathProjectService =  os.path.join(current_dir , 'projects' + os.sep + 'app' + os.sep + 'Http' + 'Services')

def wellcome():
    os.system('cls')
    print(Fore.RED+f"""     
    [*] Wellcome To add service to project Laravel [*]
 |-----------------------Tips--------------------------|
 
    {Fore.LIGHTBLACK_EX}[!] Please use only for API projects 
    [!] Please run xammp before adding
    [!] Please turn on your internet

          """)
       
def listCommendsService():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' file ' + Fore.LIGHTCYAN_EX + "(service upload file)")
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' image '+ Fore.LIGHTCYAN_EX + "(service upload image)")
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' payment ' + Fore.LIGHTCYAN_EX + "(service payment gateway default -> zarinpal)")
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' sms and email' + Fore.LIGHTCYAN_EX + "(service email and send sms defualt -> melipayamk)")
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enter = input(Fore.RED+'\n |-> ')
    if enter == '1':
        print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
        appName = input(Fore.RED+'\n |-> ')
        addFileService(appName)
    if enter == '2':
        print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
        appName = input(Fore.RED+'\n |-> ')
        addImageService(appName)
    if enter == '3':
        print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
        appName = input(Fore.RED+'\n |-> ')
        addPaymentService(appName)
    if enter == '4':
        print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
        appName = input(Fore.RED+'\n |-> ')
        addEmailAndSmsService(appName)
    if enter == '5':
        showCommends()        
    else:
        listCommendsService()
    
def addFileService(appName):
    wellcome()
    emailService = serviceFolder + os.sep + 'File'
    pathProject = projectFolder + os.sep + appName
    pathProejctAppHttp = os.path.join(current_dir , 'projects' + os.sep + appName  + os.sep + 'app' + os.sep + 'Http' + os.sep + 'Services' + os.sep + 'File')
    if os.path.exists(pathProject):
        if not os.path.exists(pathProejctAppHttp):
            print(Fore.LIGHTWHITE_EX+" [!] Please wait ...")
            time.sleep(1)
            copy_folder(emailService , pathProejctAppHttp)
            time.sleep(1)
            print(Fore.GREEN+" add file service successful")
        else:
            print(Fore.RED+" file service already exists ")
            time.sleep(2)
            listCommendsService()
            
    else:
        print(Fore.RED+"[!] project not found")
        time.sleep(2)
        listCommendsService()
        
def addEmailAndSmsService(appName):
    wellcome()
    emailAndSmsService = serviceFolder + os.sep + 'Message'
    pathProject = projectFolder + os.sep + appName
    pathProejctAppHttp = os.path.join(current_dir , 'projects' + os.sep + appName  + os.sep + 'app' + os.sep + 'Http' + os.sep + 'Services' + os.sep + 'Message')
    if os.path.exists(pathProject):
        if not os.path.exists(pathProejctAppHttp):
            print(Fore.LIGHTWHITE_EX+" [!] Please wait ...")
            time.sleep(1)
            copy_folder(emailAndSmsService , pathProejctAppHttp)
            time.sleep(1)
            print(Fore.GREEN+" add email and sms service successful")
            with open(pathProejctAppHttp + os.sep + 'help.txt', 'w') as file:
                file.write("""
                           
!!! soap client on your server enabled !!!                           

Please set config email -> 
Go to file .env
Edit config -> 
    MAIL_MAILER=smtp
    MAIL_SCHEME=null
    MAIL_HOST=smtp.googlemail.com
    MAIL_PORT=587
    MAIL_USERNAME=your email
    MAIL_PASSWORD="your password" 
    MAIL_FROM_ADDRESS="your form address"
    MAIL_FROM_NAME="${APP_NAME}"
    MAIL_ENCRYPTION=tls
    
    
Please set config sms in .env
    Go to file .env
    SMS_USERNAME=your username
    SMS_PASSWORD=your password
    SMS_FROM= from
    And Go to config folder create a sms.php and write ->
    <?php
    return [
        'username' => env('SMS_USERNAME'),
        'password' => env('SMS_PASSWORD'),
        'from' => env('SMS_FROM'),
    ];""")
            print(Fore.BLUE+"please check file help.txt in service Message Folder")
            time.sleep(2)
            
        else:
            print(Fore.RED+" email and sms service already exists ")
            time.sleep(2)
            listCommendsService()
            
    else:
        print(Fore.RED+"[!] project not found")
        time.sleep(2)
        listCommendsService()

def addImageService(appName):
    wellcome()
    imageService = serviceFolder + os.sep + 'Image'
    pathProject = projectFolder + os.sep + appName
    pathProejctAppHttp = os.path.join(current_dir , 'projects' + os.sep + appName  + os.sep + 'app' + os.sep + 'Http' + os.sep + 'Services' + os.sep + 'Image')
    print(Fore.LIGHTWHITE_EX+" [!] Please wait ...")
    print(Fore.LIGHTWHITE_EX+" [!] installing package intervention/image ...")
    try:
        os.chdir(pathProject)
        os.system('composer require intervention/image')
        time.sleep(5)
        if os.path.exists(pathProject):
            if not os.path.exists(pathProejctAppHttp):
                print(Fore.LIGHTWHITE_EX+" [!] Please wait ...")
                time.sleep(1)
                copy_folder(imageService , pathProejctAppHttp)
                time.sleep(1)
                print(Fore.GREEN+" add image service successful")
            else:
                print(Fore.RED+" image service already exists ")
                time.sleep(2)
                listCommendsService()
                
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            listCommendsService()
    except:
        print('can not download package intervention/image')
            
def addPaymentService(appName):
    wellcome()
    paymentService = serviceFolder + os.sep + 'Payment'
    pathProject = projectFolder + os.sep + appName
    pathProejctAppHttp = os.path.join(current_dir , 'projects' + os.sep + appName  + os.sep + 'app' + os.sep + 'Http' + os.sep + 'Services' + os.sep + 'Payment')
    print(Fore.LIGHTWHITE_EX+" [!] Please wait ...")
    print(Fore.LIGHTWHITE_EX+" [!] installing package pishran/zarinpal ...")
    try:
        os.chdir(pathProject)
        os.system('composer require pishran/zarinpal')
        time.sleep(5)
        with open(pathProejctAppHttp + os.sep + 'help.txt', 'w') as file:
            file.write("""
                           
Please set config pyment zarinpal -> 
    Go to file .env
    ZARINPAL_MERCHANT_ID= your Merchant_ID
    And Go to config folder create a payment.php and write ->
   <?php
    return [
        'zarinpal_api_key' => env('ZARINPAL_MERCHANT_ID'),
    ];
""")
            print(Fore.BLUE+"please check file help.txt in service payment Folder")
            time.sleep(2)
        if os.path.exists(pathProject):
            if not os.path.exists(pathProejctAppHttp):
                print(Fore.LIGHTWHITE_EX+" [!] Please wait ...")
                time.sleep(1)
                copy_folder(paymentService , pathProejctAppHttp)
                time.sleep(1)
                print(Fore.GREEN+" add file service successful")
            else:
                print(Fore.RED+" file service already exists ")
                time.sleep(2)
                listCommendsService()
                
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            listCommendsService()
    except:
        print('can not download package intervention/image')       
        
        
        
        
        