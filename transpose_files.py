import csv 
import os 
import crawler as craw
import codecs 
import time  
import numpy as np 


# Transpose the rows in the files and save them as transposed 


##########################################################
'''After Alignment transpose to a Matrix ''' 
###########################################################



path = "/home/assen/Development/stemmatology/Python_Script/files/Guide_Tree_Alignment"
save_path = "/home/assen/Development/stemmatology/Python_Script/files/Guide_Tree_Alignment/transposed"

#for looop 
#1. open every file and save it into a list 
#2. transpose every list  
#3. save every list into a different file  


list_files = [] 

for item in os.listdir(path):

	if os.path.isfile(os.path.join(path, item)):


		list_files.append(item)

print(len(list_files))


list_files = sorted(list_files)


#for i in range(len(list_files)): 

#	list_files[i] = []


'''Working code -> Loop Needed'''

#file_name = os.path.join(path + "/" + list_files[-1])  
#print(file_name)
#a = zip(*csv.reader(open(file_name, "r")))
#csv.writer(open("transposed.csv", "w")).writerows(a)



for filename in list_files:
            
	f = os.path.join(path, filename)

	file_name = os.path.join(path + "/" + filename)
            
	attrs = [] 

	a = zip(*csv.reader(open(file_name, "r")))
	file_save = os.path.join(save_path + "/" + filename)
	csv.writer(open(file_save, "w")).writerows(a)
