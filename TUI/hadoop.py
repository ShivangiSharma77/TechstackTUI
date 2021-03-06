def core():
    nn_ip = input('Enter NameNode ip and hadoop port no. ex: hdfs://1.2.3.4:9000:') 
    print(nn_ip)
    os.system ('echo \<configuration\> >> core-site.xml')
    os.system('echo \<property\> >> core-site.xml') 
    os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml") 
    os.system("echo \<value\>{}\<\/value\> >> core-site.xml".format(nn_ip)) 
    os.system('echo <\/property\> >> core-site.xml')
    os.system("echo \<\/configuration\> >> core-site.xml")
    os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
    os.system ("rm -rf core-site.xml") 
    os.system("cp cp.xml core-site.xml") 

def hdfs():
    dndir = input('Enter directory to create datanode: ')
    print(dndir)
    os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))
    os.system("ssh {} mkdir {}".format (ip, dndir)) 
    os.system("rm -rf hdfs-site.xml")
    os.system ("cp hd.xml hdfs-site.xml")

def data():
    dir = input('Enter directory of java and hadoop file: ')
    print(dir)
    os.system('ssh {} rpm -i {}/jdk-8u171-linux-x64.rpm'.format(ip,dir)) 
    os.system("ssh {} rpm -i {}\/hadoop-1.2.1-1.x86_64.rpm --force". format (ip,dir))
    core()
    hdfs()
    os.system("ssh {} hadoop-daemon.sh start datanode".format (ip))
    os.system("ssh {} jps".format(ip))