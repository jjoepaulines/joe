import os
from S3FMA import *
from boto.s3.connection import S3Connection
from boto.s3.key import Key
# Mac Address List - file name

Fname = 'mac_address.txt'

#They are using ra0 -- so decreade the last byte by four

#list which has a mac address to be quired - subract by 4
mac_list=[]
sub_value=int('4',16)

#List contains need keys

needed_key_download = []

#AWS credential's

AWS_ACCESS_KEY_ID = 'AKIAJH7PLPL7A6XIOAMQ'
AWS_SECRET_ACCESS_KEY = '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'

#Default Path & the date of log file we are looking for
default_path = '/home/joe/PycharmProjects/aws_log_analysis/Mesh_log/'
date = '2016-10-1'

#read and replace the mac address - remove the column
#then conver that to decimal for query and add to the list

with open(Fname) as f:
    content = f.readlines()
    for mac in content:
        dec_mac=int(mac.replace(':',''),16)
        # subract by four
        final_mac=dec_mac -sub_value
        mac_list.append(final_mac)
        print mac_list

# using S3FMA

s3FileManager = S3FileManager(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, use_ssl = True)

# S3 Bucket
fileNames = s3FileManager.getFileNamesInBucket('meshLogs')

#Access the s3 bucket

conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,calling_format=OrdinaryCallingFormat())
mybucket = conn.get_bucket('meshLogs')

#isolate master,slave1 and slave 2 -- create a directory

class Isolate_Almonds:

    def __init__(self):
        pass

    def create_folder(self):
        #sub folder name
        # type of file names are "5G_client_rssi",2_4_client_rssi,"Sitesurvey",Speedtest,
        f_name = ['5G_client_rssi','2_4_client_rssi','Sitesurvey','Speedtest']
        for org_n in mac_set_folders:
            for add_n in f_name:
                concodinate = 'Mesh_log/'+str(org_n)+str(add_n)
                try:
                    os.makedirs(concodinate)
                except OSError:
                    pass

    def rename_with_dash(self):
        for subdir, dirs, files in os.walk(default_path):
            for filename in files:
                paths = subdir + '/' + filename
                #print paths
                #remove the final.log before combining the files togeather
                try:
                    os.rename(paths, paths.replace(" ", "-"))
                    os.remove(subdir + "/final.log")
                except:
                    pass

    #define the path
    def combine_file(self):
        for subdir, dirs, files in os.walk(default_path):
            for filename in files:
                # print filename
                if filename.find(date) != -1:
                    # print subdir
                    # print 'cd ' + subdir + ";""cat "+filename+"  >> final.log"
                    path = subdir + '/' + filename
                    os.rename(path, path.replace(" ", "-"))
                    #print path
                    # print "cat "+path+"  >> "+subdir+"/final.log"
                    os.system("cat " + path + "  >> " + subdir + "/final.log")


# To know the unique folders that we have to create

mac_set_folders=set()


#iteration for the mac's

for macs in mac_list:
#storing the need key to the list
  for i in fileNames:
      #print i
      str_type=str(i)
      if str_type.find(str(macs)) != -1:
          #identifing the particular macs
          mac_set_folders.add(str_type[0:32])
          needed_key_download.append(str_type)

print mac_set_folders
#create a folders
folders = Isolate_Almonds()
folders.create_folder()

# Download the files to the concern directory
for keys in needed_key_download:
# check the file exist or not
      #print default_path+keys
      if str(keys).find(date) != -1:
        #check the file before downloading
        key_dash=default_path+keys
        new_f=key_dash.replace(" ", "-")
        #rename all with dash
        folders.rename_with_dash()
        if os.path.exists(new_f) == True:
         #don't download if file exist
          print keys + 'file Exist ... No need to download'
          pass
        else:
            #download the files
            s3FileManager.downloadFileFromBucket('meshLogs',keys,default_path)

#combine the files
folders.rename_with_dash()
folders.combine_file()





