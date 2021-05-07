import os
def partition():
  while True:
       os.system('clear')
       os.system("tput setaf 1")
       os.system('echo "\t\t\t Welcome To Partition Operatiion\t\t [`date +%T`]" ')  #Heading Of Partition Menu
       os.system("tput setaf 4")
       print("""
        1.Check The Partion
        2.Create A Partition
        3.Exit From TUI
        4.Go TUI-Menu Page   
       """)
       partitionCh=input("\t\tPlz Enter Your Choise :")
       if int(partitionCh) == 1:
          os.system("tput setaf 15")
          os.system('fdisk -l')
          os.system("tput setaf 4")
       elif int(partitionCh) == 2:
          help1=input("Get Information About Partition Plz Enter- h : ")
          if help1 =='h':
           os.system("tput setaf 15")
           print("""
		Help:
		  DOS (MBR)
		   a   toggle a bootable flag
		   b   edit nested BSD disklabel
		   c   toggle the dos compatibility flag

		  Generic
		   d   delete a partition
		   F   list free unpartitioned space
		   l   list known partition types
		   n   add a new partition
		   p   print the partition table
		   t   change a partition type
		   v   verify the partition table
		   i   print information about a partition

		  Misc
		   m   print this menu
		   u   change display/entry units
		   x   extra functionality (experts only)

		  Script
		   I   load disk layout from sfdisk script file
		   O   dump disk layout to sfdisk script file

		  Save & Exit
		   w   write table to disk and exit
		   q   quit without saving changes

		  Create a new label
		   g   create a new empty GPT partition table
		   G   create a nefrom test import *w empty SGI (IRIX) partition table
		   o   create a new empty DOS partition table
		   s   create a new empty Sun partition table
		""")
           os.system("tput setaf 4")
           Disk=input("Plz Enter The Disk Name For Going To inside Like (/dev/sda) :")
           os.system('fdisk {}'.format(Disk))
           os.system("tput setaf 4")
       elif int(partitionCh) == 3:
           os.system('tput setaf 15')
           exit()
       elif int(partitionCh) == 4:
           break 
       LinuxInput1=input("\t\tDo You Want Continue? (y/n)")
       if LinuxInput1 == 'n':
           break
       os.system('clear')
