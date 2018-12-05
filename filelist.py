import os
import colorama
from colorama import Fore, Back, Style


str = input("Enter the path: ")

for fname in os.listdir(str):
    path = os.path.join(str,fname)
    if os.path.isdir(path):
        print (Fore.GREEN + path)

    else:
        print (Fore.WHITE + path)
