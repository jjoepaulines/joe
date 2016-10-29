import os
from S3FMA import *
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from Mesh_details import *
import csv

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
default_path = '/home/joe/PycharmProjects/aws_log_analysis-Dev/Mesh_log/'

# Colleced information list

path_for_info='/home/joe/Log_analyser/'

#computing between dates

date_month = '2016-10-'
date_day_from = '23'
date_day_to = '29'

date_final = []
#date from till to


for i in range(int(date_day_from),int(date_day_to)):
    date_final.append(date_month+str(i))

#dictionary for maintain the instance of the class

Dict_master_instance={}

#read and replace the mac address - remove the column
#then conver that to decimal for query and add to the list

with open(Fname) as f:
    content = f.readlines()
    for mac in content:
        dec_mac=int(mac.replace(':',''),16)
        # subract by four
        final_mac=dec_mac -sub_value
        mac_list.append(final_mac)
        #creating instance to the class
        Dict_master_instance[str(final_mac)] = Mesh_details_C(str(final_mac))
        #create the instance of the mesh details here and add to dictionary

        print mac + ' -------------------- ' +str(final_mac)

# print mac_list -- display the mac - decimal

print Dict_master_instance

# using S3FMA

s3FileManager = S3FileManager(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, use_ssl = True)

# S3 Bucket
fileNames = s3FileManager.getFileNamesInBucket('meshLogs')

#isolate master,slave1 and slave 2 -- create a directory

class Isolate_Almonds:

    def __init__(self):
        pass

    def create_folder(self):
        #sub folder name
        # type of file names are "5G_client_rssi",2_4_client_rssi,"Sitesurvey",Speedtest,
        f_name = ['5G_client_rssi','2_4_client_rssi','Sitesurvey','Speedtest','Dev_info']
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

    #define the path & based on the filter files are getting dispatched
    def combine_file(self):
        for subdir, dirs, files in os.walk(default_path):
            for filename in files:
                # print filename
              for dates in date_final:
                if filename.find(dates) != -1:
                    # print subdir
                    # print 'cd ' + subdir + ";""cat "+filename+"  >> final.log"
                    path = subdir + '/' + filename
                    os.rename(path, path.replace(" ", "-"))
                    #print path
                    # print "cat "+path+"  >> "+subdir+"/final.log"
                    #Here new files has been formed by using the date as a filter
                    os.system("cat " + path + "  >> " + subdir + "/final.log")


# To know the unique folders that we have to create

mac_set_folders=set()

# set to isolate the mac address of the clients

mac_for_isolate=set()

#iteration for the mac's and storing the keys in the list

for macs in mac_list:
#storing the need key to the list
  for i in fileNames:
      #print i
      str_type=str(i)
      if str_type.find(str(macs)) != -1:
          #identifing the particular macs
          mac_set_folders.add(str_type[0:32])
          mac_for_isolate.add(str_type[0:15])
          needed_key_download.append(str_type)

#print mac_set_folders
#create a folders
folders = Isolate_Almonds()
folders.create_folder()

# Download the files to the concern directory
for keys in needed_key_download:
# check the file exist or not
   # adding the mac to
    #print keys
    for dates in date_final:

        if str(keys).find(str(dates)) != -1:
            #print "................"+str(dates)+"...................."
            #check the file before downloading
            key_dash=default_path+keys
            #print keys
            #Adding slave details to mesh detail class
            Dict_master_instance[keys[0:15]].slave_details.add(str(keys[16:31]))
            new_f=key_dash.replace(" ", "-")
            #print "neeeeeeeeeeeee"+str(new_f)
            #put a condition to fill the URL in the set
            if new_f.find('2_4_client_rssi') != -1:
                Dict_master_instance[keys[0:15]].RSSI_URL.add(new_f)
            elif new_f.find('5G_client_rssi') != -1:
                Dict_master_instance[keys[0:15]].RSSI_URL.add(new_f)
            elif new_f.find('Sitesurvey') != -1:
                Dict_master_instance[keys[0:15]].site_survey_URL.add(new_f)
            elif new_f.find('Speedtest') != -1:
                Dict_master_instance[keys[0:15]].speedtest_URL.add(new_f)
            #rename all with dash
            folders.rename_with_dash()
            if os.path.exists(new_f) == True:
             #don't download if file exist
             #print keys + 'file Exist ... No need to download'
              pass
            else:
                #download the files
                s3FileManager.downloadFileFromBucket('meshLogs',keys,default_path)

#combine the files
folders.rename_with_dash()
folders.combine_file()

Dict_master_instance['251176220101896'].write_all_content()
Dict_master_instance['251176220101896'].dispatch_all_the_URL()
Dict_master_instance['251176220101896'].identify_the_client()
Dict_master_instance['251176220101896'].writing_client_details_per_almond()







