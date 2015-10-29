# the crawler function 
import os 
import codecs 
import re 

# function - returns a list of words and saves them into n- arrays 
# input: Path to the files 
# output: matrix nm - n (rows - number of files) (m-number of words per/file)

def substitute(path): 

    for path, subdirs, files in os.walk(path):

        attr = [] 
        #print("How many files in folder: " +  str(len(files)))

        #matrix arrays of words 
        matrix = [[] for i in range(len(files))]
        
        #arrays of keys - from dictionary 
        values = [[] for i in range(len(files))]

        files = sorted(files)

        words_dictionary = [] 
        
        j = 0 

        for filename in files:
            
            f = os.path.join(path, filename)

            file_name = os.path.join(path + "/" + filename)
            
            attrs = [] 
            with codecs.open(file_name, "r", encoding='ISO-8859-1') as csv_file: 

                list_words = []
                words_lines_matrix = []

                for line in csv_file:

                        new_line = []
                        new_line = line.split()
#                        print(new_line)
                        for i in range(len(new_line)):
                            

                            list_words.append(new_line[i])
                
                values = [] 
                for m in range(len(list_words)):

                         matrix[j].append(list_words[m])
                j+=1 
        
        return(matrix,files)



# input: file path 
# output: all the words in the texts sorted 

def crawler (path):  

    words = [] 
    files_crawled = [] 

    for path, subdirs, files in os.walk(path):

        i = 1 
        files = sorted(files)

        for filename in files:
            
            f = os.path.join(path, filename)

            file_name = os.path.join(path + "/" + filename)
            
            with codecs.open(file_name, "r", encoding='ISO-8859-1') as csv_file: 

                for line in csv_file:

                    list_new = [] 
                    list_new.append(re.split('(\ |\\n)+', line))
                
                    for j in range(len(list_new)):

                     for k in range(len(list_new[j])):

                        words.append(list_new[j][k])

    words_new = sorted(set(words))
    #words_new = list(filter(None, words_new)) # fastest
    words_new = sorted(words_new)

    return (words_new)

# from list to dictionary  
# input: words 
# output: words in a dictionary form 

def get_words_dictionary(words):

    words_dictionary = {} 
    k = 1
    for l in range(1,len(words)): 
        if words[l] not in " ":  
            words_dictionary[k]= words[l]
            k+=1

    return words_dictionary
