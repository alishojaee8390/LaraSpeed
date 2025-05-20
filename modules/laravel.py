import os 
from colorama import init, Fore, Back, Style
import time
from modules.home import *

current_dir = os.getcwd()

appName = ""

def wellcome():
    os.system('cls')
    print(Fore.RED+"""
          
       [*] Wellcome To Install Laravel [*]
          
          """)

def ChoosingLaravelStructure():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' blade')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' api')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enterStructure = input(Fore.RED+'\n |-> ')
    if enterStructure == '1':
        installLaravelBlade()
    elif enterStructure == '2':
        installLaravelApi()
    elif enterStructure == '3':
        showCommends()
    else:
        ChoosingLaravelStructure()  
         
def installLaravelApi():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 9')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 10')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 11')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 12')
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version latest')
    print(Fore.RED +' ['+Fore.WHITE+'6'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enterVersion = input(Fore.RED+'\n |-> ')
  
    if os.path.exists('projects'):
        os.chdir('projects')
    else:
        os.mkdir('projects') 

    if enterVersion == '1':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^9.0 ' + enterAppName)
                target = os.path.join(current_dir, 'projects' + os.sep + enterAppName)
                if os.path.exists(target):
                    os.chdir(target)
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/ui ... ')
                    time.sleep(1)
                    os.system('composer require laravel/ui')
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/sanctum ... ')
                    time.sleep(1)
                    os.system('composer require laravel/sanctum')
                    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter back to home")

            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '2':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^10.0 ' + enterAppName)
                target = os.path.join(current_dir, 'projects' + os.sep + enterAppName)
                if os.path.exists(target):
                    os.chdir(target)
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/ui ... ')
                    time.sleep(1)
                    os.system('composer require laravel/ui')
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/sanctum ... ')
                    time.sleep(1)
                    os.system('composer require laravel/sanctum')
                    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter back to home")

            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '3':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... \n')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^11.0 ' + enterAppName)
                target = os.path.join(current_dir, 'projects' + os.sep + enterAppName)
                if os.path.exists(target):
                    os.chdir(target)
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/ui ... ')
                    time.sleep(1)
                    os.system('composer require laravel/ui')
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/sanctum ... ')
                    time.sleep(1)
                    os.system('composer require laravel/sanctum')
                    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter back to home")
                    
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '4':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^12.0 ' + enterAppName)
                target = os.path.join(current_dir, 'projects' + os.sep + enterAppName)
                if os.path.exists(target):
                    os.chdir(target)
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/ui ... ')
                    time.sleep(1)
                    os.system('composer require laravel/ui')
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/sanctum ... ')
                    time.sleep(1)
                    os.system('composer require laravel/sanctum')
                    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter back to home")
                    
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '5':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel ' + enterAppName)
                target = os.path.join(current_dir, 'projects' + os.sep + enterAppName)
                if os.path.exists(target):
                    os.chdir(target)
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/ui ... ')
                    time.sleep(1)
                    os.system('composer require laravel/ui')
                    print(Fore.LIGHTCYAN_EX+'\n  install laravel/sanctum ... ')
                    time.sleep(1)
                    os.system('composer require laravel/sanctum')
                    print(Fore.LIGHTBLACK_EX+"\n [!] Please enter back to home")
                    
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '6':
            showCommends()
    else:
        installLaravelApi()    
   
def installLaravelBlade():
    wellcome()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 9')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 10')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 11')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version 12')
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' install laravel version latest')
    print(Fore.RED +' ['+Fore.WHITE+'6'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enterVersion = input(Fore.RED+'\n |-> ')
  
    if os.path.exists('projects'):
        os.chdir('projects')
    else:
        os.mkdir('projects')    
    if enterVersion == '1':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^9.0 ' + enterAppName)
                installPackageAuth(enterAppName)
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '2':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^10.0 ' + enterAppName)
                installPackageAuth(enterAppName)
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '3':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... \n')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^11.0 ' + enterAppName)
                installPackageAuth(enterAppName)
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '4':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel:^12.0 ' + enterAppName)
                installPackageAuth(enterAppName)
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '5':
            wellcome()
            print(Fore.LIGHTBLACK_EX+'  Enter App Name')
            enterAppName = input(Fore.RED+'\n |-> ')
            if enterAppName:
                print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
                time.sleep(1)
                os.system('composer create-project --prefer-dist laravel/laravel ' + enterAppName)
                installPackageAuth(enterAppName)
            else:
                wellcome()
                print(Fore.LIGHTBLACK_EX+'  Enter App Name')
    elif enterVersion == '6':
            showCommends()
    else:
        installLaravelBlade()    
    
def installPackageAuth(appName):
    os.system('cls')
   
    print(Fore.RED+"""
          
       [*] Wellcome To Install Package Auth Laravel [*]
          
          """)
    if os.path.exists('/projects/' + appName):
        target = os.path.join(current_dir, '/projects/' + appName)
        os.chdir(target)
    else:
        print(Fore.CYAN+'[!] project not found Please create a new project [!]')
        time.sleep(3)
        installLaravelBlade()
    print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' install laravel Breeze')
    print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' install laravel Fortify')
    print(Fore.RED +' ['+Fore.WHITE+'3'+ Fore.RED+']'+ Fore.WHITE + ' install laravel Jetstream')
    print(Fore.RED +' ['+Fore.WHITE+'4'+ Fore.RED+']'+ Fore.WHITE + ' install laravel Passport')
    print(Fore.RED +' ['+Fore.WHITE+'5'+ Fore.RED+']'+ Fore.WHITE + ' install laravel Socialite')
    print(Fore.RED +' ['+Fore.WHITE+'6'+ Fore.RED+']'+ Fore.WHITE + ' Back to home')
    print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
    enterPackage = input(Fore.RED+'\n |-> ')
    if enterPackage == '1':
        print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
        time.sleep(1)
        os.system('composer require laravel/breeze --dev')
        time.sleep(1)
        print(Fore.LIGHTCYAN_EX+'\n  Installing breeze ... ')
        os.system('php artisan breeze:install')
        time.sleep(1)
        print(Fore.LIGHTCYAN_EX+'\n  run npm install ... ')
        os.system('npm install')
        time.sleep(1)
        print(Fore.LIGHTCYAN_EX+'\n  run migration ... ')
        os.system('php artisan migrate')
    elif enterPackage == '2':
        print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
        time.sleep(1)
        os.system('composer require laravel/fortify')
    elif enterPackage == '3':

        print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
        time.sleep(1)
        os.system('composer require laravel/jetstream')
        print(Fore.RED +' ['+Fore.WHITE+'1'+ Fore.RED+']'+ Fore.WHITE + ' jetstream with livewire')
        print(Fore.RED +' ['+Fore.WHITE+'2'+ Fore.RED+']'+ Fore.WHITE + ' jetstream with inertia')
        print(Fore.LIGHTBLACK_EX+"\n [!] Please select an option")
        enterJetstrim = input(Fore.RED+'\n |-> ')
        if enterJetstrim == '1':
            print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
            time.sleep(1)
            os.system('php artisan jetstream:install livewire')
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX+'\n  run npm install ... ')
            os.system('npm install')
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX+'\n  run migration ... ')
            os.system('migration')
        if enterJetstrim == '2':
            print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
            time.sleep(1)
            os.system('php artisan jetstream:install inertia')
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX+'\n  run npm install ... ')
            os.system('npm install')
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX+'\n  run migration ... ')
            os.system('migration')
    elif enterPackage == '4':
        print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
        time.sleep(1)
        os.system('composer require laravel/passport')
        time.sleep(1)
        print(Fore.LIGHTCYAN_EX+'\n  run migration ... ')
        os.system('php artisan migrate')
        time.sleep(1)
        print(Fore.LIGHTCYAN_EX+'\n  run passport install ... ')
        os.system('php artisan passport:install')
    elif enterPackage == '5':
        print(Fore.LIGHTCYAN_EX+'\n  Please Wait ... ')
        time.sleep(1)
        os.system('composer require laravel/socialite')     
    else:
        installPackageAuth()