from getpass import getuser
import pyfiglet
import os

def main():
    print(pyfiglet.figlet_format("PC-CLEANER"))

    print(f"====================\n[+] Checking C:\\Users\\{getuser()}\\AppData\\Local\\Temp\n====================")
    for ele in os.listdir(f"C:\\Users\\{getuser()}\\AppData\\Local\\Temp"):
        print(f"removing : {ele}")
        try:
            if os.path.isfile(ele):
                os.remove(ele)
            else :
                os.removedirs(ele)
        except:
            print(f"[!] No right to remove {ele}, retry in admin privileges")

    print(f"====================\n[+] Checking C:\Windows\Temp\n====================")
    for ele in os.listdir(f"C:\Windows\Temp"):
        print(f"removing : {ele}")
        try:
            if os.path.isfile(ele):
                os.remove(ele)
            else :
                os.removedirs(ele)
        except:
            print(f"[!] No right to remove {ele}, retry in admin privileges")


    print(f"====================\n[+] Listing files wheighting over 1gb :\n====================")

    walk("C:\\")
     print(f"====================\n[!] To make your PC run faster, try to check the app running in background parameters.\n====================")
            

def walk(uri):
    for root,directories,files in os.walk(uri):
        for file in files:
            if os.path.isfile(root+file):
                    w = round(float(os.path.getsize(root+file)/10**9),2)
                    if w > 1:
                        print(f"{root+file}\n {file} wheight {w}gb")
        
        for directory in directories:
            walk(str(root+"\\"+directory))

if __name__=="__main__":
    main()