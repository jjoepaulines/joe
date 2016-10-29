import re
import math,os
from os.path import join

from csvkit import py2

h='/home/joe/PycharmProjects/aws_log_analysis-Dev/Mesh_log/251176220099424/251176220099424/5G_client_rssi/2016-10-21-08:52:24'

import csv

'''

with open(h, 'rb') as csvfile:
    hf=py2.CSVKitDictReader(csvfile)
    num_lines = sum(1 for line in open(h))
    # create a new CSV file for rssi
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['BSSID','Client_MAC', 'Rssi0', 'Rssi1', 'Connection_Time', 'EpocTime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1,num_lines):
            #print hf.next()['Client_MAC']
            try:
                writer.writerow({'Client_MAC': hf.next()['Client_MAC'], 'Rssi0': hf.next()['Rssi0'], 'Rssi1': hf.next()['Rssi1'], 'Connection_Time': hf.next()['Connection_Time'],'EpocTime': hf.next()['EpocTime']})
            except:
                pass

'''

hhd='/home/joe/PycharmProjects/aws_log_analysis-Dev/Mesh_log/251176220099704/251176220099704/2_4_client_rssi/2016-10-16-09:00:40'

path_h='/home/joe/PycharmProjects/aws_log_analysis-Dev/Details_info-final/'

command = 'grep -i ' + str('A4:31:35:0A:40:CE') + ' ' + hhd + ' >> ' +path_h+'0xe471856002d4/'+str('A4:31:35:0A:40:CE')+'_RSSI'
os.system(command)

print command



print hhd[56:71]
print hhd[72:87]
#print str(h).find(date)

#if str(h).find(date) == -1:
   # pass
import time

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1477259461))


hh=str(251176216953072)
print hex(int(hh))

new_f='/home/joe/PycharmProjects/aws_log_analysis-Dev/Mesh_log/251176220099704/251176220099704/2_4_client_rssi/2016-10-26-15:30:40'
if new_f.find('2_4_client_rsi')!= -1:
    print 'there'
else:
    print 'not there'


'''
def combine_f():
  for subdir, dirs, files in os.walk(rootdir):
    for filename in files:
        #print filename
        if filename.find(date) != -1:
            #print subdir
            #print 'cd ' + subdir + ";""cat "+filename+"  >> final.log"
            path= subdir+'/'+filename
            os.rename(path, path.replace(" ", "-"))
            print path
            #print "cat "+path+"  >> "+subdir+"/final.log"
            os.system("cat "+path+"  >> "+subdir+"/final.log")
            #os.system('ls')
            #thefile = os.path.join(subdir, filename)
            #os.system("cat * >> final.log")
'''




