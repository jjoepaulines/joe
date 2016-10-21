import re
import math,os
from os.path import join


rootdir = '/home/joe/PycharmProjects/aws_log_analysis/Mesh_log/'
date_month = '2016-10-'
date_day_from = '20'
date_day_to = '23'

date_final = []
#date from till to


for i in range(20,23):
    date_final.append(date_month+str(i))

print date_final

h='/home/joe/PycharmProjects/aws_log_analysis/Mesh_log/251176220099152/251176220099152/2_4_client_rssi/2016-10-15 00:24:51'



#print str(h).find(date)

#if str(h).find(date) == -1:
   # pass





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




