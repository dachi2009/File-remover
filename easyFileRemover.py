import os
import subprocess
print('REMOVING FILES EASILY FROM NOT RECOMMENDED TO MOST RECOMMENDED')
print("\n")
print('NOTE: REMEMBER TO WHEN YOU ARE USING SUDO FOR FILES IN THE ROOT BE VERY CAREFUL ALWAYS DOUBLE-CHECK YOUR PATH AND BE SURE TO NOT DELETE IMPORTANT FILES')
print("\n")
print('NOTE: ACCIDENTAL DELETED FILES ARE NOT RECOVERABLE IF USING SHRED OR NULLIFYING IT AND CREATOR TAKES NO RESPONSIBILITY FOR THAT')
print('\n')
print('NOTE: IT IS USER CHOICE WHETHER DELETE THEM OR NOT')
print('\n')
print('NOTE: WHEN TRYING TO REMOVE FILES FROM ROOT DIRECTORY OR OWNED BY OTHER USER REMEMBER TO USE SUDO TO ESCAPE PERMISSION DENIED ERROR')
print('\n')
is_secure = False
print('secure delete is about at first shredding file')
print('NOTE:shredding means overwriting file with same size of random data and then deleting to make recovering impossible')
is_secure_user_input = input("enter y/n: ")
if is_secure_user_input == "y".lower():
    is_secure = True
else:
    is_secure = False

def Removing_file(file_path, secure=False):
    if not os.path.exists(file_path):
        print("Cant find path {}".format(file_path))
        return 0
    dangerous_files = ["/", "/home", "/root", "/dev", "/bin", "/boot",
                        "/etc", "/var", "/tmp", "/sysroot", "/sys", "/sbin",
                        "/srv", "/run", "/lib", "/media", "/lib64", "/ostree", "/mnt",
                        "/usr", "/proc", "/opt"]
    for i in dangerous_files:
        if file_path == i or file_path.startswith(i + "/"):
            print("[!] DANGER: ARE YOU SURE YOU WANT TO DELETE FILES FROM THIS PATH? {}".format(file_path), "ITS VERY DANGEROUS AND MAY BREAK IT")
            while True:
                user_input_danger = input("enter here (y/n): ").strip()
                if user_input_danger.lower() == "y":
                    print("[!] DANGEROUS BUT IT'S USER'S DECISION...")
                    if secure:
                        print("[*] Securing... {}".format(file_path))
                        print('[*] Using shred...')
                        print('[+] Shredding is recommended if you want to make data unrecoverable')
                        subprocess.run(["shred", file_path])
                        print('choose which one to use')
                        print('must be either \n1) rm \neither\n2) /dev/null method\nadditional\n3) Exit')
                        while True:
                            user_input = input("enter your choice (1 or 2) you can type 3) or exit to exit code: ").strip()
                            if user_input == "1":
                                print("[-] Not recommended much because it can leave some space on your drive")
                                subprocess.run(["rm", "-rf", file_path])
                            elif user_input == "2":
                                print("this is file {} before nullifying".format(file_path))
                                subprocess.run(["ls", "-lA", "-h", file_path])
                                with open(file=file_path, mode='w') as a:
                                    pass
                                print("file {}".format(file_path), "is nullified")
                                print('checking size...')
                                subprocess.run(["ls", "-lA", "-h", file_path])
                                if os.path.getsize(file_path) == 0:
                                    print("[+] {} successfully have been nullified".format(file_path))
                                else:
                                    print("[-] {} Couldnt be nullified perhaps use sudo?".format(file_path))
                            elif user_input == "3" or user_input == "exit".lower():
                                return "exitig"
                            else:
                                if not user_input.isdigit():
                                    print("[?] bro come on it should be integer 1 or 2 not {}".format(file_path), "and also string")
                                else:
                                    print("[?] bro seriously? chose {}".format(file_path), "it literally should be 1 or 2 dawg😭😭 ")
                    else:
                        print('Not recommended as data is recoverable since after executing this OS will treat your file as overwritable data')
                        while True:
                            user_input_2 = input("enter mthod (1 or 2) you can type 3) or exit to exit code: ").strip()
                            if user_input_2 == "1":
                                subprocess.run(["rm", "-rf", file_path])
                                '''checking if file was successfully deleted...'''
                                if not os.path.exists(file_path):
                                    print("[+] file {}".format(file_path), "has been successfully deleted :)")
                                else:
                                    print("[!] uh oh file hasn't been deleted probably permission error, maybe use sudo?")
                                    break
                            elif user_input_2 == "2":
                                print('recommended after not securing if you want to permenentaly delete file and make it unrecoverable')
                                print("this is file {} before nullifying".format(file_path))
                                subprocess.run(["ls", "-lA", "-h", file_path])
                                with open(file=file_path, mode='w') as a:
                                    pass
                                print("[+] file {}".format(file_path), "is nullified")
                                print("checking file..")
                                print("and this is after nullifying")
                                subprocess.run(["ls", '-lA', '-h', file_path])
                                if os.path.getsize(file_path) == 0:
                                    print("[+] file {}".format(file_path), "has been successfully nullified")
                                else:
                                    print("[-] uh oh {}".format(file_path), "hasnt been nullified perhaps use sudo?")
                elif user_input_danger == 'n'.lower():
                    print("[!] exiting... enter new path")
                    break
                else:
                    print("[?] seriously? should be y/n not {}".format(user_input_danger))
Removing_file(file_path=input("enter file path e.g. /path/to/your/file: "), secure=is_secure)