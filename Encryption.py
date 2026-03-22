import time
import os
import platform

app_name = "EncryptionSoftware"

if platform.system() == "Windows":
    base = os.environ["APPDATA"]

elif platform.system() == "Darwin":  # macOS
    base = os.path.expanduser("~/Library/Application Support")

else:  # Linux and others
    base = os.path.expanduser("~/.local/share")

app_folder = os.path.join(base, app_name)
os.makedirs(app_folder, exist_ok=True)

file = os.path.join(app_folder, "Encryption.txt")

def hline():
    print("-~"*51,"-",sep='')
def intro():
    # print('Please choose between the following tasks:\n\t1. Read your pre-existing encrypted text. \n\t2. Enter the text to be encrypted(retain all previous text and add to the end)\n\t3. Enter the text to be encrypted(truncate all previous text and start from stratch)\n\t4. Delete previous encrypted text.')
    print('Please choose between the following tasks:\n\t1. Read your pre-existing encrypted text. \n\t2. Enter the text to be encrypted(retain all previous text and add to the end)\n\t3. Delete all the previous encrypted text.\n\t*  UM – USER MANNUAL')
    hline()
    print("To quit the Program write 'q' in place of 1-3\nTo view Usser Mannual write 'UM' in place of 1-3")
    task=(input('Please enter the desired number (1-3) denoting the taks to be performed\nAccording to the number used for the given task: '))
    if task=='1':
        read()
        intro()
        hline()
    elif task=='2':
        append()
        intro()
    elif task=='3':
        delete()
        print('Congratulations!!!\nThe Text previously stored in the File has been successfully deleted.')
        hline()
        intro()
        hline()
    elif task=='q':
        print("Program will terminate automatically in:")
        for i in range(5, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("Exiting now. Thank you for using the software! 👋")
        exit()
        # exit()
    elif task.lower()=='um':
        print("""
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
                    ENCRYPTION – DECRYPTION SOFTWARE
                              USER MANUAL
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

► PURPOSE
  This software allows you to securely store, read, add, and delete
  encrypted text in a local file.

► HOW TO OPERATE
  • Enter the number corresponding to the desired task and press Enter.
  • Follow all on-screen prompts carefully.

► AVAILABLE OPTIONS

  1 — READ YOUR PRE-EXISTING ENCRYPTED TEXT
      • Displays all previously stored information in readable form.
      • No changes are made to the stored data.

  2 — ENTER TEXT TO BE ENCRYPTED (APPEND MODE)
      • Allows you to add new text to existing stored content.
      • Previously saved data remains unchanged.
      • Enter text line-by-line.
      • Press Enter on a blank line to finish and save.

  3 — DELETE ALL PREVIOUS ENCRYPTED TEXT
      • Permanently removes ALL stored information.
      • This action cannot be undone.
      • Use with extreme caution.

► SPECIAL COMMANDS

  UM  — Display this User Manual
  q   — Quit the program safely

► DATA ENTRY GUIDELINES

  • You may enter text in single or multiple lines.
  • Blank line input signals completion of data entry.
  • Avoid closing the program during an operation.

► IMPORTANT NOTES

  • Deleted data cannot be recovered.
  • Ensure you select the correct option before proceeding.
  • Maintain separate backups of important information.
  • This program stores data locally on the system.

► EXITING THE PROGRAM

  • Enter 'q' when prompted for task selection.
  • The program will terminate safely.

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
""")
        intro()
    else:
        print('Sorry for the inconvinience caused, Try Again!\nPlease! Only Choose between the numbers 1,2,3,4')
        intro()
    '''elif task=='3':
        insert()
        intro()'''
def read():
    print("READING MODE ON...")
    hline()
    fp=open(file,'r')
    a=(fp.read())
    b=decrypt(a)
    print(b)
    fp.close()
def insert():
    fp=open(file,'w')
    hline()
    print("INSERTION MODE ON...")
    print("Insert the text either line-by-line by pressing Enter to store it line-by-line or it can also be stored\nin a single line. After inserting all your data Just press Enter again with the last input taken to be\nblank to finally insert & save your data.")
    print("Your Previous Data was deleted and new data is being added from scratch...")
    hline()
    l=[]
    ln=[]
    while True:
        a=input("Enter: ")
        if not a:
            break
        l.append(str(a+'\n'))
    for i in l:
        a=encrypt(i)
        ln.append(a)
    fp.writelines(ln)
    fp.close()
def append():
    fp=open(file,'a')
    hline()
    print("INSERTION MODE ON...")
    print("Insert the text either line-by-line by pressing Enter to store it line-by-line or it can also be stored\nin a single line. After inserting all your data Just press Enter again with the last input taken to be\nblank to finally insert & save your data.")
    print("Your Previous Data is as-it-is and new data is being added at the end...")
    hline()
    l=[]
    ln=[]
    while True:
        a=input("Enter: ")
        if not a:
            break
        l.append(str(a+'\n'))
    for i in l:
        a=encrypt(i)
        ln.append(a)
    fp.writelines(ln)
    fp.close()
def delete():
    fp=open(file,'w')
    fp.close()
def encrypt(text, key=89):
    encrypted = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            shifted = ord(char) + key
            if shifted > 126:
                shifted = 32 + (shifted - 127)
            elif shifted < 32:
                shifted = 127 - (32 - shifted)
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_text, key=89):
    return encrypt(encrypted_text, -key)



print("-~"*15,"Welcome to Encryption-Decryption Software","~-"*15)
print("About the Creator:\nSushant Kumar Kushwaha, an 18 yo senior secondary student at Sahu Academy, Coding Prodigy, an Enthusiast\nof interpreting, using & creating technology.\nCreation Date:\tJuly 22, 2025")
hline()

intro()