import string
import os
import urllib
import csv
import time
import re
import json
import datetime
from collections import Counter
import codecs 
import numpy as np  
from difflib import Differ
from difflib import SequenceMatcher
from similiarity import similiarity
from crawler import crawler
from crawler import get_words_dictionary
from crawler import substitute

#function to filter the same words in the arrays 
def filter_results(result):
   
    filtered_result = [] 
    sorted_result = [] 

    # use just files with -, + and " "
    for i in range(len(result)): 

        if result[i][0] == "-": 
            filtered_result.append(result[i])

        elif result[i][0] == "+": 
            filtered_result.append(result[i])

        elif result[i][0] == " ": 
            filtered_result.append(result[i])
    
    #some filtering
    #m = 0
    #print(str(m) + str(len(filtered_result)))


    for i in range(len(filtered_result)): 

       # print( str(i) + str(filtered_result[i][0]) + "\t" + str(filtered_result[i+1][0]))
        
        if filtered_result[i][0] == "-": #and filtered_result[i+1][0] == "+":
     
            sorted_result.append(filtered_result[i][2:])

        elif filtered_result[i][0] == "+" and filtered_result[i-1][0] == "-": 
            sorted_result.append("@delete")

        elif filtered_result[i][0] == " ": 

            sorted_result.append(filtered_result[i][2:])

        elif filtered_result[i][0] == "+":

           sorted_result.append("")

    return (sorted_result, filtered_result)
    #return (filtered_result)

def filter_results_2(result):
   
    filtered_result = [] 

    # use just files with -, + and " "
    for i in range(len(result)): 

        if result[i][0] == "-": 
            filtered_result.append(result[i])

        elif result[i][0] == "+": 
            filtered_result.append(result[i])

#        elif result[i][0] == " ": 
 #           filtered_result.append(result[i])
    
    return (filtered_result)

def write_to_matrix_txt(files, list_compare, test):

    with open("matrix_non_filter1.txt", "w") as write_file: 

        for i in range(len(list_compare)): 

            write_file.write(str(test[i][2][0]) + ",")
            for m in range(len(list_compare[i])):
      
                if list_compare[i][m] != "@delete":

                    write_file.write(str(list_compare[i][m]) + ",")
                    
            write_file.write("\n")        

    return(print("Saved"))






# function for differentation 


#list_compare = [[] for i in range(len(matrix))]
#sorted_matrix = [[] for i in range(len(files))]
#test = [[ [] for i in range(3)] for i in range(len(matrix))]

#for i in range(len(matrix)): 


#   test[i][0].append(len(matrix[i]))
#    test[i][1].append(i)
#    test[i][2].append(files[i])
#test = sorted(test, reverse = True)


#print(" Start from here ")


#for i in range(len(sorted_matrix)): 


 #   sorted_matrix[i].extend(matrix[ test[i][1][0] ])


#for i in range(len(sorted_matrix)): 

#    print("For {} row: ".format(i) + "\t" + str(len(sorted_matrix[i])))

#print("The length of the sorted matrix is: " + str(len(sorted_matrix)))


#save_scores = [] 

#s = SequenceMatcher() 



#for i in range(len(matrix)): 

#     x = matrix[i]
#     print(x)
#     time.sleep(1)
#     s.set_seq1(x)
#     for j in range(i+1, len(matrix[i])): 

#        y = matrix[j]
#        s.set_seq2(y)
#        print(s.get_matching_blocks())


#function for differentation 
#for m in range(len(sorted_matrix)-1): 


    #list_compare[m].extend(filter_results(list(d.compare(sorted_matrix[m],sorted_matrix[m+1]))))
    #list_compare[m].extend(list(d.compare(sorted_matrix[m],sorted_matrix[m+1])))
    
    #print(m,m+1)    

#list_compare[-1].extend(filter_results(list(d.compare(sorted_matrix[-1],sorted_matrix[0]))))

#print("The length of the list: " + str(len(list_compare)+1))

#print("The final matrix has a length of :" + str(len(list_compare)+1))



#write matrix 




path = "/home/assen/Development/stemmatology/DataSet1-Heinrichi/DataSet/heinrichi"

#get words (all the words )
words = crawler(path)

matrix,files =  substitute(path)



print(len(matrix))

for l in range(len(matrix)): 

    print(str(l) + " The lenght of the {}: ".format(files[l]) + str(len(matrix[l])))

print("Number of crawled files: " + str(len(matrix)))

ratio = []
ratio, match = similiarity(matrix, files)





for i in range(10): 

    #for k in range(1): 

       # if files[k] == ratio[i].split(",")[1]:
    
            print(ratio[i].split(","))

# get the best matches for all pairs () 

d  = Differ()

list_compare = list(d.compare(matrix[24], matrix[25]))



#sorted_list, filtered_result = filter_results(list_compare)

filtered_result = filter_results_2(list_compare)

for ii in range(len(filtered_result)):

    print(filtered_result[ii])
    time.sleep(2)
    #print(sorted_list[ii])


