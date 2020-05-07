#!/usr/bin/env python3
#NOTE:THIS SCRIPT IS ONLY FOR EDUCATIONAL PURPOSES, I DON,T TAKE ANY RESPONSIBLITY OF WHAT YOU DO WITH THIS SCRIPT.
import sys
import os
import zipfile 

file_name = ''
zip_file_name = ''

def zip_cracker_code():
    zip_file_name = input("[+] Enter the zip file directory: ")
    obj = zipfile.ZipFile(zip_file_name)
    
    fi = open(file_name, 'rb')
    
    for word in fi.readlines():
          Words = word.strip()

          try:
              with zipfile.ZipFile(zip_file_name, 'r') as zip:
                                    zip_file_name.extractall(pwd = Words)
                                    print("password found: %s" %(Words.decode('utf8')))

              
          except:
              print('Trying...')
                         
             
banner = '''
  _____         ___             _           
 |_  (_)_ __   / __|_ _ __ _ __| |_____ _ _ 
  / /| | '_ \ | (__| '_/ _` / _| / / -_) '_|
 /___|_| .__/  \___|_| \__,_\__|_\_\___|_|  
       |_|

       Coded by: 0_404 :)

'''
print(banner)
file_name = input("[+] Enter bruteforce file name with full directory: ")

try:
    f = open(file_name, 'rb')
    f.close()
    print(os.path.dirname(file_name))
    user = input("[+] Is this the file directory for bruteforcing[Y/n]")
    if user == 'Y' or 'y'or 'yes':
        zip_cracker_code()
    else:
        sys.exit()
except FileNotFoundError:
    print("[+] The file u want is not found/ not in current directory")
    print("\n[+] Check your current directory by pressing cwd")
    print("\n[+] Or press q to exit")

    k = input()
    if k =='q':
        print("Bye!!")
        sys.exit()
    elif k == 'cwd':
        print(os.getcwd())

        file_name = input("[+] Enter bruteforce file name with directory: ")
        
        f = open(file_name, 'r')
        print(f.read())
        f.close()
        zip_cracker_code()
