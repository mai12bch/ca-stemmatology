import string
import os
import urllib
import csv
import time
import re
from collections import Counter
import codecs 

#i = 0


words = [] 
files_crawled = [] 


for path, subdirs, files in os.walk("/home/assen/Development/stemmatology/DataSet1-Heinrichi/DataSet/heinrichi"):

    i = 1 

  
    files = sorted(files)

    for filename in files:
    
        f = os.path.join(path, filename)

   #print(path + "\t" + filename)

    file_name = os.path.join(path + "/" + filename)

    print(filename)
    with codecs.open(file_name, "r", encoding='ISO-8859-1') as csv_file: 

        for line in csv_file:

            #print(re.split('(\ |\\""|\_|\,|\;|\?|\!|\W+|\\n)+', line))

            list_new = [] 
            #list_new.append(re.split('(\ |\\""|\_|\,|\;|\?|\!|\W+|\\n)+', line))
            list_new.append(re.split('(\ |\\n)+', line))
            
            for j in range(len(list_new)):

                for k in range(len(list_new[j])):

                    #if list_new[j][k] != ' ':

                        #print(list_new[j][k])
                        #time.sleep(0.1)

                        #if list_new[j][k] not in string.punctuation:

                    words.append(list_new[j][k])

    #time.sleep(10)          

print(len(words))

words_new = sorted(set(words))
words_new = list(filter(None, words_new)) # fastest


#print(words_new)


    #reader = csv.reader(csv_file, delimiter= " ")

    #text = [] 
#       print(filename)
#       print(reader)

    #for k in reader: 

    #   text.append(k)

    #for row in reader:
    #       time.sleep(2)   

    #print(i)
#i+=1

#print("The length of the text is " + str(len(text)))

#words = [] 

#for i in range(len(text)): 

#   for m in range(len(text[i])): 

     
#       print(text[i][m])
#       words.append(text[i][m])
#       words.sort()
#       time.sleep(1)

#print(len(words))
#print(set(words))

#words_new = ['alal', 'd', 'cd']

#print(sorted(words_new))

#print(set(list(sorted(words))))

#print(len(words))
#print(len(set(words))


with open("words.txt", "w") as write_file: 

    #writer = csv.writer(write_file)

    print("Start from here")
        
    for l in words_new: 

         #time.sleep(0.5)
        write_file.write(l +'\n')

        #print(l)
        #time.sleep(0.3)



#       print(text[i])
#       print(len(text[i]))

#c = Counter(katalog_keywords)

#with open("katalog_keywords_statitics.txt", "w") as f:

#    for k,v in c.most_common():

#       f.write( "{} {}\n".format(k,v) ) 

#katalog_keywords = list(set(katalog_keywords))
