import os
import getpass
import subprocess

# we are accessing the function from other file 
from aws_menu import *
from hadoop import *
from docker import *
from Linux_Basic import *
from Installation import installation
from Partition import *
i=0
while i<=3: 
    i=i+1
    os.system("clear") 
    os.system("tput setaf 1")
    os.system('printf "%50s\n" "WELCOME TO TUI WORLD"')
    os.system("tput setaf 4")
    Pass=getpass.getpass("Plz Enter Password :")
    if Pass != "sumit@301":
     print("\t\tPassword Is Wrong You Have 3 Attempt.You Use {} Attempt:".format(i))
     input("Press Enter Key To Continue")
     os.system("clear")
     if i == 3:
      os.system("tput setaf 1")
      print("\t\t\tSorry,You Have Only Three Attempt")
      print("\t\t\t\t Try Again Plz")
      os.system("tput setaf 4")
      exit()
    elif Pass == "sumit@301":
     break
Location=input("Plz Enter Where You Want To TUI (local/remote):") # Providing The Option To Uer Where He want to Login
os.system("clear")
if Location == 'local':	# Local-Uer If loop Start
 while True:            # while loop is running for the Local Menu
    # Menu Provide By TUI For A User For Local
    os.system("tput setaf 1")
    os.system(' echo "\t\t\t Welcome To TUI-Locally \t\t\t [`date +%T `] " ')
    os.system("tput setaf 4")
    print("""
    \t1.Linux Basic Operation Like(Create File, Remove File, Show Date)

    \t2.Partion Operation

    \t3.Installtion Of Software
   
    \t4.Docker Operation
   
    \t5. Creating LVM

    \t6. AWS Operation

    \t7.Hadoop Operation

    \t8.Exit From The TUI

    """)
    os.system("tput setaf 4")  # Changing The Color of Hedline To Red   
    print("\t\t\tPlz Enter Your Choise:",end='')
    ch=input()

    if int(ch) == 1: # Taking Input From user for choise
     
      linux()  # calling the linux function from the linux_basic.py file
      
     
    elif int(ch)==2:

       partition() # calling the partition function from the  Partition.py file

    elif int(ch)==3:

       installation()

    elif int(ch) == 4:
       while True:   # While Loop are starting fo Docker Operation
         #Menu for the Docker Operation
         os.system("clear")
         os.system("tput setaf 1")
         os.system('echo "\t\t\t Welcome To Docker Operation \t\t\t [`date +%T `]" ')   #Heading Of Docker Menu
         os.system("tput setaf 4")
         print("""
         1.Start The Docker Services/Compulsory
	 2.check The No Container are Lanuch
         3.Lanuch New The Docker Container
         4.Downloads The Docker Images
         5.Go Menu Page
         6.Exit From TUI
         7.Docker Sub command
         """)
         os.system("tput setaf 14")
         os.system("echo '\t Note:If You Not Start The Docker Services First Run It Then Use The Other option:'")
         os.system("tput setaf 4")
         print("\t\t\tPlz Enter The Choise :",end='')
         os.system("tput setaf 4")
         DockerCh=input()
         os.system("tput setaf 4")
         if int(DockerCh)==1:
            os.system("tput setaf 15")
            os.system("systemctl start docker")  # Starting the Docker Services
            os.system("tput setaf 4")
         elif int(DockerCh)==2:
            os.system("tput setaf 15")
            os.system(" docker ps -a ")     # Checking the Runnig , ShutDown Container(OS)
            os.system("tput setaf 4")
            input("Plz Enter To Continue")
         elif int(DockerCh)==3:
            ContainerName=input("Plz Enter the container Name:")
            os.system("docker container run -it --name {} centos:latest".format(ContainerName))  # Lanuching New Container 
            os.system("tput setaf 4")
         elif int(DockerCh)==5:
            os.system("tput setaf 15")
            break
         elif int(DockerCh)==6:
            os.system("tput setaf 15")
            exit()
         elif int(DockerCh)==7:
            docker()
         else:
           print("Plz Enter The Write Choise:")
         Forward=input("\t\t\tDo You Want Continue the Docker Operation ? (y/n) ")  # Taking Input for Continue or for Stop Program
         if Forward== 'n' or Forward== 'N' :
            break
         # While Loop are Ending Of Docker operation

    elif int(ch)==7:
      os.system("tput setaf 15")
      exit()
    
    elif int(ch)==8:
      print("------------------------- DISPLAYING ALL HARDDISK ATTACHED -------------------------")
      print(subprocess.getoutput("fdisk -l"))

      hd1 = input("Enter the first harddisk name : ")

      print("Creating Physical Volume ...")
      print(subprocess.getoutput("sudo pvcreate {}".format(hd1)))
      print("-----PV created-----")
      display = input("Do you want to display created Physical Volume(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("sudo pvdisplay {}".format(hd1)))
      print("----------------------------------")

      hd2 = input("Enter the second harddisk name : ")

      print("Creating Physical Volume ...")
      print(subprocess.getoutput("sudo pvcreate {}".format(hd2)))
      print("-----PV created--------")
      display = input("Do you want to display created Physical Volume(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("sudo pvdisplay {}".format(hd2)))
      print("----------------------------------")

      print("Creating VG ...")
      vg = input("Please enter your VG name : ")
      print(subprocess.getoutput("vgcreate {} {} {}".format(vg, hd1, hd2)))

      display = input("Do you want to display created VG(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("vgdisplay {}".format(vg)))
      print("----------------------------------")

      print("Creating Logical Volume from created VG ...")
      size = input("Please enter size of Logical Volume(LV): ")
      name = input("Please enter name of LV: ")
      print(subprocess.getoutput("lvcreate --size {}G --name {} {}".format(size,name,vg)))
      print("Logical Volume Created ...")
      display = input("Do you want to display created LV(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("lvdisplay {}/{}".format(vg,name)))
      print("-----------EXITING-----------")
      exit()

    elif int(ch)==9:
      os.system("clear")
      ch=0
      s="yes"
      print("------------------Welcome to AWS!!---------------\n")
      s= input("Do you wish to configure AWS?\n")
      if s.lower()=="yes":
         os.system("aws configure")
         print("AWS is configured")
      while ch!=5:
         print("-----------------AWS MENU---------------")
         ch=0
         print("""
             1.AWS ec2
             2.AWS CloudFront
             3.AWS S3
             4.AWS ebs
             5.Exit\n""")
         ch=int(input("Enter the service\n"))

         if ch==1:
           ec2()
         elif ch==2:
           cloudfront()
         elif ch==3:
           s3()
         elif ch==4:
           ebs()
         else:
           ch=5
    elif int(ch)==10:
      os.system("clear")
      print("\t\t\t------------------Welcome to hadoop!!---------------\n")
      while ch!=5:
         print("\t\t\t\t-----------------Hadoop MENU---------------")
         ch=0
         print("""
             1.create datanode
             2.
             3.
             4.Exit\n""")
         ch=int(input("Enter the service\n"))

         if ch==1:
           core()
         elif ch==2:
           hdfs()
         elif ch==3:
           data()
         else:
           ch=4

    else:
      print("Plz Choise Write Option")
      os.system("tput setaf 15")

    x=input("\t\t\tDo You Want Continue TUI-Locally ? (y/n) ")  # Taking Input For Continue Or For Stop Program
    if x== 'n' or x== 'N' :
      os.system("tput setaf 15")
      exit()
    os.system("clear")                  # Clearing The Screen For Holding The Menu at Fix Position

# Remote-user Loop is Starting
elif Location == 'remote':
 os.system("tput setaf 1")
 os.system('echo "\t\t\t Welcome To TUI-Remotly \t\t\t [`date +%T`] "')  #Heading Of Remote-Control menu
 os.system("tput setaf 4")
 RemoteUserName=input("Plz Enter User Name(root/sumit)")
 UserIp=input("Plz Enter The User Ip Befor Go To Menu :")
 os.system("clear")
 while True:   # While Loop Are Start For Remote TUI
      # Menu Provide By TUI For A User For Remote
      os.system("tput setaf 1")
      print("\t\t\t Welcome To TUI-Remotly")
      os.system("tput setaf 4")
      print("""
      \t1.Ping To User
      \t2.Today Date
      \t3.Show Calendar
      \t4.Create A User
      \t5.Give Me The User Terminal Access 
      \t6.Upload The File
      \t7.Download The File
      \t8.Exit From TUI
      """)
      RemoteChoise=input("Plz Enter The Choise :")
      if int(RemoteChoise) == 1:       # Ping To Remote Host Machine 
          os.system("ping {}".format(UserIp))
      elif int(RemoteChoise) == 2:     # Running The Date Command On Remote-Host Machine 
          os.system("ssh {0}@{1} date".format(RemoteUserName,UserIp))
      elif int(RemoteChoise) == 3:
          os.system("ssh {0}@{1} cal".format(RemoteUserName,UserIp))
      elif int(RemoteChoise) == 4:      # Creating The User On Remote Host Machine
          UserAdd=input("Plz Enter The User Name: ")
          os.system("ssh {0}@{1} useradd {2} ".format(RemoteUserName,UserIp , UserAdd))
      elif int(RemoteChoise) == 5:      # Connecting To Remote Host Machine
          os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))
      elif int(RemoteChoise) == 6:      # Uploading The File 
          os.system("tput setaf 14")
          print("\tNote: If You Don`t Know File Name Then Plz Ref Option-5 And Check File Name")
          os.system("tput setaf 4")
          Option5=input("\tDo you Want to Go To The Option-5 ? (y/n)")
          if Option5 == 'y': 
            os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))      # Connecting To Remote Host Machine
          os.system("tput setaf 4")
          RemoteHostFile=input("Ok Then Plz Enter The File Name:")          
          os.system("scp /root/Desktop/project/{2} {0}@{1}:/home/sumit/Desktop/".format(RemoteUserName,UserIp,RemoteHostFile))
      elif int(RemoteChoise) == 7:     #Downloading The File 
          os.system("tput setaf 4")
          print("\tNote: If You Don`t Know The File Name Plz Ref Option-5 And Check File Name")
          Option6=input("\tDo You Want To GO To The Option-5 ? (y/n)")
          if Option6 == 'y':
             os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))
          os.system("tput setaf 4")
          DownloadHostFile=input("Plz Enter The File Name :")
          os.system("scp {0}@{1}:/home/sumit/Desktop/{2} /root/Desktop/".format(RemoteUserName,UserIp,DownloadHostFile))
      elif int(RemoteChoise) == 8:    # Exit From TUT
          os.system("tput setaf 15")
          exit()
      p=input("Do You Want To Continue TUI-Remotelly ? (y/n)")
      if p == 'n' or p=='N':
         exit() 
      os.system("clear")
      os.system("tput setaf 15")
      # While Loop Is Ending Here 
 
