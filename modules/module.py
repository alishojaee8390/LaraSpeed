
import os 
from colorama import init, Fore, Back, Style
import time
from modules.home import *
import subprocess
current_dir = os.getcwd()
projectFolder = os.path.join(current_dir , 'projects')


def create(path , folderName , name):
    os.chdir(path)
    os.system(f'php artisan make:controller Admin/{folderName}/{name}Controller')
    os.system(f'php artisan make:request Admin/{folderName}/{name}Request')
    os.system(f'php artisan make:model {folderName}/{name} -m')
    os.system(f'php artisan make:resource Admin/{folderName}/{name}Resource')
    os.system(f'php artisan make:resource Admin/{folderName}/{name}Collection')

def migrate(path):
    os.chdir(path)
    os.system(f'php artisan migrate')

def wellcome():
    os.system('cls')
    print(Fore.RED+f"""     
    [*] Wellcome To add module to project Laravel [*]
 |-----------------------Tips--------------------------|
 
    {Fore.LIGHTBLACK_EX}[!] Please use only for API projects 
    [!] Please run xammp before adding
    [!] Please add services before adding    
    [!] Please turn on your internet

          """)

def listCommends():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' content ' + Fore.LIGHTCYAN_EX + "(modules content site)")
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' market '+ Fore.LIGHTCYAN_EX + "(modules market site)")
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' notify ' + Fore.LIGHTCYAN_EX + "(modules notify site -> email and sms)")
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' setting ' + Fore.LIGHTCYAN_EX + "(modules setting site)")
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' ticket ' + Fore.LIGHTCYAN_EX + "(modules ticket site)")
    print(Fore.RED +' ['+Fore.WHITE+'6'+ Fore.RED+']'+ Fore.WHITE + ' custom ' + Fore.LIGHTCYAN_EX + "(you custom)")
    print(Fore.RED +' ['+Fore.WHITE+'7'+ Fore.RED+']'+ Fore.WHITE +  Fore.RED + ' migreate (Please enter the database values ​​and then proceed migration )')
    print(Fore.RED +' ['+Fore.WHITE+'8'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enter = input(Fore.RED+'\n |-> ')
    if enter == '1':
        content()
    elif enter == '2':
        market()
    elif enter == '3':
       notify()
    elif enter == '4':
       setting()
    elif enter == '5':
       ticket()      
    elif enter == '6':
       ticket()      
  
        
def content():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' category ')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' menu ')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' article ')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' banner ')
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' faq ')
    print(Fore.RED +' ['+Fore.WHITE+'6'+ Fore.RED+']'+ Fore.WHITE + ' page ')
    print(Fore.RED +' ['+Fore.WHITE+'7'+ Fore.RED+']'+ Fore.WHITE + ' comment ')
    print(Fore.RED +' ['+Fore.WHITE+'8'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enter = input(Fore.RED+'\n |-> ')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
    appName = input(Fore.RED+'\n |-> ')
    myProject = os.path.join(projectFolder + os.sep + appName)
    if enter == '1':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject, 'Content' ,'Category')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            content()
        
    elif enter == '2':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Content' ,'Menu')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            content()
        
    elif enter == '3':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Content' ,'Article')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            content()
        
    elif enter == '4':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Content' ,'Banner')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            content()
        
    elif enter == '5':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Content' ,'Faq')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            content()
        
    elif enter == '6':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Content' ,'Page')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            content()
        
    elif enter == '7':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Content' ,'Comment')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            content()
    elif enter == '8':        
        listCommends()
    else:
        content()
        
def market():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' category ')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' brand ')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' product ')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' delivery ')
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' payment ')
    print(Fore.RED +' ['+Fore.WHITE+'6'+ Fore.RED+']'+ Fore.WHITE + ' comment ')
    print(Fore.RED +' ['+Fore.WHITE+'7'+ Fore.RED+']'+ Fore.WHITE + ' store ')
    print(Fore.RED +' ['+Fore.WHITE+'8'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')    
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enter = input(Fore.RED+'\n |-> ')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
    appName = input(Fore.RED+'\n |-> ')
    myProject = os.path.join(projectFolder + os.sep + appName)
    if enter == '1':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Market' ,'ProductCategory')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            market()
        
    elif enter == '2':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Market' ,'Brand')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            market()
        
    elif enter == '3':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Market' ,'Product')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            market()
        
    elif enter == '4':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Market' ,'Delivery')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            market()
        
    elif enter == '5':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Market' ,'Payment')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            market()
        
    elif enter == '6':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Market' ,'Comment')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            market()
        
    elif enter == '7':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Market' ,'Store')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            market()
    elif enter == '8':        
        listCommends()        
    else:
        market()
        
def notify():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' Email ')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' EmailFile ')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' SMS ')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')  
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enter = input(Fore.RED+'\n |-> ')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
    appName = input(Fore.RED+'\n |-> ')
    myProject = os.path.join(projectFolder + os.sep + appName)
    if enter == '1':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Notify' ,'Email')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            notify()
        
    elif enter == '2':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Notify' ,'EmailFile')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            notify()
        
    elif enter == '3':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Notify' ,'SMS')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            notify()
    elif enter == '4':        
        listCommends()
    else:
        notify()
        
        
def ticket():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' Ticket ')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' TicketPriority ')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' TicketCategory ')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' TicketAdmin ')
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enter = input(Fore.RED+'\n |-> ')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
    appName = input(Fore.RED+'\n |-> ')
    myProject = os.path.join(projectFolder + os.sep + appName)
    if enter == '1':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Ticket' ,'Ticket')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            ticket()
        
    elif enter == '2':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Ticket' ,'TicketPriority')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            ticket()
    elif enter == '3':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Ticket' ,'TicketCategory')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            ticket()
        
    elif enter == '4':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Ticket' ,'TicketAdmin')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            ticket()
    elif enter == '5':        
        listCommends()           
    else:
        ticket()
        
       
def setting():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' Setting ')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enter = input(Fore.RED+'\n |-> ')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter app name project")
    appName = input(Fore.RED+'\n |-> ')
    myProject = os.path.join(projectFolder + os.sep + appName)
    if enter == '1':
        if os.path.exists(myProject):
            print(Fore.GREEN+"\n [!] Adding to Project Please Waite ...")
            create(myProject,'Ticket' ,'Setting')
            time.sleep(3)
        else:
            print(Fore.RED+"[!] project not found")
            time.sleep(2)
            setting()
    elif enter == '2':        
        listCommends()
    else:
        setting()
        