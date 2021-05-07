import os
def dockerSoftware():
    os.system("tput setaf 15")
    os.system("yum install dokcer-ce --nobest")
    os.system("tput setaf 15")

def httpdSoftware():
    os.system("tput setaf 15")
    os.system("yum install httpd -y") #Installing the Web server
    os.system("tput setaf 4")

def installation():
  while True:
    os.system("clear")
    print("Welcome to Installation Menu")
    print("""
           1. Docker
           2. httpd server
           3. Go To the menu
           4. Exit from the TUI
        """) # creating the user
    ch=int(input("Enter your choise"))
    if ch==1:
      dockerSoftware()
    elif ch==2:
      httpdSoftware()
    elif ch==3:
        break
    elif ch==4:
        exit()
    LinuxInput1=input("\t\tDo You Want Continue? (y/n)")
    if LinuxInput1 == 'n':
      break
    os.system('clear')