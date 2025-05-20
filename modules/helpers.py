import shutil
import subprocess
import os 
from colorama import init, Fore, Back, Style


# def installComposerPackage(package_name):

#     try:
#         result = subprocess.run(
#             ['composer', 'require', package_name],
#             capture_output=True,
#             text=True,
#             check=True,
#             timeout=60 
#         )
#         print(result.stdout)
#         print(Fore.LIGHTWHITE_EX+" [!] package installed ...")

#         return True
#     # except FileNotFoundError:
#     #     print(Fore.RED+"\n check your internet or Make sure the Composer is installed.")
#     #     return False
#     except subprocess.CalledProcessError as e:
#         print(f"Error installing the package: {e.stderr}")
#         return False
#     except subprocess.TimeoutExpired:
#         print("The wait time was too long.")
#         return False
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return False



def copy_folder(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f" folder '{source_folder}' is not found")
        return False
    
    try:
        shutil.copytree(source_folder, destination_folder)
        # print(f"  '{source_folder}'  '{destination_folder}' ")
        return True
    except OSError as e:
        print(f"error {e}")
        return False
