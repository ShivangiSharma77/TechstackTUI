import os
def linux():
     os.system("clear")
     while True:    # while Loop is start For TUI-Linux Basic Operation
      os.system("tput setaf 1")
      os.system(' echo "\t\t\t Welcome To Linux Basic Operatiion \t\t\t [`date +%T `] " ')
      os.system("tput setaf 4")
      print("""                  
      \t1.Show The Date
      \t2.Show Calendar
      \t3.Create a File
      \t4.Check The File 
      \t5.Remove The File
      \t6.Read The File
      \t7.Check The Ip and Network Configuration 
      \t10.Exit From TUI-Linux
      \t11.Go To TUI-Local Page

      """)
      LinuxChoise=input("Plz Enter You Coise:")
      if int(LinuxChoise)== 1:
        os.system('tput setaf 15')
        os.system('date')  # Showing Date / date command
        os.system("tput setaf 4")
      elif int(LinuxChoise) == 2:
        os.system('tput setaf 15')
        os.system('cal')               #showing Calender
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 3:
        FileName=input("Plz Enter The File Name With Location Like (/Desktop/project/sumit.txt):")  # Creating File
        os.system('tput setaf 15')
        os.system('touch ~{0}'.format(FileName))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 4:
        FileName1=input("Plz Enter The Location Where You Want Check File :")    # Checking The File
        os.system('tput setaf 15')
        os.system('ls ~{0}'.format(FileName1))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 5:
        FileName2=input("Plz Entre The Location Of File For Delet. Like (/Desktop/project/sumit.txt)")   # Removing The File
        os.system('tput setaf 15')
        os.system('rm ~{0}'.format(FileName2))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 6:
        FileName3=input("Plz Entre The Location Of File For Read. Like (/Desktop/project/sumit.txt)")    # Reding The File 
        os.system('tput setaf 15')
        os.system('cat ~{0}'.format(FileName3))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 7:
        os.system('tput setaf 15')
        os.system('ifconfig')
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 10:      #Exiting From TUI
        os.system('tput setaf 15')
        break
      elif int(LinuxChoise) == 11:      #Exiting From TUI-Linux Basic Operation 
        os.system('tput setaf 4')
        exit()
      LinuxInput=input("\t\tDo You Want Continue? (y/n)")
      if LinuxInput == 'n':
         break 
      os.system("clear")
      
